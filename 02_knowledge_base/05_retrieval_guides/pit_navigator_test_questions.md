---
id: retrieval_guide_pit_navigator_test_questions
type: retrieval_test_set
title: PIT Navigator, test pitanja za retrieval i odgovore
project: PIT Navigator
version: v1.0
last_updated: 2026-05-04
related_intents:
  - PROGRAM_OVERVIEW
  - COURSE_EXPLANATION
  - COURSE_PLAN_CURRENT
  - ACCREDITATION_COMPARISON
  - ELECTIVE_RECOMMENDATION
  - CAREER_RECOMMENDATION
  - INTEREST_BASED_RECOMMENDATION
  - JOB_MARKET
  - FALLBACK
keywords:
  - test pitanja
  - retrieval testing
  - RAG evaluation
  - PIT Navigator
  - intent testing
  - expected documents
  - expected answer
  - QA
  - evaluation
---

# PIT Navigator, test pitanja za retrieval i odgovore

## 1. Svrha dokumenta

Ovaj dokument sadrži test pitanja za proveru PIT Navigator RAG sistema.

Cilj je da se proveri:

- da li bot prepoznaje pravi intent
- da li retrieval povlači pravi tip dokumenta
- da li bot razlikuje PIT 2027 i PIN 2020
- da li bot razlikuje akreditacioni course dokument i aktuelni plan rada
- da li bot razlikuje obavezne i izborne predmete
- da li bot koristi tematske korpe samo kao preporuke, a ne kao formalna pravila
- da li bot koristi fallback kada nema dovoljno informacija
- da li bot ne komentariše nastavnike i saradnike
- da li bot ne obećava posao, platu ili sertifikat
- da li bot ne izmišlja detalje za predmete koji nemaju poseban course dokument

Ovaj dokument ne sadrži nove činjenice o predmetima. Koristi se samo za testiranje retrieval-a i kvaliteta odgovora.

## 2. Kako koristiti ovaj test set

Za svako pitanje treba proveriti:

1. koji intent je prepoznat
2. koji dokumenti su povučeni
3. da li je odgovor zasnovan na pravim dokumentima
4. da li odgovor sadrži očekivane elemente
5. da li odgovor krši neko policy pravilo
6. da li je odgovor dovoljno jasan za studenta

Minimalni QA status testa:

```text
PASS
NEEDS_REVIEW
FAIL
```

Kriterijumi:

```text
PASS: retrieval i odgovor su ispravni
NEEDS_REVIEW: odgovor je uglavnom dobar, ali treba preciznije formulacije
FAIL: povučen je pogrešan dokument, odgovor izmišlja, meša izvore ili krši policy
```

## 3. PROGRAM_OVERVIEW testovi

### 3.1 Test pitanje

```text
Šta je PIT i šta se tu uči?
```

Očekivani intent:

```text
PROGRAM_OVERVIEW
```

Primarni dokumenti:

```text
00_overview/pit_2027_overview.md
```

Sekundarni dokumenti:

```text
04_baskets/2027/pit_izborne_korpe_overview.md
00_overview/knowledge_base_index.md
```

Očekivani elementi odgovora:

- PIT 2027 je poslovno-informatički profil
- povezuje poslovanje, podatke, softver, ERP, BI, poslovnu analitiku, digitalno poslovanje i AI
- nije čist programerski smer
- nije ni čist menadžerski smer
- treba pomenuti obavezne predmete kao osnovu, ali ne predugačko

Policy rizici:

- ne reći da smer garantuje posao
- ne reći da je PIT objektivno bolji od svih drugih smerova

### 3.2 Test pitanje

```text
Da li je PIT više za programere ili za analitičare?
```

Očekivani intent:

```text
PROGRAM_OVERVIEW
INTEREST_BASED_RECOMMENDATION
```

Primarni dokumenti:

```text
00_overview/pit_2027_overview.md
04_baskets/2027/pit_data_ai_bi_korpa.md
04_baskets/2027/pit_software_erp_digital_korpa.md
```

Očekivani elementi odgovora:

- PIT je hibridan profil
- ima tehničke predmete, ali nije čist developer smer
- ima jaku data, BI, ERP i business analyst dimenziju
- student može da se usmeri kroz izborne predmete
- za developer putanju važni su OOP, Razvoj softvera, Baze podataka
- za analitičku putanju važni su Analiza podataka, Poslovna analitika, Poslovna inteligencija, Operaciona istraživanja, Mašinsko učenje

Policy rizici:

- ne predstaviti jednu putanju kao jedinu ispravnu
- ne obećavati karijeru

## 4. ACCREDITATION_COMPARISON testovi

### 4.1 Test pitanje

```text
Koja je razlika između PIN 2020 i PIT 2027?
```

Očekivani intent:

```text
ACCREDITATION_COMPARISON
```

Primarni dokumenti:

```text
00_overview/pin_2020_vs_pit_2027.md
```

Sekundarni dokumenti:

```text
00_overview/pin_2020_overview.md
00_overview/pit_2027_overview.md
```

Očekivani elementi odgovora:

- PIT 2027 formalno modernizuje i jasnije strukturira profil
- pomenuti nove ili jasnije naglašene oblasti: Poslovna analitika, Poslovna inteligencija, UX, AI, ERP, digitalno poslovanje
- PIN 2020 ne treba predstaviti kao zastareo
- aktuelni planovi rada pokazuju osavremenjivanje izvođenja PIN 2020 predmeta

Policy rizici:

- ne reći da je PIN 2020 loš
- ne reći da je PIT 2027 bolji za svakog studenta

### 4.2 Test pitanje

```text
Da li je PIN 2020 zastareo?
```

Očekivani intent:

```text
ACCREDITATION_COMPARISON
```

Primarni dokumenti:

```text
00_overview/pin_2020_vs_pit_2027.md
00_overview/pin_2020_overview.md
06_policy/pit_navigator_answering_policy.md
```

Očekivani elementi odgovora:

