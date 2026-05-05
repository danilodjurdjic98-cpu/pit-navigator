---
id: implementation_rag_technical_spec
type: technical_spec
title: PIT Navigator, RAG tehnička specifikacija
project: PIT Navigator
version: v1.0
last_updated: 2026-05-04
status: draft_ready_for_implementation
related_documents:
  - 02_knowledge_base/README.md
  - 02_knowledge_base/00_overview/knowledge_base_index.md
  - 02_knowledge_base/00_overview/knowledge_base_changelog.md
  - 02_knowledge_base/05_retrieval_guides/pit_navigator_retrieval_map.md
  - 02_knowledge_base/05_retrieval_guides/pit_navigator_intent_examples.md
  - 02_knowledge_base/05_retrieval_guides/pit_navigator_test_questions.md
  - 02_knowledge_base/06_policy/pit_navigator_answering_policy.md
  - 02_knowledge_base/06_policy/pit_navigator_qa_checklist.md
keywords:
  - RAG
  - technical spec
  - PIT Navigator
  - implementation
  - markdown loader
  - frontmatter parser
  - chunking
  - retrieval
  - vector index
  - CLI
  - test runner
---

# PIT Navigator, RAG tehnička specifikacija

## 1. Svrha dokumenta

Ovaj dokument definiše tehničku specifikaciju za prvu RAG implementaciju PIT Navigatora.

Do sada je napravljena Markdown knowledge base dokumentacija. Nije napravljen Python kod, embedding indeks, RAG pipeline, API, UI ili aplikacija.

Svrha ovog dokumenta je da napravi most između dokumentacije i implementacije.

Ovaj dokument definiše:

- kako se učitavaju Markdown fajlovi
- kako se parsira YAML frontmatter
- koji metadata se čuva
- kako se dokumenti dele na chunk-ove
- kako se prepoznaje intent korisničkog pitanja
- kako retrieval bira prave dokumente
- kako se koristi policy sloj
- kako se generiše odgovor
- kako se testira sistem
- šta se radi u prvoj verziji
- šta se ne radi u prvoj verziji

## 2. Trenutno stanje projekta

Trenutno postoji dokumentacioni sloj:

```text
02_knowledge_base/
  README.md
  00_overview/
  01_courses/
    2027/
  03_course_plans/
    2025_2026/
  04_baskets/
    2027/
  05_retrieval_guides/
  06_policy/
```

Status dokumentacije:

```text
Knowledge base status: READY
Scope: Markdown documentation only
Ready for: initial RAG testing
Not implemented yet: Python code, RAG pipeline, embeddings, API, UI
```

## 3. Cilj prve tehničke verzije

Cilj prve tehničke verzije nije pravljenje kompletnog proizvoda.

Cilj je napraviti lokalni CLI RAG prototip koji može da:

1. učita sve `.md` fajlove iz `02_knowledge_base/`
2. pročita YAML frontmatter
3. podeli dokumente na chunk-ove
4. sačuva metadata za svaki chunk
5. napravi lokalni embedding indeks
6. prepozna osnovni intent pitanja
7. povuče relevantne chunk-ove
8. uključi policy kontekst
9. generiše odgovor
10. prikaže korišćene dokumente
11. pokrene test pitanja iz test seta

Minimalni cilj:

```text
python ask.py "Da li se na Razvoju softvera sada radi Flask?"
```

Treba da vrati:

```text
- prepoznat intent
- dokumente koji su povučeni
- odgovor
- napomenu ako je korišćen fallback
```

## 4. Šta se ne radi u prvoj tehničkoj verziji

U prvoj tehničkoj verziji ne pravimo:

- web aplikaciju
- frontend
- korisničke naloge
- bazu korisnika
- produkcioni API
- deployment
- automatsko ažuriranje dokumenata
- administrativni panel
- streaming UI
- napredni analytics dashboard
- automatsko editovanje Markdown fajlova
- scraping fakultetskog sajta
- povezivanje sa Google Drive-om
- povezivanje sa LMS-om
- proveru aktuelnih nastavnika i rasporeda
- garancije za zvanične administrativne procedure

Prva verzija je lokalni prototip za testiranje RAG logike.

