---
id: implementation_readme
type: implementation_readme
title: PIT Navigator, README za implementaciju
project: PIT Navigator
version: v1.0
last_updated: 2026-05-04
status: draft_ready_for_minimal_implementation
related_documents:
  - 03_implementation/rag_technical_spec.md
  - 02_knowledge_base/README.md
  - 02_knowledge_base/00_overview/knowledge_base_index.md
  - 02_knowledge_base/05_retrieval_guides/pit_navigator_test_questions.md
  - 02_knowledge_base/06_policy/pit_navigator_answering_policy.md
keywords:
  - implementation
  - README
  - PIT Navigator
  - RAG
  - loader
  - chunking
  - retrieval
  - CLI
  - test runner
---

# PIT Navigator, README za implementaciju

## 1. Svrha foldera

Folder `03_implementation/` služi za tehničku implementaciju PIT Navigator RAG prototipa.

Do sada je napravljena Markdown knowledge base dokumentacija u folderu:

```text
02_knowledge_base/
```

Ovaj folder služi za sledeći sloj:

```text
Markdown knowledge base
    ↓
Python loader
    ↓
frontmatter parser
    ↓
chunking
    ↓
embedding index
    ↓
retrieval
    ↓
CLI pitanje / odgovor
    ↓
testiranje
```

## 2. Trenutni status

```text
Status: implementation_not_started
Knowledge base status: READY
Technical spec status: ready_for_minimal_implementation
```

To znači:

- dokumentacija postoji
- struktura knowledge base-a je proverena
- RAG kod još nije napravljen
- embedding indeks još nije napravljen
- API i UI još nisu napravljeni

## 3. Šta se radi u prvoj implementaciji

Prva implementacija treba da bude lokalni CLI RAG prototip.

Cilj je da možemo da pokrenemo:

```text
python scripts/ask.py "Da li se na Razvoju softvera sada radi Flask?"
```

i dobijemo:

```text
- prepoznat intent
- povučene dokumente
- relevantne sekcije
- odgovor ili retrieval-only rezultat
- debug prikaz izvora
```

## 4. Šta se ne radi u prvoj implementaciji

U prvoj fazi ne pravimo:

- web aplikaciju
- frontend
- produkcioni API
- korisničke naloge
- deployment
- administrativni panel
- automatsko ažuriranje dokumenata
- scraping fakultetskog sajta
- povezivanje sa Google Drive-om
- povezivanje sa LMS-om
- zvanične administrativne procedure
- proveru aktuelnih nastavnika i rasporeda

Prva verzija služi za testiranje RAG logike.

## 5. Očekivana struktura foldera

Predložena struktura:

```text
03_implementation/
  README.md
  rag_technical_spec.md
  requirements.txt
  .env.example

  src/
    config.py
    loader.py
    frontmatter_parser.py
    markdown_splitter.py
    chunker.py
    metadata.py
    intent_classifier.py
    retriever.py
    prompt_builder.py
    generator.py
    citations.py
    qa_checks.py

  scripts/
    build_index.py
    ask.py
    test_runner.py
    inspect_index.py

  data/
    index/
    cache/
    test_results/

  tests/
    test_loader.py
    test_frontmatter.py
    test_chunking.py
    test_intent_classifier.py
    test_retrieval_rules.py
```

Minimalna prva verzija može imati samo:

```text
requirements.txt
.env.example

src/
  config.py
  loader.py
  frontmatter_parser.py
  chunker.py
  intent_classifier.py
  retriever.py
  prompt_builder.py

scripts/
  build_index.py
  ask.py
  test_runner.py

data/
  index/
  test_results/
```

## 6. Glavni ulazni folder

RAG prototip koristi očišćene Markdown dokumente iz:

```text
02_knowledge_base/
```

Ne koristi direktno:

```text
01_raw_documents/
```

Razlog:

`01_raw_documents/` sadrži izvorne PDF, DOCX i druge fajlove. Prva RAG verzija koristi samo proverene i očišćene `.md` fajlove iz knowledge base-a.

## 7. Osnovni tok implementacije

Preporučeni redosled:

```text
1. requirements.txt
2. .env.example
3. src/config.py
4. src/loader.py
5. src/frontmatter_parser.py
6. src/chunker.py
7. src/intent_classifier.py
8. src/retriever.py
9. scripts/build_index.py
10. scripts/ask.py u retrieval-only režimu
11. scripts/test_runner.py
12. LLM generisanje odgovora
```

Ne treba odmah pisati sve module. Prvo napraviti minimalnu verziju koja učitava dokumente, pravi chunk-ove i vraća relevantne izvore.

## 8. Minimalni zahtevi za loader

Loader treba da:

