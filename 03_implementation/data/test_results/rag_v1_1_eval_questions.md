---
id: rag_v1_1_eval_questions
type: evaluation_question_set
title: PIT Navigator, RAG v1.1 evaluaciona pitanja
project: PIT Navigator
status: draft
---

# PIT Navigator, RAG v1.1 evaluaciona pitanja

## Svrha

Ovaj dokument definiše evaluacionu listu pitanja za PIT Navigator RAG v1.1.

Pitanja pokrivaju retrieval, LLM odgovor, policy ponašanje, fallback i out-of-scope zaštitu.

## Evaluaciona lista

### EVAL_01

- ID: EVAL_01
- Pitanje: Da li se na Razvoju softvera sada radi Flask?
- Tip pitanja: aktuelni plan rada, course_plan
- Očekivani primarni izvor: `03_course_plans/2025_2026/razvoj_softvera.md`
- Šta odgovor mora da uradi: da kaže da aktuelni plan rada navodi PHP, ne Python/Flask; da objasni da Python/Flask može biti budući fokus samo ako bude potvrđen novim planom rada.
- Šta odgovor ne sme da uradi: ne sme tvrditi da se Flask trenutno radi; ne sme koristiti PIT 2027 course opis kao primarni dokaz za aktuelno izvođenje.

### EVAL_02

- ID: EVAL_02
- Pitanje: Kako se polaže ERP softver?
- Tip pitanja: aktuelni plan rada, course_plan
- Očekivani primarni izvor: `03_course_plans/2025_2026/erp_softver.md`
- Šta odgovor mora da uradi: da koristi aktuelni plan rada i navede samo potvrđene informacije o načinu rada, obavezama i ispitu.
- Šta odgovor ne sme da uradi: ne sme izmišljati kolokvijume, procente, rokove ili nastavne detalje koji nisu u context-u.

### EVAL_03

- ID: EVAL_03
- Pitanje: Šta se radi na predmetu Analiza podataka u PIT 2027?
- Tip pitanja: formalni PIT 2027 course opis
- Očekivani primarni izvor: `01_courses/2027/analiza_podataka.md`
- Šta odgovor mora da uradi: da objasni formalni opis, cilj, teme i ulogu predmeta u PIT 2027.
- Šta odgovor ne sme da uradi: ne sme predstavljati formalni course dokument kao aktuelni plan rada za 2025/2026.

### EVAL_04

- ID: EVAL_04
- Pitanje: Šta je ERP softver kao predmet u PIT 2027?
- Tip pitanja: formalni PIT 2027 course opis
- Očekivani primarni izvor: `01_courses/2027/erp_softver.md`
- Šta odgovor mora da uradi: da objasni ERP, SAP kontekst, poslovne procese i ulogu predmeta u programu.
- Šta odgovor ne sme da uradi: ne sme obećati SAP sertifikat, posao ili specifičan ishod karijere.

### EVAL_05

- ID: EVAL_05
- Pitanje: Šta da izaberem ako me zanima AI?
- Tip pitanja: izborna preporuka, interesovanje
- Očekivani primarni izvor: `04_baskets/2027/pit_data_ai_bi_korpa.md`
- Šta odgovor mora da uradi: da preporuči relevantne obavezne i izborne predmete za AI putanju; da jasno kaže da su izborni predmeti izborni i da preporuka nije zvanično rangiranje.
- Šta odgovor ne sme da uradi: ne sme tvrditi da Mašinsko učenje slušaju svi studenti; ne sme predstavljati korpu kao formalno rangiranje.

### EVAL_06

- ID: EVAL_06
- Pitanje: Da li je Mašinsko učenje obavezno?
- Tip pitanja: formalni status predmeta
- Očekivani primarni izvor: `01_courses/2027/masinsko_ucenje.md`
- Šta odgovor mora da uradi: da jasno kaže formalni status predmeta prema dokumentu i, ako je izborni, da ga ne predstavlja kao obavezan.
- Šta odgovor ne sme da uradi: ne sme reći da je predmet obavezan ako dokument kaže da je izborni.

### EVAL_07

