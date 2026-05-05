from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter
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
PROGRAM_NAME_MESSAGE = (
    "Naziv je Poslovne informacione tehnologije, skraćeno PIT. Na postojećem sajtu "
    "i u prethodnoj akreditaciji koristi se naziv Poslovna informatika, skraćeno PIN. "
    "Oznaka PIT 2027 se odnosi na novu akreditacionu verziju, a ne treba je "
    "predstavljati kao samo ime smera."
)
PIN_FOLLOWUP_MESSAGE = (
    "Razumem — misliš na postojeći PIN 2020. Za tu akreditaciju u bazi znanja nemam "
    "jednako detaljno razrađene izborne korpe i karijerne putanje kao za PIT 2027, "
    "pa neću izmišljati mapu predmeta.\n\n"
    "Ako te zanima AI/data pravac u okviru postojećeg PIN-a, najbezbednije je da "
    "gledaš predmete i materijale koji jačaju rad sa bazama podataka, analizu "
    "podataka, poslovno izveštavanje i programiranje.\n\n"
    "Za preciznu odluku proveri aktuelni informacioni paket i spisak izbornih "
    "predmeta za PIN, jer se struktura može razlikovati od PIT 2027."
)
PIN_AI_CAREER_MESSAGE = (
    "Ako misliš na postojeći PIN, najrealnije AI-povezane uloge posle ovog profila "
    "nisu odmah čiste 'AI engineer' pozicije, već poslovno-analitičke i digitalne "
    "uloge koje koriste AI alate.\n\n"
    "Primeri takvih uloga su:\n"
    "- data analyst / junior data analyst\n"
    "- BI analyst\n"
    "- business analyst koji koristi AI alate\n"
    "- marketing ili CRM analyst\n"
    "- reporting analyst\n"
    "- ERP/reporting analyst\n"
    "- automation / AI tools specialist u poslovnom timu\n"
    "- junior product ili business analyst za digitalne proizvode\n\n"
    "Za PIN 2020 nemam jednako detaljno razrađene karijerne korpe kao za PIT 2027, "
    "pa ovo shvati kao opšte karijerno objašnjenje povezano sa poslovnom informatikom, "
    "a ne kao zvaničnu mapu predmeta.\n\n"
    "Za jače tehničke AI uloge, kao data scientist, machine learning engineer ili "
    "AI engineer, obično je potrebno dodatno učenje programiranja, statistike, "
    "mašinskog učenja i portfolio projekti."
)
PIN_ELECTIVES_MESSAGE = (
    "Ako misliš na postojeći PIN 2020, mogu da dam korisnu orijentaciju, ali uz važnu "
    "napomenu: detaljno sam treniran pre svega na materijalima za novu akreditaciju "
    "PIT 2027. Zato ovo nije zvanična PIN mapa izbornih predmeta, nego preporuka po "
    "logici poslovne informatike i srodnih PIT oblasti.\n\n"
    "Za AI/data/BI pravac najkorisnije je da tražiš predmete i materijale koji jačaju:\n"
    "- rad sa bazama podataka\n"
    "- analizu podataka i poslovnu analitiku\n"
    "- poslovnu inteligenciju i izveštavanje\n"
    "- programiranje i razvoj softvera\n"
    "- osnovu za mašinsko učenje, optimizaciju i rad sa AI alatima\n\n"
    "Kao konkretne korisne teme/predmete, gde god su dostupni u PIN ponudi ili kroz "
    "srodne materijale, gledaj: Baze podataka, Analizu podataka, Poslovnu analitiku, "
    "Poslovnu inteligenciju, Razvoj softvera, ERP softver, Mašinsko učenje i "
    "Operaciona istraživanja.\n\n"
    "Ako te više zanima SAP/ERP putanja, prioritet bih dao ERP softveru, poslovnim "
    "procesima, bazama podataka, izveštavanju i analitici. Ako te više zanima AI/data "
    "putanja, prioritet bih dao bazama, analizi podataka, BI/analitici, programiranju "
    "i mašinskom učenju.\n\n"
    "Za konačan izbor ipak proveri aktuelni PIN spisak izbornih predmeta i pravila "
    "izbora, jer se dostupnost predmeta može razlikovati od nove PIT 2027 strukture."
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
_runtime_cache: tuple[Settings, Retriever] | None = None


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


def _get_runtime() -> tuple[Settings, Retriever]:
    global _runtime_cache
    if _runtime_cache is None:
        settings = load_settings()
        _runtime_cache = (settings, _get_retriever(settings))
    return _runtime_cache


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


def _has_explicit_accreditation_context(question: str) -> bool:
    normalized = question.casefold()
    return any(
        marker in normalized
        for marker in [
            "pit 2027",
            "pin 2020",
            "postojeći pin",
            "postojeci pin",
            "mislim na pin",
            "mislio sam na pin",
            "mislila sam na pin",
            "nova akreditacija",
            "novu akreditaciju",
            "nove akreditacije",
            "stara akreditacija",
            "staru akreditaciju",
            "stare akreditacije",
        ]
    )


def _mentions_current_delivery(question: str) -> bool:
    normalized = question.casefold()
    return any(
        marker in normalized
        for marker in [
            "trenutno",
            "sada",
            "aktuelno",
            "aktuelna",
            "aktuelni",
            "aktuelno izvođenje",
            "ove godine",
            "2025/26",
            "2025/2026",
        ]
    )


def _is_program_name_question(question: str) -> bool:
    normalized = question.casefold()
    return any(
        marker in normalized
        for marker in [
            "kako se zove smer",
            "kako se zove modul",
            "naziv smera",
            "naziv modula",
            "sta znaci pit",
            "šta znači pit",
            "sta je pit",
            "šta je pit",
            "sta je pin",
            "šta je pin",
        ]
    )


def _is_pin_followup(question: str) -> bool:
    normalized = question.casefold().strip()
    return any(
        marker in normalized
        for marker in [
            "mislim na pin",
            "mislio sam na pin",
            "mislila sam na pin",
            "postojeći pin",
            "postojeci pin",
            "za pin",
            "pin 2020",
        ]
    )


def _detect_accreditation_context(
    question: str,
    history: list[HistoryMessage],
) -> str | None:
    normalized_question = question.casefold().strip()
    pin_markers = [
        "mislim na pin",
        "mislio sam na pin",
        "mislila sam na pin",
        "pin 2020",
        "postojeći pin",
        "postojeci pin",
        "staru akreditaciju",
        "stara akreditacija",
        "stare akreditacije",
        "postojeći smer",
        "postojeci smer",
    ]
    pit_markers = [
        "mislim na pit",
        "mislio sam na pit",
        "mislila sam na pit",
        "pit 2027",
        "novu akreditaciju",
        "nova akreditacija",
        "nove akreditacije",
    ]

    if any(marker in normalized_question for marker in pit_markers):
        return "PIT 2027"
    if any(marker in normalized_question for marker in pin_markers):
        return "PIN 2020"
    if normalized_question in {"pin", "za pin"}:
        return "PIN 2020"
    if normalized_question in {"pit", "za pit"}:
        return "PIT 2027"

    for message in reversed(history[-MAX_HISTORY_MESSAGES:]):
        if message.role.strip().casefold() != "user":
            continue
        content = message.content.casefold().strip()
        if any(marker in content for marker in pit_markers) or content in {"pit", "za pit"}:
            return "PIT 2027"
        if any(marker in content for marker in pin_markers) or content in {"pin", "za pin"}:
            return "PIN 2020"

    return None


def _is_career_jobs_question(question: str) -> bool:
    normalized = question.casefold()
    return any(
        marker in normalized
        for marker in [
            "koji poslovi",
            "koje poslove",
            "poslovi postoje",
            "posao",
            "poslove",
            "šta mogu da radim",
            "sta mogu da radim",
            "posle ovog smera",
            "koristi ai",
            "koriste ai",
            "ai direktno",
            "data analyst",
            "business analyst",
            "bi analyst",
            "ai analyst",
            "ai alati",
            "uloge",
            "karijera",
        ]
    )


def _is_elective_recommendation_question(question: str, intents: list[str]) -> bool:
    normalized = question.casefold()
    if set(intents) & {
        "ELECTIVE_RECOMMENDATION",
        "INTEREST_BASED_RECOMMENDATION",
        "CAREER_RECOMMENDATION",
    }:
        return True
    return any(
        marker in normalized
        for marker in [
            "izborni",
            "izborne",
            "izbornih",
            "šta da izaberem",
            "sta da izaberem",
            "šta da uzmem",
            "sta da uzmem",
            "koji predmeti",
            "preporuči",
            "preporuci",
            "korisni predmeti",
            "zanima ai",
            "zanima me ai",
            "business analyst",
            "biznis analiti",
            "data analyst",
            "sap karijer",
            "erp karijer",
        ]
    )


def _history_has_elective_recommendation(history: list[HistoryMessage]) -> bool:
    for message in reversed(history[-MAX_HISTORY_MESSAGES:]):
        if message.role.strip().casefold() != "user":
            continue
        if _is_elective_recommendation_question(message.content, []):
            return True
    return False


def _needs_accreditation_assumption(
    question: str,
    intents: list[str],
    accreditation_context: str | None = None,
) -> bool:
    if accreditation_context is not None:
        return False
    intent_set = set(intents)
    if "COURSE_PLAN_CURRENT" in intent_set:
        return False
    if _mentions_current_delivery(question):
        return False
    if _has_explicit_accreditation_context(question):
        return False
    normalized = question.casefold()
    recommendation_signal = any(
        marker in normalized
        for marker in [
            "izborni",
            "preporu",
            "šta da izaberem",
            "sta da izaberem",
            "koji predmeti",
            "najbolji predmeti",
            "business analyst",
            "biznis analiti",
            "data analyst",
            "ai",
            "erp",
            "sap",
            "karijer",
            "perspektivan",
            "perspektivna",
        ]
    )
    return recommendation_signal or bool(
        intent_set
        & {
            "ELECTIVE_RECOMMENDATION",
            "CAREER_RECOMMENDATION",
            "INTEREST_BASED_RECOMMENDATION",
            "JOB_MARKET",
        }
    )


def _append_web_chat_instructions(
    messages: list[dict[str, str]],
    question: str,
    intents: list[str],
    accreditation_context: str | None = None,
) -> list[dict[str, str]]:
    if not messages:
        return messages

    instructions = [
        "Web chat instrukcije:",
        "- Piši prirodno, studentski i korisno; izbegavaj birokratske formulacije.",
        "- Odgovaraj u 4 do 7 kratkih celina. Koristi bullet liste kada nabrajaš predmete.",
        "- Ne piši preduge pasuse i ne ponavljaj disclaimere.",
        "- Za formalna pitanja o polaganju, ocenjivanju, statusu predmeta, aktuelnom izvođenju ili alatima koji se sada rade odgovaraj strogo na osnovu retrieved dokumenata.",
        "- Za preporuke o izbornim predmetima, šta izabrati, business/data/AI/ERP/SAP putanje i perspektivnost koristi dokumente kao osnovu, ali piši savetodavno i prirodno.",
        "- Preporuke ne predstavljaj kao zvanično rangiranje.",
        "- Za opšta karijerna objašnjenja smeš ukratko koristiti opšte znanje o ulozi, ali jasno odvoji opšte objašnjenje posla od veze sa PIT predmetima iz retrieved konteksta.",
        "- Za pitanja o poslovima i ulogama prvo odgovori koje uloge postoje; tek zatim objasni vezu sa predmetima ako je ima u retrieved kontekstu.",
        "- Za career/job pitanja jasno reci da smer i predmeti ne garantuju posao.",
        "- Za jače tehničke AI uloge kao data scientist, machine learning engineer ili AI engineer reci da je obično potrebno dodatno učenje programiranja, statistike, mašinskog učenja i portfolio projekti.",
        "- Ne izmišljaj formalna pravila fakulteta, rokove, nastavnike, cene, praksu, sertifikate ili garancije posla.",
        "- Za pitanja tipa predloži predmete ne nabrajaj previše; daj 3-5 glavnih preporuka i po potrebi reci da možeš detaljnije po putanji.",
        "- Ne predstavljaj \"PIT 2027\" kao naziv smera/modula bez objašnjenja.",
        "- Koristi \"Poslovne informacione tehnologije, skraćeno PIT\" kao naziv nove akreditacije/modula.",
        "- Koristi \"Poslovna informatika, skraćeno PIN\" za postojeći/stari naziv.",
        "- \"PIT 2027\" i \"PIN 2020\" tretiraj kao akreditacione oznake/verzije, ne kao marketinške nazive.",
    ]
    if accreditation_context == "PIN 2020":
        instructions.extend(
            [
                "- U prethodnom razgovoru korisnik je razjasnio da misli na PIN 2020. Za naredna follow-up pitanja zadrži taj kontekst, osim ako korisnik eksplicitno promeni akreditaciju.",
                "- Ne vraćaj se automatski na PIT 2027 i ne počinji odgovor PIT 2027 pretpostavkom.",
                "- Ako za PIN 2020 nema jednako detaljnih karijernih korpi kao za PIT 2027, reci to kratko i nastavi sa opštim karijernim objašnjenjem povezanim sa poslovnom informatikom.",
                "- Ako korisnik pita za izborne predmete u PIN kontekstu, svakako daj korisnu listu predmeta/tema, ali jasno napomeni da je baza detaljno trenirana pre svega na novoj akreditaciji PIT 2027 i da preporuka nije zvanična PIN mapa.",
            ]
        )
    elif accreditation_context == "PIT 2027":
        instructions.extend(
            [
                "- U prethodnom razgovoru korisnik je razjasnio da misli na PIT 2027. Za naredna follow-up pitanja zadrži taj kontekst, osim ako korisnik eksplicitno promeni akreditaciju.",
            ]
        )

    if _needs_accreditation_assumption(question, intents, accreditation_context):
        instructions.extend(
            [
                "- Korisnik nije eksplicitno naveo akreditaciju.",
                "- Pretpostavku označi kratko i prirodno, ne dupliraj uslovne fraze.",
                "- Dobra formulacija je: \"U nastavku polazim od PIT 2027, jer su izborne korpe i karijerne putanje definisane za tu verziju programa.\"",
                "- Možeš koristiti i kraće: \"Ako gledaš PIT 2027, ...\".",
                "- Ne koristi početak tipa: \"Ako misliš na PIT 2027, ako misliš...\".",
                "- Na kraju dodaj kratko: \"Ako misliš na postojeći PIN 2020, napiši mi i prilagodiću preporuku.\"",
                "- Nemoj prekidati odgovor potpitanjem; jasno označi pretpostavku i nastavi korisno.",
            ]
        )

    updated_messages = [dict(message) for message in messages]
    if updated_messages:
        updated_messages[0]["content"] = (
            updated_messages[0].get("content", "")
            + "\n\nAPI web chat dopuna: Za opšta karijerna objašnjenja smeš dati kratko opšte objašnjenje uloge, ali formalne informacije o fakultetu moraju ostati isključivo iz retrieved context-a."
        )
    updated_messages[-1]["content"] = (
        updated_messages[-1].get("content", "")
        + "\n\n"
        + "\n".join(instructions)
    )
    return updated_messages


def _apply_accreditation_assumption(
    answer: str,
    question: str,
    intents: list[str],
    accreditation_context: str | None = None,
) -> str:
    if not answer or not _needs_accreditation_assumption(
        question,
        intents,
        accreditation_context,
    ):
        return answer

    normalized_answer = answer.casefold()
    lead_pattern = re.compile(
        r"^\s*(?:ako\s+misliš\s+na\s+pit\s+2027|ako\s+gledaš\s+pit\s+2027)\s*,?\s*",
        flags=re.IGNORECASE,
    )
    if normalized_answer.lstrip().startswith("ako misliš na pit 2027, ako"):
        answer = lead_pattern.sub("", answer, count=1).lstrip()

    first_part = answer[:220].casefold()
    assumption_note = (
        "U nastavku polazim od PIT 2027, jer su izborne korpe i karijerne putanje "
        "definisane za tu verziju programa."
    )
    has_natural_assumption = (
        "u nastavku polazim od pit 2027" in first_part
        or "ako gledaš pit 2027" in first_part
        or "pit 2027" in first_part
    )
    if not has_natural_assumption:
        answer = assumption_note + "\n\n" + answer.lstrip()

    normalized_answer = answer.casefold()
    pin_note = "Ako misliš na postojeći PIN 2020, napiši mi i prilagodiću preporuku."
    already_has_pin_note = (
        "pin 2020" in normalized_answer
        and (
            "prilagodi" in normalized_answer
            or "postojeći modul poslovna informatika" in normalized_answer
            or "postojeći pin" in normalized_answer
            or "postojeci pin" in normalized_answer
        )
    )
    if pin_note.casefold() not in normalized_answer and not already_has_pin_note:
        answer = answer.rstrip() + "\n\n" + pin_note
    return answer


def _dedupe_pin_followup_note(answer: str) -> str:
    lines = answer.splitlines()
    seen_pin_note = False
    deduped_lines: list[str] = []

    for line in lines:
        normalized = line.casefold()
        is_pin_note = (
            "pin 2020" in normalized
            and "prilagodi" in normalized
            and ("ako misliš" in normalized or "ako mislis" in normalized)
        )
        if is_pin_note:
            if seen_pin_note:
                continue
            seen_pin_note = True
        deduped_lines.append(line)

    return "\n".join(deduped_lines).strip()


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


def _strip_final_source_section(answer: str) -> str:
    """Remove web-duplicated source lists while keeping CLI/prompt behavior unchanged."""
    pattern = re.compile(
        r"\n*\s*(?:\*\*)?\s*(?:Korišćeni izvori|Izvori)\s*:?\s*(?:\*\*)?\s*[\r\n]+.*\Z",
        flags=re.IGNORECASE | re.DOTALL,
    )
    return pattern.sub("", answer).rstrip()


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
    latency_ms: int | None = None,
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
    if latency_ms is not None:
        entry["latency_ms"] = latency_ms
    if error:
        entry["error"] = error
    return entry


def _elapsed_ms(start_time: float) -> int:
    return int((perf_counter() - start_time) * 1000)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "pit-navigator-api"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    start_time = perf_counter()
    conversation_id = request.conversation_id or str(uuid4())
    settings: Settings | None = None

    try:
        settings, retriever = _get_runtime()
        accreditation_context = _detect_accreditation_context(
            request.question,
            request.history,
        )
        pin_elective_followup = (
            accreditation_context == "PIN 2020"
            and (
                _is_elective_recommendation_question(request.question, [])
                or (_is_pin_followup(request.question) and _history_has_elective_recommendation(request.history))
            )
            and not _is_career_jobs_question(request.question)
        )
        effective_question = _build_effective_question(request.question, request.history)
        classification = classify(effective_question)
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
            if pin_elective_followup:
                response = ChatResponse(
                    conversation_id=conversation_id,
                    answer=PIN_ELECTIVES_MESSAGE,
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
                        latency_ms=_elapsed_ms(start_time),
                    )
                )
                return response
            if accreditation_context == "PIN 2020" and _is_career_jobs_question(request.question):
                response = ChatResponse(
                    conversation_id=conversation_id,
                    answer=PIN_AI_CAREER_MESSAGE,
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
                        latency_ms=_elapsed_ms(start_time),
                    )
                )
                return response
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
                    latency_ms=_elapsed_ms(start_time),
                )
            )
            return response

        context_results = _select_context_results(settings, results)
        if not context_results:
            if pin_elective_followup:
                response = ChatResponse(
                    conversation_id=conversation_id,
                    answer=PIN_ELECTIVES_MESSAGE,
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
                        latency_ms=_elapsed_ms(start_time),
                    )
                )
                return response
            if accreditation_context == "PIN 2020" and _is_career_jobs_question(request.question):
                response = ChatResponse(
                    conversation_id=conversation_id,
                    answer=PIN_AI_CAREER_MESSAGE,
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
                        latency_ms=_elapsed_ms(start_time),
                    )
                )
                return response
            if _is_pin_followup(request.question):
                response = ChatResponse(
                    conversation_id=conversation_id,
                    answer=PIN_FOLLOWUP_MESSAGE,
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
                        latency_ms=_elapsed_ms(start_time),
                    )
                )
                return response
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
                    latency_ms=_elapsed_ms(start_time),
                )
            )
            return response

        if _is_program_name_question(request.question):
            sources = collect_source_paths(context_results) if settings.include_sources else []
            response = ChatResponse(
                conversation_id=conversation_id,
                answer=PROGRAM_NAME_MESSAGE,
                sources=sources,
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
                    sources=response.sources,
                    detected_intents=response.detected_intents,
                    detected_course_names=response.detected_course_names,
                    provider=response.provider,
                    model=response.model,
                    fallback_used=response.fallback_used,
                    latency_ms=_elapsed_ms(start_time),
                )
            )
            return response

        if pin_elective_followup:
            response = ChatResponse(
                conversation_id=conversation_id,
                answer=PIN_ELECTIVES_MESSAGE,
                sources=collect_source_paths(context_results) if settings.include_sources else [],
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
                    sources=response.sources,
                    detected_intents=response.detected_intents,
                    detected_course_names=response.detected_course_names,
                    provider=response.provider,
                    model=response.model,
                    fallback_used=response.fallback_used,
                    latency_ms=_elapsed_ms(start_time),
                )
            )
            return response

        if accreditation_context == "PIN 2020" and _is_career_jobs_question(request.question):
            response = ChatResponse(
                conversation_id=conversation_id,
                answer=PIN_AI_CAREER_MESSAGE,
                sources=collect_source_paths(context_results) if settings.include_sources else [],
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
                    sources=response.sources,
                    detected_intents=response.detected_intents,
                    detected_course_names=response.detected_course_names,
                    provider=response.provider,
                    model=response.model,
                    fallback_used=response.fallback_used,
                    latency_ms=_elapsed_ms(start_time),
                )
            )
            return response

        if _is_pin_followup(request.question):
            response = ChatResponse(
                conversation_id=conversation_id,
                answer=PIN_FOLLOWUP_MESSAGE,
                sources=collect_source_paths(context_results) if settings.include_sources else [],
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
                    sources=response.sources,
                    detected_intents=response.detected_intents,
                    detected_course_names=response.detected_course_names,
                    provider=response.provider,
                    model=response.model,
                    fallback_used=response.fallback_used,
                    latency_ms=_elapsed_ms(start_time),
                )
            )
            return response

        messages = build_messages(
            effective_question,
            classification.intents,
            classification.course_names,
            context_results,
        )
        messages = _append_web_chat_instructions(
            messages,
            request.question,
            classification.intents,
            accreditation_context,
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
                    latency_ms=_elapsed_ms(start_time),
                    error=error,
                )
            )
            raise HTTPException(
                status_code=500,
                detail="Došlo je do greške pri obradi pitanja.",
            )

        answer = _apply_accreditation_assumption(
            _strip_final_source_section(answer),
            request.question,
            classification.intents,
            accreditation_context,
        )
        answer = _dedupe_pin_followup_note(answer)
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
                latency_ms=_elapsed_ms(start_time),
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
                latency_ms=_elapsed_ms(start_time),
                error=error,
            )
        )
        raise HTTPException(
            status_code=500,
            detail="Došlo je do greške pri obradi pitanja.",
        ) from None