- rekurzivno učita `.md` fajlove iz `02_knowledge_base/`
- ignoriše ne-Markdown fajlove
- sačuva relativnu putanju fajla
- proveri da fajl počinje sa `---`
- razdvoji frontmatter i body
- vrati listu dokumenata sa metadata

Minimalni objekat dokumenta:

```json
{
  "path": "02_knowledge_base/01_courses/2027/erp_softver.md",
  "filename": "erp_softver.md",
  "folder": "01_courses/2027",
  "frontmatter": {},
  "body": "..."
}
```

## 9. Minimalni zahtevi za chunking

Chunking treba da:

- deli dokumente po Markdown naslovima `##` i `###`
- zadrži naslov sekcije u chunk-u
- čuva metadata iz frontmatter-a
- čuva putanju dokumenta
- čuva tip dokumenta
- čuva naslov dokumenta
- čuva naziv sekcije
- ne ubacuje YAML frontmatter u tekst za embedding

Preporučena veličina chunk-a:

```text
target_chunk_size: 600 do 900 tokena
max_chunk_size: 1200 tokena
overlap: 100 do 150 tokena
```

## 9.1 Contextual chunking

Chunking ne treba da čuva samo originalni tekst sekcije.

Svaki chunk treba da ima:

```text
original_chunk_text
contextual_prefix
contextual_chunk_text
```

- `original_chunk_text` je stvarni tekst iz Markdown dokumenta.
- `contextual_prefix` je kratko automatski generisano objašnjenje na osnovu metadata.
- `contextual_chunk_text` je tekst koji se šalje embedding modelu.

**Format:**

```text
contextual_chunk_text = contextual_prefix + "\n\n" + original_chunk_text
```

**Primer:**

```text
Ovaj chunk je iz aktuelnog plana rada za predmet Razvoj softvera, školska godina 2025/2026. Dokument opisuje trenutno izvođenje, alate, ocenjivanje, vežbe, kolokvijume i ispit. Ima prednost za pitanja o tome kako se predmet sada radi.

Predmet koristi PHP, baze podataka, frontend, Scrum i timski projekat.
```

**Zašto je ovo važno:**

U knowledge base-u postoje slični dokumenti za isti predmet, na primer:

```text
01_courses/2027/razvoj_softvera.md
03_course_plans/2025_2026/razvoj_softvera.md
```

Contextual prefix pomaže retrieval-u da razlikuje formalni akreditacioni opis od aktuelnog plana rada.

## 10. Metadata za chunk

Svaki chunk treba da ima metadata kao minimum:

```json
{
  "chunk_id": "course_2027_erp_softver__chunk_003",
  "document_id": "course_2027_erp_softver",
  "document_type": "course",
  "title": "ERP softver",
  "path": "02_knowledge_base/01_courses/2027/erp_softver.md",
  "folder": "01_courses/2027",
  "section_heading": "3. Cilj predmeta",
  "keywords": ["ERP", "SAP"],
  "related_intents": ["COURSE_EXPLANATION", "CAREER_RECOMMENDATION"]
}
```

Ako polje ne postoji u frontmatter-u, ne izmišljati vrednost.

## 11. Intent klasifikacija

Prva verzija može koristiti pravila po ključnim rečima.

Očekivani intent-i:

```text
PROGRAM_OVERVIEW
COURSE_EXPLANATION
COURSE_PLAN_CURRENT
ACCREDITATION_COMPARISON
ELECTIVE_RECOMMENDATION
CAREER_RECOMMENDATION
INTEREST_BASED_RECOMMENDATION
JOB_MARKET
FALLBACK
```

Primeri pravila:

```text
"trenutno", "sada", "kako se polaže", "kolokvijum", "ispit", "plan rada" -> COURSE_PLAN_CURRENT

"šta je", "šta se radi", "čemu služi", "da li je obavezan" -> COURSE_EXPLANATION

"šta da izaberem", "koji izborni", "da li da uzmem" -> ELECTIVE_RECOMMENDATION

"PIN 2020", "PIT 2027", "razlika", "zastareo", "nova akreditacija" -> ACCREDITATION_COMPARISON

"posao", "zapošljavanje", "AI će pojesti", "tržište" -> JOB_MARKET
```

## 12. Retrieval pravila

Retrieval ne sme biti samo semantički.

Mora koristiti:

- intent
- tip dokumenta
- folder
- metadata
- naziv predmeta
- semantičku sličnost
- policy dokumente kada je potrebno

Primer:

Pitanje:

```text
Da li se na Razvoju softvera sada radi Flask?
```

Očekivano:

```text
intent: COURSE_PLAN_CURRENT
primary document: 03_course_plans/2025_2026/razvoj_softvera.md
policy document: 06_policy/pit_navigator_answering_policy.md
```

Ne sme primarno koristiti samo:

```text
01_courses/2027/razvoj_softvera.md
```