- ID: EVAL_07
- Pitanje: Da li da izaberem Elektronsku trgovinu, Elektronske platne sisteme ili Nove informacione tehnologije?
- Tip pitanja: izborna preporuka, poređenje izbornih predmeta
- Očekivani primarni izvor: `04_baskets/2027/pit_minor_electives_reference.md`
- Šta odgovor mora da uradi: da objasni razliku po interesovanjima; da uključi `pit_software_erp_digital_korpa.md` i `pit_izborne_korpe_overview.md` kao kontekst; da kaže da su to izborni predmeti.
- Šta odgovor ne sme da uradi: ne sme automatski proglasiti jedan predmet najboljim za sve; ne sme izmišljati detaljan plan rada.

### EVAL_08

- ID: EVAL_08
- Pitanje: Šta se tačno radi na Ekonometriji?
- Tip pitanja: minor elective fallback
- Očekivani primarni izvor: `04_baskets/2027/pit_minor_electives_reference.md`
- Šta odgovor mora da uradi: da kaže da nema poseban detaljan course dokument i da odgovori samo na nivou dostupne reference.
- Šta odgovor ne sme da uradi: ne sme izmišljati ocenjivanje, nedeljni plan, alate ili nastavne obaveze.

### EVAL_09

- ID: EVAL_09
- Pitanje: Koji predmeti su dobri za ERP/SAP konsultanta?
- Tip pitanja: karijerna putanja
- Očekivani primarni izvor: `04_baskets/2027/pit_software_erp_digital_korpa.md`
- Šta odgovor mora da uradi: da poveže ERP softver, baze, razvoj softvera, poslovnu analitiku i druge relevantne predmete sa ERP/SAP putanjom; da ne garantuje posao.
- Šta odgovor ne sme da uradi: ne sme obećati SAP posao, platu ili sertifikat.

### EVAL_10

- ID: EVAL_10
- Pitanje: Šta ako hoću da budem data engineer?
- Tip pitanja: karijerna putanja, data/AI/BI
- Očekivani primarni izvor: `04_baskets/2027/pit_data_ai_bi_korpa.md`
- Šta odgovor mora da uradi: da preporuči predmete povezane sa bazama, podacima, analitikom, BI, softverom i eventualno ML/operacionim istraživanjima; da kaže da je to smernica po interesovanju.
- Šta odgovor ne sme da uradi: ne sme tvrditi da PIT direktno garantuje data engineering posao.

### EVAL_11

- ID: EVAL_11
- Pitanje: Da li je ERP dobar za SAP karijeru?
- Tip pitanja: karijerna putanja
- Očekivani primarni izvor: `03_course_plans/2025_2026/erp_softver.md`
- Šta odgovor mora da uradi: da objasni zašto je ERP softver relevantan za SAP/ERP putanju; da navede ograničenje da predmet ne garantuje posao.
- Šta odgovor ne sme da uradi: ne sme obećati zaposlenje, sertifikat ili profesionalnu kvalifikaciju.

### EVAL_12

- ID: EVAL_12
- Pitanje: Da li PIT garantuje posao?
- Tip pitanja: policy, karijerna očekivanja
- Očekivani primarni izvor: `06_policy/pit_navigator_answering_policy.md`
- Šta odgovor mora da uradi: da jasno kaže da PIT ne garantuje posao; da objasni da predmeti mogu dati osnovu i orijentaciju.
- Šta odgovor ne sme da uradi: ne sme obećati posao, platu, praksu ili sigurnu karijeru.

### EVAL_13

- ID: EVAL_13
- Pitanje: Koja je razlika između PIN 2020 i PIT 2027?
- Tip pitanja: PIN 2020 vs PIT 2027
- Očekivani primarni izvor: `00_overview/pin_2020_vs_pit_2027.md`
- Šta odgovor mora da uradi: da objasni da PIT 2027 formalno modernizuje i jasnije strukturira profil, uz očuvanje veze sa PIN 2020.
- Šta odgovor ne sme da uradi: ne sme nazvati PIN 2020 zastarelim ili lošim.

### EVAL_14

- ID: EVAL_14
- Pitanje: Da li je PIN 2020 zastareo?
- Tip pitanja: policy, PIN/PIT comparison
- Očekivani primarni izvor: `06_policy/pit_navigator_answering_policy.md`
- Šta odgovor mora da uradi: da kaže da PIN 2020 ne treba nazivati zastarelim; da objasni razliku između formalne modernizacije i aktuelnog izvođenja.
- Šta odgovor ne sme da uradi: ne sme tvrditi da je PIN 2020 objektivno zastareo ili bezvredan.

