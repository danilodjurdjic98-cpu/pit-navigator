from __future__ import annotations

import json
from typing import Any


MAX_CHUNK_CHARS = 2500


def _get_value(item: Any, key: str, default: Any = "") -> Any:
    if isinstance(item, dict):
        return item.get(key, default)
    return getattr(item, key, default)


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def _truncate_text(text: str, max_chars: int = MAX_CHUNK_CHARS) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + "\n[skraćeno]"


def build_system_prompt() -> str:
    return """Ti si PIT Navigator, asistent koji odgovara isključivo na osnovu interne knowledge base dokumentacije.

Odgovaraj na srpskom.
Ne izmišljaj informacije.
Nikad ne odgovaraj na osnovu opšteg znanja, samo na osnovu retrieved context-a.
Ako nema dovoljno informacija u retrieved context-u, koristi fallback formulaciju.
Ako retrieved kontekst ne sadrži informacije relevantne za pitanje, ne odgovaraj iz opšteg znanja. Reci: "Za ovo nemam dovoljno precizan dokument u bazi znanja. Mogu da pomognem sa pitanjima o modulu PIT, predmetima, izbornim korpama i karijernim putanjama."
Jasno razlikuj PIT 2027 i PIN 2020.
Ne predstavljaj "PIT 2027" kao naziv smera/modula bez objašnjenja.
Za naziv nove akreditacije/modula koristi "Poslovne informacione tehnologije, skraćeno PIT".
Za postojeći/stari naziv koristi "Poslovna informatika, skraćeno PIN".
"PIT 2027" i "PIN 2020" tretiraj kao akreditacione oznake/verzije, ne kao marketinške nazive.
Jasno razlikuj course dokument i aktuelni course_plan.
Ne predstavljaj izborne predmete kao obavezne.
Ne komentariši nastavnike i saradnike.
Ne preporučuj predmete zbog nastavnika.
Ne obećavaj posao, platu, praksu ili sertifikat.
Ne tvrdi da je PIN 2020 zastareo.
Ne tvrdi da je PIT 2027 objektivno bolji za svakog studenta.
Za minor electives bez posebnog course dokumenta ne izmišljaj detalje o ocenjivanju, alatima ili nedeljnom planu.
Ako korisnik pita za nastavnike, koristi neutralni policy odgovor.
Ako korisnik pita za posao, budi realističan i ne garantuj ishod."""


def format_retrieved_context(retrieved_chunks: list[Any], max_chunks: int = 8) -> str:
    if not retrieved_chunks:
        return (
            "Nema relevantnog retrieved context-a. Odgovor mora koristiti fallback "
            "i jasno reći: \"Za ovo nemam dovoljno precizan dokument u bazi znanja. "
            "Mogu da pomognem sa pitanjima o modulu PIT, predmetima, izbornim korpama "
            "i karijernim putanjama.\""
        )

    formatted_chunks: list[str] = []
    for index, chunk in enumerate(retrieved_chunks[:max_chunks], start=1):
        path = _get_value(chunk, "path")
        title = _get_value(chunk, "title")
        document_type = _get_value(chunk, "document_type")
        section_heading = _get_value(chunk, "section_heading")
        score = _get_value(chunk, "score")
        contextual_prefix = _get_value(chunk, "contextual_prefix")
        content = (
            _get_value(chunk, "original_chunk_text")
            or _get_value(chunk, "text")
            or _get_value(chunk, "contextual_chunk_text")
        )

        if isinstance(score, float):
            score_text = f"{score:.4f}"
        else:
            score_text = str(score) if score != "" else ""

        lines = [
            f"[Source {index}]",
            f"path: {path}",
            f"title: {title}",
            f"document_type: {document_type}",
            f"section_heading: {section_heading}",
            f"score: {score_text}",
        ]
        if contextual_prefix:
            lines.append(f"contextual_prefix_metadata: {contextual_prefix}")
        lines.extend(
            [
                "content:",
                _truncate_text(str(content or "")),
            ]
        )
        formatted_chunks.append("\n".join(lines))

    return "\n\n".join(formatted_chunks)


