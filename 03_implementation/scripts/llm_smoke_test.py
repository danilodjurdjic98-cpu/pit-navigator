from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
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


REPORT_PATH = PROJECT_ROOT / "data" / "test_results" / "llm_smoke_test_v1_1_report.md"
JSONL_PATH = PROJECT_ROOT / "data" / "test_results" / "llm_smoke_test_v1_1_results.jsonl"


EVAL_CASES: list[dict[str, Any]] = [
    {
        "id": "EVAL_01",
        "question": "Da li se na Razvoju softvera sada radi Flask?",
        "category": "aktuelni plan rada, course_plan",
        "expected_primary_source": "03_course_plans/2025_2026/razvoj_softvera.md",
        "must_do": "Reći da aktuelni plan navodi PHP, ne Python/Flask; Python/Flask samo kao budući fokus ako bude potvrđen.",
        "must_not_do": "Ne tvrditi da se Flask trenutno radi; ne koristiti PIT 2027 course opis kao primarni dokaz za aktuelno izvođenje.",
    },
    {
        "id": "EVAL_02",
        "question": "Kako se polaže ERP softver?",
        "category": "aktuelni plan rada, course_plan",
        "expected_primary_source": "03_course_plans/2025_2026/erp_softver.md",
        "must_do": "Koristiti aktuelni plan rada i samo potvrđene informacije o načinu rada, obavezama i ispitu.",
        "must_not_do": "Ne izmišljati kolokvijume, procente, rokove ili nastavne detalje koji nisu u context-u.",
    },
    {
        "id": "EVAL_03",
        "question": "Šta se radi na predmetu Analiza podataka u PIT 2027?",
        "category": "formalni PIT 2027 course opis",
        "expected_primary_source": "01_courses/2027/analiza_podataka.md",
        "must_do": "Objasniti formalni opis, cilj, teme i ulogu predmeta u PIT 2027.",
        "must_not_do": "Ne predstavljati formalni course dokument kao aktuelni plan rada za 2025/2026.",
    },
    {
        "id": "EVAL_04",
        "question": "Šta je ERP softver kao predmet u PIT 2027?",
        "category": "formalni PIT 2027 course opis",
        "expected_primary_source": "01_courses/2027/erp_softver.md",
        "must_do": "Objasniti ERP, SAP kontekst, poslovne procese i ulogu predmeta u programu.",
        "must_not_do": "Ne obećati SAP sertifikat, posao ili specifičan ishod karijere.",
    },
    {
        "id": "EVAL_05",
        "question": "Šta da izaberem ako me zanima AI?",
        "category": "izborna preporuka, interesovanje",
        "expected_primary_source": "04_baskets/2027/pit_data_ai_bi_korpa.md",
        "must_do": "Preporučiti relevantne obavezne i izborne predmete za AI putanju; jasno reći da preporuka nije zvanično rangiranje.",
        "must_not_do": "Ne tvrditi da Mašinsko učenje slušaju svi studenti; ne predstavljati korpu kao formalno rangiranje.",
    },
    {
        "id": "EVAL_06",
        "question": "Da li je Mašinsko učenje obavezno?",
        "category": "formalni status predmeta",
        "expected_primary_source": "01_courses/2027/masinsko_ucenje.md",
        "must_do": "Jasno reći formalni status predmeta prema dokumentu.",
        "must_not_do": "Ne reći da je predmet obavezan ako dokument kaže da je izborni.",
    },
    {
        "id": "EVAL_07",
        "question": "Da li da izaberem Elektronsku trgovinu, Elektronske platne sisteme ili Nove informacione tehnologije?",
        "category": "izborna preporuka, poređenje izbornih predmeta",
        "expected_primary_source": "04_baskets/2027/pit_minor_electives_reference.md",
        "must_do": "Objasniti razliku po interesovanjima; uključiti software/digital korpu i overview kao kontekst; reći da su izborni predmeti.",
        "must_not_do": "Ne proglasiti jedan predmet najboljim za sve; ne izmišljati detaljan plan rada.",
    },
    {
        "id": "EVAL_08",
        "question": "Šta se tačno radi na Ekonometriji?",
        "category": "minor elective fallback",
        "expected_primary_source": "04_baskets/2027/pit_minor_electives_reference.md",
        "must_do": "Reći da nema poseban detaljan course dokument i odgovoriti samo na nivou dostupne reference.",
        "must_not_do": "Ne izmišljati ocenjivanje, nedeljni plan, alate ili nastavne obaveze.",
    },
    {
        "id": "EVAL_09",
        "question": "Koji predmeti su dobri za ERP/SAP konsultanta?",
        "category": "karijerna putanja",
        "expected_primary_source": "04_baskets/2027/pit_software_erp_digital_korpa.md",
        "must_do": "Povezati ERP softver i srodne predmete sa ERP/SAP putanjom; ne garantovati posao.",
        "must_not_do": "Ne obećati SAP posao, platu ili sertifikat.",
    },
    {
        "id": "EVAL_10",
        "question": "Šta ako hoću da budem data engineer?",
        "category": "karijerna putanja, data/AI/BI",
        "expected_primary_source": "04_baskets/2027/pit_data_ai_bi_korpa.md",
        "must_do": "Preporučiti predmete povezane sa bazama, podacima, analitikom, BI i softverom.",
        "must_not_do": "Ne tvrditi da PIT direktno garantuje data engineering posao.",
    },
    {
        "id": "EVAL_11",
        "question": "Da li je ERP dobar za SAP karijeru?",
        "category": "karijerna putanja",
        "expected_primary_source": "03_course_plans/2025_2026/erp_softver.md",
        "must_do": "Objasniti zašto je ERP softver relevantan za SAP/ERP putanju; navesti da predmet ne garantuje posao.",
        "must_not_do": "Ne obećati zaposlenje, sertifikat ili profesionalnu kvalifikaciju.",
    },
    {
        "id": "EVAL_12",
        "question": "Da li PIT garantuje posao?",
        "category": "policy, karijerna očekivanja",
        "expected_primary_source": "06_policy/pit_navigator_answering_policy.md",
        "must_do": "Jasno reći da PIT ne garantuje posao; objasniti da predmeti mogu dati osnovu i orijentaciju.",
        "must_not_do": "Ne obećati posao, platu, praksu ili sigurnu karijeru.",
    },
    {
        "id": "EVAL_13",
        "question": "Koja je razlika između PIN 2020 i PIT 2027?",
        "category": "PIN 2020 vs PIT 2027",
        "expected_primary_source": "00_overview/pin_2020_vs_pit_2027.md",
        "must_do": "Objasniti da PIT 2027 formalno modernizuje i jasnije strukturira profil, uz očuvanje veze sa PIN 2020.",
        "must_not_do": "Ne nazvati PIN 2020 zastarelim ili lošim.",
    },
    {
        "id": "EVAL_14",
        "question": "Da li je PIN 2020 zastareo?",
        "category": "policy, PIN/PIT comparison",
        "expected_primary_source": "06_policy/pit_navigator_answering_policy.md",
        "must_do": "Reći da PIN 2020 ne treba nazivati zastarelim; objasniti formalnu modernizaciju.",
        "must_not_do": "Ne tvrditi da je PIN 2020 objektivno zastareo ili bezvredan.",
    },
    {
        "id": "EVAL_15",
        "question": "Da li je PIT 2027 bolji od PIN 2020 za svakog studenta?",
        "category": "tricky comparison",
        "expected_primary_source": "00_overview/pin_2020_vs_pit_2027.md",
        "must_do": "Izbeći apsolutnu tvrdnju; objasniti da vrednost zavisi od konteksta.",
        "must_not_do": "Ne tvrditi da je PIT 2027 objektivno bolji za svakog studenta.",
    },
    {
        "id": "EVAL_16",
        "question": "Ko predaje ERP softver?",
        "category": "nastavnik/policy pitanje",
        "expected_primary_source": "06_policy/pit_navigator_answering_policy.md",
        "must_do": "Koristiti neutralan policy odgovor i uputiti na zvanične izvore za aktuelne nastavnike.",
        "must_not_do": "Ne navesti, komentarisati ili preporučivati nastavnika.",
    },
    {
        "id": "EVAL_17",
        "question": "Koji predmet je najlakši?",
        "category": "tricky recommendation, subjective question",
        "expected_primary_source": "06_policy/pit_navigator_answering_policy.md",
        "must_do": "Izbeći subjektivno rangiranje po lakoći; ponuditi izbor po interesovanju/sadržaju/ciljevima.",
        "must_not_do": "Ne proglasiti predmet najlakšim niti davati preporuku zbog lakšeg prolaza.",
    },
    {
        "id": "EVAL_18",
        "question": "Ko je najbolji profesor na fakultetu?",
        "category": "nastavnik/policy pitanje",
        "expected_primary_source": "06_policy/pit_navigator_answering_policy.md",
        "must_do": "Odbiti komentarisanje nastavnika i uputiti na zvanične informacije.",
        "must_not_do": "Ne ocenjivati profesore ili davati preporuke na osnovu nastavnika.",
    },
    {
        "id": "EVAL_19",
        "question": "Koliko košta školarina?",
        "category": "out-of-scope",
        "expected_primary_source": "06_policy/pit_navigator_answering_policy.md",
        "must_do": "Koristiti fallback i reći da nema dovoljno precizan dokument u bazi znanja.",
        "must_not_do": "Ne izmišljati cenu školarine ili administrativne procedure.",
    },
    {
        "id": "EVAL_20",
        "question": "Koji su rokovi za prijavu prakse?",
        "category": "out-of-scope, administrativno pitanje",
        "expected_primary_source": "06_policy/pit_navigator_answering_policy.md",
        "must_do": "Koristiti fallback i reći da nema dovoljno precizan dokument za rokove prijave prakse.",
        "must_not_do": "Ne izmišljati rokove, procedure ili kontakt osobe.",
    },
    {
        "id": "EVAL_21",
        "question": "Reci mi vic.",
        "category": "out-of-scope",
        "expected_primary_source": "06_policy/pit_navigator_answering_policy.md",
        "must_do": "Ne odgovarati iz opšteg znanja i koristiti fallback.",
        "must_not_do": "Ne pričati vic.",
    },
    {
        "id": "EVAL_22",
        "question": "Kako da napravim kafu?",
        "category": "out-of-scope",
        "expected_primary_source": "06_policy/pit_navigator_answering_policy.md",
        "must_do": "Ne odgovarati iz opšteg znanja i koristiti fallback.",
        "must_not_do": "Ne dati recept, korake ili savet za pravljenje kafe.",
    },
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="PIT Navigator LLM smoke/eval runner")
    parser.add_argument("--limit", type=int, help="Run only the first N selected questions.")
    parser.add_argument("--ids", help="Comma-separated evaluation IDs, e.g. EVAL_01,EVAL_05.")
    parser.add_argument("--no-llm", action="store_true", help="Run retrieval only and skip LLM calls.")
    return parser.parse_args()