## 5. Predložena arhitektura

Arhitektura v1:

```text
Markdown knowledge base
    ↓
Document loader
    ↓
YAML frontmatter parser
    ↓
Markdown section parser
    ↓
Chunking
    ↓
Metadata enrichment
    ↓
Embedding model
    ↓
Vector index
    ↓
Intent classifier
    ↓
Intent-aware retrieval
    ↓
Policy injection
    ↓
LLM answer generation
    ↓
Answer with citations / source list
    ↓
Test runner
```

## 6. Predložena struktura implementacije

Predložena struktura foldera:

```text
03_implementation/
  rag_technical_spec.md
  README.md
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

Napomena:

Ovo je predlog strukture. U prvoj minimalnoj verziji ne moraju svi fajlovi biti odmah implementirani. Minimalni set je:

```text
requirements.txt
src/loader.py
src/frontmatter_parser.py
src/chunker.py
src/intent_classifier.py
src/retriever.py
src/prompt_builder.py
scripts/build_index.py
scripts/ask.py
scripts/test_runner.py
```

## 7. Ulazni podaci

Primarni ulazni folder:

```text
02_knowledge_base/
```

Učitavaju se svi `.md` fajlovi iz:

```text
02_knowledge_base/
  README.md
  00_overview/
  01_courses/2027/
  03_course_plans/2025_2026/
  04_baskets/2027/
  05_retrieval_guides/
  06_policy/
```

Ne učitavati:

```text
01_raw_documents/
```

Razlog:

`01_raw_documents/` sadrži izvorne PDF, DOCX ili druge fajlove. RAG v1 koristi samo očišćene Markdown dokumente iz `02_knowledge_base/`.

## 8. Document loader

Loader treba da:

1. rekurzivno prođe kroz `02_knowledge_base/`
2. pronađe sve `.md` fajlove
3. sačuva relativnu putanju fajla
4. učita tekst
5. proveri da fajl počinje sa `---`
6. pošalje tekst frontmatter parseru
7. pošalje Markdown sadržaj chunker-u

Za svaki dokument treba napraviti objekat:

```json
{
  "path": "02_knowledge_base/01_courses/2027/erp_softver.md",
  "filename": "erp_softver.md",
  "folder": "01_courses/2027",
  "raw_text": "...",
  "frontmatter": {},
  "body": "..."
}
```

Ako fajl nema validan frontmatter:

```text
QA_STATUS: needs_review
```

i treba ga prijaviti u logu, ali ne mora nužno zaustaviti ceo proces u lokalnom prototipu.

## 9. YAML frontmatter parser

Parser treba da pročita deo između prvog para `---`.

Primer:

```yaml
---
id: course_2027_erp_softver
type: course
title: ERP softver
accreditation: 2027
module: PIT
status: obavezan
source_file: knjiga_predmeta_2027.pdf
source_status: zvanicni_akreditacioni_dokument
keywords:
  - ERP
  - SAP