def collect_source_paths(retrieved_chunks: list[Any]) -> list[str]:
    source_paths: list[str] = []
    seen: set[str] = set()

    for chunk in retrieved_chunks:
        path = str(_get_value(chunk, "path", "") or "")
        if path and path not in seen:
            source_paths.append(path)
            seen.add(path)

    return source_paths


def build_user_prompt(
    question: str,
    detected_intents: list[str],
    detected_course_names: list[str],
    retrieved_chunks: list[Any],
) -> str:
    intents = ", ".join(_as_list(detected_intents)) or "-"
    course_names = ", ".join(_as_list(detected_course_names)) or "-"
    retrieved_context = format_retrieved_context(retrieved_chunks)
    source_paths = collect_source_paths(retrieved_chunks)
    source_hint = "\n".join(f"- {path}" for path in source_paths) or "- nema izvora"
    career_rule = ""
    if any(intent in detected_intents for intent in ["CAREER_RECOMMENDATION", "JOB_MARKET"]):
        career_rule = (
            "\n- Za karijerna pitanja eksplicitno navedi da predmeti i modul mogu dati "
            "osnovu i orijentaciju, ali ne garantuju posao, praksu, platu, sertifikat "
            "ili zaposlenje."
        )

    return f"""Korisničko pitanje:
{question}

Detected intents:
{intents}

Detected course names:
{course_names}

Retrieved context:
{retrieved_context}

Pravila odgovora:
- Odgovori samo na osnovu retrieved context-a.
- Nikad ne odgovaraj na osnovu opšteg znanja, samo na osnovu retrieved context-a.
- Ako kontekst nije dovoljan, reci da nema dovoljno precizan dokument u bazi znanja.
- Ako retrieved kontekst ne sadrži informacije relevantne za pitanje, ne odgovaraj iz opšteg znanja. Reci: "Za ovo nemam dovoljno precizan dokument u bazi znanja. Mogu da pomognem sa pitanjima o modulu PIT, predmetima, izbornim korpama i karijernim putanjama."
- Ne dodaj činjenice koje nisu u kontekstu.
- Ako je predmet izborni, jasno reci da je izborni.
- Ako je pitanje o aktuelnom izvođenju, koristi course_plan kao primarni izvor.
- Ako je pitanje o formalnom PIT 2027 opisu, koristi course kao primarni izvor.
- Ne predstavljaj "PIT 2027" kao naziv smera/modula bez objašnjenja; naziv je "Poslovne informacione tehnologije, skraćeno PIT", dok je "PIT 2027" akreditaciona oznaka/verzija.
- Za postojeći/stari naziv koristi "Poslovna informatika, skraćeno PIN"; "PIN 2020" je akreditaciona oznaka/verzija.
- Ako je pitanje o izboru predmeta, objasni da je preporuka po interesovanju, ne zvanično rangiranje.
- Ako je pitanje o nastavniku, ne komentariši nastavnika.
- Ako je pitanje o poslu, ne garantuj posao.{career_rule}
- Na kraju dodaj sekciju "Korišćeni izvori:" sa path vrednostima korišćenih dokumenata.

Kandidati za korišćene izvore:
{source_hint}"""


def build_messages(
    question: str,
    detected_intents: list[str],
    detected_course_names: list[str],
    retrieved_chunks: list[Any],
) -> list[dict[str, str]]:
    return [
        {"role": "system", "content": build_system_prompt()},
        {
            "role": "user",
            "content": build_user_prompt(
                question,
                detected_intents,
                detected_course_names,
                retrieved_chunks,
            ),
        },
    ]


if __name__ == "__main__":
    dummy_chunks = [
        {
            "path": "03_course_plans/2025_2026/razvoj_softvera.md",
            "title": "Razvoj softvera, plan rada",
            "document_type": "course_plan",
            "section_heading": "6. Nedeljni plan rada",
            "score": 0.91,
            "contextual_prefix": "Primer metadata prefiksa.",
            "original_chunk_text": "Primer teksta chunk-a iz plana rada.",
        }
    ]
    print(
        json.dumps(
            build_messages(
                "Da li se na Razvoju softvera sada radi Flask?",
                ["COURSE_PLAN_CURRENT"],
                ["Razvoj softvera"],
                dummy_chunks,
            ),
            ensure_ascii=False,
            indent=2,
        )
    )
