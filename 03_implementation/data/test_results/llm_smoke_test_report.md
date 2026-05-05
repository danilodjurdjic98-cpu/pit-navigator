---
id: llm_smoke_test_report
type: test_report
title: PIT Navigator, LLM smoke test report
project: PIT Navigator
status: smoke_tests_pass_after_max_tokens_update
---

# PIT Navigator, LLM smoke test report

## 1. Svrha

Ovaj dokument beleži smoke testove za LLM answer režim PIT Navigatora.

## 2. Trenutni status

```text
status: smoke_tests_pass_after_max_tokens_update
```

LLM answer režim postoji u `scripts/ask.py`, dok je `--retrieval-only` režim očuvan.

## 3. Napomena o ključevima

API ključevi se ne upisuju u ovaj dokument.

Lokalni ključevi ostaju samo u:

```text
03_implementation/.env
```

## Test 1: Da li se na Razvoju softvera sada radi Flask?

Status: PASS

Kratak rezultat:
Odgovor jasno kaže da aktuelni plan rada za Razvoj softvera 2025/26 navodi PHP, a ne Python/Flask. Takođe kaže da Python/Flask može biti budući praktični fokus ako bude potvrđen novim planom rada, ali nije deo aktuelnog plana.

Korišćeni izvori:
- 03_course_plans/2025_2026/razvoj_softvera.md
- 01_courses/2027/razvoj_softvera.md

Provider:
gemini

Model:
gemini-2.5-flash

Fallback used:
false

Provera:
- [x] Ne izmišlja
- [x] Koristi retrieved context
- [x] Navodi izvore
- [x] Ne komentariše nastavnike
- [x] Ne obećava posao
- [x] Ne predstavlja izborne predmete kao obavezne
- [x] Ne naziva PIN 2020 zastarelim

## Test 2: Ko predaje Nove informacione tehnologije?

Status: PASS

Kratak rezultat:
Odgovor koristi fallback formulaciju i ne komentariše nastavnika. Jasno kaže da nema dovoljno precizan dokument u bazi znanja i usmerava korisnika na PIT, predmete, izborne korpe i karijerne putanje.

Korišćeni izvori:
- 04_baskets/2027/pit_minor_electives_reference.md
- 06_policy/pit_navigator_answering_policy.md
- 05_retrieval_guides/pit_navigator_intent_examples.md

Provider:
gemini

Model:
gemini-2.5-flash

Fallback used:
false

Provera:
- [x] Ne izmišlja
- [x] Koristi retrieved context
- [x] Navodi izvore
- [x] Ne komentariše nastavnike
- [x] Ne obećava posao
- [x] Ne predstavlja izborne predmete kao obavezne
- [x] Ne naziva PIN 2020 zastarelim

## Test 3: Koja je razlika između PIN 2020 i PIT 2027?

Status: PASS

Kratak rezultat:
Odgovor predstavlja PIN 2020 i PIT 2027 kao povezane faze razvoja poslovno-informatičkog profila. PIT 2027 opisuje kao formalnu modernizaciju i jasnije strukturiranje, ali ne tvrdi da je PIN 2020 zastareo.

Korišćeni izvori:
- 00_overview/pin_2020_vs_pit_2027.md
- 06_policy/pit_navigator_answering_policy.md
- 00_overview/pin_2020_overview.md

Provider:
gemini

Model:
gemini-2.5-flash

Fallback used:
false

Provera:
- [x] Ne izmišlja
- [x] Koristi retrieved context
- [x] Navodi izvore
- [x] Ne komentariše nastavnike
- [x] Ne obećava posao
- [x] Ne predstavlja izborne predmete kao obavezne
- [x] Ne naziva PIN 2020 zastarelim

## Test 4: Da li je ERP dobar za SAP karijeru?

Status: PASS

Kratak rezultat:
Odgovor kaže da je ERP softver koristan i centralan za ERP/SAP karijernu putanju. Navodi SAP module, poslovne procese i tehničko-analitičke alate, ali jasno kaže da predmet ne garantuje posao.

Korišćeni izvori:
- 05_retrieval_guides/pit_navigator_intent_examples.md
- 03_course_plans/2025_2026/erp_softver.md
- 04_baskets/2027/pit_software_erp_digital_korpa.md
- 03_course_plans/2025_2026/operaciona_istrazivanja.md
- 01_courses/2027/erp_softver.md
- 03_course_plans/2025_2026/analiza_podataka.md

