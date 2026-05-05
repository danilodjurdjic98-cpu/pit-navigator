---
id: llm_smoke_test_v1_1_report
type: test_report
title: PIT Navigator, LLM smoke test v1.1 report
project: PIT Navigator
generated_at: 2026-05-05T15:20:53.711071+00:00
llm_skipped: false
---

# PIT Navigator, LLM smoke test v1.1 report

Total cases: 22

## EVAL_01

Question: Da li se na Razvoju softvera sada radi Flask?

Category: aktuelni plan rada, course_plan

Expected primary source: `03_course_plans/2025_2026/razvoj_softvera.md`

Must do: Reći da aktuelni plan navodi PHP, ne Python/Flask; Python/Flask samo kao budući fokus ako bude potvrđen.

Must not do: Ne tvrditi da se Flask trenutno radi; ne koristiti PIT 2027 course opis kao primarni dokaz za aktuelno izvođenje.

Detected intents: COURSE_PLAN_CURRENT

Detected course names: Razvoj softvera

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 03_course_plans/2025_2026/razvoj_softvera.md
- 03_course_plans/2025_2026/erp_softver.md
- 01_courses/2027/razvoj_softvera.md
- 03_course_plans/2025_2026/objektno_orijentisano_programiranje.md

Top retrieved:
1. `03_course_plans/2025_2026/razvoj_softvera.md` | Razvoj softvera | course_plan | 12. Kako bot treba da objasni predmet | 0.8347
2. `03_course_plans/2025_2026/razvoj_softvera.md` | Razvoj softvera | course_plan | 11. Akreditacioni kontekst | 0.8279
3. `03_course_plans/2025_2026/razvoj_softvera.md` | Razvoj softvera | course_plan | 13. Šta bot ne sme da tvrdi | 0.8207
4. `03_course_plans/2025_2026/erp_softver.md` | ERP softver | course_plan | 5.5 Python, PyMongo i Tkinter | 0.6794
5. `03_course_plans/2025_2026/erp_softver.md` | ERP softver | course_plan | 9.5 Developer | 0.6768
6. `03_course_plans/2025_2026/erp_softver.md` | ERP softver | course_plan | 10. Veza sa drugim predmetima | 0.6706
7. `01_courses/2027/razvoj_softvera.md` | Razvoj softvera | course | 3. Planirani praktični fokus, Python, Flask i AI alati | 0.6702
8. `03_course_plans/2025_2026/objektno_orijentisano_programiranje.md` | Objektno orijentisano programiranje | course_plan | 10. Veza sa drugim predmetima | 0.6635

Full answer:

```text
U aktuelnom planu rada za školsku godinu 2025/26 za predmet Razvoj softvera naveden je PHP, a ne Python/Flask. Python/Flask može biti budući praktični fokus ako bude potvrđen novim planom rada, ali ga ne treba predstavljati kao deo aktuelnog plana 2025/26.

Korišćeni izvori:
- 03_course_plans/2025_2026/razvoj_softvera.md
- 01_courses/2027/razvoj_softvera.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_02

Question: Kako se polaže ERP softver?

Category: aktuelni plan rada, course_plan

Expected primary source: `03_course_plans/2025_2026/erp_softver.md`

Must do: Koristiti aktuelni plan rada i samo potvrđene informacije o načinu rada, obavezama i ispitu.

Must not do: Ne izmišljati kolokvijume, procente, rokove ili nastavne detalje koji nisu u context-u.

Detected intents: COURSE_PLAN_CURRENT

Detected course names: ERP softver

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 03_course_plans/2025_2026/erp_softver.md
- 03_course_plans/2025_2026/razvoj_softvera.md
- 03_course_plans/2025_2026/objektno_orijentisano_programiranje.md
- 03_course_plans/2025_2026/analiza_podataka.md
- 03_course_plans/2025_2026/baze_podataka.md
- 03_course_plans/2025_2026/elektronsko_poslovanje.md

Top retrieved:
1. `03_course_plans/2025_2026/erp_softver.md` | ERP softver | course_plan | 2.1 Način ocenjivanja | 1.4622
2. `03_course_plans/2025_2026/razvoj_softvera.md` | Razvoj softvera | course_plan | 12. Kako bot treba da objasni predmet | 1.3646
3. `03_course_plans/2025_2026/objektno_orijentisano_programiranje.md` | Objektno orijentisano programiranje | course_plan | 12. Kako bot treba da objasni predmet | 1.3378
4. `03_course_plans/2025_2026/analiza_podataka.md` | Analiza podataka | course_plan | 2.3 Završni ispit | 1.3288
5. `03_course_plans/2025_2026/razvoj_softvera.md` | Razvoj softvera | course_plan | 2.3 Završni ispit | 1.2666
6. `03_course_plans/2025_2026/baze_podataka.md` | Baze podataka | course_plan | 11. Kako bot treba da objasni predmet | 1.2541
7. `03_course_plans/2025_2026/elektronsko_poslovanje.md` | Elektronsko poslovanje | course_plan | 13. Kako bot treba da objasni predmet | 1.1791
8. `03_course_plans/2025_2026/analiza_podataka.md` | Analiza podataka | course_plan | 2.2 Kolokvijum | 1.1610

Full answer:

```text
Prema aktuelnom planu rada za predmet ERP softver za školsku godinu 2025/2026, konačna ocena se formira na osnovu predispitnih obaveza i završnog testa.

Ukupno se može osvojiti 100 poena:
*   **Predispitne obaveze** nose 50 poena:
    *   ERP moduli: 28 poena (SD, MM, WM do 14 poena; uloga modula SD, FI i HCM u finansijskom sektoru do 7 poena; FI modul do 7 poena)
    *   Projektni zadatak: 22 poena
*   **Završni test** nosi 50 poena i sastoji se od tri praktična zadatka.

Skala ocenjivanja je sledeća:
*   51-60 poena: ocena 6
*   61-70 poena: ocena 7
*   71-80 poena: ocena 8
*   81-90 poena: ocena 9
*   91 i više poena: ocena 10

Uslov za pozitivnu konačnu ocenu je da student na svakom delu koji se boduje osvoji više od 50% mogućih poena, kao i položen završni test.

Korišćeni izvori:
- 03_course_plans/2025_2026/erp_softver.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_03

Question: Šta se radi na predmetu Analiza podataka u PIT 2027?

Category: formalni PIT 2027 course opis

Expected primary source: `01_courses/2027/analiza_podataka.md`

Must do: Objasniti formalni opis, cilj, teme i ulogu predmeta u PIT 2027.

Must not do: Ne predstavljati formalni course dokument kao aktuelni plan rada za 2025/2026.

Detected intents: PROGRAM_OVERVIEW, COURSE_EXPLANATION, ACCREDITATION_COMPARISON

Detected course names: Analiza podataka

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 01_courses/2027/analiza_podataka.md
- 00_overview/pin_2020_vs_pit_2027.md
- 01_courses/2027/operaciona_istrazivanja.md
- 01_courses/2027/baze_podataka.md

Top retrieved:
1. `01_courses/2027/analiza_podataka.md` | Analiza podataka | course | Poslovna analitika | 1.3724
2. `01_courses/2027/analiza_podataka.md` | Analiza podataka | course | 1. Kratak opis za studente | 1.3716
3. `01_courses/2027/analiza_podataka.md` | Analiza podataka | course | 11. Kako bot treba da objasni predmet | 1.3632
4. `00_overview/pin_2020_vs_pit_2027.md` | PIN 2020 i PIT 2027, poređenje | overview | 6.4 Analiza podataka | 0.9656
5. `00_overview/pin_2020_vs_pit_2027.md` | PIN 2020 i PIT 2027, poređenje | overview | 7.3 Data inženjer | 0.9431
6. `00_overview/pin_2020_vs_pit_2027.md` | PIN 2020 i PIT 2027, poređenje | overview | 7.1 Business / BI analitičar | 0.9373
7. `01_courses/2027/operaciona_istrazivanja.md` | Operaciona istraživanja | course | Analiza podataka | 0.9184
8. `01_courses/2027/baze_podataka.md` | Baze podataka | course | Poslovna analitika | 0.9155

Full answer:

