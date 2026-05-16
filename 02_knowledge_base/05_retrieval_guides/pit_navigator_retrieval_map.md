---
id: retrieval_guide_pit_navigator_map
type: retrieval_guide
title: PIT Navigator, retrieval mapa dokumenata
project: PIT Navigator
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
  - retrieval
  - RAG
  - PIT Navigator
  - mapa dokumenata
  - intent
  - overview
  - course
  - course_plan
  - basket
  - akreditacija
  - preporuka
---

# PIT Navigator, retrieval mapa dokumenata

## 1. Svrha dokumenta

Ovaj dokument definiše koji tip knowledge base dokumenta PIT Navigator treba da koristi za različite tipove korisničkih pitanja.

Cilj je da bot ne meša:

- akreditacione dokumente PIT 2027
- aktuelne planove rada 2025/26
- overview dokumente
- poređenje PIN 2020 i PIT 2027
- tematske korpe za preporuke
- pojedinačne course dokumente
- fallback odgovore kada nema dovoljno podataka

## 2. Glavno pravilo retrieval-a

Bot prvo treba da identifikuje šta korisnik zaista pita:

1. pita o smeru / modulu uopšteno
2. pita o konkretnom predmetu
3. pita o aktuelnom izvođenju predmeta
4. pita o razlici PIN 2020 i PIT 2027
5. pita šta da izabere
6. pita za karijeru ili interesovanje
7. pita za predmet koji nije detaljno obrađen
8. pita iz perspektive drugog smera, drugog fakulteta ili opšteg interesovanja

Tek nakon toga bira dokumente.

## 3. Pregled foldera i namene

### 3.1 Overview dokumenti

Folder:

```text
02_knowledge_base/
  00_overview/
```

Dokumenti:

```text
pin_2020_overview.md
pit_2027_overview.md
pin_2020_vs_pit_2027.md
```

Koriste se za:

- opšti opis PIN 2020
- opšti opis PIT 2027
- poređenje stare i nove akreditacije
- objašnjenje modernizacije
- opštu logiku smera
- razliku između obaveznih i izbornih predmeta
- zaštitne formulacije o tome da PIN 2020 nije zastareo

### 3.2 Course dokumenti za PIT 2027

Folder:

```text
02_knowledge_base/
  01_courses/
    2027/
```

Koriste se kada korisnik pita o predmetu prema akreditaciji PIT 2027.

Ovi dokumenti opisuju:

- formalni status predmeta u PIT 2027
- ESPB
- semestar
- obavezni ili izborni status
- cilj predmeta
- ishode
- ključne teme
- vezu sa karijerama
- šta bot sme i ne sme da tvrdi

Primeri:

```text
baze_podataka.md
poslovna_analitika.md
poslovna_inteligencija.md
korisnicko_iskustvo_i_dizajn.md
elektronsko_poslovanje_i_vestacka_inteligencija.md
analiza_podataka.md
objektno_orijentisano_programiranje.md
razvoj_softvera.md
erp_softver.md
operaciona_istrazivanja.md
masinsko_ucenje.md
```

### 3.3 Aktuelni planovi rada 2025/26

Folder:

```text
02_knowledge_base/
  03_course_plans/
    2025_2026/
```

Koriste se kada korisnik pita:

- šta se trenutno radi na predmetu
- kako se predmet polaže
- koji alati se koriste u aktuelnoj nastavi
- kakav je nedeljni plan
- koje su predispitne obaveze
- kako izgleda kolokvijum ili završni ispit
- kako se predmet izvodi u praksi u školskoj godini 2025/26

Primeri:

```text
baze_podataka.md
veb_dizajn.md
elektronsko_poslovanje.md
analiza_podataka.md
objektno_orijentisano_programiranje.md
razvoj_softvera.md
erp_softver.md
operaciona_istrazivanja.md
masinsko_ucenje.md
```

Važno pravilo:

Ako korisnik pita za “trenutno”, “ove godine”, “kako se sada radi”, “kako se polaže”, “plan rada”, “kolokvijum”, “ispit”, prednost imaju `03_course_plans/2025_2026/`.

