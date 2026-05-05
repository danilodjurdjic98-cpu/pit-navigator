from __future__ import annotations

import re
from dataclasses import dataclass


INTENTS = [
    "PROGRAM_OVERVIEW",
    "COURSE_EXPLANATION",
    "COURSE_PLAN_CURRENT",
    "ACCREDITATION_COMPARISON",
    "ELECTIVE_RECOMMENDATION",
    "CAREER_RECOMMENDATION",
    "INTEREST_BASED_RECOMMENDATION",
    "JOB_MARKET",
    "FALLBACK",
]


COURSE_PATTERNS: dict[str, list[str]] = {
    "ERP softver": ["erp", "sap"],
    "Razvoj softvera": ["razvoj softvera", "flask", "php"],
    "Objektno orijentisano programiranje": ["oop", "objektno"],
    "Mašinsko učenje": ["mašinsko", "masinsko"],
    "Operaciona istraživanja": ["operaciona"],
    "Baze podataka": ["baze", "baze podataka"],
    "Poslovna inteligencija": ["bi", "poslovna inteligencija"],
    "Poslovna analitika": ["poslovna analitika"],
    "Analiza podataka": ["analiza podataka"],
    "Elektronsko poslovanje i veštačka inteligencija": [
        "elektronsko poslovanje",
        "elvi",
    ],
    "Korisničko iskustvo i dizajn": ["ux", "korisnicko iskustvo", "korisničko iskustvo"],
    "Nove informacione tehnologije": [
        "nove informacione tehnologije",
        "nove informacione",
        "novih informacionih tehnologija",
        "nit",
    ],
    "Elektronska trgovina": [
        "elektronska trgovina",
        "elektronskoj trgovini",
        "elektronsku trgovinu",
    ],
    "Elektronski platni sistemi": [
        "elektronski platni sistemi",
        "elektronske platne sisteme",
        "elektronskih platnih sistema",
        "platni sistemi",
        "platne sisteme",
        "eps",
    ],
    "Ekonometrija": [
        "ekonometrija",
        "ekonometriji",
        "ekonometriju",
        "ekonometrije",
    ],
    "Kvantitativne finansije": [
        "kvantitativne finansije",
        "kvantitativnih finansija",
    ],
    "Ekonomska statistika": [
        "ekonomska statistika",
        "ekonomskoj statistici",
    ],
    "Analiza finansijskih izveštaja": [
        "analiza finansijskih izveštaja",
        "analiza finansijskih izvestaja",
    ],
    "Upravljačko računovodstvo": [
        "upravljačko računovodstvo",
        "upravljacko racunovodstvo",
    ],
    "Računovodstveni informacioni sistemi": [
        "računovodstveni informacioni sistemi",
        "racunovodstveni informacioni sistemi",
    ],
    "Istraživanje tržišta": [
        "istraživanje tržišta",
        "istrazivanje trzista",
    ],
}


@dataclass(frozen=True)
class Classification:
    intents: list[str]
    course_names: list[str]


def _contains_any(text: str, terms: list[str]) -> bool:
    return any(term in text for term in terms)


def detect_course_names(question: str) -> list[str]:
    normalized = question.casefold()
    detected: list[str] = []
    for course_name, aliases in COURSE_PATTERNS.items():
        for alias in aliases:
            pattern = r"(?<!\w)" + re.escape(alias.casefold()) + r"(?!\w)"
            if re.search(pattern, normalized):
                detected.append(course_name)
                break
    return detected


def classify(question: str) -> Classification:
    text = question.casefold()
    intents: list[str] = []
    course_names = detect_course_names(question)

    if _contains_any(text, ["pit", "smer", "program", "šta se tu uči", "sta se tu uci"]):
        intents.append("PROGRAM_OVERVIEW")
    if _contains_any(
        text,
        ["trenutno", "sada", "ove godine", "2025/26", "2025/2026", "kako se polaže", "kako se polaze", "ocenjuje", "ocenjivanje", "ocena", "poeni", "predispitne obaveze", "završni test", "zavrsni test", "kolokvijum", "ispit", "vežbe", "vezbe", "plan rada", "projekat", "predispitne", "koji alati"],
    ):
        intents.append("COURSE_PLAN_CURRENT")
    if _contains_any(
        text,
        [
            "šta je",
            "sta je",
            "šta se radi",
            "sta se radi",
            "čemu služi",
            "cemu sluzi",
            "koje teme",
            "da li je obavezan",
            "da li je obavezno",
            "obavezno",
            "obavezan",
            "obavezna",
            "izborno",
            "izborni",
            "izborna",
            "status predmeta",
            "koliko je važan",
            "koliko je vazan",
        ],
    ):
        intents.append("COURSE_EXPLANATION")
    if _contains_any(
        text,
        ["pin 2020", "pit 2027", "stara akreditacija", "nova akreditacija", "razlika", "šta se promenilo", "sta se promenilo", "zastareo", "modernizacija"],
    ):
        intents.append("ACCREDITATION_COMPARISON")
    if _contains_any(
        text,
        [
            "da li da izaberem",
            "šta da izaberem",
            "sta da izaberem",
            "koji da izaberem",
            "da li da uzmem",
            "šta da uzmem",
            "sta da uzmem",
            "koji izborni",
            "bolje",
            "bolji izbor",
            "šta je korisnije",
            "sta je korisnije",
            "izborni",
            "izborni predmet",
        ],
    ):
        intents.append("ELECTIVE_RECOMMENDATION")
    if " ili " in text and len(course_names) >= 2:
        intents.append("ELECTIVE_RECOMMENDATION")
    if _contains_any(
        text,
        ["zanima", "interesuje", "volim", "hoću da se bavim", "hocu da se bavim"],
    ):
        intents.append("INTEREST_BASED_RECOMMENDATION")
    if _contains_any(
        text,
        [
            "data analyst",
            "data engineer",
            "data inženjer",
            "data inzenjer",
            "data engineering",
            "inženjer podataka",
            "inzenjer podataka",
            "bi analitičar",
            "bi analiticar",
            "erp konsultant",
            "sap konsultant",
            "sap karijera",
            "erp karijera",
            "dobar za sap karijeru",
            "dobar za erp karijeru",
            "developer",
            "ai konsultant",
            "finansijski analitičar",
            "finansijski analiticar",
            "business analyst",
            "hoću da budem",
            "hocu da budem",
            "želim da budem",
            "zelim da budem",
            "karijera",
        ],
    ):
        intents.append("CAREER_RECOMMENDATION")
    if _contains_any(
        text,
        ["posao", "zapošljavanje", "zaposljavanje", "tržište", "trziste", "ai će pojesti", "ai ce pojesti", "plata"],
    ):
        intents.append("JOB_MARKET")
    if _contains_any(
        text,
        ["nastavnik", "nastavnici", "saradnik", "saradnici", "rok", "procedure", "praksa", "završni rad", "zavrsni rad", "seminarski", "ko drži", "ko drzi"],
    ):
        intents.append("FALLBACK")

    if not intents:
        intents.append("FALLBACK")

    return Classification(intents=list(dict.fromkeys(intents)), course_names=course_names)