---
```

Obavezna polja koja treba čuvati ako postoje:

```text
id
type
title
project
version
accreditation
module
module_full_name
academic_year
implementation_context
related_accreditation
status
semester
espb
source_file
source_status
related_intents
related_documents
related_courses_core
related_courses_elective
keywords
last_updated
```

Ako neko polje ne postoji, ne treba izmišljati vrednost. Treba ostaviti `null` ili praznu listu.

## 10. Tipovi dokumenata

RAG mora da razlikuje tipove dokumenata.

Očekivani tipovi:

```text
overview
course
course_plan
basket_overview
thematic_basket
elective_reference
retrieval_guide
retrieval_test_set
answering_policy
qa_checklist
knowledge_base_index
changelog
```

Praktično najvažniji tipovi za retrieval:

```text
course
course_plan
basket_overview
thematic_basket
elective_reference
retrieval_guide
answering_policy
overview
```

## 11. Metadata za svaki chunk

Svaki chunk mora imati metadata.

Minimalni metadata:

```json
{
  "chunk_id": "course_2027_erp_softver__chunk_003",
  "document_id": "course_2027_erp_softver",
  "document_type": "course",
  "title": "ERP softver",
  "path": "02_knowledge_base/01_courses/2027/erp_softver.md",
  "folder": "01_courses/2027",
  "accreditation": "2027",
  "academic_year": null,
  "module": "PIT",
  "status": "obavezan",
  "source_file": "knjiga_predmeta_2027.pdf",
  "source_status": "zvanicni_akreditacioni_dokument",
  "section_heading": "3. Cilj predmeta",
  "keywords": ["ERP", "SAP"],
  "related_intents": ["COURSE_EXPLANATION", "CAREER_RECOMMENDATION"]
}
```

Za `course_plan` dokumente:

```json
{
  "document_type": "course_plan",
  "academic_year": "2025/2026",
  "implementation_context": "PIN 2020",
  "related_accreditation": "2020"
}
```

Za `thematic_basket` dokumente:

```json
{
  "document_type": "thematic_basket",
  "formal_basket": false,
  "basket_purpose": "preporuka_po_interesovanju"
}
```

## 12. Chunking strategija

Ne treba deliti dokumente nasumično.

Predložena strategija:

1. primarno deliti po Markdown naslovima `##` i `###`
2. zadržati naslov sekcije u chunk-u
3. ako je sekcija predugačka, podeliti je na manje chunk-ove
4. ne razbijati YAML frontmatter u embedding tekst
5. frontmatter čuvati kao metadata, ne kao glavni tekst chunk-a
6. svaki chunk treba da zna iz kog je dokumenta i sekcije

Preporučena veličina chunk-a:

```text
target_chunk_size: 600 do 900 tokena
max_chunk_size: 1200 tokena
overlap: 100 do 150 tokena
```

Za policy i retrieval dokumente:

```text
target_chunk_size: 500 do 800 tokena
```

Za course i course_plan dokumente:

```text
target_chunk_size: 700 do 1000 tokena
```

Za basket dokumente:

```text
target_chunk_size: 700 do 1000 tokena
```

## 13. Chunk tekst

Svaki chunk treba da sadrži kontekstualni prefiks.

Primer chunk teksta za embedding:

```text
Document title: ERP softver
Document type: course
Path: 02_knowledge_base/01_courses/2027/erp_softver.md
Section: 3. Cilj predmeta

[tekst sekcije]
```

Ovo pomaže embedding modelu da bolje razlikuje slične predmete.

## 13.1 Contextual chunk prefix

Pre embedding-a svaki chunk treba obogatiti kratkim kontekstualnim prefiksom na osnovu metadata.

Cilj je da embedding model bolje razlikuje slične tekstove iz različitih slojeva knowledge base-a, posebno:

- course dokumente
- course_plan dokumente
- thematic_basket dokumente
- elective_reference dokumente
- policy dokumente
- retrieval guide dokumente

Za prvu verziju koristi se template-based contextual retrieval, bez LLM generisanja konteksta.

To znači da se kontekst ne piše ručno i ne generiše preko LLM-a, već se automatski pravi iz frontmatter-a i putanje dokumenta.

Primeri za različite tipove dokumenata:

**Primer za course dokument:**

```text
Ovaj chunk je iz PIT 2027 course dokumenta za predmet {title}. Dokument opisuje formalni akreditacioni okvir, cilj, ishode, teme i ulogu predmeta. Ne predstavlja nužno aktuelno izvođenje za školsku godinu 2025/2026.
```

**Primer za course_plan dokument:**

```text
Ovaj chunk je iz aktuelnog plana rada za predmet {title}, školska godina {academic_year}. Dokument opisuje trenutno izvođenje, alate, ocenjivanje, vežbe, kolokvijume i ispit. Ima prednost za pitanja o tome kako se predmet sada radi.
```

**Primer za basket_overview dokument:**

```text
Ovaj chunk je iz pregleda izbornih pozicija PIT 2027. Dokument opisuje formalne izborne pozicije i praktičnu logiku preporuke. Preporuke nisu zvanično rangiranje predmeta.
```

**Primer za thematic_basket dokument:**

```text
Ovaj chunk je iz tematske korpe za PIT 2027. Dokument služi za preporuke po interesovanju i karijernim putanjama. Nije formalno rangiranje predmeta i nije zvanično pravilo izbora.
```

**Primer za elective_reference dokument:**