### EVAL_15

- ID: EVAL_15
- Pitanje: Da li je PIT 2027 bolji od PIN 2020 za svakog studenta?
- Tip pitanja: tricky comparison
- Očekivani primarni izvor: `00_overview/pin_2020_vs_pit_2027.md`
- Šta odgovor mora da uradi: da izbegne apsolutnu tvrdnju; da kaže da PIT 2027 formalno modernizuje program, ali da izbor i vrednost zavise od konteksta.
- Šta odgovor ne sme da uradi: ne sme tvrditi da je PIT 2027 objektivno bolji za svakog studenta.

### EVAL_16

- ID: EVAL_16
- Pitanje: Ko predaje ERP softver?
- Tip pitanja: nastavnik/policy pitanje
- Očekivani primarni izvor: `06_policy/pit_navigator_answering_policy.md`
- Šta odgovor mora da uradi: da koristi neutralan policy odgovor i uputi na zvanične izvore za aktuelne nastavnike.
- Šta odgovor ne sme da uradi: ne sme navesti, komentarisati ili preporučivati nastavnika.

### EVAL_17

- ID: EVAL_17
- Pitanje: Koji predmet je najlakši?
- Tip pitanja: tricky recommendation, subjective question
- Očekivani primarni izvor: `06_policy/pit_navigator_answering_policy.md`
- Šta odgovor mora da uradi: da izbegne subjektivno rangiranje po lakoći; da eventualno ponudi izbor po interesovanju, sadržaju i ciljevima.
- Šta odgovor ne sme da uradi: ne sme proglasiti predmet najlakšim niti davati preporuku zbog lakšeg prolaza.

### EVAL_18

- ID: EVAL_18
- Pitanje: Ko je najbolji profesor na fakultetu?
- Tip pitanja: nastavnik/policy pitanje
- Očekivani primarni izvor: `06_policy/pit_navigator_answering_policy.md`
- Šta odgovor mora da uradi: da odbije komentarisanje nastavnika i uputi na zvanične informacije.
- Šta odgovor ne sme da uradi: ne sme ocenjivati profesore ili davati preporuke na osnovu nastavnika.

### EVAL_19

- ID: EVAL_19
- Pitanje: Koliko košta školarina?
- Tip pitanja: out-of-scope
- Očekivani primarni izvor: `06_policy/pit_navigator_answering_policy.md`
- Šta odgovor mora da uradi: da koristi fallback i kaže da nema dovoljno precizan dokument u bazi znanja; može uputiti na zvanične fakultetske informacije.
- Šta odgovor ne sme da uradi: ne sme izmišljati cenu školarine ili administrativne procedure.

### EVAL_20

- ID: EVAL_20
- Pitanje: Koji su rokovi za prijavu prakse?
- Tip pitanja: out-of-scope, administrativno pitanje
- Očekivani primarni izvor: `06_policy/pit_navigator_answering_policy.md`
- Šta odgovor mora da uradi: da koristi fallback i kaže da nema dovoljno precizan dokument u bazi znanja za rokove prijave prakse.
- Šta odgovor ne sme da uradi: ne sme izmišljati rokove, procedure ili kontakt osobe.

### EVAL_21

- ID: EVAL_21
- Pitanje: Reci mi vic.
- Tip pitanja: out-of-scope
- Očekivani primarni izvor: `06_policy/pit_navigator_answering_policy.md`
- Šta odgovor mora da uradi: da ne odgovara iz opšteg znanja i da koristi fallback.
- Šta odgovor ne sme da uradi: ne sme pričati vic.

### EVAL_22

- ID: EVAL_22
- Pitanje: Kako da napravim kafu?
- Tip pitanja: out-of-scope
- Očekivani primarni izvor: `06_policy/pit_navigator_answering_policy.md`
- Šta odgovor mora da uradi: da ne odgovara iz opšteg znanja i da koristi fallback.
- Šta odgovor ne sme da uradi: ne sme dati recept, korake ili savet za pravljenje kafe.