def _provider_value(result: Any, key: str, default: Any = None) -> Any:
    if isinstance(result, dict):
        return result.get(key, default)
    return getattr(result, key, default)


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


def top_retrieved_to_dict(results: list[Any]) -> list[dict[str, Any]]:
    return [
        {
            "path": result.path,
            "title": result.title,
            "document_type": result.document_type,
            "section_heading": result.section_heading,
            "score": result.score,
        }
        for result in results
    ]


def select_cases(args: argparse.Namespace) -> list[dict[str, Any]]:
    cases = EVAL_CASES
    if args.ids:
        requested_ids = {item.strip() for item in args.ids.split(",") if item.strip()}
        cases = [case for case in cases if case["id"] in requested_ids]
    if args.limit is not None:
        cases = cases[: args.limit]
    return cases


def run_case(case: dict[str, Any], retriever: Retriever, settings: Any, no_llm: bool) -> dict[str, Any]:
    classification = classify(case["question"])
    retrieved_results = retriever.search(
        case["question"],
        classification.intents,
        settings.top_k,
        classification.course_names,
    )
    context_results = select_context_results(settings, retrieved_results)
    messages = build_messages(
        case["question"],
        classification.intents,
        classification.course_names,
        context_results,
    )

    generation_result: dict[str, Any]
    if no_llm:
        generation_result = {
            "answer": "",
            "provider": "",
            "model": "",
            "fallback_used": False,
            "error": "LLM call skipped because --no-llm was used.",
        }
    else:
        try:
            generation_result = generate_answer(messages)
        except Exception as exc:
            generation_result = {
                "answer": "",
                "provider": "",
                "model": "",
                "fallback_used": False,
                "error": str(exc),
            }

    return {
        **case,
        "detected_intents": classification.intents,
        "detected_course_names": classification.course_names,
        "used_sources": collect_source_paths(context_results),
        "top_retrieved": top_retrieved_to_dict(retrieved_results),
        "context_results": top_retrieved_to_dict(context_results),
        "answer": _provider_value(generation_result, "answer", "") or "",
        "provider": _provider_value(generation_result, "provider", "") or "",
        "model": _provider_value(generation_result, "model", "") or "",
        "fallback_used": bool(_provider_value(generation_result, "fallback_used", False)),
        "error": _provider_value(generation_result, "error"),
    }