jer korisnik pita za aktuelno izvođenje.

## 13. Debug output

`ask.py` u prvoj verziji treba da prikazuje debug informacije.

Minimalni debug output:

```text
Question:
Detected intent:
Detected course names:
Retrieved documents:
Retrieved sections:
Scores:
Policy chunks used:
Answer:
```

Ovo je važno da brzo vidimo da li retrieval povlači pogrešne dokumente.

## 14. Retrieval-only režim

Pre dodavanja LLM odgovora treba napraviti retrieval-only režim.

Primer:

```text
python scripts/ask.py "Šta da izaberem ako me zanima AI?" --retrieval-only
```

Očekivani izlaz:

```text
Detected intent:
ELECTIVE_RECOMMENDATION

Retrieved documents:
1. 04_baskets/2027/pit_data_ai_bi_korpa.md
2. 04_baskets/2027/pit_izborne_korpe_overview.md
3. 01_courses/2027/masinsko_ucenje.md
4. 01_courses/2027/operaciona_istrazivanja.md
5. 06_policy/pit_navigator_answering_policy.md
```

Tek kada retrieval-only radi dobro, dodaje se LLM generisanje odgovora.

## 15. Test pitanja

Test pitanja su definisana u:

```text
02_knowledge_base/05_retrieval_guides/pit_navigator_test_questions.md
```

Minimalni test set:

```text
1. Šta je PIT i šta se tu uči?
2. Koja je razlika između PIN 2020 i PIT 2027?
3. Šta se radi na Mašinskom učenju u PIT 2027?
4. Kako se sada polaže ERP?
5. Da li se na Razvoju softvera sada radi Flask?
6. Da li da uzmem Operaciona istraživanja ili Istraživanje tržišta?
7. Šta da izaberem ako me zanima AI?
8. Da li da izaberem Elektronsku trgovinu, Elektronske platne sisteme ili Nove informacione tehnologije?
9. Koji predmeti su dobri za ERP/SAP konsultanta?
10. Da li će AI pojesti ovaj smer?
11. Šta se tačno radi na Ekonometriji?
12. Ko drži Nove informacione tehnologije i da li je profesor dobar?
```

## 16. Očekivani test rezultat

Za svaki test treba proveriti:

```text
Test ID:
Question:
Detected intent:
Retrieved documents:
Expected documents:
Result: PASS / NEEDS_REVIEW / FAIL
Notes:
Policy issues:
Action needed:
```

Test je uspešan ako:

- povučen je pravi tip dokumenta
- course i course_plan nisu pomešani
- izborni predmeti nisu predstavljeni kao obavezni
- PIN 2020 nije nazvan zastarelim
- nastavnici se ne komentarišu
- posao se ne garantuje
- fallback se koristi kada nema dovoljno informacija

## 17. Prva verzija bez LLM-a

Prvi tehnički cilj može biti samo:

```text
build_index.py
ask.py --retrieval-only
```

To znači da sistem još ne daje pun prirodni odgovor, nego samo pokazuje koje dokumente bi koristio.

Ovo je korisno jer omogućava proveru retrieval-a bez rizika da LLM izmisli odgovor.

## 18. Druga verzija sa LLM-om

Kada retrieval-only prođe osnovne testove, dodaje se LLM odgovor.

Prompt mora uključiti:

- korisničko pitanje
- prepoznat intent
- relevantne chunk-ove
- relevantne policy chunk-ove
- pravila odgovaranja
- listu izvora

LLM mora dobiti jasna pravila:

```text
- Ne izmišljaj informacije.
- Ne komentariši nastavnike.
- Ne obećavaj posao.
- Ne predstavljaj izborne predmete kao obavezne.
- Razlikuj PIT 2027 i PIN 2020.
- Razlikuj course i course_plan.
- Ako nema dovoljno informacija, koristi fallback.
```

## 19. Minimalni requirements

Predloženi paketi:

```text
pyyaml
python-frontmatter
markdown
numpy
scikit-learn
sentence-transformers
rich
typer
python-dotenv
```

Opcioni paketi:

```text
faiss-cpu
tiktoken
openai
```

Za prvu retrieval-only verziju može se krenuti bez OpenAI API-ja.

## 20. Predloženi embedding model

Za lokalni prototip:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

Razlog:

- podržava više jezika
- dovoljno je dobar za srpski prototip
- radi lokalno
- jednostavan je za početak

Moguća kasnija zamena:

```text
intfloat/multilingual-e5-base
```

## 21. Konfiguracija

Predloženi `.env.example`:

```text
KNOWLEDGE_BASE_PATH=../02_knowledge_base
INDEX_PATH=./data/index
EMBEDDING_MODEL=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
TOP_K=8
DEBUG_RETRIEVAL=true
OPENAI_API_KEY=
```