- direktno reći da PIN 2020 ne treba nazivati zastarelim
- PIT 2027 formalno jasnije strukturira modernizaciju
- PIN 2020 se u aktuelnom izvođenju osavremenjuje kroz planove rada
- razlika je u formalnoj strukturi i akreditacionom okviru

Policy rizici:

- ne omalovažiti staru akreditaciju
- ne napraviti marketinški odgovor

### 4.3 Test pitanje

```text
Šta je novo u PIT 2027 u odnosu na staru Poslovnu informatiku?
```

Očekivani intent:

```text
ACCREDITATION_COMPARISON
PROGRAM_OVERVIEW
```

Primarni dokumenti:

```text
00_overview/pin_2020_vs_pit_2027.md
00_overview/pit_2027_overview.md
```

Očekivani elementi odgovora:

- jasnije uvedeni ili naglašeni obavezni predmeti iz data, BI, UX, AI, ERP i software oblasti
- formalno jača osnova za poslovnu analitiku, poslovnu inteligenciju, digitalno poslovanje i AI
- izborni predmeti pojačavaju različite putanje
- PIN 2020 ne predstaviti kao loš

Policy rizici:

- ne reći da su svi novi predmeti automatski bolji
- ne reći da stari smer više nema vrednost

## 5. COURSE_EXPLANATION testovi

### 5.1 Test pitanje

```text
Šta se radi na Mašinskom učenju u PIT 2027?
```

Očekivani intent:

```text
COURSE_EXPLANATION
```

Primarni dokumenti:

```text
01_courses/2027/masinsko_ucenje.md
```

Sekundarni dokumenti:

```text
04_baskets/2027/pit_data_ai_bi_korpa.md
03_course_plans/2025_2026/masinsko_ucenje.md
```

Očekivani elementi odgovora:

- Mašinsko učenje je izborni predmet
- važan je za AI, data science i prediktivnu analitiku
- pokriva Python implementaciju, regresiju, klasifikaciju, klasterizaciju, PCA, faktorsku analizu, stabla odlučivanja, SVM, neuronske mreže, sisteme preporuka
- ne reći da ga svi studenti obavezno slušaju

Policy rizici:

- ne predstaviti izborni predmet kao obavezan
- ne reći da predmet sam po sebi pravi data scientist-a

### 5.2 Test pitanje

```text
Šta je ERP softver?
```

Očekivani intent:

```text
COURSE_EXPLANATION
```

Primarni dokumenti:

```text
01_courses/2027/erp_softver.md
```

Sekundarni dokumenti:

```text
04_baskets/2027/pit_software_erp_digital_korpa.md
04_baskets/2027/pit_finance_analytics_korpa.md
```

Očekivani elementi odgovora:

- ERP softver je centralni predmet za ERP / SAP i poslovne informacione sisteme
- povezuje poslovne procese, integrisane sisteme, SAP module, podatke i izveštavanje
- koristan je za ERP/SAP konsultantsku, BI i business analyst putanju
- ako korisnik pita za trenutno izvođenje, treba preći na aktuelni plan rada

Policy rizici:

- ne reći da predmet daje SAP sertifikat
- ne reći da student postaje SAP konsultant samo zbog jednog predmeta

### 5.3 Test pitanje

```text
Da li je Elektronsko poslovanje i veštačka inteligencija isto što i Mašinsko učenje?
```

Očekivani intent:

```text
COURSE_EXPLANATION
```

Primarni dokumenti:

```text
01_courses/2027/elektronsko_poslovanje_i_vestacka_inteligencija.md
01_courses/2027/masinsko_ucenje.md
04_baskets/2027/pit_data_ai_bi_korpa.md
```

Očekivani elementi odgovora:

- nisu isti predmeti
- Elektronsko poslovanje i veštačka inteligencija je više primena AI u digitalnom poslovanju
- Mašinsko učenje je više modeli, algoritmi, Python i rad sa podacima
- predmeti se dopunjuju

Policy rizici:

- ne pomešati nazive
- ne predstaviti Mašinsko učenje kao obavezno ako je izborno

### 5.4 Test pitanje

```text
Da li je Razvoj softvera isto što i OOP?
```

Očekivani intent:

```text
COURSE_EXPLANATION
```

Primarni dokumenti:

```text
01_courses/2027/razvoj_softvera.md
01_courses/2027/objektno_orijentisano_programiranje.md
```

Sekundarni dokumenti:

```text
04_baskets/2027/pit_software_erp_digital_korpa.md
```

Očekivani elementi odgovora:

- nisu isti predmeti
- OOP daje osnovu programiranja kroz klase, objekte, nasleđivanje, polimorfizam i slične koncepte
- Razvoj softvera je širi predmet o aplikacijama, modeliranju, bazama, web-u, metodologiji i timskom projektu
- OOP je tehnička osnova za Razvoj softvera

Policy rizici:

- ne predstaviti ih kao isti predmet
- ne izmišljati aktuelne alate ako pitanje nije o planu rada

## 6. COURSE_PLAN_CURRENT testovi

### 6.1 Test pitanje

```text
Kako se sada polaže ERP?
```

Očekivani intent:

```text
COURSE_PLAN_CURRENT
```

Primarni dokumenti:

```text
03_course_plans/2025_2026/erp_softver.md
```

Sekundarni dokumenti:

```text
01_courses/2027/erp_softver.md
```

Očekivani elementi odgovora:

- koristiti aktuelni plan rada 2025/26
- pomenuti ocenjivanje, predispitne obaveze i ispit samo ako su u planu
- pomenuti aktuelne alate i teme ako su u planu
- jasno razlikovati aktuelno izvođenje od PIT 2027 formalnog opisa

Policy rizici:

- ne koristiti samo 2027 course dokument za ocenjivanje
- ne izmišljati ocenjivanje

### 6.2 Test pitanje

```text
Da li se na ERP-u radi MongoDB?
```

Očekivani intent:

```text
COURSE_PLAN_CURRENT
```

Primarni dokumenti:

```text
03_course_plans/2025_2026/erp_softver.md
```

Sekundarni dokumenti:

```text
01_courses/2027/erp_softver.md
04_baskets/2027/pit_software_erp_digital_korpa.md
```

Očekivani elementi odgovora:

- ako aktuelni plan potvrđuje, reći da se u aktuelnom izvođenju radi MongoDB
- povezati sa Big Data, Python, PyMongo, Tkinter i mini ERP dashboard ako je to u planu
- jasno reći da je to aktuelno izvođenje

Policy rizici:

- ne tvrditi da je MongoDB formalni obavezni deo svake buduće godine ako je potvrđen samo za aktuelni plan
- ne pomešati course i course_plan

### 6.3 Test pitanje

```text
Da li se na Razvoju softvera sada radi Flask?
```

Očekivani intent:

```text
COURSE_PLAN_CURRENT
```

Primarni dokumenti:

```text
03_course_plans/2025_2026/razvoj_softvera.md
06_policy/pit_navigator_answering_policy.md
```

Sekundarni dokumenti:

```text
01_courses/2027/razvoj_softvera.md
05_retrieval_guides/pit_navigator_retrieval_map.md
```

Očekivani elementi odgovora:

- u aktuelnom planu rada 2025/26 naveden je PHP, ako je to potvrđeno planom
- Flask može biti budući fokus samo ako se potvrdi novim planom rada
- ne predstavljati radni predlog kao zvanični aktuelni plan

Policy rizici:

- ne reći da se trenutno radi Flask
- ne mešati radni predlog i plan rada

### 6.4 Test pitanje

```text
Da li se na Operacionim istraživanjima radi Python?
```

Očekivani intent:

```text
COURSE_PLAN_CURRENT
COURSE_EXPLANATION
```

Primarni dokumenti:

```text
03_course_plans/2025_2026/operaciona_istrazivanja.md
01_courses/2027/operaciona_istrazivanja.md
```

Očekivani elementi odgovora:

- da, Python je važan deo predmeta prema aktuelnom planu
- pomenuti NumPy, Monte Carlo, MIP, Matplotlib, pandas ako su potvrđeni
- predmet je izborni
- koristan je za data, BI, AI, optimizaciju i simulacije

Policy rizici:

- ne reći da ga svi studenti slušaju
- ne preterati da predmet sam pokriva celu AI putanju

## 7. ELECTIVE_RECOMMENDATION testovi

### 7.1 Test pitanje

```text
Da li da uzmem Operaciona istraživanja ili Istraživanje tržišta?
```

Očekivani intent:

```text
ELECTIVE_RECOMMENDATION
```

Primarni dokumenti:

```text
04_baskets/2027/pit_izborne_korpe_overview.md
04_baskets/2027/pit_data_ai_bi_korpa.md
04_baskets/2027/pit_minor_electives_reference.md
01_courses/2027/operaciona_istrazivanja.md
```

Očekivani elementi odgovora:

- za data, BI, AI, Python, optimizaciju i analitiku, Operaciona istraživanja su bolji izbor
- Istraživanje tržišta ima smisla za marketing, potrošače, ankete i customer insight
- preporuka nije zvanično rangiranje
- izbor zavisi od interesovanja i izborne pozicije

Policy rizici:

- ne reći da je Istraživanje tržišta loš predmet
- ne reći da je preporuka formalno pravilo

### 7.2 Test pitanje

```text
Šta da izaberem ako me zanima AI?
```

Očekivani intent:

```text
ELECTIVE_RECOMMENDATION
INTEREST_BASED_RECOMMENDATION
```

Primarni dokumenti:

```text
04_baskets/2027/pit_data_ai_bi_korpa.md
04_baskets/2027/pit_izborne_korpe_overview.md
01_courses/2027/masinsko_ucenje.md
01_courses/2027/operaciona_istrazivanja.md
01_courses/2027/elektronsko_poslovanje_i_vestacka_inteligencija.md
```

Očekivani elementi odgovora:

- obavezna osnova: Baze podataka, Analiza podataka, Poslovna analitika, Elektronsko poslovanje i veštačka inteligencija
- Mašinsko učenje je najdirektniji izborni predmet za AI modele
- Operaciona istraživanja dodaju Python, simulacije, optimizaciju i preskriptivnu analitiku
- Poslovna inteligencija i Poslovna analitika daju poslovni kontekst
- izborni predmeti nisu obavezni za sve

Policy rizici:

- ne reći da Mašinsko učenje slušaju svi
- ne obećati AI karijeru bez dodatnog rada

### 7.3 Test pitanje

```text
Da li da izaberem Mašinsko učenje, Ekonometriju ili Kvantitativne finansije?
```

Očekivani intent:

```text
ELECTIVE_RECOMMENDATION
```

Primarni dokumenti:

```text
04_baskets/2027/pit_data_ai_bi_korpa.md
04_baskets/2027/pit_finance_analytics_korpa.md
04_baskets/2027/pit_minor_electives_reference.md
01_courses/2027/masinsko_ucenje.md
```

Očekivani elementi odgovora:

- Mašinsko učenje za AI, data science, prediktivne modele
- Ekonometrija za ekonomsko-statističko modeliranje i empirijsku analizu
- Kvantitativne finansije za finansijske modele, tržišta i rizik
- izbor zavisi od interesovanja
- ne postoji univerzalno najbolji izbor za sve

Policy rizici:

- ne predstaviti jedan predmet kao objektivno najbolji za sve
- ne izmišljati detalje za Ekonometriju i Kvantitativne finansije ako nema course dokumenta

### 7.4 Test pitanje

```text
Da li da izaberem Elektronsku trgovinu, Elektronske platne sisteme ili Nove informacione tehnologije?
```

Očekivani intent:

```text
ELECTIVE_RECOMMENDATION
```

Primarni dokumenti:

```text
04_baskets/2027/pit_software_erp_digital_korpa.md
04_baskets/2027/pit_minor_electives_reference.md
04_baskets/2027/pit_izborne_korpe_overview.md
```

Očekivani elementi odgovora:

- Elektronska trgovina za e-commerce, digitalne platforme i online prodaju
- Elektronski platni sistemi za fintech, digitalna plaćanja i bankarske digitalne kanale
- Nove informacione tehnologije za širi pregled trendova
- za konkretnu PIT putanju prva dva su često direktnija
- ne reći da su Nove informacione tehnologije loš predmet

Policy rizici:

- ne omalovažavati NIT
- ne tvrditi da postoji zvanično rangiranje

### 7.5 Test pitanje

```text
Da li da izaberem Analizu finansijskih izveštaja, Upravljačko računovodstvo ili Osnove poslovnih finansija?
```

Očekivani intent:

```text
ELECTIVE_RECOMMENDATION
```

Primarni dokumenti:

```text
04_baskets/2027/pit_finance_analytics_korpa.md
04_baskets/2027/pit_minor_electives_reference.md
04_baskets/2027/pit_izborne_korpe_overview.md
```

Očekivani elementi odgovora:

- Analiza finansijskih izveštaja je najprirodniji izbor za većinu PIT studenata koji žele finansije + podatke
- Upravljačko računovodstvo je dobro za ambicioznije studente koji žele internu kontrolu, troškove i menadžersko izveštavanje
- Osnovi poslovnih finansija su opštija finansijska osnova
- izbor zavisi od interesovanja

Policy rizici:

- ne reći da su Osnovi poslovnih finansija loš predmet
- ne predstaviti preporuku kao formalno pravilo

## 8. CAREER_RECOMMENDATION testovi

### 8.1 Test pitanje

```text
Koji predmeti su najbolji za BI analitičara?
```

Očekivani intent:

```text
CAREER_RECOMMENDATION
```

Primarni dokumenti:

```text
04_baskets/2027/pit_data_ai_bi_korpa.md
01_courses/2027/poslovna_inteligencija.md
01_courses/2027/poslovna_analitika.md
01_courses/2027/analiza_podataka.md
01_courses/2027/baze_podataka.md
```

Očekivani elementi odgovora:

- Baze podataka, Analiza podataka, Poslovna analitika, Poslovna inteligencija
- ERP softver kao izvor poslovnih podataka
- Operaciona istraživanja i Mašinsko učenje kao izborna pojačanja
- projekti, alati i portfolio su važni

Policy rizici:

- ne obećati posao
- ne reći da jedan predmet pokriva BI karijeru

### 8.2 Test pitanje

```text
Šta je dobro za ERP/SAP konsultanta?
```

Očekivani intent:

```text
CAREER_RECOMMENDATION
```

Primarni dokumenti:

```text
04_baskets/2027/pit_software_erp_digital_korpa.md
04_baskets/2027/pit_finance_analytics_korpa.md
01_courses/2027/erp_softver.md
03_course_plans/2025_2026/erp_softver.md
```

Očekivani elementi odgovora:

- ERP softver je centralni predmet
- Baze podataka, Razvoj softvera, Poslovna analitika, Poslovna inteligencija su korisni
- Računovodstveni informacioni sistemi, Analiza finansijskih izveštaja i Upravljačko računovodstvo su korisni izborni dodaci
- predmet ne daje automatski SAP sertifikat
- potrebno je dodatno učenje i praksa

Policy rizici:

- ne obećati SAP posao
- ne reći da predmet daje sertifikat ako nije potvrđeno

### 8.3 Test pitanje

```text
Koji predmeti su dobri za developera?
```

Očekivani intent:

```text
CAREER_RECOMMENDATION
```

Primarni dokumenti:

```text
04_baskets/2027/pit_software_erp_digital_korpa.md
01_courses/2027/objektno_orijentisano_programiranje.md
01_courses/2027/razvoj_softvera.md
01_courses/2027/baze_podataka.md
```

Očekivani elementi odgovora:

- OOP, Razvoj softvera, Baze podataka
- Korisničko iskustvo i dizajn kao dopuna za korisnički sloj
- Elektronsko poslovanje i veštačka inteligencija kao poslovni i AI kontekst
- Mašinsko učenje ako želi AI implementaciju
- Operaciona istraživanja ako želi Python i analitiku

Policy rizici:

- ne predstaviti PIT kao čist programerski smer
- ne reći da je dovoljno samo završiti predmete za developer posao

### 8.4 Test pitanje

```text
Koji predmeti su dobri za finansijskog analitičara?
```

Očekivani intent:

```text
CAREER_RECOMMENDATION
```

Primarni dokumenti:

```text
04_baskets/2027/pit_finance_analytics_korpa.md
04_baskets/2027/pit_minor_electives_reference.md
01_courses/2027/analiza_podataka.md
01_courses/2027/poslovna_analitika.md
01_courses/2027/poslovna_inteligencija.md
```

Očekivani elementi odgovora:

- Analiza podataka, Poslovna analitika, Poslovna inteligencija
- Analiza finansijskih izveštaja
- Upravljačko računovodstvo
- Finansijska ekonomija
- Ekonometrija
- Kvantitativne finansije
- ERP softver i Baze podataka kao podrška

Policy rizici:

- ne obećati posao u finansijama
- ne izmišljati detalje za predmete bez course dokumenta

## 9. INTEREST_BASED_RECOMMENDATION testovi

### 9.1 Test pitanje

```text
Volim podatke, ali ne bih bio čist programer. Šta ima smisla?
```

Očekivani intent:

```text
INTEREST_BASED_RECOMMENDATION
```

Primarni dokumenti:

```text
04_baskets/2027/pit_data_ai_bi_korpa.md
04_baskets/2027/pit_finance_analytics_korpa.md
00_overview/pit_2027_overview.md
```

Očekivani elementi odgovora:

- Baze podataka, Analiza podataka, Poslovna analitika, Poslovna inteligencija
- ERP softver kao poslovni izvor podataka
- Operaciona istraživanja ako želi Python, simulacije, optimizaciju
- Mašinsko učenje ako želi AI i prediktivne modele
- ne mora biti čist programer za BI, business analyst i data analyst putanje

Policy rizici:

- ne reći da programiranje nije potrebno uopšte
- ne obećati posao

### 9.2 Test pitanje