```text
Ovaj chunk je iz kratke reference za izborne predmete koji nemaju poseban course dokument. Dokument daje širi kontekst i preporuke po interesovanju, ali ne sadrži detaljan plan rada, ocenjivanje ili nedeljni raspored.
```

**Primer za answering_policy dokument:**

```text
Ovaj chunk je iz policy dokumenta PIT Navigatora. Sadrži pravila odgovaranja, zabrane, fallback formulacije i zaštitne formulacije koje odgovor mora da poštuje.
```

**Primer za retrieval_guide dokument:**

```text
Ovaj chunk je iz retrieval guide dokumenta. Sadrži pravila za izbor pravih dokumenata, intent mapiranje i prioritete retrieval-a.
```

### Računanje embedding-a

Embedding se računa nad tekstom:

```text
contextual_prefix + "\n\n" + original_chunk_text
```

### Prikaz u korisničkom odgovoru

U korisničkom odgovoru se ne prikazuje contextual prefix kao poseban tekst.

### Debug prikaz

U debug prikazu treba čuvati:

```text
contextual_prefix
original_chunk_text
contextual_chunk_text
```

### Prošireni metadata

Minimalni metadata za chunk treba proširiti ovim poljima:

```json
{
  "contextual_prefix": "...",
  "original_chunk_text": "...",
  "contextual_chunk_text": "..."
}
```

## 14. Intent klasifikacija

Prva verzija ne mora koristiti poseban ML model za intent.

Može se koristiti hibridni pristup:

1. pravila po ključnim rečima
2. semantički retrieval iz `pit_navigator_intent_examples.md`
3. fallback na generalni intent ako nije jasno

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

## 15. Pravila za intent klasifikaciju

### 15.1 COURSE_PLAN_CURRENT

Ako pitanje sadrži izraze:

```text
trenutno
sada
ove godine
2025/26
kako se polaže
kolokvijum
ispit
vežbe
plan rada
nedeljni plan
projekat
predispitne obaveze
koji alati
```

onda je intent najverovatnije:

```text
COURSE_PLAN_CURRENT
```

Prioritetni folder:

```text
03_course_plans/2025_2026/
```

### 15.2 COURSE_EXPLANATION

Ako pitanje pita:

```text
šta je predmet
šta se radi na predmetu
čemu služi
koje teme pokriva
da li je obavezan
koliko je važan
za šta je koristan
```

onda je intent najverovatnije:

```text
COURSE_EXPLANATION
```

Prioritetni folder:

```text
01_courses/2027/
```

ako korisnik pominje PIT 2027 ili novu akreditaciju.

### 15.3 ACCREDITATION_COMPARISON

Ako pitanje pominje:

```text
PIN 2020
PIT 2027
stara akreditacija
nova akreditacija
razlika
šta se promenilo
zastareo
modernizacija
```

onda je intent:

```text
ACCREDITATION_COMPARISON
```

Prioritetni dokument:

```text
00_overview/pin_2020_vs_pit_2027.md
```

### 15.4 ELECTIVE_RECOMMENDATION

Ako pitanje sadrži:

```text
šta da izaberem
koji izborni
da li da uzmem
bolji izbor
šta je korisnije
izborni predmet
```

onda je intent:

```text
ELECTIVE_RECOMMENDATION
```

Prioritetni folder:

```text
04_baskets/2027/
```

### 15.5 CAREER_RECOMMENDATION

Ako pitanje pominje:

```text
data analyst
BI analitičar
ERP konsultant
SAP konsultant
developer
AI konsultant
finansijski analitičar
business analyst
karijera
posao
```

onda je intent:

```text
CAREER_RECOMMENDATION
```

ili, ako je pitanje šire o poslu:

```text
JOB_MARKET
```

### 15.6 JOB_MARKET

Ako pitanje pominje:

```text
posao
zapošljavanje
tržište
AI će pojesti
plata
karijera posle smera
da li je dovoljno
```

onda je intent:

```text
JOB_MARKET
```

Obavezno uključiti policy dokument.

### 15.7 FALLBACK

Ako pitanje traži:

```text
nastavnike
saradnike
rokove
procedure
praksu
završni rad
seminarski rad
drugi smer
predmet bez dokumenta
detaljan plan koji ne postoji
```

