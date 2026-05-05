---
id: project_handoff_for_new_chat
type: technical_handoff
title: PIT Navigator, handoff za nastavak rada u novom ChatGPT četu
project: PIT Navigator
status: retrieval_only_stable_after_whitelist_llm_integrated
---

# PIT Navigator, handoff za novi ChatGPT čet

## 1. Kratak opis projekta

PIT Navigator je RAG asistent za module PIN 2020 i PIT 2027.

Knowledge base je organizovan kao skup Markdown fajlova. Cilj je da bot odgovara o predmetima, planovima rada, izbornim korpama, karijernim putanjama i policy/fallback slučajevima.

Primarni jezik odgovora je srpski.

## 2. Trenutna struktura foldera

```text
02_knowledge_base/
  README.md
  00_overview/
  01_courses/2027/
  03_course_plans/2025_2026/
  04_baskets/2027/
  05_retrieval_guides/
  06_policy/

03_implementation/
  README.md
  rag_technical_spec.md
  requirements.txt
  .env.example
  .env
  src/
  scripts/
  data/index/
  data/test_results/
  logs/
```

Napomena: `03_implementation/.env` postoji lokalno, ali ne sme da se prikazuje, deli ili commit-uje jer sadrži tajne API ključeve.

## 3. Status knowledge base-a

Documentation layer je `READY`.

Raniji audit je potvrdio:

- svi `.md` fajlovi počinju YAML frontmatter-om
- nema nezatvorenih Markdown code block-ova
- nema spoljašnjih copy-paste oznaka
- izborni predmeti nisu predstavljeni kao obavezni
- PIN 2020 se ne naziva zastarelim
- nastavnici se ne komentarišu
- praksa, završni rad i seminarski radovi nisu posebni dokumenti

## 4. Retrieval-only status

Retrieval-only v1 je stabilan.

`scripts/build_index.py` je prošao sa:

```text
Loaded documents: 36
Created chunks: 1166
```

Napravljeni su indeks fajlovi:

- `03_implementation/data/index/chunks.json`
- `03_implementation/data/index/embeddings.npy`
- `03_implementation/data/index/index_meta.json`

Retrieval koristi:

- local `sentence-transformers` embeddings
- model: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- contextual chunking
- metadata boosting
- rule-based intent classifier
- rule-based subject detection

## 5. Contextual chunking

Svaki chunk ima:

- `original_chunk_text`
- `contextual_prefix`
- `contextual_chunk_text`

Embedding se računa nad:

```text
contextual_chunk_text = contextual_prefix + "\n\n" + original_chunk_text
```

`contextual_prefix` se generiše template-based iz metadata, bez LLM-a.

## 6. Test runner status

Postoje:

- `03_implementation/data/test_results/test_cases.yaml`
- `03_implementation/scripts/test_runner.py`
- `03_implementation/data/test_results/test_runner_report.md`

Poslednji rezultat:

```text
total tests: 7
passed: 7
needs_review: 0
failed: 0
```

Testovi:

- `COURSE_PLAN_FLASK`
- `FALLBACK_TEACHER_NIT`
- `FALLBACK_ECONOMETRIJA`
- `ELECTIVE_AI`
- `COMPARISON_PIN_PIT`
- `CAREER_ERP_SAP`
- `ELECTIVE_ECOMMERCE_EPS_NIT`

## 7. Važne retrieval odluke

- Za pitanja sa izrazima kao što su “sada”, “trenutno”, “kako se polaže”, primat ima `course_plan`.
- Za formalni PIT 2027 opis primat ima `course`.
- Za izborne preporuke primat imaju basket dokumenti.
- Za minor electives bez course dokumenta koristi se `04_baskets/2027/pit_minor_electives_reference.md`.
- Za pitanja o nastavnicima aktivira se `06_policy/pit_navigator_answering_policy.md`.
- Za PIN 2020 vs PIT 2027 koristi se `00_overview/pin_2020_vs_pit_2027.md`.
- Ne dirati embedding sloj jer retrieval već prolazi 7/7.

## 8. Trenutni Python fajlovi

- `src/config.py`: učitava `.env` i `.env.example`, izlaže `Settings` i module-level konfiguracione varijable.
- `src/frontmatter_parser.py`: parsira YAML frontmatter i vraća body bez rušenja procesa na lošem fajlu.
- `src/loader.py`: rekurzivno učitava Markdown dokumente iz knowledge base-a.
- `src/chunker.py`: deli dokumente po Markdown heading-ima i gradi contextual chunk polja.
- `src/intent_classifier.py`: rule-based klasifikuje intent i prepoznaje nazive predmeta i skraćenice.
- `src/retriever.py`: učitava indeks, računa cosine similarity i primenjuje metadata/query boost.
- `src/prompt_builder.py`: gradi system/user prompt i OpenAI-compatible messages format za budući LLM odgovor.
- `src/generator.py`: provider-agnostic LLM generator za Gemini i OpenAI fallback.
- `scripts/build_index.py`: učitava dokumente, pravi chunk-ove, embeddings i čuva indeks.
- `scripts/ask.py`: CLI upit; default režim daje LLM odgovor, `--retrieval-only` je očuvan, a `--show-prompt` prikazuje messages pre LLM poziva.
- `scripts/test_runner.py`: pokreće automatske retrieval-only testove i piše Markdown report.