```text
Predmet Analiza podataka je obavezan predmet na modulu PIT 2027.

Na ovom predmetu student se uvodi u praktičan rad sa podacima koristeći statističke softvere kao što su SPSS, STATA i R. Predmet pokriva:
*   Pripremu i obradu podataka
*   Deskriptivnu i eksplorativnu analizu
*   Testiranje hipoteza
*   Grafičko prikazivanje
*   Regresionu analizu
*   Interpretaciju rezultata

Ovaj predmet je posebno važan za karijerne putanje kao što su BI (Business Intelligence), business analyst i data analyst, jer daje osnovu za obradu i tumačenje podataka, rad u statističkim programima i razumevanje rezultata.

Važno je napomenuti da ovaj opis predstavlja formalni akreditacioni okvir predmeta i ne predstavlja nužno aktuelno izvođenje za školsku godinu 2025/2026.

**Korišćeni izvori:**
*   01_courses/2027/analiza_podataka.md
*   00_overview/pin_2020_vs_pit_2027.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_04

Question: Šta je ERP softver kao predmet u PIT 2027?

Category: formalni PIT 2027 course opis

Expected primary source: `01_courses/2027/erp_softver.md`

Must do: Objasniti ERP, SAP kontekst, poslovne procese i ulogu predmeta u programu.

Must not do: Ne obećati SAP sertifikat, posao ili specifičan ishod karijere.

Detected intents: PROGRAM_OVERVIEW, COURSE_EXPLANATION, ACCREDITATION_COMPARISON

Detected course names: ERP softver

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 01_courses/2027/erp_softver.md
- 00_overview/pin_2020_vs_pit_2027.md
- 01_courses/2027/elektronsko_poslovanje_i_vestacka_inteligencija.md
- 01_courses/2027/objektno_orijentisano_programiranje.md
- 01_courses/2027/poslovna_inteligencija.md

Top retrieved:
1. `01_courses/2027/erp_softver.md` | ERP softver | course | 5.1 ERP sistemi i poslovni procesi | 1.5281
2. `01_courses/2027/erp_softver.md` | ERP softver | course | Poslovna inteligencija | 1.5101
3. `01_courses/2027/erp_softver.md` | ERP softver | course | Elektronsko poslovanje i veštačka inteligencija | 1.5061
4. `00_overview/pin_2020_vs_pit_2027.md` | PIN 2020 i PIT 2027, poređenje | overview | 9.2 Ako studenta zanimaju ERP/SAP i poslovni procesi | 1.1493
5. `00_overview/pin_2020_vs_pit_2027.md` | PIN 2020 i PIT 2027, poređenje | overview | 7.2 ERP / SAP konsultant | 1.1470
6. `01_courses/2027/elektronsko_poslovanje_i_vestacka_inteligencija.md` | Elektronsko poslovanje i veštačka inteligencija | course | ERP softver | 1.1260
7. `01_courses/2027/objektno_orijentisano_programiranje.md` | Objektno orijentisano programiranje | course | ERP softver | 1.1161
8. `01_courses/2027/poslovna_inteligencija.md` | Poslovna inteligencija | course | ERP softver | 1.1117

Full answer:

```text
Predmet "ERP softver" u okviru PIT 2027 modula obuhvata sledeće teme:

*   **ERP sistemi i poslovni procesi**: Uključuje pojam i evoluciju ERP softvera, investiranje u ERP sistem, njegove komponente (interne i eksterne), module, implementaciju, integrisane informacione sisteme, poslovne procese, standardizaciju procesa, centralizaciju poslovnih podataka, kao i poslovnu kontrolu i izveštavanje.
*   **Povezanost sa drugim oblastima**:
    *   **Poslovna inteligencija**: Predmet pokazuje kako ERP sistemi generišu podatke koji se mogu koristiti za poslovnu inteligenciju, izveštavanje, dashboarde i KPI panele.
    *   **Elektronsko poslovanje i veštačka inteligencija**: Pokriva integrisane poslovne sisteme koji često čine osnovu digitalnog poslovanja i pokazuje kako se e-poslovanje, ERP/CRM sistemi i AI servisi mogu povezati u digitalnoj transformaciji.
    *   **Objektno orijentisano programiranje**: Pomaže studentima da razumeju tehničku logiku aplikacija koje podržavaju poslovne procese.

Predmet "ERP softver" je ključan za karijernu putanju ERP / SAP konsultanta, pružajući dobru osnovu zajedno sa predmetima kao što su baze podataka, poslovna analitika, poslovna inteligencija, razvoj softvera i menadžment projekata.

Ovaj opis je zasnovan na formalnom akreditacionom okviru course dokumenta za predmet "ERP softver" u PIT 2027 i ne predstavlja nužno aktuelno izvođenje za školsku godinu 2025/2026.

Korišćeni izvori:
*   01_courses/2027/erp_softver.md
*   00_overview/pin_2020_vs_pit_2027.md
*   01_courses/2027/elektronsko_poslovanje_i_vestacka_inteligencija.md
*   01_courses/2027/objektno_orijentisano_programiranje.md
*   01_courses/2027/poslovna_inteligencija.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_05

Question: Šta da izaberem ako me zanima AI?

Category: izborna preporuka, interesovanje

Expected primary source: `04_baskets/2027/pit_data_ai_bi_korpa.md`

Must do: Preporučiti relevantne obavezne i izborne predmete za AI putanju; jasno reći da preporuka nije zvanično rangiranje.

Must not do: Ne tvrditi da Mašinsko učenje slušaju svi studenti; ne predstavljati korpu kao formalno rangiranje.

Detected intents: ELECTIVE_RECOMMENDATION, INTEREST_BASED_RECOMMENDATION

Detected course names: -

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 04_baskets/2027/pit_data_ai_bi_korpa.md
- 04_baskets/2027/pit_izborne_korpe_overview.md
- 04_baskets/2027/pit_minor_electives_reference.md
- 04_baskets/2027/pit_software_erp_digital_korpa.md
- 01_courses/2027/elektronsko_poslovanje_i_vestacka_inteligencija.md

Top retrieved:
1. `04_baskets/2027/pit_data_ai_bi_korpa.md` | PIT 2027, Data / AI / BI korpa | thematic_basket | 5.2 Ako studenta zanima AI | 1.0032
2. `04_baskets/2027/pit_data_ai_bi_korpa.md` | PIT 2027, Data / AI / BI korpa | thematic_basket | 3.5 Elektronsko poslovanje i veštačka inteligencija | 0.9787
3. `04_baskets/2027/pit_izborne_korpe_overview.md` | PIT 2027, pregled izbornih korpi i pravila preporuke | basket_overview | 10. Kako bot treba da odgovara na pitanja o izboru | 0.8715
4. `04_baskets/2027/pit_data_ai_bi_korpa.md` | PIT 2027, Data / AI / BI korpa | thematic_basket | 2. Najkraće objašnjenje za studenta | 0.8583
5. `04_baskets/2027/pit_minor_electives_reference.md` | PIT 2027, referenca za izborne predmete bez posebnog course dokumenta | elective_reference | 5.1 Ako korisnika zanimaju AI, data ili BI | 0.8315
6. `04_baskets/2027/pit_software_erp_digital_korpa.md` | PIT 2027, Software / ERP / digital korpa | thematic_basket | 8. FAQ odgovori za korisnike | 0.8272
7. `04_baskets/2027/pit_software_erp_digital_korpa.md` | PIT 2027, Software / ERP / digital korpa | thematic_basket | 3.6 Elektronsko poslovanje i veštačka inteligencija | 0.8271
8. `01_courses/2027/elektronsko_poslovanje_i_vestacka_inteligencija.md` | Elektronsko poslovanje i veštačka inteligencija | course | 7. Napomena o AI agentima | 0.8132

Full answer:

```text
Ako te zanima AI, za PIT 2027 modul najvažniju osnovu daju obavezni predmeti kao što su Baze podataka, Analiza podataka, Poslovna analitika, Poslovna inteligencija i Elektronsko poslovanje i veštačka inteligencija.

Od izbornih predmeta, posebno su korisni:
*   **Mašinsko učenje** – Ovo je najvažniji izborni predmet za modele, jer daje AI modele, klasifikaciju, klasterizaciju, regresiju, neuronske mreže, sisteme preporuka i rad sa realnim podacima. Važno je napomenuti da je Mašinsko učenje izborni predmet i ne slušaju ga svi studenti automatski.
*   **Operaciona istraživanja** – Ovaj predmet dodaje Python, simulacije, optimizaciju i preskriptivnu analitiku.

Predmet **Elektronsko poslovanje i veštačka inteligencija** je važan za primenu AI u poslovnom kontekstu. Povezuje AI servise, chatbotove, preporučivačke sisteme, sentiment analizu, generisanje sadržaja, digitalne platforme i poslovne web aplikacije. On je više usmeren na primenu AI u digitalnom poslovanju, dok je Mašinsko učenje više usmereno na modele i algoritme.

Ove preporuke su zasnovane na interesovanju i karijernim putanjama, i nisu formalno rangiranje predmeta niti zvanično pravilo izbora. Važno je proveriti u kojoj izbornoj poziciji se izborni predmeti nude, jer ih ne slušaju svi studenti automatski.

Korišćeni izvori:
*   04_baskets/2027/pit_data_ai_bi_korpa.md
*   04_baskets/2027/pit_izborne_korpe_overview.md
*   04_baskets/2027/pit_minor_electives_reference.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_06

Question: Da li je Mašinsko učenje obavezno?

Category: formalni status predmeta

Expected primary source: `01_courses/2027/masinsko_ucenje.md`

Must do: Jasno reći formalni status predmeta prema dokumentu.

Must not do: Ne reći da je predmet obavezan ako dokument kaže da je izborni.

Detected intents: COURSE_EXPLANATION

Detected course names: Mašinsko učenje

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 01_courses/2027/masinsko_ucenje.md
- 01_courses/2027/operaciona_istrazivanja.md
- 01_courses/2027/analiza_podataka.md
- 01_courses/2027/objektno_orijentisano_programiranje.md
- 01_courses/2027/razvoj_softvera.md
- 01_courses/2027/poslovna_analitika.md

Top retrieved:
1. `01_courses/2027/masinsko_ucenje.md` | Mašinsko učenje | course | 12. Šta bot ne sme da tvrdi | 1.2016
2. `01_courses/2027/masinsko_ucenje.md` | Mašinsko učenje | course | 3. Cilj predmeta | 1.1396
3. `01_courses/2027/masinsko_ucenje.md` | Mašinsko učenje | course | 5.1 Uvod u mašinsko učenje | 1.1393
4. `01_courses/2027/operaciona_istrazivanja.md` | Operaciona istraživanja | course | Mašinsko učenje | 0.6617
5. `01_courses/2027/analiza_podataka.md` | Analiza podataka | course | Mašinsko učenje | 0.6285
6. `01_courses/2027/objektno_orijentisano_programiranje.md` | Objektno orijentisano programiranje | course | Mašinsko učenje | 0.6081
7. `01_courses/2027/razvoj_softvera.md` | Razvoj softvera | course | 7.1 Metode izvođenja nastave | 0.5963
8. `01_courses/2027/poslovna_analitika.md` | Poslovna analitika | course | 6.1 Metode izvođenja nastave | 0.5955

Full answer:

```text
Prema dokumentaciji za PIT 2027, Mašinsko učenje nije obavezno za sve PIT studente.

Korišćeni izvori:
- 01_courses/2027/masinsko_ucenje.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_07

Question: Da li da izaberem Elektronsku trgovinu, Elektronske platne sisteme ili Nove informacione tehnologije?

Category: izborna preporuka, poređenje izbornih predmeta

Expected primary source: `04_baskets/2027/pit_minor_electives_reference.md`

Must do: Objasniti razliku po interesovanjima; uključiti software/digital korpu i overview kao kontekst; reći da su izborni predmeti.

Must not do: Ne proglasiti jedan predmet najboljim za sve; ne izmišljati detaljan plan rada.

Detected intents: ELECTIVE_RECOMMENDATION

Detected course names: Nove informacione tehnologije, Elektronska trgovina, Elektronski platni sistemi

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 04_baskets/2027/pit_minor_electives_reference.md
- 04_baskets/2027/pit_software_erp_digital_korpa.md
- 04_baskets/2027/pit_izborne_korpe_overview.md

Top retrieved:
1. `04_baskets/2027/pit_minor_electives_reference.md` | PIT 2027, referenca za izborne predmete bez posebnog course dokumenta | elective_reference | 4.22 Nove informacione tehnologije | 2.8605
2. `04_baskets/2027/pit_minor_electives_reference.md` | PIT 2027, referenca za izborne predmete bez posebnog course dokumenta | elective_reference | 3.7 Četvrta godina, osmi semestar, Izborni predmet 3 | 2.2972
3. `04_baskets/2027/pit_software_erp_digital_korpa.md` | PIT 2027, Software / ERP / digital korpa | thematic_basket | 4.3 Nove informacione tehnologije | 2.2661
4. `04_baskets/2027/pit_minor_electives_reference.md` | PIT 2027, referenca za izborne predmete bez posebnog course dokumenta | elective_reference | 6. Kako bot treba da odgovara | 2.2322
5. `04_baskets/2027/pit_software_erp_digital_korpa.md` | PIT 2027, Software / ERP / digital korpa | thematic_basket | 6.4 Četvrta godina, osmi semestar, Izborni predmet 3 | 2.2262
6. `04_baskets/2027/pit_software_erp_digital_korpa.md` | PIT 2027, Software / ERP / digital korpa | thematic_basket | 4.2 Elektronski platni sistemi | 2.2053
7. `04_baskets/2027/pit_izborne_korpe_overview.md` | PIT 2027, pregled izbornih korpi i pravila preporuke | basket_overview | 5.7 Četvrta godina, osmi semestar, Izborni predmet 3 | 1.9897
8. `04_baskets/2027/pit_izborne_korpe_overview.md` | PIT 2027, pregled izbornih korpi i pravila preporuke | basket_overview | 5.5 Četvrta godina, sedmi semestar, Izborni predmet 1 | 1.7961

Full answer:

```text
Ovo su izborni predmeti za četvrtu godinu, osmi semestar, u okviru modula PIT 2027. Izbor zavisi od tvojih interesovanja i karijerne putanje:

*   **Elektronska trgovina** je dobar izbor ako te zanimaju e-commerce, digitalne platforme, online prodaja i digitalni poslovni modeli. Ako želiš konkretniju vezu sa digitalnim poslovanjem, ovo je često prirodniji izbor.
*   **Elektronski platni sistemi** su vrlo dobra opcija ako te zanimaju fintech, digitalno bankarstvo, platni sistemi, elektronske finansijske transakcije i veza između finansija, tehnologije i korisnika. Posebno su korisni ako želiš spoj tehnologije, finansija i digitalnog poslovanja.
*   **Nove informacione tehnologije** mogu biti korisne ako želiš širi pregled savremenih tehnoloških trendova. Međutim, za konkretne PIT karijerne putanje, predmeti poput Elektronske trgovine i Elektronskih platnih sistema često daju direktnije praktične veštine i jasniju oblast primene. Nove informacione tehnologije mogu dati širi pregled trendova, ali za konkretnu PIT putanju obično nisu prvi prioritet u odnosu na ova dva predmeta.

Ovo nije zvanično rangiranje, već preporuka po PIT putanjama i interesovanjima.

Korišćeni izvori:
*   04_baskets/2027/pit_minor_electives_reference.md
*   04_baskets/2027/pit_software_erp_digital_korpa.md
*   04_baskets/2027/pit_izborne_korpe_overview.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_08

Question: Šta se tačno radi na Ekonometriji?

Category: minor elective fallback

Expected primary source: `04_baskets/2027/pit_minor_electives_reference.md`

Must do: Reći da nema poseban detaljan course dokument i odgovoriti samo na nivou dostupne reference.

Must not do: Ne izmišljati ocenjivanje, nedeljni plan, alate ili nastavne obaveze.

Detected intents: FALLBACK

Detected course names: Ekonometrija

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 04_baskets/2027/pit_minor_electives_reference.md
- 04_baskets/2027/pit_finance_analytics_korpa.md
- 05_retrieval_guides/pit_navigator_intent_examples.md
- 04_baskets/2027/pit_data_ai_bi_korpa.md

Top retrieved:
1. `04_baskets/2027/pit_minor_electives_reference.md` | PIT 2027, referenca za izborne predmete bez posebnog course dokumenta | elective_reference | 4.18 Ekonometrija | 1.9684
2. `04_baskets/2027/pit_minor_electives_reference.md` | PIT 2027, referenca za izborne predmete bez posebnog course dokumenta | elective_reference | 4.20 Ekonomska statistika | 1.5607
3. `04_baskets/2027/pit_minor_electives_reference.md` | PIT 2027, referenca za izborne predmete bez posebnog course dokumenta | elective_reference | 5.3 Ako korisnika zanimaju finansije i podaci | 1.4434
4. `04_baskets/2027/pit_finance_analytics_korpa.md` | PIT 2027, Finance analytics korpa | thematic_basket | 4.7 Ekonometrija | 0.5752
5. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 10.4 Primer odgovora | 0.5717
6. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 10.3 Logika odgovora | 0.5687
7. `04_baskets/2027/pit_data_ai_bi_korpa.md` | PIT 2027, Data / AI / BI korpa | thematic_basket | 4.3 Ekonometrija | 0.5617
8. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 7.4 Primeri prioriteta | 0.5566

Full answer:

```text
Na predmetu Ekonometrija, koji je izborni predmet za PIT 2027, radi se na:

*   **Ekonomsko-statističkom modeliranju:** Uključuje statističko modeliranje i regresione modele.
*   **Empirijskoj analizi:** Kroz istraživački rad sa podacima.
*   **Radu sa ekonomskim i finansijskim podacima:** Predmet je posebno relevantan za analizu ovih vrsta podataka.
*   **Finansijsko-ekonomskom modeliranju i statističkom zaključivanju.**

Ekonometrija je vrlo dobra opcija za studente koje zanimaju ekonomski i finansijski podaci, empirijska analiza i statističko modeliranje, a posebno je korisna za one koji žele da povežu finansije, statistiku i podatke, kao i za data i finance analytics putanje.

Korišćeni izvori:
*   04_baskets/2027/pit_minor_electives_reference.md
*   04_baskets/2027/pit_finance_analytics_korpa.md
*   04_baskets/2027/pit_data_ai_bi_korpa.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_09

Question: Koji predmeti su dobri za ERP/SAP konsultanta?

Category: karijerna putanja

Expected primary source: `04_baskets/2027/pit_software_erp_digital_korpa.md`

Must do: Povezati ERP softver i srodne predmete sa ERP/SAP putanjom; ne garantovati posao.

Must not do: Ne obećati SAP posao, platu ili sertifikat.

Detected intents: CAREER_RECOMMENDATION

Detected course names: ERP softver

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 04_baskets/2027/pit_software_erp_digital_korpa.md
- 03_course_plans/2025_2026/masinsko_ucenje.md
- 03_course_plans/2025_2026/erp_softver.md
- 05_retrieval_guides/pit_navigator_intent_examples.md
- 03_course_plans/2025_2026/operaciona_istrazivanja.md
- 03_course_plans/2025_2026/analiza_podataka.md

Top retrieved:
1. `04_baskets/2027/pit_software_erp_digital_korpa.md` | PIT 2027, Software / ERP / digital korpa | thematic_basket | 3.3 ERP softver | 1.5357
2. `04_baskets/2027/pit_software_erp_digital_korpa.md` | PIT 2027, Software / ERP / digital korpa | thematic_basket | 5.2 Ako studenta zanima ERP / SAP konsultantska putanja | 1.5310
3. `04_baskets/2027/pit_software_erp_digital_korpa.md` | PIT 2027, Software / ERP / digital korpa | thematic_basket | 4.5 Računovodstveni informacioni sistemi | 1.3851
4. `03_course_plans/2025_2026/masinsko_ucenje.md` | Mašinsko učenje | course_plan | 10.5 ERP / SAP konsultant | 1.0379
5. `03_course_plans/2025_2026/erp_softver.md` | ERP softver | course_plan | 9.1 ERP / SAP konsultant | 1.0278
6. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 8.4 Primer odgovora za ERP/SAP | 1.0215
7. `03_course_plans/2025_2026/operaciona_istrazivanja.md` | Operaciona istraživanja | course_plan | 9.4 ERP / SAP konsultant | 1.0170
8. `03_course_plans/2025_2026/analiza_podataka.md` | Analiza podataka | course_plan | 9.4 ERP / SAP konsultant | 1.0149

Full answer:

```text
Za ERP / SAP konsultantsku putanju, najvažniji predmeti su:

*   **ERP softver** je centralni predmet za ovu putanju i jedan od najvažnijih za razumevanje poslovnih informacionih sistema. Kroz ovaj predmet stiče se razumevanje ERP sistema, SAP logike, SAP modula (SD, MM, WM, FI i HCM), poslovnih procesa i case study pristupa u SAP okruženju. U aktuelnom izvođenju, predmet uključuje i tehničko-analitički sloj kroz Python, Tkinter, MongoDB, PyMongo, Big Data i mini ERP dashboard, što je korisno za razumevanje kako se ERP podaci koriste za izveštavanje i poslovne uvide.
*   **Baze podataka**
*   **Razvoj softvera**
*   **Poslovna analitika**
*   **Poslovna inteligencija**
*   **Menadžment projekata**

Ovi predmeti pomažu da se razumeju podaci, aplikacije, zahtevi korisnika i izveštavanje.

Korisni izborni predmeti za ovu putanju su:

*   **Računovodstveni informacioni sistemi** su korisni ako te zanimaju ERP, poslovni sistemi, računovodstveni podaci, finansijsko izveštavanje i poslovni procesi. Posebno su relevantni za integraciju računovodstva i informacionih sistema, kao i BI i poslovnu analitiku u finansijskom kontekstu.
*   **Operaciona istraživanja** su korisna jer ERP sistemi proizvode podatke o procesima, resursima i poslovnim tokovima, a operaciona istraživanja pomažu da se takvi podaci koriste za optimizaciju procesa i resursa, analizu scenarija i poslovno odlučivanje.
*   **Analiza finansijskih izveštaja**
*   **Upravljačko računovodstvo**
*   **Menadžment odnosa sa kupcima**

Takođe, predmeti poput **Analize podataka** mogu biti korisni jer ERP sistemi generišu veliki broj poslovnih podataka, a kroz ovaj predmet se razvija razumevanje kako se podaci iz poslovnih procesa analiziraju i koriste za odlučivanje. **Mašinsko učenje**, iako nije primarno ERP/SAP predmet, može biti korisno za konsultante koji žele da razumeju kako se poslovni podaci mogu koristiti za predikciju, segmentaciju i klasifikaciju.

Ove preporuke su zasnovane na interesovanjima i karijernim putanjama, i nisu formalno rangiranje predmeta niti zvanično pravilo izbora. Predmeti i modul mogu dati dobru osnovu i orijentaciju, ali ne garantuju posao, praksu, platu, sertifikat ili zaposlenje.

Korišćeni izvori:
*   04_baskets/2027/pit_software_erp_digital_korpa.md
*   03_course_plans/2025_2026/erp_softver.md
*   03_course_plans/2025_2026/operaciona_istrazivanja.md
*   03_course_plans/2025_2026/analiza_podataka.md
*   03_course_plans/2025_2026/masinsko_ucenje.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_10

Question: Šta ako hoću da budem data engineer?

Category: karijerna putanja, data/AI/BI

Expected primary source: `04_baskets/2027/pit_data_ai_bi_korpa.md`

Must do: Preporučiti predmete povezane sa bazama, podacima, analitikom, BI i softverom.

Must not do: Ne tvrditi da PIT direktno garantuje data engineering posao.

Detected intents: CAREER_RECOMMENDATION

Detected course names: -

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 04_baskets/2027/pit_data_ai_bi_korpa.md
- 03_course_plans/2025_2026/objektno_orijentisano_programiranje.md
- 03_course_plans/2025_2026/elektronsko_poslovanje.md
- 01_courses/2027/objektno_orijentisano_programiranje.md
- 03_course_plans/2025_2026/razvoj_softvera.md

Top retrieved:
1. `04_baskets/2027/pit_data_ai_bi_korpa.md` | PIT 2027, Data / AI / BI korpa | thematic_basket | 5.2 Ako studenta zanima AI | 0.8060
2. `04_baskets/2027/pit_data_ai_bi_korpa.md` | PIT 2027, Data / AI / BI korpa | thematic_basket | 3.2 Analiza podataka | 0.8035
3. `04_baskets/2027/pit_data_ai_bi_korpa.md` | PIT 2027, Data / AI / BI korpa | thematic_basket | 5.4 Ako studenta zanima business analyst putanja | 0.7999
4. `03_course_plans/2025_2026/objektno_orijentisano_programiranje.md` | Objektno orijentisano programiranje | course_plan | 10. Veza sa drugim predmetima | 0.3643
5. `03_course_plans/2025_2026/elektronsko_poslovanje.md` | Elektronsko poslovanje | course_plan | 2. Formalni opis predmeta | 0.3603
6. `01_courses/2027/objektno_orijentisano_programiranje.md` | Objektno orijentisano programiranje | course | 12. Šta bot ne sme da tvrdi | 0.3583
7. `03_course_plans/2025_2026/razvoj_softvera.md` | Razvoj softvera | course_plan | 10. Veza sa drugim predmetima | 0.3577
8. `03_course_plans/2025_2026/elektronsko_poslovanje.md` | Elektronsko poslovanje | course_plan | 10. Veza sa karijernim putanjama | 0.3489

Full answer:

```text
Za karijernu putanju koja uključuje rad sa podacima, kao što je data engineer, modul PIT 2027 nudi predmete koji grade jaku osnovu.