onda uključiti:

```text
FALLBACK
```

i policy dokument.

## 16. Intent-aware retrieval

Retrieval ne sme biti samo semantički.

Mora kombinovati:

1. intent
2. tip dokumenta
3. folder
4. metadata
5. semantičku sličnost
6. keywords
7. policy prioritet

Primer:

Pitanje:

```text
Da li se na Razvoju softvera sada radi Flask?
```

Intent:

```text
COURSE_PLAN_CURRENT
```

Prioritetni dokumenti:

```text
03_course_plans/2025_2026/razvoj_softvera.md
06_policy/pit_navigator_answering_policy.md
05_retrieval_guides/pit_navigator_retrieval_map.md
```

Ne sme biti primarno:

```text
01_courses/2027/razvoj_softvera.md
```

osim kao sekundarni kontekst.

## 17. Retrieval prioritet po intent-u

### 17.1 PROGRAM_OVERVIEW

Prioritet:

```text
00_overview/pit_2027_overview.md
00_overview/pin_2020_overview.md
00_overview/knowledge_base_index.md
```

### 17.2 ACCREDITATION_COMPARISON

Prioritet:

```text
00_overview/pin_2020_vs_pit_2027.md
00_overview/pin_2020_overview.md
00_overview/pit_2027_overview.md
06_policy/pit_navigator_answering_policy.md
```

### 17.3 COURSE_EXPLANATION

Prioritet:

```text
01_courses/2027/[predmet].md
```

Sekundarno:

```text
04_baskets/2027/[relevantna_korpa].md
03_course_plans/2025_2026/[predmet].md
```

### 17.4 COURSE_PLAN_CURRENT

Prioritet:

```text
03_course_plans/2025_2026/[predmet].md
```

Sekundarno:

```text
01_courses/2027/[predmet].md
06_policy/pit_navigator_answering_policy.md
```

### 17.5 ELECTIVE_RECOMMENDATION

Prioritet:

```text
04_baskets/2027/pit_izborne_korpe_overview.md
04_baskets/2027/[relevantna_tematska_korpa].md
04_baskets/2027/pit_minor_electives_reference.md
```

Sekundarno:

```text
01_courses/2027/[predmet].md
03_course_plans/2025_2026/[predmet].md
```

### 17.6 CAREER_RECOMMENDATION

Prioritet:

```text
04_baskets/2027/pit_data_ai_bi_korpa.md
04_baskets/2027/pit_software_erp_digital_korpa.md
04_baskets/2027/pit_finance_analytics_korpa.md
```

Sekundarno:

```text
01_courses/2027/
06_policy/pit_navigator_answering_policy.md
```

### 17.7 JOB_MARKET

Prioritet:

```text
00_overview/pit_2027_overview.md
04_baskets/2027/
06_policy/pit_navigator_answering_policy.md
```

### 17.8 FALLBACK

Prioritet:

```text
06_policy/pit_navigator_answering_policy.md
05_retrieval_guides/pit_navigator_retrieval_map.md
04_baskets/2027/pit_minor_electives_reference.md
00_overview/knowledge_base_index.md
```

## 18. Metadata boosting

Retrieval treba da pojača dokumente po metadata.

Predložena pravila:

```text
Ako intent = COURSE_PLAN_CURRENT:
  boost document_type = course_plan
  boost folder = 03_course_plans/2025_2026

Ako intent = COURSE_EXPLANATION:
  boost document_type = course
  boost folder = 01_courses/2027

Ako intent = ELECTIVE_RECOMMENDATION:
  boost document_type = thematic_basket, basket_overview, elective_reference
  boost folder = 04_baskets/2027

Ako intent = ACCREDITATION_COMPARISON:
  boost pin_2020_vs_pit_2027.md

Ako intent = FALLBACK:
  boost answering_policy
  boost retrieval_map
```

## 19. Document name matching

Pre semantičkog retrieval-a treba pokušati prepoznavanje naziva predmeta.

Mapa normalizovanih naziva:

