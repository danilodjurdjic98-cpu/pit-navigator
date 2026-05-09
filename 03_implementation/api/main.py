from __future__ import annotations

import json
import re
import sys
from collections.abc import Iterator
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter
from typing import Any
from uuid import uuid4

import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.config import Settings, load_settings  # noqa: E402
from src.generator import generate_answer, generate_answer_stream  # noqa: E402
from src.intent_classifier import Classification, classify, detect_course_names  # noqa: E402
from src.prompt_builder import build_messages, collect_source_paths  # noqa: E402
from src.retriever import Retriever  # noqa: E402


OUT_OF_SCOPE_MESSAGE = (
    "Za ovo nemam dovoljno precizan dokument u bazi znanja. Mogu da pomognem "
    "sa pitanjima o modulu PIT, predmetima, izbornim korpama i karijernim putanjama."
)
CERTIFICATE_MESSAGE = (
    "U dostupnim dokumentima nemam potvrdu da smer automatski nudi profesionalne "
    "sertifikate.\n\n"
    "Ispravno je reći da pojedini predmeti mogu dati osnovu za rad sa alatima i "
    "oblastima kao što su baze podataka, ERP/SAP, Power BI, Python, Java, web "
    "tehnologije ili AI alati, ali to nije isto što i zvaničan profesionalni "
    "sertifikat.\n\n"
    "Ako student želi sertifikat, to se obično proverava posebno: preko fakultetskih "
    "obaveštenja, partnerskih programa ili eksternih sertifikacionih kuća. PIT "
    "Navigator ne treba da tvrdi da sertifikat postoji ako to nije eksplicitno "
    "potvrđeno u dokumentima."
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
PIN_OUTLOOK_MESSAGE = (
    "Za postojeci modul Poslovna informatika, skraceno PIN (akreditacija PIN 2020), "
    "najpostenije je reci: perspektivan je kao poslovno-informaticki profil, ali "
    "ne treba ga posmatrati kao garanciju posla niti kao cisto programerski smer.\n\n"
    "Njegova prednost je sto spaja ekonomiju, poslovne procese, informacione sisteme, "
    "baze podataka, analitiku, ERP/SAP logiku i razvoj poslovnih aplikacija. To je "
    "dobar temelj za uloge kao sto su business analyst, BI/reporting analyst, ERP "
    "konsultant, data analyst pocetnog nivoa, IT/business consultant ili junior uloga "
    "u digitalnoj transformaciji.\n\n"
    "Za jacu konkurentnost na trzistu vazno je da uz fakultet gradis prakticne "
    "vestine: SQL, Excel/Power BI, osnove programiranja, razumevanje poslovnih "
    "procesa, projekte i praksu. Sa tim dodatkom PIN moze da bude vrlo upotrebljiva "
    "osnova, posebno za pozicije koje traze most izmedju biznisa i IT-ja.\n\n"
    "Ovo je AI procena, ne zvanicna garancija zaposlenja. Za PIN 2020 nemam jednako "
    "detaljno razradjene karijerne korpe kao za PIT 2027, pa ovo tretiraj kao "
    "karijernu orijentaciju, ne kao zvanican opis ishoda modula."
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
PIT_ELECTIVE_BASKETS_MESSAGE = (
    "Za PIT 2027 izborne predmete je najbolje gledati na dva nacina: formalno po "
    "izbornim pozicijama i prakticno po tematskim korpama.\n\n"
    "Formalne izborne pozicije u PIT 2027:\n\n"
    "Treca godina, peti semestar\n"
    "- Izborni predmet 1: Menadzment odnosa sa kupcima, Poresko planiranje, "
    "Finansijska i aktuarska matematika\n"
    "- Izborni predmet 2: Linearna algebra, Teorija verovatnoce\n\n"
    "Treca godina, sesti semestar\n"
    "- Izborni predmet 3: Racunovodstveni informacioni sistemi, Marketing, "
    "Organizacija, Finansijska ekonomija, Medjunarodne finansije, Monetarna "
    "ekonomija, Makroekonomski modeli, Ekonomija i biznis u turizmu\n"
    "- Izborni predmet 4: Analiza finansijskih izvestaja, Upravljacko "
    "racunovodstvo, Osnovi poslovnih finansija\n\n"
    "Cetvrta godina, sedmi semestar\n"
    "- Izborni predmet 1: Istrazivanje trzista, Operaciona istrazivanja\n\n"
    "Cetvrta godina, osmi semestar\n"
    "- Izborni predmet 2: Masinsko ucenje, Ekonometrija, Kvantitativne finansije, "
    "Ekonomska statistika\n"
    "- Izborni predmet 3: Elektronska trgovina, Nove informacione tehnologije, "
    "Elektronski platni sistemi\n\n"
    "Tematske korpe za lakse razmisljanje o karijeri:\n\n"
    "Data / AI / BI korpa:\n"
    "- Baze podataka, Analiza podataka, Poslovna analitika, Poslovna inteligencija, "
    "Operaciona istrazivanja, Masinsko ucenje, Elektronsko poslovanje i vestacka "
    "inteligencija, ERP softver\n\n"
    "Software / ERP / digital korpa:\n"
    "- Objektno orijentisano programiranje, Razvoj softvera, ERP softver, Baze "
    "podataka, Korisnicko iskustvo i dizajn, Elektronsko poslovanje i vestacka "
    "inteligencija, Elektronska trgovina, Elektronski platni sistemi, Nove "
    "informacione tehnologije\n\n"
    "Finance analytics korpa:\n"
    "- Analiza podataka, Poslovna analitika, Poslovna inteligencija, Operaciona "
    "istrazivanja, Masinsko ucenje, Ekonometrija, Kvantitativne finansije, "
    "Finansijska ekonomija, Analiza finansijskih izvestaja, Racunovodstveni "
    "informacioni sistemi\n\n"
    "Napomena: tematske korpe nisu formalno pravilo izbora, nego prakticna mapa po "
    "interesovanjima. Formalno, student bira predmete u okviru izbornih pozicija."
)
PIT_ELECTIVE_RECOMMENDATION_MESSAGE = (
    "Ako nemas vec jasno interesovanje, ja bih birao kombinaciju koja ti daje najjaci "
    "PIT profil: podaci + poslovni sistemi + finansijsko razumevanje + malo tehnicke "
    "osnove.\n\n"
    "Moja opsta preporuka po izbornim pozicijama:\n\n"
    "- Treca godina, peti semestar, Izborni predmet 1: Menadzment odnosa sa kupcima, "
    "ako zelis CRM, korisnike i poslovne sisteme. Ako te vise vuku finansije, onda "
    "Poresko planiranje ima smisla kao finansijsko-regulatorna dopuna.\n"
    "- Treca godina, peti semestar, Izborni predmet 2: Linearna algebra, jer je dobra "
    "osnova za podatke, modele, optimizaciju i masinsko ucenje.\n"
    "- Treca godina, sesti semestar, Izborni predmet 3: Racunovodstveni informacioni "
    "sistemi su vrlo jak izbor za PIT, jer povezuju racunovodstvo, ERP, poslovne "
    "podatke i informacione sisteme. Ako hoces ozbiljniji finansijski pravac, "
    "Finansijska ekonomija je takodje vazna opcija.\n"
    "- Treca godina, sesti semestar, Izborni predmet 4: Analiza finansijskih izvestaja "
    "je jedan od najkorisnijih finansijskih izbora za PIT, jer direktno jaca rad sa "
    "finansijskim podacima, BI-jem i poslovnim odlucivanjem. Za ambiciozniji "
    "menadzersko-kontrolni pravac, Upravljacko racunovodstvo je takodje vrlo dobro.\n"
    "- Cetvrta godina, sedmi semestar: Operaciona istrazivanja, jer daju Python, "
    "optimizaciju, simulacije i analiticko modeliranje.\n"
    "- Cetvrta godina, osmi semestar, Izborni predmet 2: Masinsko ucenje ako te vise "
    "zanima AI/data; Ekonometrija ili Kvantitativne finansije ako hoces da pojacas "
    "finansijsko-analiticki profil.\n"
    "- Cetvrta godina, osmi semestar, Izborni predmet 3: Elektronska trgovina za "
    "e-commerce/digital business, ili Elektronski platni sistemi ako te zanimaju "
    "fintech i digitalna placanja.\n\n"
    "Najuravnotezenija PIT kombinacija bi bila: Linearna algebra, Racunovodstveni "
    "informacioni sistemi, Analiza finansijskih izvestaja, Operaciona istrazivanja, "
    "pa zatim Masinsko ucenje ili Kvantitativne finansije/Ekonometrija, zavisno od "
    "toga da li vise zelis AI/data ili finance analytics.\n\n"
    "Posebno bih naglasio finansijske predmete: Analiza finansijskih izvestaja, "
    "Upravljacko racunovodstvo, Racunovodstveni informacioni sistemi, Finansijska "
    "ekonomija, Ekonometrija i Kvantitativne finansije nisu sporedni za PIT. Oni daju "
    "kontekst da podatke i sisteme povezes sa realnim poslovnim odlukama, izvestajima, "
    "ERP/SAP procesima i finansijskom analitikom."
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
    question: str = Field(..., min_length=1, max_length=2000)
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


@dataclass(frozen=True)
class ChatGenerationContext:
    conversation_id: str
    question: str
    messages: list[dict[str, str]]
    sources: list[str]
    detected_intents: list[str]
    detected_course_names: list[str]
    accreditation_context: str | None


@asynccontextmanager
async def lifespan(app: FastAPI):
    loop = asyncio.get_event_loop()
    try:
        await loop.run_in_executor(None, _get_runtime)
    except Exception as exc:
        print(f"[startup] Pre-warm failed (index may be missing): {exc}")
    yield


app = FastAPI(title="PIT Navigator API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://pin.ekof.bg.ac.rs",
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
            "modul poslovna informatika",
            "smer poslovna informatika",
            "mislim na stari",
            "stari modul",
            "starom modulu",
            "stari smer",
            "starom smeru",
            "stara verzija",
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
        "modul poslovna informatika",
        "smer poslovna informatika",
        "mislim na stari",
        "stari modul",
        "starom modulu",
        "stari smer",
        "starom smeru",
        "stara verzija",
    ]
    pit_markers = [
        "mislim na pit",
        "mislio sam na pit",
        "mislila sam na pit",
        "pit 2027",
        "na pit",
        "za pit",
        "modul pit",
        "smer pit",
        "pit modul",
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


def _is_employment_outlook_question(question: str) -> bool:
    normalized = question.casefold()
    if any(
        marker in normalized
        for marker in [
            "kompetent",
            "trzistu",
            "tržištu",
            "tržište rada",
            "zavrsim",
            "završim",
            "budućnost",
        ]
    ):
        return True
    return any(
        marker in normalized
        for marker in [
            "perspektiv",
            "zaposl",
            "posao",
            "poslove",
            "poslova",
            "trziste rada",
            "tržište rada",
            "plata",
            "plate",
            "karijer",
            "isplati",
            "isplativo",
            "buducnost",
            "budućnost",
        ]
    )


def _is_program_level_career_question(question: str) -> bool:
    normalized = question.casefold()
    return _is_employment_outlook_question(question) and any(
        marker in normalized
        for marker in [
            "smer",
            "modul",
            "program",
            "profil",
            "kad zavrsim",
            "kad završim",
            "kada zavrsim",
            "kada završim",
            "zavrsim ovaj",
            "završim ovaj",
        ]
    )


def _is_certificate_question(question: str) -> bool:
    normalized = question.casefold()
    return any(
        marker in normalized
        for marker in [
            "sertifikat",
            "sertifikate",
            "sertifikata",
            "sertifikaciju",
            "certifikat",
            "certificate",
        ]
    )


def _is_elective_basket_list_question(question: str) -> bool:
    normalized = question.casefold()
    has_elective_marker = any(
        marker in normalized
        for marker in [
            "korpa",
            "korpe",
            "korpama",
            "izborne",
            "izborni",
            "izbornih",
            "izborne pozicije",
        ]
    )
    has_list_marker = any(
        marker in normalized
        for marker in [
            "spisak",
            "lista",
            "listu",
            "sve",
            "svih",
            "daj",
            "navedi",
            "nabroj",
            "po korpama",
        ]
    )
    return has_elective_marker and has_list_marker


def _is_generic_elective_pick_question(question: str) -> bool:
    normalized = question.casefold()
    if any(
        marker in normalized
        for marker in [
            "ai",
            "data",
            "bi",
            "erp",
            "sap",
            "program",
            "developer",
            "finans",
            "marketing",
            "e-commerce",
            "fintech",
        ]
    ):
        return False
    return any(
        marker in normalized
        for marker in [
            "koje predlazes",
            "koje predlaÅ¾eÅ¡",
            "sta predlazes",
            "Å¡ta predlaÅ¾eÅ¡",
            "sta da uzmem",
            "Å¡ta da uzmem",
            "koje da uzmem",
            "koje da izaberem",
            "sta da izaberem",
            "Å¡ta da izaberem",
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


def _history_has_employment_outlook_question(history: list[HistoryMessage]) -> bool:
    for message in reversed(history[-MAX_HISTORY_MESSAGES:]):
        if message.role.strip().casefold() != "user":
            continue
        if _is_employment_outlook_question(message.content):
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
    if _is_employment_outlook_question(question):
        instructions.extend(
            [
                "- Ako korisnik pita za perspektivu, zaposlenje, poslove, plate ili isplativost, odgovori kao AI/Gemini procena zasnovana na dostupnom kontekstu i opstem karijernom rasudjivanju.",
                "- U takvom odgovoru eksplicitno napomeni kratko: \"Ovo je AI procena, ne zvanicna garancija zaposlenja.\"",
                "- Budi koristan i konkretan: navedi zasto je pravac perspektivan, koje uloge su realisticne i sta student treba dodatno da gradi kroz vestine, projekte i praksu.",
                "- Ne navodi plate, rokove zaposljavanja ili sigurnost posla kao cinjenice.",
            ]
        )
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


def _make_response(
    *,
    conversation_id: str,
    answer: str,
    sources: list[str] | None = None,
    provider: str = "",
    model: str = "",
    fallback_used: bool = False,
    detected_intents: list[str] | None = None,
    detected_course_names: list[str] | None = None,
) -> ChatResponse:
    return ChatResponse(
        conversation_id=conversation_id,
        answer=answer,
        sources=sources or [],
        provider=provider,
        model=model,
        fallback_used=fallback_used,
        detected_intents=detected_intents or [],
        detected_course_names=detected_course_names or [],
    )


def _log_response(
    response: ChatResponse,
    request: ChatRequest,
    start_time: float,
    error: str | None = None,
) -> None:
    _write_chat_log(
        _base_log_entry(
            conversation_id=response.conversation_id,
            question=request.question,
            answer=response.answer,
            sources=response.sources,
            detected_intents=response.detected_intents,
            detected_course_names=response.detected_course_names,
            provider=response.provider,
            model=response.model,
            fallback_used=response.fallback_used,
            latency_ms=_elapsed_ms(start_time),
            error=error,
        )
    )


def _prepare_chat(
    request: ChatRequest,
    conversation_id: str,
    settings: Settings,
    retriever: Retriever,
    start_time: float,
) -> ChatResponse | ChatGenerationContext:
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
    pin_outlook_followup = (
        accreditation_context == "PIN 2020"
        and (
            _is_employment_outlook_question(request.question)
            or (_is_pin_followup(request.question) and _history_has_employment_outlook_question(request.history))
        )
    )
    is_program_level_career = _is_program_level_career_question(request.question)
    current_question_course_names = detect_course_names(request.question)
    effective_question = (
        request.question
        if is_program_level_career or current_question_course_names
        else _build_effective_question(request.question, request.history)
    )
    classification = classify(effective_question)
    if is_program_level_career:
        classification = Classification(
            intents=["PROGRAM_OVERVIEW", "CAREER_RECOMMENDATION", "JOB_MARKET"],
            course_names=[],
        )
    if pin_outlook_followup:
        classification = Classification(
            intents=list(
                dict.fromkeys(classification.intents + ["PROGRAM_OVERVIEW", "CAREER_RECOMMENDATION", "JOB_MARKET"])
            ),
            course_names=[],
        )
        response = _make_response(
            conversation_id=conversation_id,
            answer=PIN_OUTLOOK_MESSAGE,
            sources=[],
            detected_intents=classification.intents,
            detected_course_names=classification.course_names,
        )
        _log_response(response, request, start_time)
        return response
    if accreditation_context != "PIN 2020" and _is_elective_basket_list_question(request.question):
        classification = Classification(
            intents=list(dict.fromkeys(classification.intents + ["ELECTIVE_RECOMMENDATION"])),
            course_names=[],
        )
        response = _make_response(
            conversation_id=conversation_id,
            answer=PIT_ELECTIVE_BASKETS_MESSAGE,
            sources=[],
            detected_intents=classification.intents,
            detected_course_names=classification.course_names,
        )
        _log_response(response, request, start_time)
        return response
    if accreditation_context != "PIN 2020" and _is_generic_elective_pick_question(request.question):
        classification = Classification(
            intents=list(
                dict.fromkeys(
                    classification.intents
                    + ["ELECTIVE_RECOMMENDATION", "INTEREST_BASED_RECOMMENDATION"]
                )
            ),
            course_names=[],
        )
        response = _make_response(
            conversation_id=conversation_id,
            answer=PIT_ELECTIVE_RECOMMENDATION_MESSAGE,
            sources=[],
            detected_intents=classification.intents,
            detected_course_names=classification.course_names,
        )
        _log_response(response, request, start_time)
        return response
    if _is_certificate_question(request.question):
        classification = Classification(
            intents=list(dict.fromkeys(classification.intents + ["PROGRAM_OVERVIEW"])),
            course_names=[],
        )
        response = _make_response(
            conversation_id=conversation_id,
            answer=CERTIFICATE_MESSAGE,
            sources=[],
            detected_intents=classification.intents,
            detected_course_names=classification.course_names,
        )
        _log_response(response, request, start_time)
        return response
    results = retriever.search(
        effective_question,
        classification.intents,
        settings.top_k,
        classification.course_names,
    )

    def direct(answer: str, sources: list[str] | None = None) -> ChatResponse:
        response = _make_response(
            conversation_id=conversation_id,
            answer=answer,
            sources=sources,
            detected_intents=classification.intents,
            detected_course_names=classification.course_names,
        )
        _log_response(response, request, start_time)
        return response

    if (
        not results
        or (
            settings.refuse_out_of_scope
            and results[0].score < settings.min_retrieval_score
        )
    ):
        if pin_elective_followup:
            return direct(PIN_ELECTIVES_MESSAGE)
        if (
            accreditation_context == "PIN 2020"
            and _is_career_jobs_question(request.question)
            and not _is_employment_outlook_question(request.question)
        ):
            return direct(PIN_AI_CAREER_MESSAGE)
        return direct(OUT_OF_SCOPE_MESSAGE)

    context_results = _select_context_results(settings, results)
    if not context_results:
        if pin_elective_followup:
            return direct(PIN_ELECTIVES_MESSAGE)
        if (
            accreditation_context == "PIN 2020"
            and _is_career_jobs_question(request.question)
            and not _is_employment_outlook_question(request.question)
        ):
            return direct(PIN_AI_CAREER_MESSAGE)
        if _is_pin_followup(request.question):
            return direct(PIN_FOLLOWUP_MESSAGE)
        return direct(OUT_OF_SCOPE_MESSAGE)

    sources = collect_source_paths(context_results) if settings.include_sources else []

    if _is_program_name_question(request.question):
        return direct(PROGRAM_NAME_MESSAGE, sources)
    if pin_elective_followup:
        return direct(PIN_ELECTIVES_MESSAGE, sources)
    if (
        accreditation_context == "PIN 2020"
        and _is_career_jobs_question(request.question)
        and not _is_employment_outlook_question(request.question)
    ):
        return direct(PIN_AI_CAREER_MESSAGE, sources)
    if _is_pin_followup(request.question):
        return direct(PIN_FOLLOWUP_MESSAGE, sources)

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
    return ChatGenerationContext(
        conversation_id=conversation_id,
        question=request.question,
        messages=messages,
        sources=sources,
        detected_intents=classification.intents,
        detected_course_names=classification.course_names,
        accreditation_context=accreditation_context,
    )


def _finalize_generated_answer(
    answer: str,
    request: ChatRequest,
    context: ChatGenerationContext,
) -> str:
    answer = _apply_accreditation_assumption(
        _strip_final_source_section(answer),
        request.question,
        context.detected_intents,
        context.accreditation_context,
    )
    return _dedupe_pin_followup_note(answer)


def _sse_event(event: str, data: dict[str, Any]) -> str:
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "pit-navigator-api"}


@app.get("/health/deep")
def health_deep() -> dict[str, Any]:
    try:
        settings, retriever = _get_runtime()
        return {
            "status": "ok",
            "service": "pit-navigator-api",
            "model_loaded": retriever.model is not None,
            "index_chunks": len(retriever.chunks),
            "provider": settings.llm_provider,
            "fallback_provider": settings.llm_fallback_provider,
        }
    except Exception as exc:
        return {"status": "error", "detail": str(exc)[:200]}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    start_time = perf_counter()
    conversation_id = request.conversation_id or str(uuid4())
    settings: Settings | None = None

    try:
        settings, retriever = _get_runtime()
        prepared = _prepare_chat(request, conversation_id, settings, retriever, start_time)
        if isinstance(prepared, ChatResponse):
            return prepared

        generation_result = generate_answer(prepared.messages, settings)
        answer = _provider_value(generation_result, "answer", "") or ""
        provider = _provider_value(generation_result, "provider", settings.llm_provider) or ""
        model = _provider_value(generation_result, "model", _model_for_settings(settings)) or ""
        fallback_used = bool(_provider_value(generation_result, "fallback_used", False))
        generator_error = _provider_value(generation_result, "error")

        if not answer:
            error = _sanitize_error(generator_error or "Generator nije vratio odgovor.", settings)
            _write_chat_log(
                _base_log_entry(
                    conversation_id=prepared.conversation_id,
                    question=request.question,
                    sources=prepared.sources,
                    detected_intents=prepared.detected_intents,
                    detected_course_names=prepared.detected_course_names,
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

        final_answer = _finalize_generated_answer(answer, request, prepared)
        response = _make_response(
            conversation_id=prepared.conversation_id,
            answer=final_answer,
            sources=prepared.sources,
            provider=provider,
            model=model,
            fallback_used=fallback_used,
            detected_intents=prepared.detected_intents,
            detected_course_names=prepared.detected_course_names,
        )
        _log_response(
            response,
            request,
            start_time,
            error=_sanitize_error(generator_error, settings) if generator_error else None,
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


@app.post("/chat/stream")
def chat_stream(request: ChatRequest) -> StreamingResponse:
    start_time = perf_counter()
    conversation_id = request.conversation_id or str(uuid4())
    settings: Settings | None = None

    def event_stream() -> Iterator[str]:
        nonlocal settings
        try:
            settings, retriever = _get_runtime()
            prepared = _prepare_chat(request, conversation_id, settings, retriever, start_time)
            if isinstance(prepared, ChatResponse):
                yield _sse_event(
                    "final",
                    {
                        "conversation_id": prepared.conversation_id,
                        "answer": prepared.answer,
                        "sources": prepared.sources,
                        "provider": prepared.provider,
                        "model": prepared.model,
                        "fallback_used": prepared.fallback_used,
                        "detected_intents": prepared.detected_intents,
                        "detected_course_names": prepared.detected_course_names,
                    },
                )
                return

            yield _sse_event(
                "meta",
                {
                    "conversation_id": prepared.conversation_id,
                    "sources": prepared.sources,
                    "detected_intents": prepared.detected_intents,
                    "detected_course_names": prepared.detected_course_names,
                },
            )

            raw_answer_parts: list[str] = []
            provider = settings.llm_provider
            model = _model_for_settings(settings)
            fallback_used = False
            generator_error: Any = None

            for generation_event in generate_answer_stream(prepared.messages, settings):
                event_type = generation_event.get("type")
                if event_type == "token":
                    token = generation_event.get("text", "")
                    if token:
                        raw_answer_parts.append(token)
                        yield _sse_event("token", {"text": token})
                    continue
                if event_type == "final":
                    provider = generation_event.get("provider", provider) or ""
                    model = generation_event.get("model", model) or ""
                    fallback_used = bool(generation_event.get("fallback_used", False))
                    generator_error = generation_event.get("error")
                    break
                if event_type == "error":
                    provider = generation_event.get("provider", provider) or ""
                    model = generation_event.get("model", model) or ""
                    fallback_used = bool(generation_event.get("fallback_used", False))
                    generator_error = generation_event.get("error")
                    error = _sanitize_error(generator_error or "Generator nije vratio odgovor.", settings)
                    _write_chat_log(
                        _base_log_entry(
                            conversation_id=prepared.conversation_id,
                            question=request.question,
                            sources=prepared.sources,
                            detected_intents=prepared.detected_intents,
                            detected_course_names=prepared.detected_course_names,
                            provider=provider,
                            model=model,
                            fallback_used=fallback_used,
                            latency_ms=_elapsed_ms(start_time),
                            error=error,
                        )
                    )
                    yield _sse_event("error", {"detail": "Doslo je do greske pri obradi pitanja."})
                    return

            raw_answer = "".join(raw_answer_parts)
            if not raw_answer:
                error = _sanitize_error(generator_error or "Generator nije vratio odgovor.", settings)
                _write_chat_log(
                    _base_log_entry(
                        conversation_id=prepared.conversation_id,
                        question=request.question,
                        sources=prepared.sources,
                        detected_intents=prepared.detected_intents,
                        detected_course_names=prepared.detected_course_names,
                        provider=provider,
                        model=model,
                        fallback_used=fallback_used,
                        latency_ms=_elapsed_ms(start_time),
                        error=error,
                    )
                )
                yield _sse_event("error", {"detail": "Doslo je do greske pri obradi pitanja."})
                return

            final_answer = _finalize_generated_answer(raw_answer, request, prepared)
            response = _make_response(
                conversation_id=prepared.conversation_id,
                answer=final_answer,
                sources=prepared.sources,
                provider=provider,
                model=model,
                fallback_used=fallback_used,
                detected_intents=prepared.detected_intents,
                detected_course_names=prepared.detected_course_names,
            )
            _log_response(
                response,
                request,
                start_time,
                error=_sanitize_error(generator_error, settings) if generator_error else None,
            )
            yield _sse_event(
                "final",
                {
                    "conversation_id": response.conversation_id,
                    "answer": response.answer,
                    "sources": response.sources,
                    "provider": response.provider,
                    "model": response.model,
                    "fallback_used": response.fallback_used,
                    "detected_intents": response.detected_intents,
                    "detected_course_names": response.detected_course_names,
                },
            )
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
            yield _sse_event("error", {"detail": "Doslo je do greske pri obradi pitanja."})

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
