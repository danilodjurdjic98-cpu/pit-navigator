---
id: implementation_retrieval_only_v1_report
type: test_report
title: PIT Navigator, retrieval-only v1 test report
project: PIT Navigator
version: retrieval_only_v1
last_updated: 2026-05-04
status: retrieval_only_stable_after_whitelist
related_documents:
  - 03_implementation/rag_technical_spec.md
  - 03_implementation/README.md
  - 02_knowledge_base/05_retrieval_guides/pit_navigator_test_questions.md
  - 02_knowledge_base/06_policy/pit_navigator_answering_policy.md
keywords:
  - retrieval-only
  - test report
  - PIT Navigator
  - RAG
  - retrieval testing
  - contextual chunking
  - metadata boosting
  - stable
---

# PIT Navigator, retrieval-only v1 test report

## 1. Svrha dokumenta

Ovaj dokument beleži rezultate prvog retrieval-only testiranja PIT Navigator RAG prototipa.

Testiranje je rađeno bez LLM answer generation-a.

Cilj testiranja bio je da se proveri:

- da li se Markdown knowledge base uspešno učitava
- da li se kreiraju chunk-ovi
- da li contextual chunking radi
- da li se prepoznaju intent-i
- da li se prepoznaju nazivi predmeta
- da li retrieval povlači prave dokumente
- da li metadata boosting radi za kritične slučajeve
- da li se course i course_plan dokumenti razlikuju
- da li se policy dokumenti aktiviraju kada treba
- da li se minor electives reference koristi za predmete bez posebnog course dokumenta

## 2. Status

```text
retrieval_only_v1_status: stable_for_initial_testing
```

Zaključak:

Retrieval-only v1 je stabilan za početno testiranje i spreman je kao osnova za sledeći korak, odnosno LLM answer generation.

## 3. Tehnički status

Pokrenuto je:

```text
python scripts/build_index.py
```

Rezultat:

```text
Loaded documents: 36
Created chunks: 1166
warnings: 0
```

Indeks je napravljen lokalno u:

```text
03_implementation/data/index/
```

Očekivani fajlovi:

```text
chunks.json
embeddings.npy
index_meta.json
```

## 4. Napomene o okruženju

Tokom pokretanja pojavila su se HuggingFace upozorenja:

```text
Warning: You are sending unauthenticated requests to the HF Hub.
UNEXPECTED embeddings.position_ids
symlink warning on Windows
```

Ova upozorenja nisu blokirala rad.

Model je uspešno preuzet i embedding indeks je napravljen.

## 5. Implementirane komponente

U retrieval-only v1 postoje:

```text
src/config.py
src/frontmatter_parser.py
src/loader.py
src/chunker.py
src/intent_classifier.py
src/retriever.py

scripts/build_index.py
scripts/ask.py
```

Implementirano je:

- učitavanje Markdown dokumenata
- YAML frontmatter parsing
- chunking po Markdown sekcijama
- template-based contextual chunk prefix
- embedding nad `contextual_chunk_text`
- lokalni retrieval preko sentence-transformers embedding-a
- rule-based intent detection
- subject/course name detection
- metadata boosting
- debug output
- retrieval-only CLI režim

## 6. Contextual chunking status

Contextual chunking radi.

Svaki chunk ima:

```text
original_chunk_text
contextual_prefix
contextual_chunk_text
```

Embedding se računa nad:

```text
contextual_chunk_text = contextual_prefix + "\n\n" + original_chunk_text
```

Debug output prikazuje `contextual_prefix`, što je potvrđeno tokom testiranja.

## 7. Test 1, Razvoj softvera i Flask

Komanda:

```text
python scripts/ask.py "Da li se na Razvoju softvera sada radi Flask?" --retrieval-only
```

Očekivanje:

- intent treba da bude `COURSE_PLAN_CURRENT`
- predmet treba da bude `Razvoj softvera`
- top rezultati treba da favorizuju `03_course_plans/2025_2026/razvoj_softvera.md`

Rezultat:

```text
PASS
```

Potvrđeno:

- `Detected intent: COURSE_PLAN_CURRENT`
- `Detected course names: Razvoj softvera`
- top rezultati su iz `03_course_plans/2025_2026/razvoj_softvera.md`
- document_type je `course_plan`
- contextual prefix jasno kaže da je dokument aktuelni plan rada 2025/2026

Zaključak:

Course_plan prioritet radi za pitanja koja sadrže “sada” ili “trenutno”.

## 8. Test 2, nastavnik i Nove informacione tehnologije

Komanda:

```text
python scripts/ask.py "Ko drži Nove informacione tehnologije i da li je profesor dobar?" --retrieval-only
```

Prvi rezultat je bio `NEEDS_REVIEW`, jer predmet nije bio prepoznat.

