from __future__ import annotations

import concurrent.futures
from collections.abc import Iterator
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .config import Settings, load_settings


Message = dict[str, str]


@dataclass(frozen=True)
class ProviderResult:
    answer: str
    provider: str
    model: str
    fallback_used: bool
    error: str | None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class ProviderError(RuntimeError):
    pass


def _call_with_timeout(fn: Any, timeout_seconds: int) -> Any:
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(fn)
        try:
            return future.result(timeout=timeout_seconds)
        except concurrent.futures.TimeoutError:
            raise ProviderError(f"LLM call timed out after {timeout_seconds}s")


def generate_answer(messages: list[Message], settings: Settings | None = None) -> dict[str, Any]:
    if settings is None:
        settings = load_settings()
    primary_provider = settings.llm_provider.strip().lower()
    fallback_provider = settings.llm_fallback_provider.strip().lower()

    try:
        result = _generate_with_provider(primary_provider, messages, settings)
        _log_generation(settings, messages, result)
        return result.to_dict()
    except Exception as exc:
        primary_error = f"primary provider failed: {exc}"
        if not settings.fallback_on_error or not fallback_provider or fallback_provider == primary_provider:
            result = ProviderResult(
                answer="",
                provider=primary_provider,
                model=_model_for_provider(primary_provider, settings),
                fallback_used=False,
                error=primary_error,
            )
            _log_generation(settings, messages, result)
            return result.to_dict()

        try:
            fallback_result = _generate_with_provider(fallback_provider, messages, settings)
            result = ProviderResult(
                answer=fallback_result.answer,
                provider=fallback_result.provider,
                model=fallback_result.model,
                fallback_used=True,
                error=primary_error,
            )
            _log_generation(settings, messages, result)
            return result.to_dict()
        except Exception as fallback_exc:
            result = ProviderResult(
                answer="",
                provider=fallback_provider,
                model=_model_for_provider(fallback_provider, settings),
                fallback_used=True,
                error=f"{primary_error}; fallback provider failed: {fallback_exc}",
            )
            _log_generation(settings, messages, result)
            return result.to_dict()


def generate_answer_stream(messages: list[Message], settings: Settings | None = None) -> Iterator[dict[str, Any]]:
    if settings is None:
        settings = load_settings()
    primary_provider = settings.llm_provider.strip().lower()
    fallback_provider = settings.llm_fallback_provider.strip().lower()
    yielded_text = False

    try:
        for event in _generate_stream_with_provider(primary_provider, messages, settings):
            if event.get("type") == "token" and event.get("text"):
                yielded_text = True
            yield event
    except Exception as exc:
        primary_error = f"primary provider failed: {exc}"
        if yielded_text or not settings.fallback_on_error or not fallback_provider or fallback_provider == primary_provider:
            result = ProviderResult(
                answer="",
                provider=primary_provider,
                model=_model_for_provider(primary_provider, settings),
                fallback_used=False,
                error=primary_error,
            )
            _log_generation(settings, messages, result)
            yield {
                "type": "error",
                "provider": result.provider,
                "model": result.model,
                "fallback_used": result.fallback_used,
                "error": result.error,
            }
            return

        try:
            for event in _generate_stream_with_provider(
                fallback_provider,
                messages,
                settings,
                fallback_used=True,
                error=primary_error,
            ):
                yield event
        except Exception as fallback_exc:
            result = ProviderResult(
                answer="",
                provider=fallback_provider,
                model=_model_for_provider(fallback_provider, settings),
                fallback_used=True,
                error=f"{primary_error}; fallback provider failed: {fallback_exc}",
            )
            _log_generation(settings, messages, result)
            yield {
                "type": "error",
                "provider": result.provider,
                "model": result.model,
                "fallback_used": result.fallback_used,
                "error": result.error,
            }


def generate_with_gemini(messages: list[Message]) -> ProviderResult:
    settings = load_settings()
    return _generate_with_gemini(messages, settings)


def generate_with_openai(messages: list[Message]) -> ProviderResult:
    settings = load_settings()
    return _generate_with_openai(messages, settings)


def _generate_with_provider(
    provider: str,
    messages: list[Message],
    settings: Settings,
) -> ProviderResult:
    if provider == "gemini":
        return _generate_with_gemini(messages, settings)
    if provider == "openai":
        return _generate_with_openai(messages, settings)
    raise ProviderError(f"Unsupported LLM provider: {provider}")


def _generate_stream_with_provider(
    provider: str,
    messages: list[Message],
    settings: Settings,
    fallback_used: bool = False,
    error: str | None = None,
) -> Iterator[dict[str, Any]]:
    if provider == "gemini":
        yield from _generate_stream_with_gemini(messages, settings, fallback_used, error)
        return
    if provider == "openai":
        yield from _generate_stream_with_openai(messages, settings, fallback_used, error)
        return
    raise ProviderError(f"Unsupported LLM provider: {provider}")


def _generate_with_gemini(messages: list[Message], settings: Settings) -> ProviderResult:
    if not settings.gemini_api_key:
        raise ProviderError("Missing GEMINI_API_KEY for Gemini provider.")

    try:
        from google import genai
        from google.genai import types
    except ImportError as exc:
        raise ProviderError("Missing google-genai package. Install requirements.txt.") from exc

    system_instruction, contents = _messages_to_gemini_prompt(messages)
    client = genai.Client(api_key=settings.gemini_api_key)
    generate_config = types.GenerateContentConfig(
        system_instruction=system_instruction or None,
        temperature=settings.llm_temperature,
        max_output_tokens=settings.llm_max_tokens,
        top_p=settings.llm_top_p,
        thinking_config=types.ThinkingConfig(thinking_budget=0),
    )

    def _call() -> Any:
        return client.models.generate_content(
            model=settings.gemini_model,
            contents=contents,
            config=generate_config,
        )

    response = _call_with_timeout(_call, settings.llm_timeout)
    answer = getattr(response, "text", None) or str(response)
    return ProviderResult(
        answer=answer,
        provider="gemini",
        model=settings.gemini_model,
        fallback_used=False,
        error=None,
    )


