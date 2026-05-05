from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
from sentence_transformers import SentenceTransformer


MINOR_ELECTIVE_TERMS = [
    "nove informacione tehnologije",
    "nove informacione",
    "novih informacionih tehnologija",
    "nit",
    "elektronska trgovina",
    "elektronskoj trgovini",
    "elektronsku trgovinu",
    "elektronski platni sistemi",
    "elektronske platne sisteme",
    "elektronskih platnih sistema",
    "platni sistemi",
    "platne sisteme",
    "eps",
    "ekonometrija",
    "ekonometriji",
    "ekonometriju",
    "ekonometrije",
    "kvantitativne finansije",
    "kvantitativnih finansija",
    "ekonomska statistika",
    "ekonomskoj statistici",
    "analiza finansijskih izveštaja",
    "analiza finansijskih izvestaja",
    "upravljačko računovodstvo",
    "upravljacko racunovodstvo",
    "računovodstveni informacioni sistemi",
    "racunovodstveni informacioni sistemi",
    "istraživanje tržišta",
    "istrazivanje trzista",
]

MINOR_ELECTIVE_COURSE_NAMES = {
    "Nove informacione tehnologije",
    "Elektronska trgovina",
    "Elektronski platni sistemi",
    "Ekonometrija",
    "Kvantitativne finansije",
    "Ekonomska statistika",
    "Analiza finansijskih izveštaja",
    "Upravljačko računovodstvo",
    "Računovodstveni informacioni sistemi",
    "Istraživanje tržišta",
}

DIGITAL_ELECTIVE_COURSE_NAMES = {
    "Elektronska trgovina",
    "Elektronski platni sistemi",
    "Nove informacione tehnologije",
}

INSTRUCTOR_TERMS = [
    "profesor",
    "nastavnik",
    "saradnik",
    "ko drži",
    "ko drzi",
    "predaje",
]

ASSESSMENT_QUERY_TERMS = [
    "polaže",
    "polaze",
    "ocenjuje",
    "ocenjivanje",
    "poeni",
    "predispitne",
]

ASSESSMENT_CHUNK_TERMS = [
    "način ocenjivanja",
    "nacin ocenjivanja",
    "predispitne obaveze",
    "završni test",
    "zavrsni test",
    "poena",
]

FORMAL_PIT_2027_TERMS = [
    "pit 2027",
    "u pit 2027",
]

COMPARISON_QUERY_TERMS = [
    "razlika",
    "pin",
    "2020",
    "vs",
    "bolji",
    "zastareo",
]

STATUS_QUERY_TERMS = [
    "obavezno",
    "obavezan",
    "obavezna",
    "izborno",
    "izborni",
    "izborna",
    "status predmeta",
]

DATA_ENGINEER_QUERY_TERMS = [
    "data engineer",
    "data inženjer",
    "data inzenjer",
    "data engineering",
    "inženjer podataka",
    "inzenjer podataka",
]

EXACT_BOOST_TERMS = {
    "flask",
    "php",
    "sap",
    "erp",
    "mongodb",
    "pymongo",
    "tkinter",
    "sql",
    "python",
    "java",
    "javascript",
    "wordpress",
    "woocommerce",
    "cypress",
    "selenium",
    "postman",
    "jmeter",
    "mysql",
    "postgresql",
    "postgres",
    "openai",
    "gemini",
    "rag",
    "ai",
    "bi",
}

EXACT_BOOST_PHRASES = {
    "power bi",
}


@dataclass(frozen=True)
class RetrievalResult:
    score: float
    path: str
    title: str
    document_type: str
    section_heading: str
    contextual_prefix: str
    original_chunk_text: str = ""
    contextual_chunk_text: str = ""