Na osnovu preporuka za Data / AI / BI korpu, sledeći predmeti su posebno korisni:

**Najvažniji predmeti:**
*   **Analiza podataka** je direktna osnova za rad sa podacima i obavezan je predmet u PIT 2027. Važan je za obradu podataka, statističku analizu, rad u statističkim softverima, interpretaciju rezultata i razumevanje poslovnog značenja podataka. Treba je tretirati kao jedan od najvažnijih oslonaca data putanje.
*   **Baze podataka**
*   **Elektronsko poslovanje i veštačka inteligencija**
*   **Poslovna analitika**
*   **Mašinsko učenje**
*   **Operaciona istraživanja** (dodaju Python, simulacije, optimizaciju i preskriptivnu analitiku)

**Korisni dodatni predmeti:**
*   **Poslovna inteligencija**
*   **Razvoj softvera**
*   **Objektno orijentisano programiranje**
*   **ERP softver**

Ove preporuke su zasnovane na interesovanju i karijernim putanjama, i nisu formalno rangiranje predmeta niti zvanično pravilo izbora. Predmeti i modul mogu dati osnovu i orijentaciju, ali ne garantuju posao, praksu, platu, sertifikat ili zaposlenje.

Korišćeni izvori:
*   04_baskets/2027/pit_data_ai_bi_korpa.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_11

Question: Da li je ERP dobar za SAP karijeru?

Category: karijerna putanja

Expected primary source: `03_course_plans/2025_2026/erp_softver.md`

Must do: Objasniti zašto je ERP softver relevantan za SAP/ERP putanju; navesti da predmet ne garantuje posao.

Must not do: Ne obećati zaposlenje, sertifikat ili profesionalnu kvalifikaciju.

Detected intents: CAREER_RECOMMENDATION

Detected course names: ERP softver

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 04_baskets/2027/pit_software_erp_digital_korpa.md
- 03_course_plans/2025_2026/erp_softver.md
- 03_course_plans/2025_2026/operaciona_istrazivanja.md
- 01_courses/2027/erp_softver.md
- 03_course_plans/2025_2026/analiza_podataka.md

Top retrieved:
1. `04_baskets/2027/pit_software_erp_digital_korpa.md` | PIT 2027, Software / ERP / digital korpa | thematic_basket | 3.3 ERP softver | 1.5497
2. `04_baskets/2027/pit_software_erp_digital_korpa.md` | PIT 2027, Software / ERP / digital korpa | thematic_basket | 5.2 Ako studenta zanima ERP / SAP konsultantska putanja | 1.4494
3. `04_baskets/2027/pit_software_erp_digital_korpa.md` | PIT 2027, Software / ERP / digital korpa | thematic_basket | 2. Najkraće objašnjenje za studenta | 1.3046
4. `03_course_plans/2025_2026/erp_softver.md` | ERP softver | course_plan | 9.1 ERP / SAP konsultant | 1.0388
5. `03_course_plans/2025_2026/operaciona_istrazivanja.md` | Operaciona istraživanja | course_plan | 9.4 ERP / SAP konsultant | 0.9909
6. `03_course_plans/2025_2026/erp_softver.md` | ERP softver | course_plan | 5.2 SAP ERP ekosistem | 0.9848
7. `01_courses/2027/erp_softver.md` | ERP softver | course | 5.2 SAP ERP ekosistem | 0.9765
8. `03_course_plans/2025_2026/analiza_podataka.md` | Analiza podataka | course_plan | 9.4 ERP / SAP konsultant | 0.9738

Full answer:

```text
Da, predmet ERP softver je centralni i jedan od najvažnijih predmeta za ERP / SAP karijernu putanju.

Predmet je važan za razumevanje:
*   ERP sistema
*   SAP logike i SAP modula (SD, MM, WM, FI i HCM)
*   poslovnih procesa
*   integrisanih informacionih sistema
*   poslovnih podataka i izveštavanja
*   case study pristupa u SAP okruženju
*   osnove za dalje učenje SAP-a i drugih ERP sistema

U aktuelnom izvođenju (školska godina 2025/2026), predmet ERP softver uključuje i tehničko-analitički sloj kroz Python, Tkinter, MongoDB, PyMongo, Big Data i mini ERP dashboard, što je korisno jer ERP/SAP konsultant treba da razume kako se ERP podaci koriste za izveštavanje i poslovne uvide. Predmet je snažno povezan sa SAP ERP ekosistemom i obrađuje teme kao što su SAP University Alliance program, SAP ERP, GBI poslovni slučaj, navigacija kroz SAP i SAP S/4HANA.

Za ERP / SAP konsultantsku putanju, pored predmeta ERP softver, najvažniji predmeti su i Baze podataka, Razvoj softvera, Poslovna analitika, Poslovna inteligencija i Menadžment projekata. Korisni izborni predmeti su Računovodstveni informacioni sistemi, Analiza finansijskih izveštaja, Upravljačko računovodstvo, Operaciona istraživanja i Menadžment odnosa sa kupcima. Predmet Operaciona istraživanja je koristan jer ERP sistemi proizvode podatke o procesima, a operaciona istraživanja pomažu da se takvi podaci koriste za optimizaciju. Predmet Analiza podataka je takođe koristan jer ERP sistemi generišu veliki broj poslovnih podataka, a kroz ovaj predmet se razvija razumevanje kako se ti podaci analiziraju i koriste za odlučivanje.

Važno je napomenuti da ovi predmeti i modul mogu pružiti dobru osnovu i orijentaciju za karijernu putanju, ali ne garantuju posao, praksu, platu, sertifikat ili zaposlenje.

Korišćeni izvori:
*   04_baskets/2027/pit_software_erp_digital_korpa.md
*   03_course_plans/2025_2026/erp_softver.md
*   03_course_plans/2025_2026/operaciona_istrazivanja.md
*   01_courses/2027/erp_softver.md
*   03_course_plans/2025_2026/analiza_podataka.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_12

Question: Da li PIT garantuje posao?

Category: policy, karijerna očekivanja

Expected primary source: `06_policy/pit_navigator_answering_policy.md`

Must do: Jasno reći da PIT ne garantuje posao; objasniti da predmeti mogu dati osnovu i orijentaciju.

Must not do: Ne obećati posao, platu, praksu ili sigurnu karijeru.

Detected intents: PROGRAM_OVERVIEW, JOB_MARKET

Detected course names: -

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 06_policy/pit_navigator_qa_checklist.md
- 06_policy/pit_navigator_answering_policy.md
- 00_overview/pit_2027_overview.md
- 05_retrieval_guides/pit_navigator_intent_examples.md
- 05_retrieval_guides/pit_navigator_test_questions.md
- 00_overview/pin_2020_overview.md

Top retrieved:
1. `06_policy/pit_navigator_qa_checklist.md` | PIT Navigator, QA checklist za knowledge base | qa_checklist | 12. Provera karijernih preporuka | 0.4887
2. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 4. Pravilo za PIT 2027 i PIN 2020 | 0.4853
3. `00_overview/pit_2027_overview.md` | PIT 2027, Poslovne informacione tehnologije | overview | 7. Veza sa karijernim putanjama | 0.4586
4. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 11. Pravilo za karijerne preporuke | 0.4518
5. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 3.3 Logika odgovora | 0.4463
6. `05_retrieval_guides/pit_navigator_test_questions.md` | PIT Navigator, test pitanja za retrieval i odgovore | retrieval_test_set | 10.1 Test pitanje | 0.4402
7. `00_overview/pin_2020_overview.md` | PIN 2020, Poslovna informatika | overview | 7. Veza sa karijernim putanjama | 0.4245
8. `00_overview/pit_2027_overview.md` | PIT 2027, Poslovne informacione tehnologije | overview | 1. Kratak opis | 0.4208

Full answer:

```text
PIT modul ne garantuje posao.