def _generate_stream_with_gemini(
    messages: list[Message],
    settings: Settings,
    fallback_used: bool = False,
    error: str | None = None,
) -> Iterator[dict[str, Any]]:
    if not settings.gemini_api_key:
        raise ProviderError("Missing GEMINI_API_KEY for Gemini provider.")

    try:
        from google import genai
        from google.genai import types
    except ImportError as exc:
        raise ProviderError("Missing google-genai package. Install requirements.txt.") from exc

    system_instruction, contents = _messages_to_gemini_prompt(messages)
    client = genai.Client(api_key=settings.gemini_api_key)
    answer_parts: list[str] = []
    response_stream = client.models.generate_content_stream(
        model=settings.gemini_model,
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction or None,
            temperature=settings.llm_temperature,
            max_output_tokens=settings.llm_max_tokens,
            top_p=settings.llm_top_p,
            thinking_config=types.ThinkingConfig(thinking_budget=0),
        ),
    )
    for chunk in response_stream:
        text = getattr(chunk, "text", None) or ""
        if not text:
            continue
        answer_parts.append(text)
        yield {"type": "token", "text": text}

    result = ProviderResult(
        answer="".join(answer_parts),
        provider="gemini",
        model=settings.gemini_model,
        fallback_used=fallback_used,
        error=error,
    )
    _log_generation(settings, messages, result)
    yield result.to_dict() | {"type": "final"}


def _generate_with_openai(messages: list[Message], settings: Settings) -> ProviderResult:
    if not settings.openai_api_key:
        raise ProviderError("Missing OPENAI_API_KEY for OpenAI provider.")

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise ProviderError("Missing openai package. Install requirements.txt.") from exc

    client = OpenAI(api_key=settings.openai_api_key, timeout=settings.llm_timeout)
    response = client.chat.completions.create(
        model=settings.openai_model,
        messages=messages,
        temperature=settings.llm_temperature,
        max_tokens=settings.llm_max_tokens,
        top_p=settings.llm_top_p,
    )
    answer = response.choices[0].message.content or ""
    return ProviderResult(
        answer=answer,
        provider="openai",
        model=settings.openai_model,
        fallback_used=False,
        error=None,
    )


def _generate_stream_with_openai(
    messages: list[Message],
    settings: Settings,
    fallback_used: bool = False,
    error: str | None = None,
) -> Iterator[dict[str, Any]]:
    if not settings.openai_api_key:
        raise ProviderError("Missing OPENAI_API_KEY for OpenAI provider.")

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise ProviderError("Missing openai package. Install requirements.txt.") from exc

    client = OpenAI(api_key=settings.openai_api_key, timeout=settings.llm_timeout)
    answer_parts: list[str] = []
    stream = client.chat.completions.create(
        model=settings.openai_model,
        messages=messages,
        temperature=settings.llm_temperature,
        max_tokens=settings.llm_max_tokens,
        top_p=settings.llm_top_p,
        stream=True,
    )
    for chunk in stream:
        text = chunk.choices[0].delta.content or ""
        if not text:
            continue
        answer_parts.append(text)
        yield {"type": "token", "text": text}

    result = ProviderResult(
        answer="".join(answer_parts),
        provider="openai",
        model=settings.openai_model,
        fallback_used=fallback_used,
        error=error,
    )
    _log_generation(settings, messages, result)
    yield result.to_dict() | {"type": "final"}


def _messages_to_gemini_prompt(messages: list[Message]) -> tuple[str, str]:
    system_parts: list[str] = []
    content_parts: list[str] = []

    for message in messages:
        role = message.get("role", "user")
        content = message.get("content", "")
        if role == "system":
            system_parts.append(content)
        else:
            content_parts.append(f"{role.upper()}:\n{content}")

    return "\n\n".join(system_parts), "\n\n".join(content_parts)


def _model_for_provider(provider: str, settings: Settings) -> str:
    if provider == "gemini":
        return settings.gemini_model
    if provider == "openai":
        return settings.openai_model
    return ""


def _prompt_length(messages: list[Message]) -> int:
    return sum(len(message.get("content", "")) for message in messages)


def _log_generation(
    settings: Settings,
    messages: list[Message],
    result: ProviderResult,
) -> None:
    if not settings.log_prompts:
        return

    log_path = Path(settings.log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{datetime.now(timezone.utc).isoformat()} "
        f"provider={result.provider} "
        f"model={result.model} "
        f"fallback_used={str(result.fallback_used).lower()} "
        f"prompt_chars={_prompt_length(messages)} "
        f"error={result.error or ''}\n"
    )
    with log_path.open("a", encoding="utf-8") as log_file:
        log_file.write(line)


if __name__ == "__main__":
    settings = load_settings()
    dummy_messages = [
        {"role": "system", "content": "Ti si PIT Navigator."},
        {"role": "user", "content": "Kratko odgovori da je generator konfigurisan."},
    ]
    provider = settings.llm_provider.strip().lower()
    key_available = bool(
        settings.gemini_api_key if provider == "gemini" else settings.openai_api_key
    )

    print(f"Configured provider: {provider}")
    print(f"Configured model: {_model_for_provider(provider, settings)}")
    print(f"Prompt chars: {_prompt_length(dummy_messages)}")
    if not key_available:
        print("API key is missing for the configured provider; no API call was made.")
    else:
        print(generate_answer(dummy_messages))
