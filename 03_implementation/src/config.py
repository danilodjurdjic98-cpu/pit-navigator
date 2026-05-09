from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    load_dotenv = None


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _bool_env(value: str | None, default: bool) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def _path_env(name: str, default: str) -> Path:
    raw_value = os.getenv(name, default)
    path = Path(raw_value)
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    return path.resolve()


@dataclass(frozen=True)
class Settings:
    knowledge_base_path: Path
    index_path: Path
    embedding_model: str
    top_k: int
    debug_retrieval: bool
    llm_provider: str
    llm_fallback_provider: str
    fallback_on_error: bool
    gemini_api_key: str
    gemini_model: str
    openai_api_key: str
    openai_model: str
    llm_temperature: float
    llm_max_tokens: int
    llm_top_p: float
    llm_timeout: int
    max_context_chunks: int
    max_total_context_chars: int
    min_retrieval_score: float
    log_level: str
    log_prompts: bool
    log_file: Path
    refuse_out_of_scope: bool
    include_sources: bool


def load_settings() -> Settings:
    if load_dotenv is not None:
        load_dotenv(PROJECT_ROOT / ".env")
        load_dotenv(PROJECT_ROOT / ".env.example")

    return Settings(
        knowledge_base_path=_path_env("KNOWLEDGE_BASE_PATH", "../02_knowledge_base"),
        index_path=_path_env("INDEX_PATH", "./data/index"),
        embedding_model=os.getenv(
            "EMBEDDING_MODEL",
            "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        ),
        top_k=int(os.getenv("TOP_K", "8")),
        debug_retrieval=_bool_env(os.getenv("DEBUG_RETRIEVAL"), True),
        llm_provider=os.getenv("LLM_PROVIDER", "gemini"),
        llm_fallback_provider=os.getenv("LLM_FALLBACK_PROVIDER", "openai"),
        fallback_on_error=_bool_env(os.getenv("FALLBACK_ON_ERROR"), True),
        gemini_api_key=os.getenv("GEMINI_API_KEY", ""),
        gemini_model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        openai_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        llm_temperature=float(os.getenv("LLM_TEMPERATURE", "0.3")),
        llm_max_tokens=int(os.getenv("LLM_MAX_TOKENS", "2000")),
        llm_top_p=float(os.getenv("LLM_TOP_P", "0.95")),
        llm_timeout=int(os.getenv("LLM_TIMEOUT", "30")),
        max_context_chunks=int(os.getenv("MAX_CONTEXT_CHUNKS", "10")),
        max_total_context_chars=int(os.getenv("MAX_TOTAL_CONTEXT_CHARS", "12000")),
        min_retrieval_score=float(os.getenv("MIN_RETRIEVAL_SCORE", "0.3")),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
        log_prompts=_bool_env(os.getenv("LOG_PROMPTS"), True),
        log_file=_path_env("LOG_FILE", "logs/pit_navigator.log"),
        refuse_out_of_scope=_bool_env(os.getenv("REFUSE_OUT_OF_SCOPE"), True),
        include_sources=_bool_env(os.getenv("INCLUDE_SOURCES"), True),
    )


SETTINGS = load_settings()

KNOWLEDGE_BASE_PATH = SETTINGS.knowledge_base_path
INDEX_PATH = SETTINGS.index_path
EMBEDDING_MODEL = SETTINGS.embedding_model
TOP_K = SETTINGS.top_k
DEBUG_RETRIEVAL = SETTINGS.debug_retrieval

LLM_PROVIDER = SETTINGS.llm_provider
LLM_FALLBACK_PROVIDER = SETTINGS.llm_fallback_provider
FALLBACK_ON_ERROR = SETTINGS.fallback_on_error
GEMINI_API_KEY = SETTINGS.gemini_api_key
GEMINI_MODEL = SETTINGS.gemini_model
OPENAI_API_KEY = SETTINGS.openai_api_key
OPENAI_MODEL = SETTINGS.openai_model
LLM_TEMPERATURE = SETTINGS.llm_temperature
LLM_MAX_TOKENS = SETTINGS.llm_max_tokens
LLM_TOP_P = SETTINGS.llm_top_p
LLM_TIMEOUT = SETTINGS.llm_timeout
MAX_CONTEXT_CHUNKS = SETTINGS.max_context_chunks
MAX_TOTAL_CONTEXT_CHARS = SETTINGS.max_total_context_chars
MIN_RETRIEVAL_SCORE = SETTINGS.min_retrieval_score
LOG_LEVEL = SETTINGS.log_level
LOG_PROMPTS = SETTINGS.log_prompts
LOG_FILE = SETTINGS.log_file
REFUSE_OUT_OF_SCOPE = SETTINGS.refuse_out_of_scope
INCLUDE_SOURCES = SETTINGS.include_sources