Ako korisnik pita za “PIT 2027”, “nova akreditacija”, “novi smer”, prednost imaju `01_courses/2027/`.

### 3.4 Izborne korpe i preporuke

Folder:

```text
02_knowledge_base/
  04_baskets/
    2027/
```

Dokumenti:

```text
pit_izborne_korpe_overview.md
pit_data_ai_bi_korpa.md
pit_software_erp_digital_korpa.md
pit_finance_analytics_korpa.md
```

Koriste se kada korisnik pita:

- šta da izaberem
- koji izborni predmet je bolji za mene
- šta ako me zanima AI
- šta ako me zanima BI
- šta ako me zanima ERP
- šta ako me zanimaju finansije i podaci
- da li da izaberem predmet X ili Y
- koji izborni predmeti su korisni za određenu karijeru

Važno pravilo:

Ovi dokumenti nisu formalni kurikulum. Oni su tematske korpe za preporuke. Formalna pravila izbornih pozicija i dalje se proveravaju kroz `pit_izborne_korpe_overview.md` i izvorni kurikulum.

## 4. Intent mapa

### 4.1 PROGRAM_OVERVIEW

Korisnik pita:

- Šta je PIT?
- Šta je PIN?
- Šta se uči na ovom smeru?
- Kakav je smer?
- Koje oblasti pokriva?
- Da li je smer više poslovni ili IT?
- Zašto da upišem ovaj smer?
- Šta dobijam upisivanjem ovog smera?
- Šta ja konkretno dobijam ako izaberem PIT?
- Da li ovaj smer ima smisla za mene?
- Gde mogu da pročitam više o smeru?
- Gde je karijerni vodič za PIT/PIN?
- Gde se objavljuju kvartalni izveštaji?

Primarni dokumenti:

```text
00_overview/pit_2027_overview.md
00_overview/pin_2020_overview.md
```

Sekundarni dokumenti:

```text
00_overview/pin_2020_vs_pit_2027.md
04_baskets/2027/pit_izborne_korpe_overview.md
```

Pravilo odgovora:

- Ako korisnik pita za novi smer, koristi PIT 2027 overview.
- Ako pita za stari smer, koristi PIN 2020 overview.
- Ako nije jasno, objasni oba kratko i pitaj da li ga zanima nova ili stara akreditacija.
- Ako korisnik pita "zašto da upišem", "šta dobijam" ili govori iz lične perspektive, odgovori kao PROGRAM_OVERVIEW uz kratko povezivanje sa interesovanjima, izbornim usmerenjima i realnom napomenom da smer ne garantuje posao bez dodatnog rada, projekata i prakse.
- Ako korisnik pita gde može da pročita više ili traži dodatne informacije, uputi ga na `https://pin.ekof.bg.ac.rs/pit-navigator/zasto-pin.html`; napomeni da se na toj stranici nalazi i karijerni vodič sa pregledom mogućih pravaca.
- Ako korisnik pita za kvartalne izveštaje, reci da se objavljuju na početnoj stranici sajta i da izlaze kvartalno. Ne koristi sadržaj izveštaja za dopunjavanje baze znanja; izveštaje samo konstatuj kao dodatne javne materijale.

### 4.2 ACCREDITATION_COMPARISON

Korisnik pita:

- Koja je razlika između PIN 2020 i PIT 2027?
- Šta se promenilo?
- Da li je PIT bolji?
- Da li je PIN zastareo?
- Šta je novo u novoj akreditaciji?

Primarni dokument:

```text
00_overview/pin_2020_vs_pit_2027.md
```

Sekundarni dokumenti:

```text
00_overview/pin_2020_overview.md
00_overview/pit_2027_overview.md
03_course_plans/2025_2026/
01_courses/2027/
```

Pravilo odgovora:

Bot treba da kaže da PIT 2027 formalno modernizuje strukturu kroz nove obavezne predmete i jasnije izborne pozicije, ali ne sme da kaže da je PIN 2020 zastareo, loš ili manje vredan.