```text
baze -> Baze podataka
baze podataka -> Baze podataka
poslovna analitika -> Poslovna analitika
pa -> Poslovna analitika, samo ako kontekst potvrđuje
poslovna inteligencija -> Poslovna inteligencija
bi -> Poslovna inteligencija, samo ako kontekst potvrđuje
ux -> Korisničko iskustvo i dizajn
korisnicko iskustvo -> Korisničko iskustvo i dizajn
elvi -> Elektronsko poslovanje i veštačka inteligencija
elektronsko poslovanje i ai -> Elektronsko poslovanje i veštačka inteligencija
analiza podataka -> Analiza podataka
oop -> Objektno orijentisano programiranje
objektno -> Objektno orijentisano programiranje
razvoj softvera -> Razvoj softvera
erp -> ERP softver
sap -> ERP softver, u kontekstu predmeta
operaciona -> Operaciona istraživanja
operaciona istrazivanja -> Operaciona istraživanja
masinsko -> Mašinsko učenje
masinsko ucenje -> Mašinsko učenje
```

Ako se prepozna predmet, retrieval treba da boost-uje dokumente tog predmeta.

## 20. Policy injection

Policy dokument ne treba uvek ceo ubacivati u prompt.

Treba koristiti relevantne policy chunk-ove u zavisnosti od intent-a.

Primeri:

### 20.1 Ako pitanje pominje posao, tržište, AI

Uključiti policy sekcije o:

```text
karijerne preporuke
tržište rada i AI
zabrana obećavanja posla
```

### 20.2 Ako pitanje pominje nastavnike

Uključiti policy sekcije o:

```text
nastavnici i saradnici
fallback
```

### 20.3 Ako pitanje pominje izborni predmet

Uključiti policy sekcije o:

```text
izborni predmeti
izborne korpe
preporuke nisu formalno rangiranje
```

### 20.4 Ako pitanje pominje PIN 2020 i PIT 2027

Uključiti policy sekcije o:

```text
PIN 2020 se ne naziva zastarelim
PIT 2027 je formalna modernizacija
```

### 20.5 Ako pitanje pominje aktuelno izvođenje

Uključiti policy sekcije o:

```text
aktuelni plan rada ima prednost za operativna pitanja
akreditacioni opis nije isto što i plan rada
radni predlog nije zvaničan plan
```

## 21. Prompt builder

Prompt za LLM treba da ima sledeće delove:

```text
1. System instruction
2. User question
3. Detected intent
4. Retrieved context
5. Relevant policy rules
6. Answer requirements
7. Source list
```

Predloženi prompt skeleton:

```text
Ti si PIT Navigator, asistent koji odgovara na osnovu interne knowledge base dokumentacije.

Korisničko pitanje:
{question}

Prepoznat intent:
{intent}

Relevantni kontekst:
{retrieved_chunks}

Relevantna pravila:
{policy_chunks}

Pravila odgovora:
- Odgovori na srpskom.
- Ne izmišljaj informacije.
- Jasno razlikuj PIT 2027 i PIN 2020.
- Jasno razlikuj course dokument i aktuelni plan rada.
- Ne predstavljaj izborne predmete kao obavezne.
- Ne komentariši nastavnike i saradnike.
- Ne obećavaj posao, platu ili sertifikat.
- Ako nema dovoljno informacija, koristi fallback formulaciju.
- Odgovor neka bude praktičan i razumljiv studentu.

Odgovor:
```

## 22. Citiranje izvora u prvoj verziji

U lokalnoj CLI verziji dovoljno je prikazati listu izvora ispod odgovora.

Primer:

```text
Izvori korišćeni u odgovoru:
- 03_course_plans/2025_2026/razvoj_softvera.md
- 06_policy/pit_navigator_answering_policy.md
```

Kasnije se može dodati preciznije citiranje po chunk-u.

U prvoj verziji treba obavezno prikazati:

```text
path
document title
document type
section heading
similarity score
```

Primer debug prikaza:

```text
Retrieved sources:
1. 03_course_plans/2025_2026/razvoj_softvera.md
   type: course_plan
   section: 6. Nedeljni plan rada
   score: 0.83

2. 06_policy/pit_navigator_answering_policy.md
   type: answering_policy
   section: 16. Pravilo za radne predloge
   score: 0.76
```

## 23. Odgovor korisniku

