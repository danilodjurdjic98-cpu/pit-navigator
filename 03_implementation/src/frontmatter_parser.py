from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import yaml


@dataclass(frozen=True)
class ParsedMarkdown:
    frontmatter: dict[str, Any]
    body: str
    warning: str | None = None


def parse_frontmatter(raw_text: str) -> ParsedMarkdown:
    if not raw_text.startswith("---"):
        return ParsedMarkdown({}, raw_text, "Missing YAML frontmatter.")

    lines = raw_text.splitlines()
    if not lines or lines[0].strip() != "---":
        return ParsedMarkdown({}, raw_text, "Invalid YAML frontmatter opening marker.")

    closing_index: int | None = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing_index = index
            break

    if closing_index is None:
        return ParsedMarkdown({}, raw_text, "Missing YAML frontmatter closing marker.")

    yaml_text = "\n".join(lines[1:closing_index])
    body = "\n".join(lines[closing_index + 1 :]).lstrip("\n")

    try:
        parsed = yaml.safe_load(yaml_text) or {}
    except yaml.YAMLError as exc:
        return ParsedMarkdown({}, body, f"Invalid YAML frontmatter: {exc}")

    if not isinstance(parsed, dict):
        return ParsedMarkdown({}, body, "YAML frontmatter is not a mapping.")

    return ParsedMarkdown(parsed, body)