Ispravna formulacija:

> PIT 2027 formalno jasnije strukturira oblasti kao što su poslovna analitika, poslovna inteligencija, UX, AI i digitalno poslovanje. To ne znači da je PIN 2020 zastareo, jer se PIN 2020 u aktuelnom izvođenju osavremenjuje kroz planove rada, alate, primere i praktičnu nastavu.

### 4.3 COURSE_EXPLANATION

Korisnik pita:

- Šta se radi na predmetu?
- Čemu služi predmet?
- Da li je predmet važan?
- Koje teme pokriva?
- Za koju karijeru je koristan?

Ako pita za PIT 2027:

Primarni folder:

```text
01_courses/2027/
```

Ako pita za trenutno izvođenje:

Primarni folder:

```text
03_course_plans/2025_2026/
```

Ako pitanje nije jasno:

Bot treba da kaže:

> Ako pitaš za formalni opis u PIT 2027, koristi se akreditacioni course dokument. Ako pitaš kako se predmet trenutno izvodi, relevantniji je aktuelni plan rada 2025/26.

### 4.4 COURSE_PLAN_CURRENT

Korisnik pita:

- Kako se polaže?
- Koliko ima kolokvijuma?
- Koji softver se koristi?
- Kakav je nedeljni plan?
- Šta se radi na vežbama?
- Koji su alati ove godine?
- Kako izgleda završni ispit?

Primarni folder:

```text
03_course_plans/2025_2026/
```

Ne koristiti primarno:

```text
01_courses/2027/
```

osim za poređenje ili akreditacioni kontekst.

Pravilo odgovora:

Ako postoji aktuelni plan rada, on ima prednost za operativne detalje.

Primer:

> Za aktuelno izvođenje 2025/26, relevantan je plan rada. Akreditacioni opis PIT 2027 daje formalni okvir, ali plan rada pokazuje kako se predmet zaista izvodi te školske godine.

### 4.5 ELECTIVE_RECOMMENDATION

Korisnik pita:

- Šta da izaberem?
- Koji izborni predmet je bolji?
- Da li da uzmem X ili Y?
- Šta je korisnije za AI?
- Šta je korisnije za ERP?
- Šta je korisnije za finansije i podatke?

Primarni dokumenti:

```text
04_baskets/2027/pit_izborne_korpe_overview.md
04_baskets/2027/pit_data_ai_bi_korpa.md
04_baskets/2027/pit_software_erp_digital_korpa.md
04_baskets/2027/pit_finance_analytics_korpa.md
```

Sekundarni dokumenti:

```text
01_courses/2027/
03_course_plans/2025_2026/
```

Pravilo odgovora:

Bot treba prvo da identifikuje interesovanje korisnika:

- AI / data / BI
- software / ERP / digital
- finance analytics
- e-commerce / fintech
- business analyst / consulting

Zatim treba da kaže:

- koji obavezni predmeti već daju osnovu
- koji izborni predmeti pojačavaju pravac
- da izbor zavisi od izborne pozicije
- da preporuka nije formalno rangiranje predmeta

Bot ne sme da kaže da je izborni predmet obavezan ako nije obavezan.

### 4.6 CAREER_RECOMMENDATION

Korisnik pita:

- Šta je dobro za data analyst?
- Šta je dobro za BI?
- Šta je dobro za AI konsultanta?
- Šta je dobro za ERP/SAP?
- Šta je dobro za developera?
- Koji predmeti vode ka nekoj karijeri?

Primarni dokumenti:

```text
04_baskets/2027/pit_data_ai_bi_korpa.md
04_baskets/2027/pit_software_erp_digital_korpa.md
04_baskets/2027/pit_finance_analytics_korpa.md
```

Sekundarni dokumenti:

```text
01_courses/2027/
03_course_plans/2025_2026/
00_overview/pit_2027_overview.md
```

Pravilo odgovora:

Bot ne sme da obećava zaposlenje.

Ispravna formulacija:

> Ovi predmeti ne garantuju posao, ali razvijaju korisnu osnovu za tu putanju.

