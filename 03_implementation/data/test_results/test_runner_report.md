# PIT Navigator retrieval-only test runner report

Generated at: 2026-05-09T21:33:25.272836+00:00

## Summary

- Total tests: 7
- Passed: 6
- Needs review: 1
- Failed: 0

## Details

### COURSE_PLAN_FLASK: PASS

Question: Da li se na Razvoju softvera sada radi Flask?

Detected intents: COURSE_PLAN_CURRENT, COURSE_EXPLANATION
Detected course names: Razvoj softvera

Retrieved documents:
1. `03_course_plans/2025_2026/razvoj_softvera.md`
   - title: Razvoj softvera
   - document_type: course_plan
   - section_heading: 12. Kako bot treba da objasni predmet
   - score: 0.8347
2. `03_course_plans/2025_2026/razvoj_softvera.md`
   - title: Razvoj softvera
   - document_type: course_plan
   - section_heading: 11. Akreditacioni kontekst
   - score: 0.8279
3. `03_course_plans/2025_2026/razvoj_softvera.md`
   - title: Razvoj softvera
   - document_type: course_plan
   - section_heading: 13. Šta bot ne sme da tvrdi
   - score: 0.8207
4. `01_courses/2027/razvoj_softvera.md`
   - title: Razvoj softvera
   - document_type: course
   - section_heading: 3. Planirani praktični fokus, Python, Flask i AI alati
   - score: 0.8202
5. `01_courses/2027/razvoj_softvera.md`
   - title: Razvoj softvera
   - document_type: course
   - section_heading: 13. Šta bot ne sme da tvrdi
   - score: 0.7764

### FALLBACK_TEACHER_NIT: PASS

Question: Ko drži Nove informacione tehnologije i da li je profesor dobar?

Detected intents: COURSE_EXPLANATION, FALLBACK
Detected course names: Nove informacione tehnologije

Retrieved documents:
1. `04_baskets/2027/pit_minor_electives_reference.md`
   - title: PIT 2027, referenca za izborne predmete bez posebnog course dokumenta
   - document_type: elective_reference
   - section_heading: 4.22 Nove informacione tehnologije
   - score: 1.9237
2. `04_baskets/2027/pit_minor_electives_reference.md`
   - title: PIT 2027, referenca za izborne predmete bez posebnog course dokumenta
   - document_type: elective_reference
   - section_heading: 3.7 Četvrta godina, osmi semestar, Izborni predmet 3
   - score: 1.4497
3. `04_baskets/2027/pit_minor_electives_reference.md`
   - title: PIT 2027, referenca za izborne predmete bez posebnog course dokumenta
   - document_type: elective_reference
   - section_heading: 6. Kako bot treba da odgovara
   - score: 1.3522
4. `06_policy/pit_navigator_answering_policy.md`
   - title: PIT Navigator, pravila odgovaranja
   - document_type: answering_policy
   - section_heading: 10. Pravilo za nastavnike i saradnike
   - score: 1.0601
5. `06_policy/pit_navigator_answering_policy.md`
   - title: PIT Navigator, pravila odgovaranja
   - document_type: answering_policy
   - section_heading: 9. Pravilo za predmete koji nisu prvi prioritet
   - score: 1.0188

### FALLBACK_ECONOMETRIJA: PASS

Question: Šta se tačno radi na Ekonometriji?

Detected intents: FALLBACK
Detected course names: Ekonometrija

Retrieved documents:
1. `04_baskets/2027/pit_minor_electives_reference.md`
   - title: PIT 2027, referenca za izborne predmete bez posebnog course dokumenta
   - document_type: elective_reference
   - section_heading: 4.18 Ekonometrija
   - score: 1.9684
2. `04_baskets/2027/pit_minor_electives_reference.md`
   - title: PIT 2027, referenca za izborne predmete bez posebnog course dokumenta
   - document_type: elective_reference
   - section_heading: 4.20 Ekonomska statistika
   - score: 1.5607
3. `04_baskets/2027/pit_minor_electives_reference.md`
   - title: PIT 2027, referenca za izborne predmete bez posebnog course dokumenta
   - document_type: elective_reference
   - section_heading: 5.3 Ako korisnika zanimaju finansije i podaci
   - score: 1.4434
4. `04_baskets/2027/pit_finance_analytics_korpa.md`
   - title: PIT 2027, Finance analytics korpa
   - document_type: thematic_basket
   - section_heading: 4.7 Ekonometrija
   - score: 0.5752
5. `05_retrieval_guides/pit_navigator_intent_examples.md`
   - title: PIT Navigator, primeri intent-a i očekivanog retrieval-a
   - document_type: retrieval_guide
   - section_heading: 10.4 Primer odgovora
   - score: 0.5717

### ELECTIVE_AI: PASS

Question: Šta da izaberem ako me zanima AI?

Detected intents: ELECTIVE_RECOMMENDATION, INTEREST_BASED_RECOMMENDATION
Detected course names: -

Retrieved documents:
1. `04_baskets/2027/pit_data_ai_bi_korpa.md`
   - title: PIT 2027, Data / AI / BI korpa
   - document_type: thematic_basket
   - section_heading: 5.2 Ako studenta zanima AI
   - score: 1.0032
2. `04_baskets/2027/pit_data_ai_bi_korpa.md`
   - title: PIT 2027, Data / AI / BI korpa
   - document_type: thematic_basket
   - section_heading: 3.5 Elektronsko poslovanje i veštačka inteligencija
   - score: 0.9787
