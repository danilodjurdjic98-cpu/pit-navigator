from __future__ import annotations

import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.config import load_settings  # noqa: E402
from src.intent_classifier import classify  # noqa: E402
from src.retriever import RetrievalResult, Retriever  # noqa: E402


TEST_CASES_PATH = PROJECT_ROOT / "data" / "test_results" / "test_cases.yaml"
REPORT_PATH = PROJECT_ROOT / "data" / "test_results" / "test_runner_report.md"


@dataclass(frozen=True)
class TestOutcome:
    test_id: str
    question: str
    status: str
    detected_intents: list[str]
    detected_course_names: list[str]
    retrieved_results: list[RetrievalResult]
    missing_intents: list[str]
    missing_course_names: list[str]
    missing_paths: list[str]
    notes: list[str]


def load_test_cases(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing test cases file: {path}")

    raw_cases = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    if not isinstance(raw_cases, list):
        raise ValueError("test_cases.yaml must contain a list of test cases.")
    return raw_cases


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def _path_folder(path: str) -> str:
    return str(Path(path).parent).replace("\\", "/")


def _has_relevant_folder_match(missing_paths: list[str], retrieved_paths: list[str]) -> bool:
    retrieved_folders = {_path_folder(path) for path in retrieved_paths}
    return any(_path_folder(path) in retrieved_folders for path in missing_paths)


def evaluate_case(
    test_case: dict[str, Any],
    retriever: Retriever,
    top_k: int,
) -> TestOutcome:
    test_id = str(test_case.get("id", "UNKNOWN"))
    question = str(test_case.get("question", ""))
    expected_intents = _as_list(test_case.get("expected_intents"))
    expected_course_names = _as_list(test_case.get("expected_course_names"))
    expected_paths = _as_list(test_case.get("expected_paths"))

    classification = classify(question)
    results = retriever.search(
        question,
        classification.intents,
        top_k,
        classification.course_names,
    )
    retrieved_paths = [result.path for result in results]

    missing_intents = [
        intent for intent in expected_intents if intent not in classification.intents
    ]
    missing_course_names = [
        course_name
        for course_name in expected_course_names
        if course_name not in classification.course_names
    ]
    missing_paths = [path for path in expected_paths if path not in retrieved_paths]

    notes: list[str] = []
    if missing_intents:
        notes.append(f"Missing intents: {', '.join(missing_intents)}")
    if missing_course_names:
        notes.append(f"Missing course names: {', '.join(missing_course_names)}")
    if missing_paths:
        notes.append(f"Missing paths: {', '.join(missing_paths)}")

    if missing_intents or missing_course_names:
        status = "FAIL"
    elif not missing_paths:
        status = "PASS"
    elif _has_relevant_folder_match(missing_paths, retrieved_paths):
        status = "NEEDS_REVIEW"
        notes.append("At least one retrieved result is from an expected folder.")
    else:
        status = "FAIL"

    return TestOutcome(
        test_id=test_id,
        question=question,
        status=status,
        detected_intents=classification.intents,
        detected_course_names=classification.course_names,
        retrieved_results=results,
        missing_intents=missing_intents,
        missing_course_names=missing_course_names,
        missing_paths=missing_paths,
        notes=notes,
    )


def write_report(outcomes: list[TestOutcome], report_path: Path) -> None:
    lines: list[str] = [
        "# PIT Navigator retrieval-only test runner report",
        "",
        f"Generated at: {datetime.now(timezone.utc).isoformat()}",
        "",
        "## Summary",
        "",
    ]

    total = len(outcomes)
    passed = sum(1 for outcome in outcomes if outcome.status == "PASS")
    needs_review = sum(1 for outcome in outcomes if outcome.status == "NEEDS_REVIEW")
    failed = sum(1 for outcome in outcomes if outcome.status == "FAIL")

    lines.extend(
        [
            f"- Total tests: {total}",
            f"- Passed: {passed}",
            f"- Needs review: {needs_review}",
            f"- Failed: {failed}",
            "",
            "## Details",
            "",
        ]
    )

    for outcome in outcomes:
        lines.extend(
            [
                f"### {outcome.test_id}: {outcome.status}",
                "",
                f"Question: {outcome.question}",
                "",
                f"Detected intents: {', '.join(outcome.detected_intents) or '-'}",
                f"Detected course names: {', '.join(outcome.detected_course_names) or '-'}",
                "",
            ]
        )

        if outcome.notes:
            lines.append("Notes:")
            lines.extend(f"- {note}" for note in outcome.notes)
            lines.append("")

        lines.append("Retrieved documents:")
        for index, result in enumerate(outcome.retrieved_results, start=1):
            lines.extend(
                [
                    f"{index}. `{result.path}`",
                    f"   - title: {result.title}",
                    f"   - document_type: {result.document_type}",
                    f"   - section_heading: {result.section_heading}",
                    f"   - score: {result.score:.4f}",
                ]
            )
        lines.append("")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    settings = load_settings()
    test_cases = load_test_cases(TEST_CASES_PATH)
    retriever = Retriever(settings.index_path, settings.embedding_model)

    outcomes = [
        evaluate_case(test_case, retriever, settings.top_k)
        for test_case in test_cases
    ]

    total = len(outcomes)
    passed = sum(1 for outcome in outcomes if outcome.status == "PASS")
    needs_review = sum(1 for outcome in outcomes if outcome.status == "NEEDS_REVIEW")
    failed = sum(1 for outcome in outcomes if outcome.status == "FAIL")

    for outcome in outcomes:
        print(f"{outcome.status}: {outcome.test_id}")

    print()
    print("Summary:")
    print(f"total tests: {total}")
    print(f"passed: {passed}")
    print(f"needs_review: {needs_review}")
    print(f"failed: {failed}")

    write_report(outcomes, REPORT_PATH)
    print()
    print(f"Report: {REPORT_PATH}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