### 4.7 INTEREST_BASED_RECOMMENDATION

Korisnik ne pita za karijeru, već za interesovanje:

- Volim podatke
- Zanima me AI
- Volim finansije
- Hoću nešto praktično
- Ne volim previše programiranje
- Hoću više biznis nego kodiranje
- Hoću tehničkiji pravac

Primarni dokumenti:

```text
04_baskets/2027/
```

Sekundarni dokumenti:

```text
01_courses/2027/
03_course_plans/2025_2026/
```

Pravilo odgovora:

Bot treba da odgovori kroz interesovanje, ne kroz rigidnu karijeru.

Primer:

> Ako te zanimaju podaci, a ne želiš nužno programersku karijeru, smisleni su Analiza podataka, Poslovna analitika, Poslovna inteligencija, ERP softver i izborni predmeti kao što su Operaciona istraživanja ili Mašinsko učenje, zavisno od toga koliko želiš modelarski i AI pravac.

### 4.8 JOB_MARKET

Korisnik pita:

- Da li se sa ovim smerom može naći posao?
- Koje poslove mogu da radim?
- Da li će AI pojesti ovaj smer?
- Da li je smer relevantan za tržište?
- Koje karijere imaju smisla?

Primarni dokumenti:

```text
00_overview/pit_2027_overview.md
00_overview/pin_2020_overview.md
00_overview/pin_2020_vs_pit_2027.md
04_baskets/2027/
```

Sekundarni dokumenti:

```text
01_courses/2027/
03_course_plans/2025_2026/
```

Pravilo odgovora:

Bot treba da bude realističan, ne marketinški prazan.

Ne sme da kaže:

- posao je zagarantovan
- smer sigurno vodi do određene plate
- AI neće uticati na profesije
- jedan predmet je dovoljan za karijeru

Može da kaže:

> PIT daje relevantnu kombinaciju poslovnih, analitičkih i informacionih znanja. Najotpornije putanje su one gde student kombinuje poslovno razumevanje, podatke, alate, procese i sposobnost da koristi AI kao pomoć u radu.

## 5. Pravila za konkretne tipove pitanja

### 5.1 Ako korisnik pita za predmet iz 2027

Primeri:

- Šta se radi na Poslovnoj analitici?
- Šta je ERP softver u PIT 2027?
- Da li je Mašinsko učenje obavezno?
- Šta se radi na Razvoju softvera u novoj akreditaciji?

Koristi:

```text
01_courses/2027/[predmet].md
```

Ako postoji i aktuelni plan rada, može se dodati:

> Za operativne detalje izvođenja nastave, koristi se aktuelni plan rada ako je dostupan.

### 5.2 Ako korisnik pita za trenutno izvođenje

Primeri:

- Kako se sada polaže ERP?
- Da li se sada radi MongoDB?
- Da li se na Razvoju softvera sada radi PHP ili Flask?
- Kako izgleda OOP ove godine?

Koristi:

```text
03_course_plans/2025_2026/[predmet].md
```

Ako postoji razlika između aktuelnog plana i buduće ideje, bot treba da kaže:

> U aktuelnom planu rada 2025/26 stoji X. Ako postoji ideja da se predmet ubuduće osavremeni ka Y, to ne treba predstavljati kao deo trenutnog plana dok nije potvrđeno novim planom rada.

### 5.3 Ako korisnik pita za Python

Relevantni dokumenti:

```text
03_course_plans/2025_2026/operaciona_istrazivanja.md
03_course_plans/2025_2026/erp_softver.md
03_course_plans/2025_2026/masinsko_ucenje.md
01_courses/2027/operaciona_istrazivanja.md
01_courses/2027/erp_softver.md
01_courses/2027/masinsko_ucenje.md
```

Moguće objašnjenje:

> Python se posebno javlja u Operacionim istraživanjima, Mašinskom učenju i ERP softveru. Operaciona istraživanja ga koriste za simulacije, optimizaciju i analizu podataka, Mašinsko učenje za ML metode i realne skupove podataka, a ERP softver za tehničko-analitički sloj kroz Python, Tkinter, MongoDB i dashboard.