```text
Hoću više biznis nego kodiranje, šta da biram?
```

Očekivani intent:

```text
INTEREST_BASED_RECOMMENDATION
ELECTIVE_RECOMMENDATION
```

Primarni dokumenti:

```text
04_baskets/2027/pit_minor_electives_reference.md
04_baskets/2027/pit_finance_analytics_korpa.md
04_baskets/2027/pit_software_erp_digital_korpa.md
```

Očekivani elementi odgovora:

- Poslovna analitika, Poslovna inteligencija, ERP softver, Menadžment projekata
- izborni predmeti: Menadžment odnosa sa kupcima, Računovodstveni informacioni sistemi, Analiza finansijskih izveštaja, Upravljačko računovodstvo, Finansijska ekonomija, Elektronska trgovina, Elektronski platni sistemi
- jasno reći da izbor zavisi od izborne pozicije

Policy rizici:

- ne omalovažiti tehničke predmete
- ne izmišljati detalje za minor electives

### 9.3 Test pitanje

```text
Zanima me AI, ali nisam siguran da volim programiranje.
```

Očekivani intent:

```text
INTEREST_BASED_RECOMMENDATION
ELECTIVE_RECOMMENDATION
```

Primarni dokumenti:

```text
04_baskets/2027/pit_data_ai_bi_korpa.md
01_courses/2027/elektronsko_poslovanje_i_vestacka_inteligencija.md
01_courses/2027/masinsko_ucenje.md
01_courses/2027/poslovna_analitika.md
```

Očekivani elementi odgovora:

- ako želi poslovnu AI stranu: Elektronsko poslovanje i veštačka inteligencija, Poslovna analitika, Poslovna inteligencija
- ako želi ozbiljniji AI/modelarski pravac: Mašinsko učenje i postepeno građenje Python osnove
- Operaciona istraživanja dodaju Python, optimizaciju i simulacije
- realan ton, bez obeshrabrivanja

Policy rizici:

- ne reći da AI može bez ikakve tehničke osnove
- ne obeshrabriti korisnika

## 10. JOB_MARKET testovi

### 10.1 Test pitanje

```text
Da li se sa PIT-om može naći posao?
```

Očekivani intent:

```text
JOB_MARKET
```

Primarni dokumenti:

```text
00_overview/pit_2027_overview.md
04_baskets/2027/pit_data_ai_bi_korpa.md
04_baskets/2027/pit_software_erp_digital_korpa.md
04_baskets/2027/pit_finance_analytics_korpa.md
06_policy/pit_navigator_answering_policy.md
```

Očekivani elementi odgovora:

- PIT daje relevantnu osnovu za BI, business analyst, ERP/SAP, data, digital transformation i neke developer putanje
- posao nije garantovan
- važni su projekti, praksa, alati, portfolio i dodatno učenje
- AI menja rutinske poslove, ali poslovno-tehnički profil ostaje koristan ako se razvija praktično

Policy rizici:

- ne garantovati posao
- ne garantovati platu
- ne dati lažnu sigurnost

### 10.2 Test pitanje

```text
Da li će AI pojesti ovaj smer?
```

Očekivani intent:

```text
JOB_MARKET
```

Primarni dokumenti:

```text
00_overview/pit_2027_overview.md
00_overview/pin_2020_vs_pit_2027.md
04_baskets/2027/pit_data_ai_bi_korpa.md
06_policy/pit_navigator_answering_policy.md
```

Očekivani elementi odgovora:

- AI će promeniti rutinske zadatke
- smer nije automatski ugrožen ako student kombinuje poslovanje, podatke, procese, alate, ERP, BI i AI
- najotpornije putanje su one koje povezuju poslovni problem i tehnologiju
- potreban je praktičan rad i korišćenje AI alata

Policy rizici:

- ne reći da AI neće uticati
- ne reći da će AI sve uništiti
- ne reći da je smer sam po sebi dovoljan

### 10.3 Test pitanje

```text
Da li je PIT dovoljan za data analyst posao?
```

Očekivani intent:

```text
JOB_MARKET
CAREER_RECOMMENDATION
```

Primarni dokumenti:

```text
04_baskets/2027/pit_data_ai_bi_korpa.md
00_overview/pit_2027_overview.md
06_policy/pit_navigator_answering_policy.md
```

Očekivani elementi odgovora:

- PIT daje dobru osnovu kroz Baze podataka, Analizu podataka, Poslovnu analitiku, Poslovnu inteligenciju
- Operaciona istraživanja i Mašinsko učenje su jaka izborna pojačanja
- za posao su potrebni projekti, alati, portfolio i dodatni rad
- ne garantovati zaposlenje

Policy rizici:

- ne reći da je smer sam po sebi dovoljan
- ne obećati posao

## 11. FALLBACK testovi

### 11.1 Test pitanje

```text
Šta se tačno radi na Elektronskoj trgovini i kako se polaže?
```

Očekivani intent:

```text
FALLBACK
COURSE_EXPLANATION
```

Primarni dokumenti:

```text
04_baskets/2027/pit_minor_electives_reference.md
04_baskets/2027/pit_software_erp_digital_korpa.md
06_policy/pit_navigator_answering_policy.md
```

Očekivani elementi odgovora:

- Elektronska trgovina je korisna za e-commerce, online prodaju, digitalne platforme i digitalne poslovne modele
- za detaljan sadržaj i ocenjivanje nema poseban course dokument u bazi
- treba proveriti zvanični silabus ili plan rada
- ne izmišljati ocenjivanje

Policy rizici:

- ne izmišljati nedeljni plan
- ne izmišljati način polaganja

### 11.2 Test pitanje

```text
Ko drži Nove informacione tehnologije i da li je profesor dobar?
```

Očekivani intent:

```text
FALLBACK
```

Primarni dokumenti:

```text
06_policy/pit_navigator_answering_policy.md
04_baskets/2027/pit_minor_electives_reference.md
```

Očekivani elementi odgovora:

- bot ne ocenjuje nastavnike i saradnike
- za aktuelne informacije o nastavnicima treba proveriti zvanični raspored, silabus ili stranicu fakulteta
- može neutralno objasniti gde se predmet uklapa, bez komentarisanja profesora

Policy rizici:

- ne komentarisati profesora
- ne preporučivati predmet zbog nastavnika
- ne odvraćati od predmeta zbog nastavnika

### 11.3 Test pitanje

```text
Kako se prijavljuje praksa i koji su rokovi?
```

Očekivani intent:

```text
FALLBACK
```

Primarni dokumenti:

```text
06_policy/pit_navigator_answering_policy.md
05_retrieval_guides/pit_navigator_retrieval_map.md
```

Očekivani elementi odgovora:

- praksa se ne obrađuje kao poseban knowledge base dokument
- za procedure, rokove i pravila treba proveriti zvanična fakultetska uputstva
- ne izmišljati rokove

Policy rizici:

- ne izmišljati administrativna pravila
- ne izmišljati rokove

### 11.4 Test pitanje

```text
Studiram drugi smer. Da li mogu da koristim ove preporuke?
```

Očekivani intent:

```text
FALLBACK
INTEREST_BASED_RECOMMENDATION
```

Primarni dokumenti:

```text
06_policy/pit_navigator_answering_policy.md
05_retrieval_guides/pit_navigator_retrieval_map.md
04_baskets/2027/
```

Očekivani elementi odgovora:

- preporuke mogu služiti kao orijentir za veštine
- formalna pravila zavise od njegovog programa
- bot ne zna strukturu drugog smera ako nije u bazi
- može navesti korisna znanja: baze, analiza podataka, BI, poslovna analitika, ERP, softver, AI

Policy rizici:

- ne tvrditi da zna drugi smer
- ne davati formalne preporuke za program koji nije u bazi

## 12. Testovi za konflikt izvora

### 12.1 Test pitanje

```text
U PIT 2027 se na Razvoju softvera radi Flask, jel tako?
```

Očekivani intent:

```text
COURSE_PLAN_CURRENT
COURSE_EXPLANATION
```

Primarni dokumenti:

```text
03_course_plans/2025_2026/razvoj_softvera.md
01_courses/2027/razvoj_softvera.md
06_policy/pit_navigator_answering_policy.md
```

Očekivani elementi odgovora:

- razlikovati formalni PIT 2027 opis od aktuelnog plana rada
- reći da se u aktuelnom planu 2025/26 radi PHP ako je to potvrđeno
- Flask može biti radni budući predlog samo ako se potvrdi novim planom
- ne potvrditi pogrešnu pretpostavku korisnika

Policy rizici:

- ne pristati na netačnu premisu
- ne predstaviti radni predlog kao zvanični plan

### 12.2 Test pitanje

```text
Da li se ERP u 2027 radi isto kao trenutno?
```

Očekivani intent:

```text
COURSE_EXPLANATION
COURSE_PLAN_CURRENT
```

Primarni dokumenti:

```text
01_courses/2027/erp_softver.md
03_course_plans/2025_2026/erp_softver.md
05_retrieval_guides/pit_navigator_retrieval_map.md
```

Očekivani elementi odgovora:

- 2027 course dokument daje formalni akreditacioni okvir
- 2025/26 plan rada daje aktuelno izvođenje
- moguće je porediti, ali ne tvrditi da će buduće izvođenje biti identično aktuelnom dok ne postoji plan za tu godinu
- jasno razdvojiti izvore

Policy rizici:

- ne tvrditi da se buduća godina izvodi identično
- ne mešati formalni opis i plan rada

## 13. Testovi za predmete bez posebnog course dokumenta

### 13.1 Test pitanje

```text
Šta se radi na Ekonometriji?
```

Očekivani intent:

```text
COURSE_EXPLANATION
FALLBACK
```

Primarni dokumenti:

```text
04_baskets/2027/pit_minor_electives_reference.md
04_baskets/2027/pit_finance_analytics_korpa.md
```

Očekivani elementi odgovora:

- Ekonometrija je korisna za ekonomske i finansijske podatke, statističko modeliranje, empirijsku analizu
- nema poseban course dokument u bazi
- za detaljan sadržaj, ocenjivanje i plan rada treba proveriti zvanični silabus ili plan rada

Policy rizici:

- ne izmišljati nedeljni plan
- ne izmišljati ocenjivanje
- ne izmišljati softver

### 13.2 Test pitanje

```text
Da li su Kvantitativne finansije korisne za finance analytics?
```

Očekivani intent:

```text
COURSE_EXPLANATION
CAREER_RECOMMENDATION
```

Primarni dokumenti:

```text
04_baskets/2027/pit_minor_electives_reference.md
04_baskets/2027/pit_finance_analytics_korpa.md
```

Očekivani elementi odgovora:

- da, korisne su za finansijske modele, tržišta, rizik i kvantitativnu analizu
- posebno su važne za spoj finansija, modela i podataka
- nema detaljnog course dokumenta, pa ne izmišljati detalje

Policy rizici:

- ne izmišljati sadržaj
- ne garantovati posao

## 14. Testovi za Markdown i format odgovora

### 14.1 Test pitanje

```text
Daj mi kratak odgovor, šta je najbolje za AI?
```

Očekivani intent:

```text
ELECTIVE_RECOMMENDATION
INTEREST_BASED_RECOMMENDATION
```

Primarni dokumenti:

```text
04_baskets/2027/pit_data_ai_bi_korpa.md
```

Očekivani elementi odgovora:

- kratak odgovor
- Mašinsko učenje kao najdirektniji izborni predmet
- Operaciona istraživanja kao jako pojačanje za Python, simulacije i optimizaciju
- obavezna osnova: Baze podataka, Analiza podataka, Poslovna analitika, Elektronsko poslovanje i veštačka inteligencija
- bez predugačke liste

Policy rizici:

- ne dati predugačak odgovor ako korisnik traži kratko
- ne reći da je Mašinsko učenje obavezno

### 14.2 Test pitanje

```text
Objasni kao studentu prve godine šta je BI putanja.
```

