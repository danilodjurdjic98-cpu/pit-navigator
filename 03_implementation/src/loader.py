from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .frontmatter_parser import parse_frontmatter


@dataclass(frozen=True)
class Document:
    path: str
    relative_path: str
    filename: str
    folder: str
    raw_text: str
    frontmatter: dict[str, Any]
    body: str
    warning: str | None = None


def load_markdown_documents(knowledge_base_path: Path) -> list[Document]:
    root = knowledge_base_path.resolve()
    documents: list[Document] = []

    for file_path in sorted(root.rglob("*.md")):
        if not file_path.is_file():
            continue

        raw_text = file_path.read_text(encoding="utf-8")
        parsed = parse_frontmatter(raw_text)
        relative_path = file_path.relative_to(root).as_posix()
        folder = Path(relative_path).parent.as_posix()
        if folder == ".":
            folder = ""

        documents.append(
            Document(
                path=file_path.as_posix(),
                relative_path=relative_path,
                filename=file_path.name,
                folder=folder,
                raw_text=raw_text,
                frontmatter=parsed.frontmatter,
                body=parsed.body,
                warning=parsed.warning,
            )
        )

    return documents
