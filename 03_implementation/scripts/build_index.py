from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.chunker import chunk_documents  # noqa: E402
from src.config import load_settings  # noqa: E402
from src.loader import load_markdown_documents  # noqa: E402


def main() -> None:
    settings = load_settings()
    settings.index_path.mkdir(parents=True, exist_ok=True)

    documents = load_markdown_documents(settings.knowledge_base_path)
    chunks = chunk_documents(documents)
    chunk_dicts = [chunk.to_dict() for chunk in chunks]
    texts = [chunk.contextual_chunk_text for chunk in chunks]

    if not texts:
        raise RuntimeError("No chunks were created from the knowledge base.")

    model = SentenceTransformer(settings.embedding_model)
    embeddings = model.encode(texts, normalize_embeddings=True, show_progress_bar=True)

    (settings.index_path / "chunks.json").write_text(
        json.dumps(chunk_dicts, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    np.save(settings.index_path / "embeddings.npy", embeddings)
    (settings.index_path / "index_meta.json").write_text(
        json.dumps(
            {
                "created_at": datetime.now(timezone.utc).isoformat(),
                "embedding_model": settings.embedding_model,
                "document_count": len(documents),
                "chunk_count": len(chunks),
                "warnings": [
                    {"path": document.relative_path, "warning": document.warning}
                    for document in documents
                    if document.warning
                ],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"Loaded documents: {len(documents)}")
    print(f"Created chunks: {len(chunks)}")
    print(f"Index path: {settings.index_path}")


if __name__ == "__main__":
    main()
