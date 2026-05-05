from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.config import Settings, load_settings  # noqa: E402
from src.generator import generate_answer  # noqa: E402
from src.intent_classifier import classify  # noqa: E402
from src.prompt_builder import build_messages, collect_source_paths  # noqa: E402
from src.retriever import Retriever  # noqa: E402


OUT_OF_SCOPE_MESSAGE = (
    "Za ovo nemam dovoljno precizan dokument u bazi znanja. Mogu da pomognem "
    "sa pitanjima o modulu PIT, predmetima, izbornim korpama i karijernim putanjama."
)

MAX_HISTORY_MESSAGES = 6
MAX_HISTORY_MESSAGE_CHARS = 1000
MAX_ERROR_CHARS = 500
CHAT_LOG_PATH = PROJECT_ROOT / "data" / "logs" / "chat_api_log.jsonl"


class HistoryMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    conversation_id: str | None = None
    question: str = Field(..., min_length=1)
    history: list[HistoryMessage] = Field(default_factory=list)


class ChatResponse(BaseModel):
    conversation_id: str
    answer: str
    sources: list[str]
    provider: str
    model: str
    fallback_used: bool
    detected_intents: list[str]
    detected_course_names: list[str]


app = FastAPI(title="PIT Navigator API")

# Production deployment should add: https://pin.ekof.bg.ac.rs
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "http://127.0.0.1:8000",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

_retriever_cache: dict[tuple[str, str], Retriever] = {}


def _chunk_text_length(result: Any) -> int:
    return len(
        getattr(result, "original_chunk_text", "")
        or getattr(result, "contextual_chunk_text", "")
        or ""
    )


def _select_context_results(settings: Settings, results: list[Any]) -> list[Any]:
    context_results: list[Any] = []
    total_chars = 0

    for result in results:
        if result.score < settings.min_retrieval_score:
            continue
        chunk_chars = _chunk_text_length(result)
        if context_results and total_chars + chunk_chars > settings.max_total_context_chars:
            continue
        context_results.append(result)
        total_chars += chunk_chars
        if len(context_results) >= settings.max_context_chunks:
            break

    return context_results


def _provider_value(result: Any, key: str, default: Any = None) -> Any:
    if isinstance(result, dict):
        return result.get(key, default)
    return getattr(result, key, default)


def _get_retriever(settings: Settings) -> Retriever:
    cache_key = (str(settings.index_path), settings.embedding_model)
    if cache_key not in _retriever_cache:
        _retriever_cache[cache_key] = Retriever(settings.index_path, settings.embedding_model)
    return _retriever_cache[cache_key]


def _normalize_history_role(role: str) -> str:
    normalized = role.strip().lower()
    if normalized == "assistant":
        return "Assistant"
    return "User"


def _truncate(value: str, max_chars: int) -> str:
    if len(value) <= max_chars:
        return value
    return value[:max_chars].rstrip() + "..."


def _build_history_context(history: list[HistoryMessage]) -> str:
    selected_messages = history[-MAX_HISTORY_MESSAGES:]
    lines: list[str] = []

    for message in selected_messages:
        content = message.content.strip()
        if not content:
            continue
        lines.append(
            f"{_normalize_history_role(message.role)}: "
            f"{_truncate(content, MAX_HISTORY_MESSAGE_CHARS)}"
        )

    if not lines:
        return ""

    return (
        "Prethodni tok razgovora, samo za razumevanje referenci, nije izvor činjenica:\n"
        + "\n".join(lines)
    )


def _build_effective_question(question: str, history: list[HistoryMessage]) -> str:
    history_context = _build_history_context(history)
    if not history_context:
        return question
    return f"{history_context}\n\nTrenutno pitanje korisnika:\n{question}"


def _model_for_settings(settings: Settings) -> str:
    provider = settings.llm_provider.strip().lower()
    if provider == "gemini":
        return settings.gemini_model
    if provider == "openai":
        return settings.openai_model
    return ""


def _sanitize_error(error: Any, settings: Settings | None = None) -> str:
    sanitized = _truncate(str(error or ""), MAX_ERROR_CHARS)
    if settings is not None:
        for secret in [settings.gemini_api_key, settings.openai_api_key]:
            if secret:
                sanitized = sanitized.replace(secret, "[redacted]")
    return sanitized


