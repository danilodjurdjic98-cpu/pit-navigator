from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.config import load_settings  # noqa: E402
from src.generator import generate_answer  # noqa: E402
from src.intent_classifier import classify  # noqa: E402
from src.prompt_builder import build_messages, collect_source_paths  # noqa: E402
from src.retriever import Retriever  # noqa: E402


OUT_OF_SCOPE_MESSAGE = (
    "Za ovo nemam dovoljno precizan dokument u bazi znanja. Mogu da pomognem "
    "sa pitanjima o modulu PIT, predmetima, izbornim korpama i karijernim putanjama."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="PIT Navigator CLI")
    parser.add_argument("question", help="Korisničko pitanje")
    parser.add_argument(
        "--retrieval-only",
        action="store_true",
        help="Prikaži samo retrieval rezultate.",
    )
    parser.add_argument(
        "--show-prompt",
        action="store_true",
        help="Prikaži system/user messages pre LLM poziva.",
    )
    return parser.parse_args()


def print_retrieval_output(args: argparse.Namespace, settings: Any, classification: Any, results: list[Any]) -> None:
    print("Question:")
    print(args.question)
    print()
    print("Detected intent:")
    print(", ".join(classification.intents))
    print()
    print("Detected course names:")
    print(", ".join(classification.course_names) if classification.course_names else "-")
    print()
    print("Retrieved documents:")

    for index, result in enumerate(results, start=1):
        print(f"{index}. {result.path}")
        print(f"   title: {result.title}")
        print(f"   document_type: {result.document_type}")
        print(f"   section_heading: {result.section_heading}")
        print(f"   score: {result.score:.4f}")
        if settings.debug_retrieval:
            print(f"   contextual_prefix: {result.contextual_prefix}")
        print()


def _chunk_text_length(result: Any) -> int:
    return len(
        getattr(result, "original_chunk_text", "")
        or getattr(result, "contextual_chunk_text", "")
        or ""
    )


def select_context_results(settings: Any, results: list[Any]) -> list[Any]:
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


def print_sources(context_results: list[Any]) -> None:
    print()
    print("Korišćeni izvori:")
    for path in collect_source_paths(context_results):
        print(f"- {path}")


def print_provider_debug(settings: Any, generation_result: Any) -> None:
    if not settings.debug_retrieval:
        return
    print()
    print("LLM debug:")
    print(f"provider: {_provider_value(generation_result, 'provider', '-')}")
    print(f"model: {_provider_value(generation_result, 'model', '-')}")
    print(f"fallback_used: {_provider_value(generation_result, 'fallback_used', False)}")


def main() -> None:
    args = parse_args()
    settings = load_settings()
    classification = classify(args.question)
    retriever = Retriever(settings.index_path, settings.embedding_model)
    results = retriever.search(
        args.question,
        classification.intents,
        settings.top_k,
        classification.course_names,
    )

    if args.retrieval_only:
        print_retrieval_output(args, settings, classification, results)
        return

    if not results:
        print(OUT_OF_SCOPE_MESSAGE)
        return

    if settings.refuse_out_of_scope and results[0].score < settings.min_retrieval_score:
        print(OUT_OF_SCOPE_MESSAGE)
        return

    context_results = select_context_results(settings, results)
    if not context_results:
        print(OUT_OF_SCOPE_MESSAGE)
        return

    messages = build_messages(
        args.question,
        classification.intents,
        classification.course_names,
        context_results,
    )

    if args.show_prompt:
        print("Messages:")
        print(json.dumps(messages, ensure_ascii=False, indent=2))
        print()

    generation_result = generate_answer(messages)
    answer = _provider_value(generation_result, "answer", "") or ""
    error = _provider_value(generation_result, "error")

    if not answer:
        print("LLM generation error:")
        print(error or "Generator nije vratio odgovor.")
        print_provider_debug(settings, generation_result)
        print_sources(context_results)
        return

    print(answer)
    if error and settings.debug_retrieval:
        print()
        print(f"Generator warning: {error}")
    if settings.include_sources and "Korišćeni izvori:" not in answer:
        print_sources(context_results)
    print_provider_debug(settings, generation_result)


if __name__ == "__main__":
    main()