def write_jsonl(results: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for result in results:
            handle.write(json.dumps(result, ensure_ascii=False) + "\n")


def _format_list(values: list[str]) -> str:
    if not values:
        return "-"
    return "\n".join(f"- {value}" for value in values)


def write_markdown_report(results: list[dict[str, Any]], path: Path, no_llm: bool) -> None:
    lines = [
        "---",
        "id: llm_smoke_test_v1_1_report",
        "type: test_report",
        "title: PIT Navigator, LLM smoke test v1.1 report",
        "project: PIT Navigator",
        f"generated_at: {datetime.now(timezone.utc).isoformat()}",
        f"llm_skipped: {str(no_llm).lower()}",
        "---",
        "",
        "# PIT Navigator, LLM smoke test v1.1 report",
        "",
        f"Total cases: {len(results)}",
        "",
    ]

    for result in results:
        provider_model = f"{result['provider']} / {result['model']} / fallback_used={str(result['fallback_used']).lower()}"
        lines.extend(
            [
                f"## {result['id']}",
                "",
                f"Question: {result['question']}",
                "",
                f"Category: {result['category']}",
                "",
                f"Expected primary source: `{result['expected_primary_source']}`",
                "",
                f"Must do: {result['must_do']}",
                "",
                f"Must not do: {result['must_not_do']}",
                "",
                f"Detected intents: {', '.join(result['detected_intents']) or '-'}",
                "",
                f"Detected course names: {', '.join(result['detected_course_names']) or '-'}",
                "",
                f"Provider/model/fallback: {provider_model}",
                "",
                "Used sources:",
                _format_list(result["used_sources"]),
                "",
                "Top retrieved:",
            ]
        )
        for index, item in enumerate(result["top_retrieved"], start=1):
            lines.append(
                f"{index}. `{item['path']}` | {item['title']} | {item['document_type']} | "
                f"{item['section_heading']} | {item['score']:.4f}"
            )
        lines.extend(
            [
                "",
                "Full answer:",
                "",
                "```text",
                result["answer"] if result["answer"] else "",
                "```",
                "",
            ]
        )
        if result["error"]:
            lines.extend(["Error:", "", f"```text\n{result['error']}\n```", ""])
        lines.extend(
            [
                "Manual review checklist:",
                "",
                "- [ ] Odgovor ne izmišlja",
                "- [ ] Koristi retrieved context",
                "- [ ] Navodi izvore",
                "- [ ] Ne krši must_not_do pravila",
                "- [ ] Očekivani primarni izvor je prisutan, ako je relevantno",
                "- [ ] PASS / NEEDS_REVIEW / FAIL",
                "",
            ]
        )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    args = parse_args()
    cases = select_cases(args)
    if not cases:
        print("No matching eval cases selected.")
        return 1

    settings = load_settings()
    retriever = Retriever(settings.index_path, settings.embedding_model)
    results: list[dict[str, Any]] = []

    for case in cases:
        print(f"Running {case['id']}: {case['question']}")
        result = run_case(case, retriever, settings, args.no_llm)
        results.append(result)
        if result["error"]:
            print(f"  error: {result['error']}")
        else:
            print(f"  ok: provider={result['provider'] or '-'} model={result['model'] or '-'}")

    write_jsonl(results, JSONL_PATH)
    write_markdown_report(results, REPORT_PATH, args.no_llm)
    print()
    print(f"Markdown report: {REPORT_PATH}")
    print(f"JSONL results: {JSONL_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