def _write_chat_log(entry: dict[str, Any]) -> None:
    CHAT_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with CHAT_LOG_PATH.open("a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _base_log_entry(
    *,
    conversation_id: str,
    question: str,
    answer: str = "",
    sources: list[str] | None = None,
    detected_intents: list[str] | None = None,
    detected_course_names: list[str] | None = None,
    provider: str = "",
    model: str = "",
    fallback_used: bool = False,
    error: str | None = None,
) -> dict[str, Any]:
    entry: dict[str, Any] = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "conversation_id": conversation_id,
        "question": question,
        "answer_preview": answer[:500],
        "answer_length": len(answer),
        "sources": sources or [],
        "detected_intents": detected_intents or [],
        "detected_course_names": detected_course_names or [],
        "provider": provider,
        "model": model,
        "fallback_used": fallback_used,
    }
    if error:
        entry["error"] = error
    return entry


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "pit-navigator-api"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    conversation_id = request.conversation_id or str(uuid4())
    settings: Settings | None = None

    try:
        settings = load_settings()
        effective_question = _build_effective_question(request.question, request.history)
        classification = classify(effective_question)
        retriever = _get_retriever(settings)
        results = retriever.search(
            effective_question,
            classification.intents,
            settings.top_k,
            classification.course_names,
        )

        if (
            not results
            or (
                settings.refuse_out_of_scope
                and results[0].score < settings.min_retrieval_score
            )
        ):
            response = ChatResponse(
                conversation_id=conversation_id,
                answer=OUT_OF_SCOPE_MESSAGE,
                sources=[],
                provider="",
                model="",
                fallback_used=False,
                detected_intents=classification.intents,
                detected_course_names=classification.course_names,
            )
            _write_chat_log(
                _base_log_entry(
                    conversation_id=conversation_id,
                    question=request.question,
                    answer=response.answer,
                    detected_intents=response.detected_intents,
                    detected_course_names=response.detected_course_names,
                )
            )
            return response

        context_results = _select_context_results(settings, results)
        if not context_results:
            response = ChatResponse(
                conversation_id=conversation_id,
                answer=OUT_OF_SCOPE_MESSAGE,
                sources=[],
                provider="",
                model="",
                fallback_used=False,
                detected_intents=classification.intents,
                detected_course_names=classification.course_names,
            )
            _write_chat_log(
                _base_log_entry(
                    conversation_id=conversation_id,
                    question=request.question,
                    answer=response.answer,
                    detected_intents=response.detected_intents,
                    detected_course_names=response.detected_course_names,
                )
            )
            return response

        messages = build_messages(
            effective_question,
            classification.intents,
            classification.course_names,
            context_results,
        )
        generation_result = generate_answer(messages)
        answer = _provider_value(generation_result, "answer", "") or ""
        provider = _provider_value(generation_result, "provider", settings.llm_provider) or ""
        model = _provider_value(generation_result, "model", _model_for_settings(settings)) or ""
        fallback_used = bool(_provider_value(generation_result, "fallback_used", False))
        generator_error = _provider_value(generation_result, "error")

        if not answer:
            error = _sanitize_error(generator_error or "Generator nije vratio odgovor.", settings)
            _write_chat_log(
                _base_log_entry(
                    conversation_id=conversation_id,
                    question=request.question,
                    sources=collect_source_paths(context_results),
                    detected_intents=classification.intents,
                    detected_course_names=classification.course_names,
                    provider=provider,
                    model=model,
                    fallback_used=fallback_used,
                    error=error,
                )
            )
            raise HTTPException(
                status_code=500,
                detail="Došlo je do greške pri obradi pitanja.",
            )

        sources = collect_source_paths(context_results) if settings.include_sources else []
        response = ChatResponse(
            conversation_id=conversation_id,
            answer=answer,
            sources=sources,
            provider=provider,
            model=model,
            fallback_used=fallback_used,
            detected_intents=classification.intents,
            detected_course_names=classification.course_names,
        )
        _write_chat_log(
            _base_log_entry(
                conversation_id=conversation_id,
                question=request.question,
                answer=response.answer,
                sources=response.sources,
                detected_intents=response.detected_intents,
                detected_course_names=response.detected_course_names,
                provider=response.provider,
                model=response.model,
                fallback_used=response.fallback_used,
                error=_sanitize_error(generator_error, settings) if generator_error else None,
            )
        )
        return response
    except HTTPException:
        raise
    except Exception as exc:
        error = _sanitize_error(exc, settings)
        _write_chat_log(
            _base_log_entry(
                conversation_id=conversation_id,
                question=request.question,
                error=error,
            )
        )
        raise HTTPException(
            status_code=500,
            detail="Došlo je do greške pri obradi pitanja.",
        ) from None
