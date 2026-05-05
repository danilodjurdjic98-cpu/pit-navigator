from __future__ import annotations

import re
from dataclasses import dataclass, asdict
from typing import Any

from .loader import Document


HEADING_RE = re.compile(r"^(#{2,3})\s+(.+?)\s*$", re.MULTILINE)


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    document_id: str
    document_type: str
    title: str
    path: str
    folder: str
    section_heading: str
    keywords: list[str]
    related_intents: list[str]
    contextual_prefix: str
    original_chunk_text: str
    contextual_chunk_text: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def _document_id(document: Document) -> str:
    value = document.frontmatter.get("id")
    if value:
        return str(value)
    return document.relative_path.replace("/", "_").replace("\\", "_").removesuffix(".md")


def build_contextual_prefix(frontmatter: dict[str, Any], title: str) -> str:
    document_type = str(frontmatter.get("type") or "")
    academic_year = str(frontmatter.get("academic_year") or "nepoznata")

    if document_type == "course":
        return (
            f"Ovaj chunk je iz PIT 2027 course dokumenta za predmet {title}. "
            "Dokument opisuje formalni akreditacioni okvir, cilj, ishode, teme i ulogu predmeta. "
            "Ne predstavlja nužno aktuelno izvođenje za školsku godinu 2025/2026."
        )
    if document_type == "course_plan":
        return (
            f"Ovaj chunk je iz aktuelnog plana rada za predmet {title}, školska godina {academic_year}. "
            "Dokument opisuje trenutno izvođenje, alate, ocenjivanje, vežbe, kolokvijume i ispit. "
            "Ima prednost za pitanja o tome kako se predmet sada radi."
        )
    if document_type == "basket_overview":
        return (
            "Ovaj chunk je iz pregleda izbornih pozicija PIT 2027. "
            "Dokument opisuje formalne izborne pozicije i praktičnu logiku preporuke. "
            "Preporuke nisu zvanično rangiranje predmeta."
        )
    if document_type == "thematic_basket":
        return (
            "Ovaj chunk je iz tematske korpe za PIT 2027. "
            "Dokument služi za preporuke po interesovanju i karijernim putanjama. "
            "Nije formalno rangiranje predmeta i nije zvanično pravilo izbora."
        )
    if document_type == "elective_reference":
        return (
            "Ovaj chunk je iz kratke reference za izborne predmete koji nemaju poseban course dokument. "
            "Dokument daje širi kontekst i preporuke po interesovanju, ali ne sadrži detaljan plan rada, "
            "ocenjivanje ili nedeljni raspored."
        )
    if document_type == "answering_policy":
        return (
            "Ovaj chunk je iz policy dokumenta PIT Navigatora. "
            "Sadrži pravila odgovaranja, zabrane, fallback formulacije i zaštitne formulacije "
            "koje odgovor mora da poštuje."
        )
    if "retrieval" in document_type:
        return (
            "Ovaj chunk je iz retrieval guide dokumenta. "
            "Sadrži pravila za izbor pravih dokumenata, intent mapiranje i prioritete retrieval-a."
        )
    return (
        f"Ovaj chunk je iz PIT Navigator knowledge base dokumenta {title}. "
        "Koristi se kao kontekst u skladu sa tipom dokumenta i korisničkim pitanjem."
    )


def _split_sections(body: str) -> list[tuple[str, str]]:
    matches = list(HEADING_RE.finditer(body))
    if not matches:
        stripped = body.strip()
        return [("Document body", stripped)] if stripped else []

    sections: list[tuple[str, str]] = []
    first_prefix = body[: matches[0].start()].strip()
    if first_prefix:
        sections.append(("Document intro", first_prefix))

    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        heading = match.group(2).strip()
        text = body[start:end].strip()
        if text:
            sections.append((heading, text))

    return sections


def chunk_documents(documents: list[Document]) -> list[Chunk]:
    chunks: list[Chunk] = []

    for document in documents:
        frontmatter = document.frontmatter
        document_id = _document_id(document)
        document_type = str(frontmatter.get("type") or "")
        title = str(frontmatter.get("title") or document.filename)
        keywords = _as_list(frontmatter.get("keywords"))
        related_intents = _as_list(frontmatter.get("related_intents"))
        prefix = build_contextual_prefix(frontmatter, title)

        for section_index, (section_heading, section_text) in enumerate(_split_sections(document.body), start=1):
            original_chunk_text = section_text.strip()
            contextual_chunk_text = f"{prefix}\n\n{original_chunk_text}"
            chunks.append(
                Chunk(
                    chunk_id=f"{document_id}__chunk_{section_index:03d}",
                    document_id=document_id,
                    document_type=document_type,
                    title=title,
                    path=document.relative_path,
                    folder=document.folder,
                    section_heading=section_heading,
                    keywords=keywords,
                    related_intents=related_intents,
                    contextual_prefix=prefix,
                    original_chunk_text=original_chunk_text,
                    contextual_chunk_text=contextual_chunk_text,
                )
            )

    return chunks