Nakon izmene `intent_classifier.py` i `retriever.py`, ponovljeni test je prošao.

Rezultat:

```text
PASS
```

Potvrđeno:

- `Detected intent: FALLBACK`
- `Detected course names: Nove informacione tehnologije`
- top rezultati uključuju `06_policy/pit_navigator_answering_policy.md`
- top rezultati uključuju `04_baskets/2027/pit_minor_electives_reference.md`
- policy dokument ostaje visoko kada pitanje traži ocenu profesora

Zaključak:

Fallback i policy aktivacija rade za pitanja o nastavnicima i saradnicima.

## 9. Test 3, Ekonometrija

Komanda:

```text
python scripts/ask.py "Šta se tačno radi na Ekonometriji?" --retrieval-only
```

Prvi rezultat je bio `NEEDS_REVIEW`, jer:

- predmet nije bio prepoznat
- `pit_minor_electives_reference.md`, sekcija `4.18 Ekonometrija`, bila je tek na 8. mestu
- sekcija `Monetarna ekonomija` bila je iznad exact match sekcije

Nakon izmene `intent_classifier.py`, `retriever.py` i `ask.py`, test je prošao.

Rezultat:

```text
PASS
```

Potvrđeno:

- `Detected intent: FALLBACK`
- `Detected course names: Ekonometrija`
- top rezultat je `04_baskets/2027/pit_minor_electives_reference.md`
- section_heading je `4.18 Ekonometrija`
- srodne sekcije kao `Monetarna ekonomija` više nisu iznad exact match sekcije

Zaključak:

Minor elective fallback radi za predmete bez posebnog course dokumenta.

## 10. Test 4, izbor za AI

Komanda:

```text
python scripts/ask.py "Šta da izaberem ako me zanima AI?" --retrieval-only
```

Rezultat:

```text
PASS
```

Potvrđeno:

- top rezultat je `04_baskets/2027/pit_data_ai_bi_korpa.md`
- visoko je povučena sekcija `5.2 Ako studenta zanima AI`
- povučen je i `pit_izborne_korpe_overview.md`
- retrieval jasno prepoznaje da je pitanje o izboru po interesovanju

Napomena:

Među top rezultatima nisu bili pojedinačni course dokumenti za:

```text
01_courses/2027/masinsko_ucenje.md
01_courses/2027/operaciona_istrazivanja.md
01_courses/2027/elektronsko_poslovanje_i_vestacka_inteligencija.md
```

Ovo nije blokirajući problem za v1, jer tematska korpa sadrži relevantnu preporuku.

Za v1.1 razmotriti document diversity, da se uz korpu povuče i bar jedan pojedinačni course dokument.

## 11. Test 5, PIN 2020 vs PIT 2027

Komanda:

```text
python scripts/ask.py "Koja je razlika između PIN 2020 i PIT 2027?" --retrieval-only
```

Rezultat:

```text
PASS
```

Potvrđeno:

- top rezultat je `00_overview/pin_2020_vs_pit_2027.md`
- comparison dokument dominira retrieval-om
- povučene su relevantne sekcije:
  - `Document intro`
  - `1. Kratak zaključak`
  - `2. Kako bot treba da objasni razliku`
  - `4. Šta ostaje zajedničko`
  - `5. Šta se formalno pojačava u PIT 2027`
  - `8. Kako odgovoriti studentu koji pita šta je bolje`

Zaključak:

Comparison retrieval radi dobro.

## 12. Test 6, ERP/SAP konsultant

Komanda:

```text
python scripts/ask.py "Koji predmeti su dobri za ERP/SAP konsultanta?" --retrieval-only
```

Rezultat:

```text
PASS
```

Potvrđeno:

- `Detected intent: CAREER_RECOMMENDATION`
- `Detected course names: ERP softver`
- top rezultati uključuju:
  - `04_baskets/2027/pit_finance_analytics_korpa.md`
  - `04_baskets/2027/pit_software_erp_digital_korpa.md`
  - `03_course_plans/2025_2026/erp_softver.md`
  - `05_retrieval_guides/pit_navigator_intent_examples.md`

Napomena:

U top rezultatima se pojavio i `03_course_plans/2025_2026/masinsko_ucenje.md`, sekcija `ERP / SAP konsultant`.

To nije blokirajući problem, ali za v1.1 treba razmotriti document diversity i subject exact boost za career pitanja, kako bi `ERP softver` bio dosledno iznad srodnih predmeta.

## 13. Test 7, Elektronska trgovina vs Elektronski platni sistemi vs Nove informacione tehnologije

Komanda:

```text
python scripts/ask.py "Da li da izaberem Elektronsku trgovinu, Elektronske platne sisteme ili Nove informacione tehnologije?" --retrieval-only
```

Prvi rezultat je bio `NEEDS_REVIEW`, jer:

- intent je bio `FALLBACK`, a trebalo je `ELECTIVE_RECOMMENDATION`
- `Elektronski platni sistemi` nisu bili prepoznati
- `pit_software_erp_digital_korpa.md` nije bio u top rezultatima
- `pit_izborne_korpe_overview.md` nije bio u top rezultatima

Nakon izmene `intent_classifier.py` i `retriever.py`, test je prošao.

Rezultat:

```text
PASS
```

Potvrđeno:

- `Detected intent: ELECTIVE_RECOMMENDATION`
- `Detected course names` uključuje:
  - `Nove informacione tehnologije`
  - `Elektronska trgovina`
  - `Elektronski platni sistemi`
- top rezultati uključuju:
  - `04_baskets/2027/pit_minor_electives_reference.md`
  - `04_baskets/2027/pit_software_erp_digital_korpa.md`
  - `04_baskets/2027/pit_izborne_korpe_overview.md`
- povučena je izborna pozicija:
  - `Četvrta godina, osmi semestar, Izborni predmet 3`

Napomena:

`Nove informacione tehnologije` su i dalje veoma visoko u retrieval rezultatima. To nije problem za retrieval-only v1, jer su sva tri predmeta i relevantne korpe povučeni.

Kada se doda LLM answer generation, policy i korpe treba da usmere odgovor tako da se NIT ne favorizuje automatski kao najbolji izbor, već da se preporuka veže za interesovanje korisnika.

## 14. Ukupan rezultat testiranja

Ukupan status:

```text
retrieval_only_v1_status: stable_for_initial_testing
```

Prošli testovi:

```text
[x] Flask / Razvoj softvera, course_plan prioritet
[x] Nastavnik / NIT, policy fallback
[x] Ekonometrija, minor elective fallback
[x] AI izbor, data AI BI korpa
[x] PIN 2020 vs PIT 2027, comparison dokument
[x] ERP/SAP konsultant, career recommendation
[x] Elektronska trgovina vs EPS vs NIT, elective recommendation
```

## 15. Poznate granice retrieval-only v1

Retrieval-only v1 radi dovoljno dobro za početno testiranje, ali ima sledeće poznate granice:

### 15.1 Nema LLM odgovora

Sistem za sada ne generiše finalni prirodni odgovor korisniku.

Trenutno prikazuje samo:

- pitanje
- prepoznat intent
- prepoznate predmete
- retrieved dokumente
- section heading
- score
- contextual prefix

### 15.2 Nema document diversity pravila

U nekim testovima svih top 8 rezultata dolazi iz istog dokumenta.

To nije blokirajući problem za retrieval-only v1, ali za v1.1 treba razmotriti:

- ograničenje maksimalnog broja chunk-ova po dokumentu
- obavezno dodavanje sekundarnog dokumenta po intent-u
- bar jedan policy chunk za rizične intent-e
- bar jedan course dokument kada je primary rezultat basket

### 15.3 Nema BM25

Trenutna verzija koristi embedding similarity + metadata boosting.

BM25 nije implementiran.

Za v1.1 razmotriti hibridni retrieval:

```text
dense embedding score + BM25 score + metadata boost
```

### 15.4 Nema reranker

Trenutna verzija nema reranker.

Za v1.2 razmotriti reranking top 20 rezultata.

### 15.5 Nema automatski test runner

Testovi su pokretani ručno preko `scripts/ask.py`.

Za sledeću verziju treba napraviti:

```text
scripts/test_runner.py
```

koji automatski proverava minimalni test set.

## 16. Izmene urađene tokom testiranja

Tokom testiranja su menjani samo retrieval-only fajlovi:

```text
03_implementation/src/intent_classifier.py
03_implementation/src/retriever.py
03_implementation/scripts/ask.py
```

Nisu menjani dokumenti u:

```text
02_knowledge_base/
```

Nije menjan:

```text
03_implementation/scripts/build_index.py
```

Osim ako nije drugačije navedeno, indeks nije morao ponovo da se gradi za izmene u classifier/retriever logici.

## 17. Preporuke za v1.1

Za sledeću iteraciju preporučuje se:

```text
[ ] document diversity
[ ] required secondary documents po intent-u
[ ] obavezni policy chunk za rizična pitanja
[ ] BM25 lexical retrieval
[ ] simple hybrid score: dense + BM25 + metadata boost
[ ] automatski test_runner.py
[ ] JSON/YAML test set na osnovu pit_navigator_test_questions.md
```

## 18. Preporuke za LLM answer generation

Pre dodavanja LLM odgovora treba definisati:

```text
[ ] prompt_builder.py
[ ] minimalni system prompt
[ ] format izvora u odgovoru
[ ] fallback format
[ ] zabrane iz answering policy dokumenta
[ ] način uključivanja policy chunk-ova
[ ] da li LLM odgovor uvek prikazuje izvore
```

