from __future__ import annotations

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


def generate_answer(messages: list[Message]) -> dict[str, Any]:
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
    response = client.models.generate_content(
        model=settings.gemini_model,
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction or None,
            temperature=settings.llm_temperature,
            max_output_tokens=settings.llm_max_tokens,
            top_p=settings.llm_top_p,
        ),
    )
    answer = getattr(response, "text", None) or str(response)
    return ProviderResult(
        answer=answer,
        provider="gemini",
        model=settings.gemini_model,
        fallback_used=False,
        error=None,
    )


def _generate_with_openai(messages: list[Message], settings: Settings) -> ProviderResult:
    if not settings.openai_api_key:
        raise ProviderError("Missing OPENAI_API_KEY for OpenAI provider.")

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise ProviderError("Missing openai package. Install requirements.txt.") from exc

    client = OpenAI(api_key=settings.openai_api_key)
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
    log_path.write_text(
        (log_path.read_text(encoding="utf-8") if log_path.exists() else "") + line,
        encoding="utf-8",
    )


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
