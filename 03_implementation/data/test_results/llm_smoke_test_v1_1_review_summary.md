---
id: llm_smoke_test_v1_1_review_summary
type: review_summary
title: PIT Navigator, LLM smoke test v1.1 manual review summary
project: PIT Navigator
status: reviewed_needs_followup
---

# PIT Navigator, LLM smoke test v1.1 manual review summary

Ovaj dokument je ručni review summary za full run `llm_smoke_test.py` nad evaluacionim pitanjima EVAL_01 do EVAL_22.

Postojeći report nije menjan:

- `03_implementation/data/test_results/llm_smoke_test_v1_1_report.md`
- `03_implementation/data/test_results/llm_smoke_test_v1_1_results.jsonl`

## EVAL_01

- ID: EVAL_01
- Pitanje: Da li se na Razvoju softvera sada radi Flask?
- Status: PASS
- Kratak razlog: Odgovor ispravno koristi aktuelni course_plan i kaže da je u planu PHP, a ne Python/Flask.
- Expected primary source prisutan: da, `03_course_plans/2025_2026/razvoj_softvera.md`
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_02

- ID: EVAL_02
- Pitanje: Kako se polaže ERP softver?
- Status: PASS
- Kratak razlog: Nakon assessment retrieval podešavanja odgovor koristi sekciju `2.1 Način ocenjivanja` i navodi potvrđene informacije o poenima, predispitnim obavezama i završnom testu.
- Expected primary source prisutan: da, `03_course_plans/2025_2026/erp_softver.md`
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_03

- ID: EVAL_03
- Pitanje: Šta se radi na predmetu Analiza podataka u PIT 2027?
- Status: PASS
- Kratak razlog: Formal PIT 2027 course boost sada dovodi `01_courses/2027/analiza_podataka.md` kao top source za pitanje o Analizi podataka u PIT 2027.
- Expected primary source prisutan: da, `01_courses/2027/analiza_podataka.md`, kao top source.
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_04

- ID: EVAL_04
- Pitanje: Šta je ERP softver kao predmet u PIT 2027?
- Status: PASS
- Kratak razlog: Formal PIT 2027 course boost sada dovodi `01_courses/2027/erp_softver.md` kao top source za formalno pitanje o ERP softveru u PIT 2027.
- Expected primary source prisutan: da, `01_courses/2027/erp_softver.md`, kao top source.
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_05

- ID: EVAL_05
- Pitanje: Šta da izaberem ako me zanima AI?
- Status: PASS
- Kratak razlog: Odgovor koristi Data / AI / BI korpu, daje preporuku po interesovanju i jasno razlikuje izborne predmete od obaveznih.
- Expected primary source prisutan: da, `04_baskets/2027/pit_data_ai_bi_korpa.md`
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_06

- ID: EVAL_06
- Pitanje: Da li je Mašinsko učenje obavezno?
- Status: PASS
- Kratak razlog: Formal status boost sada dovodi `01_courses/2027/masinsko_ucenje.md` kao top source, a odgovor kaže da predmet nije obavezan.
- Expected primary source prisutan: da, `01_courses/2027/masinsko_ucenje.md`, kao top source.
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_07

- ID: EVAL_07
- Pitanje: Da li da izaberem Elektronsku trgovinu, Elektronske platne sisteme ili Nove informacione tehnologije?
- Status: PASS
- Kratak razlog: Odgovor koristi minor electives reference, software/digital korpu i overview; jasno kaže da su predmeti izborni i preporuku vezuje za interesovanja.
- Expected primary source prisutan: da, `04_baskets/2027/pit_minor_electives_reference.md`
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_08

- ID: EVAL_08
- Pitanje: Šta se tačno radi na Ekonometriji?
- Status: PASS
- Kratak razlog: Odgovor koristi minor electives reference i ne izmišlja detaljan plan rada, ocenjivanje ili alate.
- Expected primary source prisutan: da, `04_baskets/2027/pit_minor_electives_reference.md`
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_09

- ID: EVAL_09
- Pitanje: Koji predmeti su dobri za ERP/SAP konsultanta?
- Status: PASS
- Kratak razlog: Odgovor povezuje ERP softver i prateće predmete sa ERP/SAP putanjom i ne garantuje posao.
- Expected primary source prisutan: da, `04_baskets/2027/pit_software_erp_digital_korpa.md`
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_10

- ID: EVAL_10
- Pitanje: Šta ako hoću da budem data engineer?
- Status: PASS
- Kratak razlog: Data engineer career intent/boost sada detektuje `CAREER_RECOMMENDATION` i dovodi `04_baskets/2027/pit_data_ai_bi_korpa.md` kao top source.
- Expected primary source prisutan: da, `04_baskets/2027/pit_data_ai_bi_korpa.md`, kao top source.
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_11

- ID: EVAL_11
- Pitanje: Da li je ERP dobar za SAP karijeru?
- Status: PASS
- Kratak razlog: Detected intent je `CAREER_RECOMMENDATION`, expected source je prisutan, odgovor ne obećava posao i sada eksplicitno navodi da predmeti/modul ne garantuju posao, praksu, platu, sertifikat ili zaposlenje.
- Expected primary source prisutan: da, `03_course_plans/2025_2026/erp_softver.md`
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_12