## 9. LLM status

- `src/prompt_builder.py` postoji.
- `src/generator.py` postoji.
- `scripts/ask.py` podržava default LLM answer režim.
- `--retrieval-only` režim je očuvan.
- `--show-prompt` postoji za debug prompta pre LLM poziva.
- Default provider je Gemini.
- Fallback provider je OpenAI.
- API ključevi su u lokalnom `.env` i ne smeju se prikazivati.
- Ručni LLM testovi su prošli.
- Poslednji provereni LLM provider: `gemini`.
- Poslednji provereni LLM model: `gemini-2.5-flash`.
- Poslednji provereni `fallback_used`: `false`.

## 10. LLM konfiguracija

Vrednosti iz `.env.example`, bez pravih ključeva:

```text
LLM_PROVIDER=gemini
LLM_FALLBACK_PROVIDER=openai
FALLBACK_ON_ERROR=true
GEMINI_MODEL=gemini-2.5-flash
OPENAI_MODEL=gpt-5.4-mini
LLM_TEMPERATURE=0.3
LLM_MAX_TOKENS=4000
LLM_TOP_P=0.95
MAX_CONTEXT_CHUNKS=10
MAX_TOTAL_CONTEXT_CHARS=12000
MIN_RETRIEVAL_SCORE=0.3
LOG_PROMPTS=true
REFUSE_OUT_OF_SCOPE=true
INCLUDE_SOURCES=true
```

## 11. Najnoviji problem koji treba nastaviti

Config problem je rešen.

`src/config.py` sada izlaže module-level varijable kao:

- `config.LLM_PROVIDER`
- `config.GEMINI_MODEL`
- `config.OPENAI_MODEL`
- `config.GEMINI_API_KEY`
- `config.OPENAI_API_KEY`

Poslednja provera je potvrdila da se provider i model vrednosti učitavaju i da su API key vrednosti setovane, bez prikazivanja samih ključeva.

Retrieval status je:

```text
stable_after_whitelist
```

Exact-term boost je ograničen na whitelist tehničke termine, a obične reči se ne boostuju.

## 12. Sledeći preporučeni koraci

1. Napraviti `llm_smoke_test_report.md`.
2. Testirati out-of-scope pitanja.
3. Proveriti da LLM ne odgovara iz opšteg znanja.
4. Testirati 7 pitanja kroz LLM odgovor i upisati rezultate.
5. Proveriti da LLM ne krši policy.
6. Zadržati `--retrieval-only` kao stabilni debug režim.
7. Tek kasnije razmišljati o BM25, rerankeru i document diversity unapređenjima.

## 13. Komande za proveru

```powershell
cd 03_implementation
python -m compileall src scripts
python scripts/test_runner.py
python scripts/build_index.py
python scripts/ask.py "Da li se na Razvoju softvera sada radi Flask?" --retrieval-only
```

## 14. Važne zabrane

- ne slati API keys u chat
- ne commitovati `.env`
- ne menjati `02_knowledge_base` bez posebnog razloga
- ne uvoditi BM25/reranker sada
- ne menjati embedding sada
- ne gasiti retrieval-only režim
- ne dozvoliti LLM-u da odgovara iz opšteg znanja

## 15. Ready state

Current state: retrieval-only stable after whitelist, LLM config/generator/ask.py integration prepared and manually checked with Gemini. Next step is `llm_smoke_test_report.md` and out-of-scope testing.

## 16. Final local status update

Status checklist:

- [x] LLM smoke testovi 7/7 PASS
- [x] LLM_MAX_TOKENS povecan na 4000 zbog Gemini MAX_TOKENS presecanja
- [x] llm_smoke_test_report.md azuriran
- [x] retrieval status stable_after_whitelist
- [x] out-of-scope status: PASS

Out-of-scope testovi su potvrdili:

- ne odgovara iz opsteg znanja
- koristi fallback kad nema relevantnog konteksta
- ne izmislja cenu skolarine
- ne prica viceve
- ne daje recept za kafu
- ne komentarise profesore
- ne izmislja rokove za praksu
- navodi izvore ako su korisceni
- nema traceback gresaka

Current state: retrieval-only stable after whitelist, LLM smoke tests 7/7 PASS, out-of-scope smoke tests PASS, Gemini default answer mode working, and `--retrieval-only` preserved.
