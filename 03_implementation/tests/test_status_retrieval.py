"""Regression checks for course-status evidence in the actual retrieval index."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.config import load_settings
from src.intent_classifier import classify
from src.prompt_builder import format_retrieved_context
from src.retriever import Retriever


class CourseStatusRetrievalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.settings = load_settings()
        cls.retriever = Retriever(cls.settings.index_path, cls.settings.embedding_model)

    def test_machine_learning_status_reaches_prompt(self):
        for question in (
            "Da li je Mašinsko učenje obavezno?",
            "Da li je Mašinsko učenje izborni predmet?",
        ):
            with self.subTest(question=question):
                classification = classify(question)
                results = self.retriever.search(
                    question, classification.intents, self.settings.top_k,
                    classification.course_names,
                )
                self.assertEqual(results[0].path, "01_courses/2027/masinsko_ucenje.md")
                self.assertIn("Formalni opis predmeta", results[0].section_heading)
                context = format_retrieved_context(results[:1])
                self.assertIn("predmet je izborni u PIT 2027", context)
                self.assertIn("PIT 6", context)


if __name__ == "__main__":
    unittest.main()