Odgovor treba da bude:

- kratak kada korisnik traži kratak odgovor
- detaljan kada korisnik traži analizu
- praktičan
- bez nepotrebnog formalizma
- bez izmišljanja
- sa jasnom napomenom kada je nešto izborno
- sa fallback formulacijom kada nema dovoljno podataka

Primer dobar odgovor:

```text
Ne, u aktuelnom planu rada 2025/26 za Razvoj softvera ne treba predstavljati Flask kao ono što se trenutno radi. Aktuelni plan navodi PHP, baze podataka, frontend, Scrum i timski projekat.

Python/Flask može biti budući fokus samo ako bude potvrđen novim planom rada. Dakle, za sada ga treba voditi kao radni predlog, ne kao aktuelni plan.
```

## 24. Test runner

Test runner treba da koristi:

```text
02_knowledge_base/05_retrieval_guides/pit_navigator_test_questions.md
```

Prva verzija može ručno definisati test pitanja u posebnom JSON/YAML fajlu, ili ih parsirati iz Markdown dokumenta.

Preporučeni lakši pristup za v1:

```text
03_implementation/data/test_questions.yaml
```

Format:

```yaml
- id: COURSE_PLAN_03
  question: "Da li se na Razvoju softvera sada radi Flask?"
  expected_intent:
    - COURSE_PLAN_CURRENT
  expected_documents:
    - "03_course_plans/2025_2026/razvoj_softvera.md"
    - "06_policy/pit_navigator_answering_policy.md"
  forbidden_claims:
    - "trenutno se radi Flask"
    - "Flask je aktuelni plan"
```

Test runner treba da za svako pitanje prikaže:

```text
Test ID
Question
Detected intent
Retrieved documents
Expected documents
PASS / NEEDS_REVIEW / FAIL
Notes
```

## 25. Minimalni test set

Za početak koristiti 12 pitanja:

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

## 26. Očekivani izlaz ask.py

Komanda:

```text
python scripts/ask.py "Šta da izaberem ako me zanima AI?"
```

Očekivani izlaz:

```text
Detected intent:
ELECTIVE_RECOMMENDATION, INTEREST_BASED_RECOMMENDATION

Retrieved documents:
1. 04_baskets/2027/pit_data_ai_bi_korpa.md
2. 04_baskets/2027/pit_izborne_korpe_overview.md
3. 01_courses/2027/masinsko_ucenje.md
4. 01_courses/2027/operaciona_istrazivanja.md
5. 06_policy/pit_navigator_answering_policy.md

Answer:
[odgovor korisniku]
```

## 27. Greške koje sistem mora izbeći

Sistem ne sme da:

- koristi `course` dokument kada je pitanje očigledno o aktuelnom planu rada
- koristi `course_plan` kao formalni opis PIT 2027
- kaže da je izborni predmet obavezan
- kaže da PIN 2020 jeste zastareo
- komentariše nastavnike
- izmišlja ocenjivanje
- izmišlja nedeljni plan
- izmišlja alate
- obećava posao
- obećava platu
- obećava sertifikat
- kaže da Flask trenutno postoji u Razvoju softvera ako nije potvrđeno planom rada
- koristi tematsku korpu kao formalno rangiranje predmeta
- izmišlja detalje za predmete iz minor electives reference

## 28. Minimalni requirements

Predloženi Python paketi:

```text
pyyaml
python-frontmatter
markdown
tiktoken
numpy
scikit-learn
sentence-transformers
faiss-cpu
rich
typer
python-dotenv
```

Alternativa bez FAISS-a za prvu probu:

```text
scikit-learn
sentence-transformers
numpy
```

U tom slučaju retrieval može koristiti cosine similarity preko embedding matrice.

## 29. Embedding model

Za lokalnu verziju predlog:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

Razlog:

- podržava više jezika
- radi sa srpskim dovoljno dobro za prototip
- može lokalno da se koristi
- jednostavan je za testiranje

Moguća bolja opcija kasnije:

```text
intfloat/multilingual-e5-base
```

Za E5 modele treba koristiti odgovarajući format:

```text
query: ...
passage: ...
```

Za prvu verziju može se krenuti jednostavnije sa `paraphrase-multilingual-MiniLM-L12-v2`.