LLM answer generation ne treba dodavati dok retrieval-only v1 nije sačuvan kao stabilna osnova.

## 19. Sledeći preporučeni korak

Sledeći korak:

```text
Dodati LLM answer generation ili prvo implementirati test_runner.py.
```

Preporuka:

Prvo napraviti `test_runner.py`, jer će kasnije svaka izmena retrieval-a ili LLM prompt-a moći automatski da se proveri na istom test setu.

## 20. Zaključak

Retrieval-only v1 je uspešno prošao početne kritične testove.

Sistem trenutno pravilno razlikuje:

- aktuelni plan rada i akreditacioni course dokument
- policy pitanja i sadržajna pitanja
- minor electives bez posebnog course dokumenta
- izborne preporuke
- career recommendation pitanja
- comparison pitanja za PIN 2020 i PIT 2027

Status:

```text
stable_for_initial_testing
```

Ova verzija je spremna kao osnova za nastavak implementacije.

## 21. Trenutni status posle whitelist kontrole

Status:

```text
retrieval_only_stable_after_whitelist
```

Potvrđeno:

- `python -m compileall src scripts` prolazi
- `python scripts/test_runner.py` daje 7/7 PASS
- `RetrievalResult` nosi `original_chunk_text` i `contextual_chunk_text`
- exact-term boost je ograničen na whitelist tehničke termine
- exact-term boost više ne važi za obične reči
- `CAREER_RECOMMENDATION` + ERP/SAP basket boost je zadržan kao uski exception
- `--retrieval-only` režim u `ask.py` je očuvan

Whitelist termini:

```text
flask, php, sap, erp, mongodb, pymongo, tkinter, power bi, sql, python,
java, javascript, wordpress, woocommerce, cypress, selenium, postman,
jmeter, mysql, postgresql, postgres, openai, gemini, rag, ai, bi
```

Obične reči ne smeju biti boostovane, posebno:

```text
sada, radi, izaberem, zanima, razlika, između, predmet, student, plan, dobar
```

## 22. Potvrđeni retrieval-only upiti posle whitelist kontrole

### 22.1 Razvoj softvera i Flask

Upit:

```text
Da li se na Razvoju softvera sada radi Flask?
```

Rezultat:

- očekivano vraća `course_plan`
- očekivano vraća `03_course_plans/2025_2026/razvoj_softvera.md`

### 22.2 AI izbor

Upit:

```text
Šta da izaberem ako me zanima AI?
```

Rezultat:

- očekivano vraća `04_baskets/2027/pit_data_ai_bi_korpa.md`
- očekivano vraća `04_baskets/2027/pit_izborne_korpe_overview.md`

### 22.3 PIN 2020 vs PIT 2027

Upit:

```text
Koja je razlika između PIN 2020 i PIT 2027?
```

Rezultat:

- očekivano vraća `00_overview/pin_2020_vs_pit_2027.md`

### 22.4 Elektronska trgovina vs EPS vs NIT

Upit:

```text
Da li da izaberem Elektronsku trgovinu, Elektronske platne sisteme ili Nove informacione tehnologije?
```

Rezultat:

- očekivano vraća `04_baskets/2027/pit_minor_electives_reference.md`
- očekivano vraća `04_baskets/2027/pit_software_erp_digital_korpa.md`
- očekivano vraća `04_baskets/2027/pit_izborne_korpe_overview.md`

### 22.5 ERP/SAP konsultant, izborni predmeti

Upit:

```text
Koji izborni predmeti su najbolji ako želim karijeru kao ERP SAP konsultant?
```

Rezultat:

- detected intents: `ELECTIVE_RECOMMENDATION`, `CAREER_RECOMMENDATION`
- detected course: `ERP softver`
- `04_baskets/2027/pit_software_erp_digital_korpa.md` je na pozicijama 1, 2 i 3

### 22.6 SAP konsultant, šta izabrati

Upit:

```text
Šta da izaberem ako hoću da radim kao SAP konsultant?
```

Rezultat:

- detected intents: `ELECTIVE_RECOMMENDATION`, `CAREER_RECOMMENDATION`
- detected course: `ERP softver`
- `04_baskets/2027/pit_software_erp_digital_korpa.md` je na pozicijama 1, 2 i 3

## 23. Zaključak posle whitelist kontrole

Retrieval-only osnova ostaje stabilna.

`original_chunk_text` i `contextual_chunk_text` ostaju u `RetrievalResult` jer su potrebni za LLM prompt context.

Exact-term boost se zadržava samo kao kontrolisani whitelist mehanizam za tehničke termine.

ERP/SAP career basket boost se zadržava kao uski exception:

```text
CAREER_RECOMMENDATION + ERP/SAP signal + 04_baskets/2027/pit_software_erp_digital_korpa.md
```