class Retriever:
    def __init__(self, index_path: Path, embedding_model: str) -> None:
        self.index_path = index_path
        self.embedding_model = embedding_model
        self.chunks = self._load_chunks()
        self.embeddings = self._load_embeddings()
        self.model = SentenceTransformer(embedding_model)

    def _load_chunks(self) -> list[dict[str, Any]]:
        chunks_path = self.index_path / "chunks.json"
        if not chunks_path.exists():
            raise FileNotFoundError(
                f"Missing index file: {chunks_path}. Run python scripts/build_index.py first."
            )
        return json.loads(chunks_path.read_text(encoding="utf-8"))

    def _load_embeddings(self) -> np.ndarray:
        embeddings_path = self.index_path / "embeddings.npy"
        if not embeddings_path.exists():
            raise FileNotFoundError(
                f"Missing index file: {embeddings_path}. Run python scripts/build_index.py first."
            )
        return np.load(embeddings_path)

    def search(
        self,
        question: str,
        intents: list[str],
        top_k: int,
        course_names: list[str] | None = None,
    ) -> list[RetrievalResult]:
        query_embedding = self.model.encode([question], normalize_embeddings=True)
        scores = np.matmul(self.embeddings, query_embedding[0])
        detected_course_names = course_names or []
        boosted_scores = scores + np.array(
            [
                self._metadata_boost(chunk, intents, question, detected_course_names)
                for chunk in self.chunks
            ],
            dtype=np.float32,
        )

        top_indices = self._select_diverse_top_indices(boosted_scores, top_k)
        return [
            RetrievalResult(
                score=float(boosted_scores[index]),
                path=str(self.chunks[index].get("path", "")),
                title=str(self.chunks[index].get("title", "")),
                document_type=str(self.chunks[index].get("document_type", "")),
                section_heading=str(self.chunks[index].get("section_heading", "")),
                contextual_prefix=str(self.chunks[index].get("contextual_prefix", "")),
                original_chunk_text=str(self.chunks[index].get("original_chunk_text", "")),
                contextual_chunk_text=str(self.chunks[index].get("contextual_chunk_text", "")),
            )
            for index in top_indices
        ]

    def _select_diverse_top_indices(self, scores: np.ndarray, top_k: int) -> list[int]:
        ranked_indices = np.argsort(scores)[::-1]
        selected: list[int] = []
        per_path_counts: dict[str, int] = {}
        max_chunks_per_path = 3

        for index in ranked_indices:
            path = str(self.chunks[index].get("path", ""))
            if per_path_counts.get(path, 0) >= max_chunks_per_path:
                continue
            selected.append(int(index))
            per_path_counts[path] = per_path_counts.get(path, 0) + 1
            if len(selected) >= top_k:
                break

        return selected

    @staticmethod
    def _metadata_boost(
        chunk: dict[str, Any],
        intents: list[str],
        question: str,
        course_names: list[str],
    ) -> float:
        document_type = str(chunk.get("document_type") or "")
        path = str(chunk.get("path") or "")
        section_heading = str(chunk.get("section_heading") or "")
        original_chunk_text = str(chunk.get("original_chunk_text") or "")
        question_text = question.casefold()
        section_text = section_heading.casefold()
        chunk_text = original_chunk_text.casefold()
        boost = 0.0

        if "COURSE_PLAN_CURRENT" in intents and document_type == "course_plan":
            boost += 0.20
        if (
            document_type == "course_plan"
            and any(term in question_text for term in ASSESSMENT_QUERY_TERMS)
            and any(term in section_text or term in chunk_text for term in ASSESSMENT_CHUNK_TERMS)
        ):
            boost += 0.65
        boost += Retriever._exact_query_term_boost(question_text, section_text, chunk_text)
        if "COURSE_EXPLANATION" in intents and document_type == "course":
            boost += 0.15
        if (
            document_type == "course"
            and path.startswith("01_courses/2027/")
            and course_names
            and any(term in question_text for term in FORMAL_PIT_2027_TERMS)
            and not any(term in question_text for term in COMPARISON_QUERY_TERMS)
            and Retriever._matches_detected_course(chunk, course_names)
        ):
            boost += 0.45
        if (
            document_type == "course"
            and path.startswith("01_courses/2027/")
            and course_names
            and any(term in question_text for term in STATUS_QUERY_TERMS)
            and Retriever._matches_detected_course(chunk, course_names)
        ):
            boost += 0.50
        if "ELECTIVE_RECOMMENDATION" in intents and document_type in {
            "basket_overview",
            "thematic_basket",
            "elective_reference",
        }:
            boost += 0.20
        if "ELECTIVE_RECOMMENDATION" in intents and any(
            course_name in DIGITAL_ELECTIVE_COURSE_NAMES for course_name in course_names
        ):
            if "04_baskets/2027/pit_software_erp_digital_korpa.md" in path:
                boost += 1.40
            if "04_baskets/2027/pit_izborne_korpe_overview.md" in path:
                boost += 1.20
            if "04_baskets/2027/pit_minor_electives_reference.md" in path:
                boost += 0.45
        if (
            "CAREER_RECOMMENDATION" in intents
            and ("ERP softver" in course_names or "erp" in question_text or "sap" in question_text)
            and "04_baskets/2027/pit_software_erp_digital_korpa.md" in path
        ):
            boost += 0.55
        if (
            "CAREER_RECOMMENDATION" in intents
            and any(term in question_text for term in DATA_ENGINEER_QUERY_TERMS)
            and "04_baskets/2027/pit_data_ai_bi_korpa.md" in path
        ):
            boost += 0.55
        if "ACCREDITATION_COMPARISON" in intents and "pin_2020_vs_pit_2027.md" in path:
            boost += 0.25
        if "FALLBACK" in intents and document_type in {"answering_policy", "retrieval_guide"}:
            boost += 0.20
        if (
            "FALLBACK" in intents
            and "04_baskets/2027/pit_minor_electives_reference.md" in path
            and any(term in question_text for term in MINOR_ELECTIVE_TERMS)
        ):
            boost += 0.45
        if (
            "04_baskets/2027/pit_minor_electives_reference.md" in path
            and any(course_name in MINOR_ELECTIVE_COURSE_NAMES for course_name in course_names)
        ):
            boost += 0.25
            matched_exact_course = False
            for course_name in course_names:
                normalized_course = course_name.casefold()
                if normalized_course in section_text:
                    boost += 0.75
                    matched_exact_course = True
                elif normalized_course in chunk_text:
                    boost += 0.35
                    matched_exact_course = True

            if not matched_exact_course:
                boost -= 0.25
        if (
            "FALLBACK" in intents
            and "06_policy/pit_navigator_answering_policy.md" in path
            and any(term in question_text for term in INSTRUCTOR_TERMS)
        ):
            boost += 0.45

        return boost

    @staticmethod
    def _normalize_for_match(value: str) -> str:
        normalized = unicodedata.normalize("NFKD", value.casefold())
        ascii_text = "".join(char for char in normalized if not unicodedata.combining(char))
        return re.sub(r"[^a-z0-9]+", " ", ascii_text).strip()

    @staticmethod
    def _matches_detected_course(chunk: dict[str, Any], course_names: list[str]) -> bool:
        title = Retriever._normalize_for_match(str(chunk.get("title") or ""))
        path = Retriever._normalize_for_match(str(chunk.get("path") or ""))
        for course_name in course_names:
            normalized_course = Retriever._normalize_for_match(course_name)
            if normalized_course and (normalized_course == title or normalized_course in path):
                return True
        return False

    @staticmethod
    def _exact_query_term_boost(question_text: str, section_text: str, chunk_text: str) -> float:
        boost = 0.0
        terms = {
            term for term in re.findall(r"[\wšđčćžŠĐČĆŽ]+", question_text.casefold())
            if term in EXACT_BOOST_TERMS
        }
        phrases = {phrase for phrase in EXACT_BOOST_PHRASES if phrase in question_text}

        for term in terms | phrases:
            if term in section_text:
                boost += 0.18
            elif term in chunk_text:
                boost += 0.12
        return min(boost, 0.45)