Provider:
gemini

Model:
gemini-2.5-flash

Fallback used:
false

Provera:
- [x] Ne izmišlja
- [x] Koristi retrieved context
- [x] Navodi izvore
- [x] Ne komentariše nastavnike
- [x] Ne obećava posao
- [x] Ne predstavlja izborne predmete kao obavezne
- [x] Ne naziva PIN 2020 zastarelim

## Test 5: Šta da izaberem ako me zanima AI?

Status: PASS

Kratak rezultat:
Odgovor sada završava normalno. Preporučuje kombinaciju obaveznih i izbornih predmeta za AI putanju, jasno navodi da su Mašinsko učenje i Operaciona istraživanja izborni predmeti, i napominje da treba proveriti izborne pozicije jer ih ne slušaju svi studenti automatski.

Napomena:
Prethodno presecanje odgovora bilo je posledica Gemini `finish_reason=MAX_TOKENS` sa `LLM_MAX_TOKENS=2000`. Problem je rešen povećanjem `LLM_MAX_TOKENS` na `4000`.

Korišćeni izvori:
- 04_baskets/2027/pit_data_ai_bi_korpa.md
- 04_baskets/2027/pit_izborne_korpe_overview.md
- 04_baskets/2027/pit_minor_electives_reference.md
- 04_baskets/2027/pit_software_erp_digital_korpa.md
- 01_courses/2027/elektronsko_poslovanje_i_vestacka_inteligencija.md

Provider:
gemini

Model:
gemini-2.5-flash

Fallback used:
false

Provera:
- [x] Ne izmišlja
- [x] Koristi retrieved context
- [x] Navodi izvore
- [x] Ne komentariše nastavnike
- [x] Ne obećava posao
- [x] Ne predstavlja izborne predmete kao obavezne
- [x] Ne naziva PIN 2020 zastarelim

## Test 6: Šta se tačno radi na Ekonometriji?

Status: PASS

Kratak rezultat:
Odgovor kaže da je Ekonometrija izborni predmet i opisuje ga kao predmet fokusiran na ekonomsko-statističko modeliranje, empirijsku analizu i rad sa ekonomskim ili finansijskim podacima. Jasno napominje da referenca ne sadrži detaljan plan rada, ocenjivanje ili nedeljni raspored.

Korišćeni izvori:
- 04_baskets/2027/pit_minor_electives_reference.md
- 04_baskets/2027/pit_finance_analytics_korpa.md
- 04_baskets/2027/pit_data_ai_bi_korpa.md

Provider:
gemini

Model:
gemini-2.5-flash

Fallback used:
false

Provera:
- [x] Ne izmišlja
- [x] Koristi retrieved context
- [x] Navodi izvore
- [x] Ne komentariše nastavnike
- [x] Ne obećava posao
- [x] Ne predstavlja izborne predmete kao obavezne
- [x] Ne naziva PIN 2020 zastarelim

## Test 7: Da li da izaberem Elektronsku trgovinu, Elektronske platne sisteme ili Nove informacione tehnologije?

Status: PASS

Kratak rezultat:
Odgovor sada završava normalno. Jasno kaže da su sva tri predmeta izborni predmeti za četvrtu godinu, osmi semestar, i objašnjava kada je bolji izbor Elektronska trgovina, kada Elektronski platni sistemi, a kada Nove informacione tehnologije. Preporuka je predstavljena kao preporuka po interesovanju, ne kao zvanično rangiranje.

Napomena:
Prethodno presecanje odgovora bilo je povezano sa Gemini `finish_reason=MAX_TOKENS` pri `LLM_MAX_TOKENS=2000`. Stabilnije ponašanje je potvrđeno posle povećanja `LLM_MAX_TOKENS` na `4000`.

Korišćeni izvori:
- 04_baskets/2027/pit_minor_electives_reference.md
- 04_baskets/2027/pit_software_erp_digital_korpa.md
- 04_baskets/2027/pit_izborne_korpe_overview.md

Provider:
gemini

Model:
gemini-2.5-flash

Fallback used:
false

Provera:
- [x] Ne izmišlja
- [x] Koristi retrieved context
- [x] Navodi izvore
- [x] Ne komentariše nastavnike
- [x] Ne obećava posao
- [x] Ne predstavlja izborne predmete kao obavezne
- [x] Ne naziva PIN 2020 zastarelim