### 5.4 Ako korisnik pita za AI

Relevantni dokumenti:

```text
04_baskets/2027/pit_data_ai_bi_korpa.md
01_courses/2027/elektronsko_poslovanje_i_vestacka_inteligencija.md
01_courses/2027/masinsko_ucenje.md
01_courses/2027/operaciona_istrazivanja.md
03_course_plans/2025_2026/masinsko_ucenje.md
```

Pravilo:

- Elektronsko poslovanje i veštačka inteligencija = AI u digitalnom poslovanju
- Mašinsko učenje = modeli i algoritmi
- Operaciona istraživanja = Python, simulacije, optimizacija, preskriptivna analitika
- Poslovna analitika i Poslovna inteligencija = poslovna primena podataka i uvida

### 5.5 Ako korisnik pita za ERP / SAP

Relevantni dokumenti:

```text
01_courses/2027/erp_softver.md
03_course_plans/2025_2026/erp_softver.md
04_baskets/2027/pit_software_erp_digital_korpa.md
04_baskets/2027/pit_finance_analytics_korpa.md
```

Pravilo:

Bot treba da kaže da je ERP softver centralni predmet za ERP / SAP putanju, ali ne sme da kaže da predmet obezbeđuje SAP sertifikat ili da student postaje SAP konsultant samo zbog jednog predmeta.

### 5.6 Ako korisnik pita za finansije + podaci

Relevantni dokumenti:

```text
04_baskets/2027/pit_finance_analytics_korpa.md
04_baskets/2027/pit_data_ai_bi_korpa.md
01_courses/2027/operaciona_istrazivanja.md
01_courses/2027/masinsko_ucenje.md
01_courses/2027/erp_softver.md
```

Pravilo:

Preporučena logika:

- Analiza finansijskih izveštaja za većinu PIT studenata
- Upravljačko računovodstvo za ambicioznije studente koji žele internu kontrolu, troškove i menadžersko izveštavanje
- Finansijska ekonomija za dublje finansijsko razumevanje
- Računovodstveni informacioni sistemi za ERP, BI i računovodstvene podatke
- Kvantitativne finansije, Ekonometrija i Mašinsko učenje za modele, podatke i finansijsku analitiku

### 5.7 Ako korisnik pita za e-commerce / fintech

Relevantni dokumenti:

```text
04_baskets/2027/pit_software_erp_digital_korpa.md
01_courses/2027/elektronsko_poslovanje_i_vestacka_inteligencija.md
```

Ako pita za izborne predmete:

- Elektronska trgovina = e-commerce, online prodaja, digitalne platforme
- Elektronski platni sistemi = fintech, digitalna plaćanja, bankarski digitalni kanali
- Nove informacione tehnologije = širi pregled trendova, ali nije prvi prioritet ako student želi konkretnu PIT putanju

## 6. Pravila za korisnike sa drugih smerova ili fakulteta

Ako korisnik nije sa PIT-a ili PIN-a, bot ne treba da tvrdi da zna strukturu njegovog smera.

Ispravna formulacija:

> Ne znam tačno strukturu tvog smera ako nije deo ove baze znanja, ali za ovu oblast korisna znanja su: baze podataka, analiza podataka, poslovna analitika, poslovna inteligencija, osnove programiranja, ERP sistemi, digitalno poslovanje i, ako te zanima AI, mašinsko učenje i operaciona istraživanja.

Ako korisnik pita da li može da koristi preporuke iako nije na PIT-u:

> Možeš ih koristiti kao orijentir za veštine, ali formalna pravila izbora predmeta zavise od tvog studijskog programa i zvaničnog kurikuluma.

## 7. Fallback pravila

Ako ne postoji detaljan dokument za predmet, bot treba da koristi:

1. `pit_izborne_korpe_overview.md`
2. relevantnu tematsku korpu
3. `pit_2027_overview.md`
4. `pin_2020_vs_pit_2027.md`

Bot ne sme da izmišlja detalje o predmetu koji nije obrađen.