`OPENAI_API_KEY` nije potreban za retrieval-only lokalnu verziju ako se koriste lokalni embeddings.

## 22. Pravila koja implementacija mora poštovati

Implementacija mora poštovati:

```text
02_knowledge_base/06_policy/pit_navigator_answering_policy.md
02_knowledge_base/06_policy/pit_navigator_qa_checklist.md
02_knowledge_base/05_retrieval_guides/pit_navigator_retrieval_map.md
```

Posebno:

- ne izmišljati informacije
- ne komentarisati nastavnike i saradnike
- ne garantovati posao, platu ili sertifikat
- ne predstavljati izborne predmete kao obavezne
- ne nazivati PIN 2020 zastarelim
- ne mešati PIT 2027 course dokument i aktuelni plan rada
- ne predstavljati radne predloge kao zvanične planove
- koristiti fallback za predmete bez posebnog dokumenta

## 23. Prvi konkretan zadatak za Codex

Kada krene implementacija, prvi prompt za Codex može biti:

```text
Napravi minimalnu Python strukturu za PIT Navigator RAG prototip prema 03_implementation/rag_technical_spec.md i 03_implementation/README.md.

Za sada ne pravi LLM odgovor i ne koristi OpenAI API.

Napravi:
- requirements.txt
- .env.example
- src/config.py
- src/loader.py
- src/frontmatter_parser.py
- src/chunker.py
- src/intent_classifier.py
- src/retriever.py
- scripts/build_index.py
- scripts/ask.py

Cilj:
- učitati sve .md fajlove iz 02_knowledge_base/
- parsirati YAML frontmatter
- napraviti chunk-ove po Markdown naslovima
- napraviti lokalne embeddings koristeći sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
- sačuvati indeks u 03_implementation/data/index/
- omogućiti komandu:
  python scripts/ask.py "Da li se na Razvoju softvera sada radi Flask?" --retrieval-only

U retrieval-only režimu prikaži:
- pitanje
- prepoznat intent
- prepoznate nazive predmeta
- top retrieved dokumente
- section heading
- document type
- score

Važno:
- ne praviti frontend
- ne praviti API
- ne praviti LLM answer generation
- ne menjati 02_knowledge_base dokumente
```

## 24. Checklist za implementaciju

```text
[ ] requirements.txt postoji
[ ] .env.example postoji
[ ] src/config.py postoji
[ ] src/loader.py postoji
[ ] src/frontmatter_parser.py postoji
[ ] src/chunker.py postoji
[ ] src/intent_classifier.py postoji
[ ] src/retriever.py postoji
[ ] scripts/build_index.py postoji
[ ] scripts/ask.py postoji
[ ] build_index.py uspešno učitava .md fajlove
[ ] frontmatter parser radi
[ ] chunking radi
[ ] indeks se čuva u data/index/
[ ] ask.py --retrieval-only vraća dokumente
[ ] test pitanje za Flask vraća course_plan, ne samo course
[ ] test pitanje za nastavnika aktivira policy/fallback
[ ] test pitanje za Ekonometriju koristi minor electives reference
```

## 25. Povezani dokumenti

## Local API

Pokretanje lokalnog FastAPI backend-a:

```bash
python -m uvicorn api.main:app --reload --host 127.0.0.1 --port 8000
```

Primer health testa:

```bash
curl -X GET http://127.0.0.1:8000/health
```

Primer chat testa bez conversation_id:

```bash
curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d "{\"question\":\"Da li se na Razvoju softvera sada radi Flask?\",\"history\":[]}"
```

Primer chat testa sa conversation_id:

```bash
curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d "{\"conversation_id\":\"demo-1\",\"question\":\"A šta sa ERP karijerom?\",\"history\":[{\"role\":\"user\",\"content\":\"Šta da izaberem ako me zanima AI?\"},{\"role\":\"assistant\",\"content\":\"AI putanja uključuje Baze podataka, Analizu podataka, Poslovnu analitiku i druge predmete.\"}]}"
```

Ovaj README se oslanja na:

```text
03_implementation/rag_technical_spec.md

02_knowledge_base/README.md
02_knowledge_base/00_overview/knowledge_base_index.md
02_knowledge_base/00_overview/knowledge_base_changelog.md
02_knowledge_base/05_retrieval_guides/pit_navigator_retrieval_map.md
02_knowledge_base/05_retrieval_guides/pit_navigator_intent_examples.md
02_knowledge_base/05_retrieval_guides/pit_navigator_test_questions.md
02_knowledge_base/06_policy/pit_navigator_answering_policy.md
02_knowledge_base/06_policy/pit_navigator_qa_checklist.md
```

Napomena: ovaj README ne implementira RAG sistem. On samo objašnjava kako treba krenuti u minimalnu implementaciju.