3. `04_baskets/2027/pit_izborne_korpe_overview.md`
   - title: PIT 2027, pregled izbornih korpi i pravila preporuke
   - document_type: basket_overview
   - section_heading: 10. Kako bot treba da odgovara na pitanja o izboru
   - score: 0.8715
4. `04_baskets/2027/pit_data_ai_bi_korpa.md`
   - title: PIT 2027, Data / AI / BI korpa
   - document_type: thematic_basket
   - section_heading: 2. Najkraće objašnjenje za studenta
   - score: 0.8583
5. `04_baskets/2027/pit_minor_electives_reference.md`
   - title: PIT 2027, referenca za izborne predmete bez posebnog course dokumenta
   - document_type: elective_reference
   - section_heading: 5.1 Ako korisnika zanimaju AI, data ili BI
   - score: 0.8315

### COMPARISON_PIN_PIT: PASS

Question: Koja je razlika između PIN 2020 i PIT 2027?

Detected intents: PROGRAM_OVERVIEW, ACCREDITATION_COMPARISON
Detected course names: -

Retrieved documents:
1. `00_overview/pin_2020_vs_pit_2027.md`
   - title: PIN 2020 i PIT 2027, poređenje
   - document_type: overview
   - section_heading: Document intro
   - score: 1.0023
2. `00_overview/pin_2020_vs_pit_2027.md`
   - title: PIN 2020 i PIT 2027, poređenje
   - document_type: overview
   - section_heading: 5. Šta se formalno pojačava u PIT 2027
   - score: 0.9855
3. `00_overview/pin_2020_vs_pit_2027.md`
   - title: PIN 2020 i PIT 2027, poređenje
   - document_type: overview
   - section_heading: 1. Kratak zaključak
   - score: 0.9805
4. `06_policy/pit_navigator_answering_policy.md`
   - title: PIT Navigator, pravila odgovaranja
   - document_type: answering_policy
   - section_heading: 4. Pravilo za PIT 2027 i PIN 2020
   - score: 0.8226
5. `05_retrieval_guides/pit_navigator_retrieval_map.md`
   - title: PIT Navigator, retrieval mapa dokumenata
   - document_type: retrieval_guide
   - section_heading: 9. Pravila za modernizaciju PIN 2020
   - score: 0.7937

### CAREER_ERP_SAP: PASS

Question: Koji predmeti su dobri za ERP/SAP konsultanta?

Detected intents: COURSE_EXPLANATION, CAREER_RECOMMENDATION
Detected course names: ERP softver

Retrieved documents:
1. `01_courses/2027/erp_softver.md`
   - title: ERP softver
   - document_type: course
   - section_heading: 9.1 ERP / SAP konsultant
   - score: 1.5810
2. `04_baskets/2027/pit_software_erp_digital_korpa.md`
   - title: PIT 2027, Software / ERP / digital korpa
   - document_type: thematic_basket
   - section_heading: 3.3 ERP softver
   - score: 1.5357
3. `04_baskets/2027/pit_software_erp_digital_korpa.md`
   - title: PIT 2027, Software / ERP / digital korpa
   - document_type: thematic_basket
   - section_heading: 5.2 Ako studenta zanima ERP / SAP konsultantska putanja
   - score: 1.5310
4. `01_courses/2027/erp_softver.md`
   - title: ERP softver
   - document_type: course
   - section_heading: 5.2 SAP ERP ekosistem
   - score: 1.5089
5. `03_course_plans/2025_2026/erp_softver.md`
   - title: ERP softver
   - document_type: course_plan
   - section_heading: 9.1 ERP / SAP konsultant
   - score: 1.4778

### ELECTIVE_ECOMMERCE_EPS_NIT: NEEDS_REVIEW

Question: Da li da izaberem Elektronsku trgovinu, Elektronske platne sisteme ili Nove informacione tehnologije?

Detected intents: COURSE_EXPLANATION, ELECTIVE_RECOMMENDATION
Detected course names: Nove informacione tehnologije, Elektronska trgovina, Elektronski platni sistemi

Notes:
- Missing paths: 04_baskets/2027/pit_izborne_korpe_overview.md
- At least one retrieved result is from an expected folder.

Retrieved documents:
1. `04_baskets/2027/pit_minor_electives_reference.md`
   - title: PIT 2027, referenca za izborne predmete bez posebnog course dokumenta
   - document_type: elective_reference
   - section_heading: 4.22 Nove informacione tehnologije
   - score: 2.8605
2. `04_baskets/2027/pit_minor_electives_reference.md`
   - title: PIT 2027, referenca za izborne predmete bez posebnog course dokumenta
   - document_type: elective_reference
   - section_heading: 3.7 Četvrta godina, osmi semestar, Izborni predmet 3
   - score: 2.2972
3. `04_baskets/2027/pit_software_erp_digital_korpa.md`
   - title: PIT 2027, Software / ERP / digital korpa
   - document_type: thematic_basket
   - section_heading: 4.3 Nove informacione tehnologije
   - score: 2.2661
4. `04_baskets/2027/pit_minor_electives_reference.md`
   - title: PIT 2027, referenca za izborne predmete bez posebnog course dokumenta
   - document_type: elective_reference
   - section_heading: 6. Kako bot treba da odgovara
   - score: 2.2322
5. `04_baskets/2027/pit_software_erp_digital_korpa.md`
   - title: PIT 2027, Software / ERP / digital korpa
   - document_type: thematic_basket
   - section_heading: 6.4 Četvrta godina, osmi semestar, Izborni predmet 3
   - score: 2.2262