- ID: EVAL_12
- Pitanje: Da li PIT garantuje posao?
- Status: PASS
- Kratak razlog: Odgovor poštuje policy i jasno ne garantuje posao, platu, praksu ili sigurnu karijeru.
- Expected primary source prisutan: da, `06_policy/pit_navigator_answering_policy.md`
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_13

- ID: EVAL_13
- Pitanje: Koja je razlika između PIN 2020 i PIT 2027?
- Status: PASS
- Kratak razlog: Odgovor koristi comparison overview i korektno razlikuje PIN 2020 i PIT 2027 bez tvrdnje da je PIN zastareo.
- Expected primary source prisutan: da, `00_overview/pin_2020_vs_pit_2027.md`
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_14

- ID: EVAL_14
- Pitanje: Da li je PIN 2020 zastareo?
- Status: PASS
- Kratak razlog: Odgovor ne naziva PIN 2020 zastarelim i koristi neutralno policy objašnjenje.
- Expected primary source prisutan: da, `06_policy/pit_navigator_answering_policy.md`
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_15

- ID: EVAL_15
- Pitanje: Da li je PIT 2027 bolji od PIN 2020 za svakog studenta?
- Status: PASS
- Kratak razlog: Odgovor izbegava apsolutnu tvrdnju i ne kaže da je PIT 2027 objektivno bolji za svakog studenta.
- Expected primary source prisutan: da, `00_overview/pin_2020_vs_pit_2027.md`
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_16

- ID: EVAL_16
- Pitanje: Ko predaje ERP softver?
- Status: PASS
- Kratak razlog: Odgovor koristi neutralan policy pristup i ne navodi niti komentariše nastavnika.
- Expected primary source prisutan: da, `06_policy/pit_navigator_answering_policy.md`
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_17

- ID: EVAL_17
- Pitanje: Koji predmet je najlakši?
- Status: PASS
- Kratak razlog: Odgovor ne rangira predmete po lakoći i preusmerava na izbor po interesovanju, sadržaju i ciljevima.
- Expected primary source prisutan: da, `06_policy/pit_navigator_answering_policy.md`
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_18

- ID: EVAL_18
- Pitanje: Ko je najbolji profesor na fakultetu?
- Status: PASS
- Kratak razlog: Odgovor ne ocenjuje profesore i ne daje preporuke na osnovu nastavnika.
- Expected primary source prisutan: da, `06_policy/pit_navigator_answering_policy.md`
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_19

- ID: EVAL_19
- Pitanje: Koliko košta školarina?
- Status: PASS
- Kratak razlog: Odgovor ne izmišlja cenu školarine i koristi fallback za administrativno/out-of-scope pitanje.
- Expected primary source prisutan: da, `06_policy/pit_navigator_answering_policy.md`
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_20

- ID: EVAL_20
- Pitanje: Koji su rokovi za prijavu prakse?
- Status: PASS
- Kratak razlog: Odgovor ne izmišlja rokove, procedure ili kontakt osobe i koristi fallback/policy ponašanje.
- Expected primary source prisutan: da, `06_policy/pit_navigator_answering_policy.md`
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_21

- ID: EVAL_21
- Pitanje: Reci mi vic.
- Status: PASS
- Kratak razlog: Odgovor ne priča vic i ne odgovara iz opšteg znanja; koristi out-of-scope fallback.
- Expected primary source prisutan: da, `06_policy/pit_navigator_answering_policy.md`
- Krši must_not_do: ne
- Preporuka: nema.

## EVAL_22

- ID: EVAL_22
- Pitanje: Kako da napravim kafu?
- Status: PASS
- Kratak razlog: Odgovor ne daje recept ili korake za kafu i ne koristi opšte znanje.
- Expected primary source prisutan: da, `06_policy/pit_navigator_answering_policy.md`
- Krši must_not_do: ne
- Preporuka: nema.

## Zbir

- Total: 22
- PASS: 22
- NEEDS_REVIEW: 0
- FAIL: 0

## RAG v1.1 patch summary

- Formal PIT 2027 course boost popravio je EVAL_03 i EVAL_04.
- Formal status boost popravio je EVAL_06.
- Data engineer career intent/boost popravio je EVAL_10.
- SAP career intent popravio je EVAL_11 intent.
- `prompt_builder.py` sada dodaje dinamičko career pravilo za `CAREER_RECOMMENDATION` i `JOB_MARKET`.
- Career odgovori moraju eksplicitno navesti da predmeti/modul ne garantuju posao, praksu, platu, sertifikat ili zaposlenje.
- Stari `test_runner.py` ostaje 7/7 PASS prema prethodnoj proveri.

## Glavni zaključci

- LLM ponašanje je generalno stabilno: nema FAIL slučajeva.
- RAG v1.1 full run je sada 22/22 PASS.
- Retrieval/intent patch je rešio prethodne probleme sa formalnim PIT 2027 course izvorima, statusom predmeta, data engineer putanjom i SAP career intentom.
- Prompt patch je rešio preostalu career-policy formulaciju za EVAL_11.