Očekivani intent:

```text
CAREER_RECOMMENDATION
PROGRAM_OVERVIEW
```

Primarni dokumenti:

```text
04_baskets/2027/pit_data_ai_bi_korpa.md
01_courses/2027/poslovna_inteligencija.md
00_overview/pit_2027_overview.md
```

Očekivani elementi odgovora:

- jednostavan jezik
- BI znači rad sa podacima, izveštajima, dashboardima i KPI pokazateljima
- važni predmeti: Baze podataka, Analiza podataka, Poslovna analitika, Poslovna inteligencija
- ERP softver kao izvor poslovnih podataka
- Operaciona istraživanja i Mašinsko učenje kao naprednija pojačanja

Policy rizici:

- ne koristiti previše žargona bez objašnjenja
- ne obećati posao

## 15. MBA i značaj predmeta testovi

### 15.1 Test pitanje

```text
Da li je Master in Business Analytics dobar nastavak posle PIT-a?
```

Očekivani intent:

```text
PROGRAM_OVERVIEW
COURSE_EXPLANATION
```

Primarni dokumenti:

```text
00_overview/mba_business_analytics_as_pit_continuation.md
05_retrieval_guides/pit_course_importance_guide.md
```

Očekivani elementi odgovora:

- MBA je prirodan nastavak za PIT/PIN studente koje zanimaju business analytics, data management, BI, Python/R, ML osnove, data storytelling i digital transformation
- nije jedini mogući nastavak
- nije čisti data science ili software engineering master
- ne garantuje posao

### 15.2 Test pitanje

```text
Šta dobijam ako posle PIT-a upišem MBA?
```

Očekivani intent:

```text
PROGRAM_OVERVIEW
COURSE_EXPLANATION
```

Primarni dokumenti:

```text
00_overview/mba_business_analytics_as_pit_continuation.md
05_retrieval_guides/pit_course_importance_guide.md
```

Očekivani elementi odgovora:

- produbljivanje poslovne analitike
- data management, Python/R, ML/statističko modelovanje, BI i data storytelling
- marketing/customer analytics, financial/risk analytics, consulting analytics
- privatnost, bezbednost i etika podataka

### 15.3 Test pitanje

```text
Da li je MBA više za data science ili business analytics?
```

Očekivani intent:

```text
COURSE_EXPLANATION
CAREER_RECOMMENDATION
```

Primarni dokumenti:

```text
00_overview/mba_business_analytics_as_pit_continuation.md
```

Očekivani elementi odgovora:

- MBA treba predstaviti kao business analytics profil
- može uključiti ML i statističko modelovanje, ali nije isto što i čisti data science master
- fokus je na poslovnoj odluci, interpretaciji i primeni podataka

### 15.4 Test pitanje

```text
Koji predmeti na PIT-u su najbolja priprema za MBA?
```

Očekivani intent:

```text
PROGRAM_OVERVIEW
COURSE_EXPLANATION
CAREER_RECOMMENDATION
```

Primarni dokumenti:

```text
00_overview/mba_business_analytics_as_pit_continuation.md
05_retrieval_guides/pit_course_importance_guide.md
```

Očekivani elementi odgovora:

- Baze podataka, Analiza podataka, Poslovna analitika, Poslovna inteligencija, ERP softver
- Operaciona istraživanja i Mašinsko učenje kao jaka analitička pojačanja
- Analiza finansijskih izveštaja, Istraživanje tržišta i Menadžment projekata za domenske putanje

### 15.5 Test pitanje

```text
Koji je značaj Operacionih istraživanja?
```

Očekivani intent:

```text
COURSE_EXPLANATION
```

Primarni dokumenti:

```text
05_retrieval_guides/pit_course_importance_guide.md
01_courses/2027/operaciona_istrazivanja.md
03_course_plans/2025_2026/operaciona_istrazivanja.md
```

Očekivani elementi odgovora:

- most između poslovnog odlučivanja, optimizacije, simulacija i preskriptivne analitike
- dodaje "šta da uradimo" dimenziju
- korisno za business analytics, finance/risk, supply chain, pricing, resource allocation i consulting
- ne predstaviti kao čist programerski predmet

### 15.6 Test pitanje

```text
Koliko je Mašinsko učenje važno za AI putanju?
```

Očekivani intent:

```text
COURSE_EXPLANATION
CAREER_RECOMMENDATION
```

Primarni dokumenti:

```text
05_retrieval_guides/pit_course_importance_guide.md
01_courses/2027/masinsko_ucenje.md
```

Očekivani elementi odgovora:

- najdirektniji predmet za AI/data modeling putanju
- klasifikacija, regresija, klasterovanje, evaluacija i interpretacija modela
- ne pravi automatski ML inženjera
- vredan je kada se model poveže sa poslovnom odlukom

### 15.7 Test pitanje

```text
Zašto je Analiza finansijskih izveštaja korisna za PIT studenta?
```

Očekivani intent:

```text
COURSE_EXPLANATION
CAREER_RECOMMENDATION
```

Primarni dokumenti:

```text
05_retrieval_guides/pit_course_importance_guide.md
04_baskets/2027/pit_finance_analytics_korpa.md
04_baskets/2027/pit_minor_electives_reference.md
```

Očekivani elementi odgovora:

- daje finansijski kontekst za BI, ERP i analitičke modele
- povezuje izveštaje, pokazatelje, profitabilnost, likvidnost, zaduženost, efikasnost i performanse
- korisna je za finance analytics, controlling, consulting, risk/credit analytics i ERP/FI
- nije tehnički data predmet, već domensko znanje za analitiku

### 15.8 Dodatna pitanja za pokrivanje

```text
Koji je značaj Baza podataka?
Koji je značaj ERP softvera?
Koji predmet je najvažniji za business analyst putanju?
Koji predmeti su najkorisniji za finance analytics?
Ako hoću konsultantsku analytics putanju, šta da biram?
```

Primarni dokumenti:

```text
05_retrieval_guides/pit_course_importance_guide.md
00_overview/mba_business_analytics_as_pit_continuation.md
04_baskets/2027/pit_data_ai_bi_korpa.md
04_baskets/2027/pit_finance_analytics_korpa.md
04_baskets/2027/pit_software_erp_digital_korpa.md
```

Policy rizici za celu sekciju:

- ne garantovati posao, praksu, platu ili uspeh
- ne predstaviti PIT kao čisto programerski smer
- ne predstaviti MBA kao čisti data science master
- ne tvrditi da jedan predmet sam pokriva celu karijeru

## 16. Kurikulum PIT 2027 testovi

### 16.1 Test pitanje

```text
Koji su predmeti na PIT smeru?
```

Očekivani intent:

```text
PROGRAM_OVERVIEW
```

Primarni dokumenti:

```text
00_overview/pit_2027_curriculum_structure.md
00_overview/pit_2027_overview.md
```

Očekivani elementi odgovora:

- odgovor po godinama i semestrima
- obavezni predmeti odvojeni od izbornih blokova
- jasno reći da se struktura odnosi na PIT 2027
- ne mešati sa PIN 2020

### 16.2 Dodatna kurikulumska pitanja

```text
Daj mi kurikulum PIT-a.
Šta se sluša u trećoj godini na PIT-u?
Šta se sluša u četvrtoj godini na PIT-u?
Koji su izborni blokovi na PIT-u?
Koji predmeti su obavezni u petom semestru?
Koji predmeti su obavezni u šestom semestru?
Koji predmeti su obavezni u sedmom semestru?
Koji predmeti su obavezni u osmom semestru?
Koje predmete da biram ako ciljam MBA Business Analytics?
Koje predmete da biram ako ciljam finance analytics?
Koje predmete da biram ako ciljam ERP/SAP?
```

Primarni dokumenti:

```text
00_overview/pit_2027_curriculum_structure.md
04_baskets/2027/pit_izborne_korpe_overview.md
04_baskets/2027/pit_data_ai_bi_korpa.md
04_baskets/2027/pit_finance_analytics_korpa.md
04_baskets/2027/pit_software_erp_digital_korpa.md
00_overview/mba_business_analytics_as_pit_continuation.md
```

Očekivani elementi odgovora:

- za treću godinu pomenuti peti i šesti semestar
- za četvrtu godinu pomenuti sedmi i osmi semestar
- za izborne blokove navesti pravila izbora i ne predstavljati ih kao obavezne za sve
- za karijerne putanje povezati predmete sa putanjom, bez garancije posla
- ako korisnik pita za trenutni PIN, napomenuti da se dokument odnosi na PIT 2027

Policy rizici:

- ne izmišljati predmete van spiska
- ne garantovati posao
- ne mešati PIT 2027 sa PIN 2020
- ne zatrpavati korisnika šiframa ako traži kratak odgovor

## 17. Minimalni test set za prvu proveru

Ako se radi brza QA provera, dovoljno je testirati ova pitanja:

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

Očekivanje:

- sva pitanja treba da prođu bez izmišljanja
- course i course_plan pitanja treba da se razlikuju
- izborni predmeti ne smeju biti predstavljeni kao obavezni
- nastavnici se ne komentarišu
- fallback se koristi kada nema detaljnog dokumenta

## 18. Šta znači uspešan test

Test je uspešan ako bot:

- povuče pravi tip dokumenta
- odgovori u skladu sa intent-om
- razlikuje PIT 2027 i PIN 2020
- razlikuje course i course_plan
- ne izmišlja detalje
- ne komentariše nastavnike
- ne obećava posao
- jasno kaže kada je predmet izborni
- koristi fallback kada nema dovoljno informacija
- daje praktičan i razumljiv odgovor

## 19. Šta znači neuspešan test

Test nije uspešan ako bot:

- koristi pogrešan dokument
- izmišlja sadržaj predmeta
- izmišlja ocenjivanje
- meša 2027 akreditaciju i 2025/26 plan rada
- kaže da je izborni predmet obavezan
- kaže da je PIN 2020 zastareo
- komentariše nastavnika ili saradnika
- obećava posao, platu ili sertifikat
- koristi tematsku korpu kao formalno pravilo
- ne koristi fallback kada nema detaljan dokument

## 20. Preporučeni zapis rezultata testiranja

Za svaki test koristiti format:

```text
Test ID:
Question:
Expected intent:
Retrieved documents:
Expected documents:
Result: PASS / NEEDS_REVIEW / FAIL
Notes:
Policy issues:
Action needed:
```

Primer:

```text
Test ID: ELECTIVE_01
Question: Da li da uzmem Operaciona istraživanja ili Istraživanje tržišta?
Expected intent: ELECTIVE_RECOMMENDATION
Retrieved documents:
- 04_baskets/2027/pit_data_ai_bi_korpa.md
- 04_baskets/2027/pit_minor_electives_reference.md
Expected documents:
- 04_baskets/2027/pit_data_ai_bi_korpa.md
- 04_baskets/2027/pit_minor_electives_reference.md
Result: PASS
Notes: odgovor pravilno preporučuje Operaciona istraživanja za data/AI/BI putanju
Policy issues: none
Action needed: none
```

## 21. Povezani dokumenti

Ovaj test set je povezan sa:

```text
00_overview/knowledge_base_index.md
00_overview/knowledge_base_changelog.md
00_overview/pit_2027_curriculum_structure.md

05_retrieval_guides/pit_navigator_retrieval_map.md
05_retrieval_guides/pit_navigator_intent_examples.md
05_retrieval_guides/pit_navigator_test_questions.md

06_policy/pit_navigator_answering_policy.md
06_policy/pit_navigator_qa_checklist.md

04_baskets/2027/pit_izborne_korpe_overview.md
04_baskets/2027/pit_minor_electives_reference.md
```

Napomena: ovaj dokument je namenjen testiranju retrieval-a i kvaliteta odgovora. Ne koristi se kao primarni izvor za sadržaj o predmetima, već kao evaluacioni set za proveru da li PIT Navigator pravilno koristi knowledge base.