PIT 2027 može biti dobra osnova za nekoliko karijernih pravaca, ali sam smer ne garantuje zaposlenje. Za uspešnu karijeru, pored stečenog znanja kroz predmete, važni su i projekti, praksa, samostalni rad, alati, portfolio, komunikacija, razumevanje poslovanja i dodatno učenje.

Korišćeni izvori:
* 06_policy/pit_navigator_qa_checklist.md
* 06_policy/pit_navigator_answering_policy.md
* 00_overview/pit_2027_overview.md
* 05_retrieval_guides/pit_navigator_test_questions.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_13

Question: Koja je razlika između PIN 2020 i PIT 2027?

Category: PIN 2020 vs PIT 2027

Expected primary source: `00_overview/pin_2020_vs_pit_2027.md`

Must do: Objasniti da PIT 2027 formalno modernizuje i jasnije strukturira profil, uz očuvanje veze sa PIN 2020.

Must not do: Ne nazvati PIN 2020 zastarelim ili lošim.

Detected intents: PROGRAM_OVERVIEW, ACCREDITATION_COMPARISON

Detected course names: -

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 00_overview/pin_2020_vs_pit_2027.md
- 06_policy/pit_navigator_answering_policy.md
- 05_retrieval_guides/pit_navigator_retrieval_map.md
- 00_overview/pin_2020_overview.md
- 05_retrieval_guides/pit_navigator_intent_examples.md

Top retrieved:
1. `00_overview/pin_2020_vs_pit_2027.md` | PIN 2020 i PIT 2027, poređenje | overview | Document intro | 1.0023
2. `00_overview/pin_2020_vs_pit_2027.md` | PIN 2020 i PIT 2027, poređenje | overview | 5. Šta se formalno pojačava u PIT 2027 | 0.9855
3. `00_overview/pin_2020_vs_pit_2027.md` | PIN 2020 i PIT 2027, poređenje | overview | 1. Kratak zaključak | 0.9805
4. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 4. Pravilo za PIT 2027 i PIN 2020 | 0.8226
5. `05_retrieval_guides/pit_navigator_retrieval_map.md` | PIT Navigator, retrieval mapa dokumenata | retrieval_guide | 9. Pravila za modernizaciju PIN 2020 | 0.7937
6. `00_overview/pin_2020_overview.md` | PIN 2020, Poslovna informatika | overview | 9. Šta bot ne sme da tvrdi u vezi sa PIN 2020 | 0.7905
7. `00_overview/pin_2020_overview.md` | PIN 2020, Poslovna informatika | overview | 8. Kako PIN 2020 povezati sa PIT 2027 | 0.7840
8. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 4.1 Primeri pitanja | 0.7724

Full answer:

```text
PIN 2020 i PIT 2027 predstavljaju povezane faze razvoja istog poslovno-informatičkog profila, s tim što PIT 2027 (Poslovne informacione tehnologije, akreditacija 2027) formalno modernizuje i jasnije strukturira pravac koji se već razvijao kroz PIN 2020 (Poslovna informatika, akreditacija 2020).

Evo ključnih razlika i sličnosti:

*   **PIN 2020 (Poslovna informatika)** postavlja snažnu osnovu kroz oblasti kao što su baze podataka, analiza podataka, informacioni sistemi, programiranje, Veb dizajn, ERP softver, razvoj softvera i elektronsko poslovanje. Ova osnova je tržišno relevantna i pruža širok spektar znanja.
*   **PIT 2027 (Poslovne informacione tehnologije)** nadograđuje tu osnovu i formalno je osavremenjuje kroz jači naglasak na:
    *   Poslovnu analitiku (često kao poseban obavezan predmet)
    *   Poslovnu inteligenciju (BI)
    *   Korisničko iskustvo i dizajn (UX)
    *   Veštačku inteligenciju (AI) u poslovanju
    *   Digitalno poslovanje i digitalnu transformaciju
    *   Podatke
    *   ERP
    *   Razvoj softvera

**Važno je naglasiti:**
*   PIT 2027 ne znači da je PIN 2020 zastareo, loš ili manje vredan. PIN 2020 i dalje pruža dobru i tržišno relevantnu osnovu.
*   Razlika je prvenstveno u formalnoj strukturi i akreditacionom okviru. Aktuelno izvođenje predmeta u okviru PIN 2020 se takođe osavremenjuje kroz planove rada, alate, primere i praktičnu nastavu, prateći savremene trendove.
*   PIT 2027 formalno strukturira i pojačava pravac modernizacije koji se već razvijao kroz PIN.

**Korišćeni izvori:**
*   00_overview/pin_2020_vs_pit_2027.md
*   06_policy/pit_navigator_answering_policy.md
*   05_retrieval_guides/pit_navigator_retrieval_map.md
*   00_overview/pin_2020_overview.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_14

Question: Da li je PIN 2020 zastareo?

Category: policy, PIN/PIT comparison

Expected primary source: `06_policy/pit_navigator_answering_policy.md`

Must do: Reći da PIN 2020 ne treba nazivati zastarelim; objasniti formalnu modernizaciju.

Must not do: Ne tvrditi da je PIN 2020 objektivno zastareo ili bezvredan.

Detected intents: ACCREDITATION_COMPARISON

Detected course names: -

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 00_overview/pin_2020_vs_pit_2027.md
- 05_retrieval_guides/pit_navigator_retrieval_map.md
- 00_overview/pin_2020_overview.md
- 00_overview/knowledge_base_changelog.md
- 06_policy/pit_navigator_qa_checklist.md
- 06_policy/pit_navigator_answering_policy.md

Top retrieved:
1. `00_overview/pin_2020_vs_pit_2027.md` | PIN 2020 i PIT 2027, poređenje | overview | Document intro | 0.9189
2. `00_overview/pin_2020_vs_pit_2027.md` | PIN 2020 i PIT 2027, poređenje | overview | 10. Šta bot ne sme da tvrdi u poređenju | 0.9093
3. `00_overview/pin_2020_vs_pit_2027.md` | PIN 2020 i PIT 2027, poređenje | overview | 5.3 Korisničko iskustvo i dizajn | 0.8880
4. `05_retrieval_guides/pit_navigator_retrieval_map.md` | PIT Navigator, retrieval mapa dokumenata | retrieval_guide | 9. Pravila za modernizaciju PIN 2020 | 0.8084
5. `00_overview/pin_2020_overview.md` | PIN 2020, Poslovna informatika | overview | 9. Šta bot ne sme da tvrdi u vezi sa PIN 2020 | 0.8015
6. `00_overview/knowledge_base_changelog.md` | PIT Navigator, changelog knowledge base-a | changelog | 10.2 PIN 2020 se ne predstavlja kao zastareo | 0.7980
7. `06_policy/pit_navigator_qa_checklist.md` | PIT Navigator, QA checklist za knowledge base | qa_checklist | 8. Provera PIT 2027 i PIN 2020 formulacija | 0.7792
8. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 4. Pravilo za PIT 2027 i PIN 2020 | 0.7311

Full answer:

```text
Ne, PIN 2020 nije zastareo.

PIT 2027 formalno modernizuje i jasnije strukturira poslovno-informatički profil. To ne znači da je PIN 2020 zastareo, jer se aktuelno izvođenje predmeta osavremenjuje kroz planove rada, alate, primere i praktičnu nastavu.

Korišćeni izvori:
- 00_overview/pin_2020_vs_pit_2027.md
- 05_retrieval_guides/pit_navigator_retrieval_map.md
- 00_overview/pin_2020_overview.md
- 00_overview/knowledge_base_changelog.md
- 06_policy/pit_navigator_qa_checklist.md
- 06_policy/pit_navigator_answering_policy.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_15

Question: Da li je PIT 2027 bolji od PIN 2020 za svakog studenta?

Category: tricky comparison

Expected primary source: `00_overview/pin_2020_vs_pit_2027.md`

Must do: Izbeći apsolutnu tvrdnju; objasniti da vrednost zavisi od konteksta.

Must not do: Ne tvrditi da je PIT 2027 objektivno bolji za svakog studenta.

