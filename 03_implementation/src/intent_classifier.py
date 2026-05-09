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


PROGRAM_NAME_QUERY_TERMS = [
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


COURSE_PATTERNS: dict[str, list[str]] = {
    "ERP softver": ["erp", "sap"],
    "Razvoj softvera": [
        "razvoj softvera",
        "razvoju softvera",
        "razvoja softvera",
        "razvojem softvera",
        "predmet razvoj softvera",
        "predmetu razvoj softvera",
        "flask",
        "php",
    ],
    "Objektno orijentisano programiranje": ["oop", "objektno"],
    "Mašinsko učenje": ["mašinsko", "masinsko"],
    "Operaciona istraživanja": ["operaciona"],
    "Baze podataka": ["baze", "baze podataka"],
    "Poslovna inteligencija": ["bi", "poslovna inteligencija"],
    "Poslovna analitika": [
        "poslovna analitika",
        "poslovne analitike",
        "poslovnoj analitici",
        "predmet poslovna analitika",
        "predmetu poslovna analitika",
    ],
    "Poslovna informatika": [
        "poslovna informatika",
        "poslovne informatike",
        "poslovnoj informatici",
        "poslovnu informatiku",
        "poslovni informacioni sistemi",
    ],
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

    if _contains_any(text, PROGRAM_NAME_QUERY_TERMS):
        intents.append("PROGRAM_OVERVIEW")
        if _contains_any(text, ["pin", "pit"]):
            intents.append("ACCREDITATION_COMPARISON")
    if _contains_any(text, ["pit", "smer", "program", "šta se tu uči", "sta se tu uci"]):
        intents.append("PROGRAM_OVERVIEW")
    if course_names and _contains_any(text, ["konkretno", "predmet", "predmetu"]):
        intents.append("COURSE_EXPLANATION")
    if _contains_any(
        text,
        ["trenutno", "sada", "ove godine", "2025/26", "2025/2026", "kako se polaže", "kako se polaze", "ocenjuje", "ocenjivanje", "ocena", "poeni", "predispitne obaveze", "završni test", "zavrsni test", "kolokvijum", "ispit", "vežbe", "vezbe", "plan rada", "projekat", "predispitne", "koji alati", "šta se radi na predmetu", "sta se radi na predmetu", "šta se uči na", "sta se uci na", "da li se na", "radi sql", "radi java", "radi power bi", "radi erp"],
    ):
        intents.append("COURSE_PLAN_CURRENT")
    if course_names and _contains_any(text, ["sta se radi na", "šta se radi na"]):
        intents.append("COURSE_PLAN_CURRENT")
    if _contains_any(text, ["sta se konkretno radi", "šta se konkretno radi", "konkretno radi"]):
        intents.append("COURSE_PLAN_CURRENT")
    if _contains_any(
        text,
        [
            "programski jezik",
            "programski jezici",
            "koji jezik",
            "koji programski",
            "neki programski",
            "radi php",
            "radi python",
            "radi flask",
            "php",
            "python",
            "flask",
        ],
    ):
        intents.append("COURSE_PLAN_CURRENT")
    if _contains_any(
        text,
        [
            "šta je",
            "sta je",
            "šta se radi",
            "sta se radi",
            "šta se uči",
            "sta se uci",
            "čemu služi",
            "cemu sluzi",
            "koje teme",
            "koja je uloga",
            "uloga",
            "šta su",
            "sta su",
            "šta se iz",
            "sta se iz",
            "konkretno predmet",
            "konkretno o predmetu",
            "konkretno za predmet",
            "predmet ",
            "predmetu ",
            "koje karijere",
            "karijere",
            "ovaj predmet",
            "course plan",
            "course_plan",
            "kao predmet",
            "opiši predmet",
            "opisi predmet",
            "objasni predmet",
            "da li ",
            "da li se",
            "da li je",
            "da li su",
            "uključuje",
            "ukljucuje",
            "obuhvata",
            "pokriva",
            "pomaže",
            "pomaze",
            "dovoljna",
            "dovoljan",
            "dovoljno",
            "korisna",
            "koristan",
            "veza",
            "povezuje",
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
            "bi analyst",
            "ai analyst",
            "ai alati",
            "hoću da budem",
            "hocu da budem",
            "želim da budem",
            "zelim da budem",
            "karijera",
            "kompetent",
            "uloge",
            "posle ovog smera",
            "zavrsim ovaj smer",
            "završim ovaj smer",
        ],
    ):
        intents.append("CAREER_RECOMMENDATION")
    if _contains_any(
        text,
        [
            "posao",
            "poslovi",
            "poslove",
            "radim",
            "zapošljavanje",
            "zaposljavanje",
            "tržište",
            "trziste",
            "koristi ai",
            "koriste ai",
            "ai će pojesti",
            "ai ce pojesti",
            "plata",
            "kompetent",
            "trzistu",
            "tržištu",
            "zavrsim",
            "završim",
        ],
    ):
        intents.append("JOB_MARKET")
    if _contains_any(
        text,
        ["nastavnik", "nastavnici", "saradnik", "saradnici", "rok", "procedure", "praksa", "završni rad", "zavrsni rad", "seminarski", "ko drži", "ko drzi"],
    ):
        intents.append("FALLBACK")

    if not intents:
        intents.append("FALLBACK")

    deduped_intents = list(dict.fromkeys(intents))
    if "programski" in text and "PROGRAM_OVERVIEW" in deduped_intents:
        deduped_intents.remove("PROGRAM_OVERVIEW")

    return Classification(intents=deduped_intents, course_names=course_names)