## 30. LLM model

Ova specifikacija ne propisuje konkretan LLM.

Moguće opcije:

```text
OpenAI API
lokalni LLM
drugi API model
```

Za početak se može čak testirati samo retrieval bez generisanja odgovora.

Minimalni redosled:

```text
1. build_index.py
2. inspect_index.py
3. ask.py sa retrieval-only režimom
4. ask.py sa LLM odgovorom
5. test_runner.py
```

## 31. Konfiguracija

Predloženi `.env.example`:

```text
OPENAI_API_KEY=
EMBEDDING_MODEL=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
KNOWLEDGE_BASE_PATH=../02_knowledge_base
INDEX_PATH=./data/index
TOP_K=8
DEBUG_RETRIEVAL=true
```

Ako se koristi lokalni embedding model, `OPENAI_API_KEY` nije potreban za embedding.

## 32. Debug režim

U debug režimu ask.py treba da prikaže:

```text
- original question
- normalized question
- detected intent
- detected course names
- retrieval filters
- retrieved documents
- retrieved sections
- scores
- final context length
- policy chunks used
```

Ovo je važno da bi se brzo otkrilo kada retrieval povlači pogrešan dokument.

## 33. QA pravila za implementaciju

Implementacija mora poštovati:

```text
02_knowledge_base/06_policy/pit_navigator_answering_policy.md
02_knowledge_base/06_policy/pit_navigator_qa_checklist.md
02_knowledge_base/05_retrieval_guides/pit_navigator_retrieval_map.md
```

Posebno proveriti:

- izborni predmeti se ne predstavljaju kao obavezni
- PIN 2020 se ne naziva zastarelim
- nastavnici se ne komentarišu
- posao se ne garantuje
- course i course_plan se razlikuju
- minor electives ne dobijaju izmišljene detalje
- praksa i završni rad ne dobijaju izmišljene procedure

## 34. Status ove specifikacije

```text
SPEC_STATUS: ready_for_minimal_implementation
```

Ova specifikacija je dovoljna da se krene u minimalnu Python implementaciju.

Prvi konkretni implementacioni koraci:

```text
1. napraviti requirements.txt
2. napraviti loader.py
3. napraviti frontmatter_parser.py
4. napraviti chunker.py
5. napraviti build_index.py
6. napraviti ask.py u retrieval-only režimu
7. testirati 12 pitanja
```

## 35. Checklist, šta je sledeće

```text
[ ] Sačuvati 03_implementation/rag_technical_spec.md
[ ] Napraviti 03_implementation/README.md
[ ] Napraviti 03_implementation/requirements.txt
[ ] Napraviti 03_implementation/.env.example
[ ] Napraviti osnovnu src/ strukturu
[ ] Implementirati Markdown loader
[ ] Implementirati frontmatter parser
[ ] Implementirati chunking
[ ] Implementirati build_index.py
[ ] Implementirati ask.py retrieval-only
[ ] Testirati minimalni set od 12 pitanja
[ ] Tek onda dodati LLM generisanje odgovora
[ ] Implementirati contextual chunk prefix
[ ] Embedding računati nad contextual_chunk_text
[ ] U debug prikazu prikazati contextual_prefix
[ ] Kasnije dodati BM25 kao drugi retrieval signal
[ ] Kasnije dodati reranker
```

## 36. Povezani dokumenti

Ova specifikacija se oslanja na:

```text
02_knowledge_base/README.md
02_knowledge_base/00_overview/knowledge_base_index.md
02_knowledge_base/00_overview/knowledge_base_changelog.md
02_knowledge_base/05_retrieval_guides/pit_navigator_retrieval_map.md
02_knowledge_base/05_retrieval_guides/pit_navigator_intent_examples.md
02_knowledge_base/05_retrieval_guides/pit_navigator_test_questions.md
02_knowledge_base/06_policy/pit_navigator_answering_policy.md
02_knowledge_base/06_policy/pit_navigator_qa_checklist.md
```

Napomena: ovaj dokument ne implementira RAG sistem. On samo definiše tehnička pravila i redosled implementacije. Python kod, indeksiranje i testiranje se rade u sledećem koraku.