# PIT Navigator

PIT Navigator je RAG prototip za pomoć studentima pri razumevanju programa Poslovna informatika i tehnologije, izbornih predmeta, aktuelnih planova rada i mogućih karijernih putanja.

Projekat kombinuje:

- očišćenu Markdown bazu znanja
- lokalni RAG backend
- frontend chat prototip
- pripremljen paket za ručni upload na server

Glavni cilj je da korisnik može da postavi pitanje o PIT programu, predmetima ili izborima, a sistem vrati odgovor zasnovan na proverljivim izvorima iz knowledge base-a.

## Struktura projekta

```text
pit-navigator-faks/
  00_project_rules/
  01_raw_documents/
  02_knowledge_base/
  03_implementation/
  04_frontend_site/
  05_server_upload/
  promotional_pdf/
  README.md
```

## Folderi

### `00_project_rules/`

Pravila, smernice i početna logika projekta.

### `01_raw_documents/`

Sirovi ulazni dokumenti, kao što su PDF, DOCX i drugi izvorni materijali.

Ovaj folder se ne koristi direktno u RAG prototipu. Prva verzija koristi očišćene Markdown dokumente iz `02_knowledge_base/`.

### `02_knowledge_base/`

Glavna baza znanja za RAG.

Sadrži:

- pregled programa
- course dokumente za PIT 2027
- aktuelne planove rada za 2025/2026
- izborne korpe
- retrieval vodiče
- policy i QA pravila

Početni fajlovi:

```text
02_knowledge_base/README.md
02_knowledge_base/00_overview/knowledge_base_index.md
02_knowledge_base/05_retrieval_guides/pit_navigator_retrieval_map.md
02_knowledge_base/06_policy/pit_navigator_answering_policy.md
```

### `03_implementation/`

Python implementacija RAG prototipa.

Sadrži backend, indeksiranje, retrieval logiku, API i test skripte.

Važni fajlovi:

```text
03_implementation/README.md
03_implementation/rag_technical_spec.md
03_implementation/requirements.txt
03_implementation/.env.example
03_implementation/scripts/build_index.py
03_implementation/scripts/ask.py
03_implementation/api/main.py
```

### `04_frontend_site/`

Frontend chat prototip.

Sadrži:

```text
04_frontend_site/pit-navigator.html
04_frontend_site/pit-navigator.css
04_frontend_site/pit-navigator.js
04_frontend_site/README.md
```

Frontend očekuje lokalni backend na:

```text
http://127.0.0.1:8000/chat
http://127.0.0.1:8000/chat/stream
```

### `05_server_upload/`

Production-ready frontend paket za ručni upload na server.

Ciljna putanja:

```text
/home/azecevic/public_html/pin/pit-navigator/
```

Odgovarajući URL:

```text
https://pin.ekof.bg.ac.rs/pin/pit-navigator/
```

Detalji su u:

```text
05_server_upload/README.md
```

### `promotional_pdf/`

Materijali vezani za promotivni PDF.

## Lokalno pokretanje backend-a

Iz foldera `03_implementation/`:

```bash
cd 03_implementation
pip install -r requirements.txt
python scripts/build_index.py
python -m uvicorn api.main:app --reload --host 127.0.0.1 --port 8000
```

Za LLM odgovore potreban je lokalni `.env` fajl, napravljen po uzoru na:

```text
03_implementation/.env.example
```

Ako se koristi Gemini, potreban je:

```text
GEMINI_API_KEY
```

## Lokalno pokretanje frontend-a

U drugom terminalu:

```bash
cd 04_frontend_site
python -m http.server 5500
```

Zatim otvoriti:

```text
http://127.0.0.1:5500/pit-navigator.html
```

## Brzi test backend-a

Health check:

```bash
curl -X GET http://127.0.0.1:8000/health
```

Chat test:

```bash
curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d "{\"question\":\"Da li se na Razvoju softvera sada radi Flask?\",\"history\":[]}"
```

Retrieval-only test:

```bash
cd 03_implementation
python scripts/ask.py "Šta da izaberem ako me zanima AI?" --retrieval-only
```

## Pravila odgovaranja

PIT Navigator mora da poštuje policy dokumente iz knowledge base-a.

Posebno:

- ne izmišljati informacije
- ne komentarisati nastavnike i saradnike
- ne garantovati posao, platu ili sertifikat
- ne predstavljati izborne predmete kao obavezne
- razlikovati PIT 2027 i PIN 2020
- razlikovati formalni course dokument i aktuelni plan rada
- koristiti fallback kada nema dovoljno informacija

Glavni policy fajlovi:

```text
02_knowledge_base/06_policy/pit_navigator_answering_policy.md
02_knowledge_base/06_policy/pit_navigator_qa_checklist.md
02_knowledge_base/05_retrieval_guides/pit_navigator_retrieval_map.md
```

## Deployment napomena

Na server se uploaduje samo pripremljen frontend iz:

```text
05_server_upload/pit-navigator/
```

Ne uploadovati:

- `.env` fajlove
- `03_implementation/`
- `02_knowledge_base/`
- `01_raw_documents/`
- `00_project_rules/`
- lokalne logove, indekse i test rezultate

Pre upload-a obavezno podesiti produkcioni API URL u:

```text
05_server_upload/pit-navigator/index.html
```

## Korisni README fajlovi

```text
02_knowledge_base/README.md
03_implementation/README.md
04_frontend_site/README.md
05_server_upload/README.md
```

## Status

Knowledge base je pripremljena za RAG testiranje.

Implementacioni deo sadrži lokalni backend, skripte za indeksiranje i frontend prototip. Root README služi kao glavna mapa projekta i ulazna tačka za rad.