Ispravna formulacija:

> Za taj predmet nemam detaljan pojedinačni dokument u bazi znanja. Mogu da ga smestim u širi kontekst PIT 2027 na osnovu kurikuluma i tematskih korpi, ali za detalje o sadržaju, ocenjivanju i planu rada treba proveriti zvanični silabus ili plan rada.

## 8. Pravila za konflikt izvora

Ako se razlikuju:

- akreditaciona knjiga predmeta
- aktuelni plan rada
- radni predlog budućeg izvođenja

redosled poverenja je:

1. aktuelni plan rada za operativna pitanja
2. akreditacioni dokument za formalni status predmeta
3. overview i comparison dokumenti za interpretaciju
4. radni predlog samo kao napomena, ne kao zvanična tvrdnja

Primer:

Razvoj softvera:

- aktuelni plan 2025/26 = PHP, baze, frontend, Scrum, projekat
- radni predlog = Python/Flask i AI-assisted development
- bot ne sme da kaže da se trenutno radi Flask ako to nije potvrđeno planom rada

Ispravna formulacija:

> U aktuelnom planu rada 2025/26 naveden je PHP. Python/Flask i AI-assisted development mogu biti budući fokus samo ako budu potvrđeni novim planom rada.

## 9. Pravila za modernizaciju PIN 2020

Bot ne sme da predstavi PIN 2020 kao zastareo.

Kada se poredi sa PIT 2027, bot treba da koristi formulacije:

- PIT 2027 formalno modernizuje strukturu
- PIN 2020 se u aktuelnom izvođenju osavremenjuje kroz planove rada
- razlika je u formalnoj strukturi i akreditacionom okviru, ne u tome da je staro automatski loše

Primer:

> PIT 2027 uvodi jasnije strukturisanu modernizaciju kroz nove obavezne predmete i izborne pozicije. Međutim, PIN 2020 ne treba predstavljati kao zastareo, jer aktuelni planovi rada pokazuju da se predmeti osavremenjuju kroz alate, primere i praktičnu nastavu.

## 10. Šta bot ne sme da radi

Bot ne sme da:

- izmišlja sadržaj predmeta koji nije u dokumentima
- tvrdi da svi studenti slušaju izborni predmet
- tvrdi da izborni predmet garantuje posao
- tvrdi da jedan predmet pokriva celu karijeru
- tvrdi da je PIT 2027 automatski bolji za svakog studenta
- tvrdi da je PIN 2020 zastareo
- komentariše nastavnike i saradnike
- preporučuje ili ne preporučuje predmet zbog nastavnika
- tvrdi da postoji zvanično rangiranje izbornih predmeta ako ono nije navedeno
- meša aktuelni plan rada sa akreditacionim opisom
- predstavlja radne predloge kao zvaničan plan rada

## 11. Minimalni odgovor kada nema dovoljno informacija

Ako nema dovoljno informacija, bot treba da kaže:

> Za ovo nemam dovoljno precizan dokument u bazi znanja. Mogu da odgovorim na osnovu dostupnog kurikuluma i srodnih dokumenata, ali za tačan sadržaj, ocenjivanje ili aktuelno izvođenje treba proveriti zvanični plan rada ili silabus.

## 12. Izvori i povezani dokumenti

Ovaj retrieval guide oslanja se na sledeću strukturu:

```text
00_overview/
01_courses/2027/
03_course_plans/2025_2026/
04_baskets/2027/
```

Posebno važni dokumenti:

```text
00_overview/pin_2020_overview.md
00_overview/pit_2027_overview.md
00_overview/pin_2020_vs_pit_2027.md

04_baskets/2027/pit_izborne_korpe_overview.md
04_baskets/2027/pit_data_ai_bi_korpa.md
04_baskets/2027/pit_software_erp_digital_korpa.md
04_baskets/2027/pit_finance_analytics_korpa.md
```

Napomena: ovaj dokument ne sadrži detalje svih predmeta, već pravila koji dokumenti imaju prioritet u retrieval-u za različite tipove pitanja.