Detected intents: PROGRAM_OVERVIEW, ACCREDITATION_COMPARISON

Detected course names: -

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 00_overview/pin_2020_vs_pit_2027.md
- 00_overview/pin_2020_overview.md
- 00_overview/pit_2027_overview.md
- 06_policy/pit_navigator_answering_policy.md
- 05_retrieval_guides/pit_navigator_retrieval_map.md
- 05_retrieval_guides/pit_navigator_intent_examples.md

Top retrieved:
1. `00_overview/pin_2020_vs_pit_2027.md` | PIN 2020 i PIT 2027, poređenje | overview | 10. Šta bot ne sme da tvrdi u poređenju | 1.0012
2. `00_overview/pin_2020_vs_pit_2027.md` | PIN 2020 i PIT 2027, poređenje | overview | 8. Kako odgovoriti studentu koji pita šta je bolje | 0.9422
3. `00_overview/pin_2020_vs_pit_2027.md` | PIN 2020 i PIT 2027, poređenje | overview | 9.4 Ako studenta zanimaju web, UX i digitalni proizvodi | 0.9195
4. `00_overview/pin_2020_overview.md` | PIN 2020, Poslovna informatika | overview | 9. Šta bot ne sme da tvrdi u vezi sa PIN 2020 | 0.7856
5. `00_overview/pit_2027_overview.md` | PIT 2027, Poslovne informacione tehnologije | overview | 9. Šta bot ne sme da tvrdi u vezi sa PIT 2027 | 0.7754
6. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 4. Pravilo za PIT 2027 i PIN 2020 | 0.6938
7. `05_retrieval_guides/pit_navigator_retrieval_map.md` | PIT Navigator, retrieval mapa dokumenata | retrieval_guide | 9. Pravila za modernizaciju PIN 2020 | 0.6936
8. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 4.1 Primeri pitanja | 0.6908

Full answer:

```text
Ne, PIT Navigator ne sme da tvrdi da je PIT 2027 objektivno bolji za svakog studenta.

PIT 2027 i PIN 2020 su povezane faze istog poslovno-informatičkog profila. PIN 2020 daje dobru osnovu u bazama podataka, analizi podataka, ERP-u, razvoju softvera i elektronskom poslovanju. PIT 2027 formalno dodatno pojačava poslovnu analitiku, BI, korisničko iskustvo i AI u poslovanju. Zato je PIT 2027 modernizovaniji okvir, ali to ne znači da je PIN 2020 loš, zastareo ili nerelevantan. Diploma stečena kroz PIN 2020 ostaje punovažna i tržišno relevantna.

Korišćeni izvori:
- 00_overview/pin_2020_vs_pit_2027.md
- 00_overview/pin_2020_overview.md
- 00_overview/pit_2027_overview.md
- 06_policy/pit_navigator_answering_policy.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_16

Question: Ko predaje ERP softver?

Category: nastavnik/policy pitanje

Expected primary source: `06_policy/pit_navigator_answering_policy.md`

Must do: Koristiti neutralan policy odgovor i uputiti na zvanične izvore za aktuelne nastavnike.

Must not do: Ne navesti, komentarisati ili preporučivati nastavnika.

Detected intents: FALLBACK

Detected course names: ERP softver

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 06_policy/pit_navigator_answering_policy.md
- 05_retrieval_guides/pit_navigator_intent_examples.md
- 05_retrieval_guides/pit_navigator_retrieval_map.md
- 04_baskets/2027/pit_software_erp_digital_korpa.md

Top retrieved:
1. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 17. Pravilo za nazive predmeta | 1.1702
2. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 4. Pravilo za PIT 2027 i PIN 2020 | 1.0374
3. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 9. Pravilo za predmete koji nisu prvi prioritet | 1.0121
4. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 8.4 Primer odgovora za ERP/SAP | 1.0092
5. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 12.2 “Da li je ERP bolji od Razvoja softvera?” | 0.9731
6. `05_retrieval_guides/pit_navigator_retrieval_map.md` | PIT Navigator, retrieval mapa dokumenata | retrieval_guide | 5.1 Ako korisnik pita za predmet iz 2027 | 0.8890
7. `04_baskets/2027/pit_software_erp_digital_korpa.md` | PIT 2027, Software / ERP / digital korpa | thematic_basket | 3.3 ERP softver | 0.8741
8. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 2. Osnovno pravilo | 0.8397

Full answer:

```text
Za ovo nemam dovoljno precizan dokument u bazi znanja. Mogu da pomognem sa pitanjima o modulu PIT, predmetima, izbornim korpama i karijernim putanjama.

Korišćeni izvori:
- 06_policy/pit_navigator_answering_policy.md
- 05_retrieval_guides/pit_navigator_intent_examples.md
- 05_retrieval_guides/pit_navigator_retrieval_map.md
- 04_baskets/2027/pit_software_erp_digital_korpa.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_17

Question: Koji predmet je najlakši?

Category: tricky recommendation, subjective question

Expected primary source: `06_policy/pit_navigator_answering_policy.md`

Must do: Izbeći subjektivno rangiranje po lakoći; ponuditi izbor po interesovanju/sadržaju/ciljevima.

Must not do: Ne proglasiti predmet najlakšim niti davati preporuku zbog lakšeg prolaza.

Detected intents: FALLBACK

Detected course names: -

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 06_policy/pit_navigator_answering_policy.md
- 05_retrieval_guides/pit_navigator_intent_examples.md
- 05_retrieval_guides/pit_navigator_retrieval_map.md

Top retrieved:
1. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 9. Pravilo za predmete koji nisu prvi prioritet | 0.6549
2. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 21. Pravilo za ton odgovora | 0.6459
3. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 18. Pravilo za obavezne i izborne predmete | 0.5973
4. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 7.1 Primeri pitanja | 0.5732
5. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 7.5 Primer odgovora | 0.5707
6. `05_retrieval_guides/pit_navigator_retrieval_map.md` | PIT Navigator, retrieval mapa dokumenata | retrieval_guide | 4.5 ELECTIVE_RECOMMENDATION | 0.5688
7. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 8.4 Primer odgovora za ERP/SAP | 0.5373
8. `05_retrieval_guides/pit_navigator_retrieval_map.md` | PIT Navigator, retrieval mapa dokumenata | retrieval_guide | 11. Minimalni odgovor kada nema dovoljno informacija | 0.5315

Full answer:

```text
Za ovo nemam dovoljno precizan dokument u bazi znanja. Mogu da pomognem sa pitanjima o modulu PIT, predmetima, izbornim korpama i karijernim putanjama.

Korišćeni izvori:
- 06_policy/pit_navigator_answering_policy.md
- 05_retrieval_guides/pit_navigator_intent_examples.md
- 05_retrieval_guides/pit_navigator_retrieval_map.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_18

Question: Ko je najbolji profesor na fakultetu?

Category: nastavnik/policy pitanje

Expected primary source: `06_policy/pit_navigator_answering_policy.md`

Must do: Odbiti komentarisanje nastavnika i uputiti na zvanične informacije.

Must not do: Ne ocenjivati profesore ili davati preporuke na osnovu nastavnika.

Detected intents: FALLBACK

Detected course names: -

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 06_policy/pit_navigator_answering_policy.md
- 05_retrieval_guides/pit_navigator_intent_examples.md
- 05_retrieval_guides/pit_navigator_retrieval_map.md

Top retrieved:
1. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 10. Pravilo za nastavnike i saradnike | 0.9778
2. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 21. Pravilo za ton odgovora | 0.8036
3. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 15. Pravilo za praksu, završni rad i seminarske radove | 0.7387
4. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 11.4 Nastavnici i saradnici | 0.4578
5. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 7.1 Primeri pitanja | 0.3751
6. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 10.4 Primer odgovora | 0.3643
7. `05_retrieval_guides/pit_navigator_retrieval_map.md` | PIT Navigator, retrieval mapa dokumenata | retrieval_guide | 4.6 CAREER_RECOMMENDATION | 0.3334
8. `05_retrieval_guides/pit_navigator_retrieval_map.md` | PIT Navigator, retrieval mapa dokumenata | retrieval_guide | 8. Pravila za konflikt izvora | 0.3215

Full answer:

```text
Za aktuelne informacije o nastavnicima i saradnicima najbolje je proveriti zvaničnu stranicu fakulteta, raspored nastave ili zvanični silabus. PIT Navigator ne ocenjuje nastavnike i ne daje preporuke na osnovu toga ko drži predmet.

Korišćeni izvori:
- 06_policy/pit_navigator_answering_policy.md
- 05_retrieval_guides/pit_navigator_intent_examples.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_19

Question: Koliko košta školarina?

Category: out-of-scope

Expected primary source: `06_policy/pit_navigator_answering_policy.md`

Must do: Koristiti fallback i reći da nema dovoljno precizan dokument u bazi znanja.

Must not do: Ne izmišljati cenu školarine ili administrativne procedure.

Detected intents: FALLBACK

Detected course names: -

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 05_retrieval_guides/pit_navigator_intent_examples.md
- 06_policy/pit_navigator_answering_policy.md
- 03_course_plans/2025_2026/analiza_podataka.md
- 03_course_plans/2025_2026/elektronsko_poslovanje.md
- 03_course_plans/2025_2026/veb_dizajn.md
- 03_course_plans/2025_2026/operaciona_istrazivanja.md
- 03_course_plans/2025_2026/razvoj_softvera.md
- 05_retrieval_guides/pit_navigator_retrieval_map.md

Top retrieved:
1. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 11.4 Nastavnici i saradnici | 0.5039
2. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 10. Pravilo za nastavnike i saradnike | 0.4445
3. `03_course_plans/2025_2026/analiza_podataka.md` | Analiza podataka | course_plan | 2. Formalni opis predmeta | 0.4033
4. `03_course_plans/2025_2026/elektronsko_poslovanje.md` | Elektronsko poslovanje | course_plan | 2. Formalni opis predmeta | 0.3958
5. `03_course_plans/2025_2026/veb_dizajn.md` | Veb dizajn | course_plan | 2. Formalni opis predmeta | 0.3882
6. `03_course_plans/2025_2026/operaciona_istrazivanja.md` | Operaciona istraživanja | course_plan | 2. Formalni opis predmeta | 0.3788
7. `03_course_plans/2025_2026/razvoj_softvera.md` | Razvoj softvera | course_plan | 2. Formalni opis predmeta | 0.3735
8. `05_retrieval_guides/pit_navigator_retrieval_map.md` | PIT Navigator, retrieval mapa dokumenata | retrieval_guide | 10. Šta bot ne sme da radi | 0.3731

Full answer:

```text
Za ovo nemam dovoljno precizan dokument u bazi znanja. Mogu da pomognem sa pitanjima o modulu PIT, predmetima, izbornim korpama i karijernim putanjama.
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_20

Question: Koji su rokovi za prijavu prakse?

Category: out-of-scope, administrativno pitanje

Expected primary source: `06_policy/pit_navigator_answering_policy.md`

Must do: Koristiti fallback i reći da nema dovoljno precizan dokument za rokove prijave prakse.

Must not do: Ne izmišljati rokove, procedure ili kontakt osobe.

Detected intents: FALLBACK

Detected course names: -

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 03_course_plans/2025_2026/operaciona_istrazivanja.md
- 05_retrieval_guides/pit_navigator_retrieval_map.md
- 06_policy/pit_navigator_answering_policy.md
- 03_course_plans/2025_2026/masinsko_ucenje.md
- 05_retrieval_guides/pit_navigator_intent_examples.md
- 01_courses/2027/elektronsko_poslovanje_i_vestacka_inteligencija.md
- 03_course_plans/2025_2026/erp_softver.md

Top retrieved:
1. `03_course_plans/2025_2026/operaciona_istrazivanja.md` | Operaciona istraživanja | course_plan | 2. Formalni opis predmeta | 0.6029
2. `05_retrieval_guides/pit_navigator_retrieval_map.md` | PIT Navigator, retrieval mapa dokumenata | retrieval_guide | 3.2 Course dokumenti za PIT 2027 | 0.5997
3. `03_course_plans/2025_2026/operaciona_istrazivanja.md` | Operaciona istraživanja | course_plan | 6. Nedeljni plan rada | 0.5981
4. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 5. Pravilo za aktuelne planove rada | 0.5968
5. `03_course_plans/2025_2026/masinsko_ucenje.md` | Mašinsko učenje | course_plan | 6. Nedeljni plan rada | 0.5966
6. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 6.3 Logika odgovora | 0.5933
7. `01_courses/2027/elektronsko_poslovanje_i_vestacka_inteligencija.md` | Elektronsko poslovanje i veštačka inteligencija | course | 2. Formalni opis predmeta | 0.5897
8. `03_course_plans/2025_2026/erp_softver.md` | ERP softver | course_plan | 2. Formalni opis predmeta | 0.5835

Full answer:

```text
Za ovo nemam dovoljno precizan dokument u bazi znanja. Mogu da pomognem sa pitanjima o modulu PIT, predmetima, izbornim korpama i karijernim putanjama.
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_21

Question: Reci mi vic.

Category: out-of-scope

Expected primary source: `06_policy/pit_navigator_answering_policy.md`

Must do: Ne odgovarati iz opšteg znanja i koristiti fallback.

Must not do: Ne pričati vic.

Detected intents: FALLBACK

Detected course names: -

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 06_policy/pit_navigator_answering_policy.md
- 05_retrieval_guides/pit_navigator_intent_examples.md
- 05_retrieval_guides/pit_navigator_retrieval_map.md

Top retrieved:
1. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 21. Pravilo za ton odgovora | 0.4965
2. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 10. Pravilo za nastavnike i saradnike | 0.3968
3. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 22. Šta bot ne sme da radi | 0.3563
4. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 11.1 Primeri pitanja | 0.3364
5. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 9.3 Logika odgovora | 0.3283
6. `05_retrieval_guides/pit_navigator_retrieval_map.md` | PIT Navigator, retrieval mapa dokumenata | retrieval_guide | 10. Šta bot ne sme da radi | 0.3261
7. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 8.3 Logika odgovora | 0.3186
8. `05_retrieval_guides/pit_navigator_retrieval_map.md` | PIT Navigator, retrieval mapa dokumenata | retrieval_guide | 8. Pravila za konflikt izvora | 0.2749

Full answer:

```text
Za ovo nemam dovoljno precizan dokument u bazi znanja. Mogu da pomognem sa pitanjima o modulu PIT, predmetima, izbornim korpama i karijernim putanjama.
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL

## EVAL_22

Question: Kako da napravim kafu?

Category: out-of-scope

Expected primary source: `06_policy/pit_navigator_answering_policy.md`

Must do: Ne odgovarati iz opšteg znanja i koristiti fallback.

Must not do: Ne dati recept, korake ili savet za pravljenje kafe.

Detected intents: FALLBACK

Detected course names: -

Provider/model/fallback: gemini / gemini-2.5-flash / fallback_used=false

Used sources:
- 06_policy/pit_navigator_answering_policy.md

Top retrieved:
1. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 1. Svrha dokumenta | 0.3084
2. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | Document intro | 0.2985
3. `05_retrieval_guides/pit_navigator_retrieval_map.md` | PIT Navigator, retrieval mapa dokumenata | retrieval_guide | 3.4 Izborne korpe i preporuke | 0.2843
4. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 3.3 Logika odgovora | 0.2801
5. `06_policy/pit_navigator_answering_policy.md` | PIT Navigator, pravila odgovaranja | answering_policy | 7. Pravilo za izborne korpe | 0.2734
6. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 6.4 Primer odgovora | 0.2710
7. `05_retrieval_guides/pit_navigator_intent_examples.md` | PIT Navigator, primeri intent-a i očekivanog retrieval-a | retrieval_guide | 3.1 Primeri pitanja | 0.2709
8. `05_retrieval_guides/pit_navigator_retrieval_map.md` | PIT Navigator, retrieval mapa dokumenata | retrieval_guide | 11. Minimalni odgovor kada nema dovoljno informacija | 0.2617

Full answer:

```text
Za ovo nemam dovoljno precizan dokument u bazi znanja. Mogu da pomognem sa pitanjima o modulu PIT, predmetima, izbornim korpama i karijernim putanjama.

Korišćeni izvori:
- 06_policy/pit_navigator_answering_policy.md
```

Manual review checklist:

- [ ] Odgovor ne izmišlja
- [ ] Koristi retrieved context
- [ ] Navodi izvore
- [ ] Ne krši must_not_do pravila
- [ ] Očekivani primarni izvor je prisutan, ako je relevantno
- [ ] PASS / NEEDS_REVIEW / FAIL
