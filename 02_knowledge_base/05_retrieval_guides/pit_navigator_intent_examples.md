---
id: retrieval_guide_pit_navigator_intent_examples
type: retrieval_guide
title: PIT Navigator, primeri intent-a i očekivanog retrieval-a
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
  - intent examples
  - retrieval examples
  - PIT Navigator
  - pitanja korisnika
  - primeri pitanja
  - RAG
  - intent
  - course
  - course_plan
  - elective recommendation
  - fallback
---

# PIT Navigator, primeri intent-a i očekivanog retrieval-a

## 1. Svrha dokumenta

Ovaj dokument daje primere korisničkih pitanja i mapira ih na odgovarajući intent, primarne dokumente i očekivanu logiku odgovora.

Cilj dokumenta je da PIT Navigator lakše prepozna šta korisnik zaista pita i da izvuče pravi deo baze znanja.

Ovaj dokument ne sadrži detalje predmeta. On služi kao mapa primera za retrieval i klasifikaciju pitanja.

## 2. Osnovno pravilo

Bot ne treba da se oslanja samo na ključne reči.

Isto ime predmeta može da znači različit intent u zavisnosti od pitanja.

Primer:

- “Šta je ERP softver?” znači COURSE_EXPLANATION.
- “Kako se sada polaže ERP?” znači COURSE_PLAN_CURRENT.
- “Da li je ERP važan za SAP konsultanta?” znači CAREER_RECOMMENDATION.
- “Da li je ERP isti u 2020 i 2027?” znači ACCREDITATION_COMPARISON.
- “Da li da biram ERP ili nešto drugo?” može značiti ELECTIVE_RECOMMENDATION ili INTEREST_BASED_RECOMMENDATION, zavisno od konteksta.

Bot prvo treba da razume nameru, pa tek onda da bira dokumente.

## 3. PROGRAM_OVERVIEW

### 3.1 Primeri pitanja

Korisnik može pitati:

- Šta je PIT?
- Šta je PIN?
- Šta se uči na PIT-u?
- Kakav je smer Poslovne informacione tehnologije?
- Da li je PIT više poslovni ili IT smer?
- Koje oblasti pokriva PIT?
- Da li je ovo više za programere ili za analitičare?
- Šta je poenta ovog modula?
- Kako bih ukratko objasnio PIT studentima?

### 3.2 Primarni dokumenti

Koristi:

```text
00_overview/pit_2027_overview.md
00_overview/pin_2020_overview.md
```

Ako korisnik pita za poređenje ili staro/novo:

```text
00_overview/pin_2020_vs_pit_2027.md
```

### 3.3 Logika odgovora

Ako korisnik pita za PIT 2027, bot treba da predstavi PIT kao poslovno-informatički profil koji povezuje:

- poslovanje
- podatke
- softver
- poslovnu analitiku
- poslovnu inteligenciju
- ERP
- digitalno poslovanje
- AI
- korisničko iskustvo

Ako korisnik pita za PIN 2020, bot treba da predstavi PIN kao prethodni poslovno-informatički profil koji se kroz aktuelnu nastavu osavremenjuje.

### 3.4 Primer odgovora

> PIT 2027 je poslovno-informatički profil koji povezuje poslovanje, podatke, softver, ERP, BI, analitiku, digitalno poslovanje i AI. Nije čist programerski smer, ali ima važne tehničke predmete. Nije ni čist menadžerski smer, jer student uči i baze, analitiku, softver i poslovne informacione sisteme.

## 4. ACCREDITATION_COMPARISON

### 4.1 Primeri pitanja

Korisnik može pitati:

- Koja je razlika između PIN 2020 i PIT 2027?
- Šta se promenilo u novoj akreditaciji?
- Da li je PIT bolji od PIN-a?
- Da li je PIN zastareo?
- Šta je novo u PIT 2027?
- Da li PIT 2027 zamenjuje PIN 2020?
- Šta je ostalo isto, a šta je novo?
- Da li su predmeti moderniji u 2027?
- Kako da objasnim modernizaciju smera?

### 4.2 Primarni dokumenti

Koristi:

```text
00_overview/pin_2020_vs_pit_2027.md
```

Sekundarno:

```text
00_overview/pin_2020_overview.md
00_overview/pit_2027_overview.md
03_course_plans/2025_2026/
01_courses/2027/
```

### 4.3 Logika odgovora

Bot treba da kaže:

- PIT 2027 formalno modernizuje i jasnije strukturira profil.
- PIN 2020 ne treba predstavljati kao zastareo.
- Razlika je u formalnoj strukturi, novim obaveznim predmetima i jasnijoj integraciji oblasti kao što su AI, BI, UX, poslovna analitika i digitalno poslovanje.
- PIN 2020 se u aktuelnom izvođenju osavremenjuje kroz planove rada, alate, primere i praksu.

### 4.4 Primer odgovora

> PIT 2027 jasnije formalizuje modernizaciju poslovno-informatičkog profila, posebno kroz predmete kao što su Poslovna analitika, Poslovna inteligencija, Korisničko iskustvo i dizajn, Elektronsko poslovanje i veštačka inteligencija i ERP softver. To ne znači da je PIN 2020 zastareo. PIN 2020 se u aktuelnom izvođenju osavremenjuje kroz planove rada, alate i praktične primere.

## 5. COURSE_EXPLANATION

### 5.1 Primeri pitanja

Korisnik može pitati:

- Šta se radi na Poslovnoj analitici?
- Šta je Poslovna inteligencija?
- Čemu služi ERP softver?
- Šta se uči na Bazama podataka?
- Da li je Mašinsko učenje obavezno?
- Šta su Operaciona istraživanja?
- Da li je Razvoj softvera programerski predmet?
- Za šta je koristan OOP?
- Šta je Korisničko iskustvo i dizajn?
- Da li je Elektronsko poslovanje i veštačka inteligencija isto što i Mašinsko učenje?

### 5.2 Primarni dokumenti

Ako korisnik pita za PIT 2027:

```text
01_courses/2027/[predmet].md
```

Ako korisnik pita za aktuelno izvođenje:

```text
03_course_plans/2025_2026/[predmet].md
```

### 5.3 Logika odgovora

Bot treba da odgovori kroz:

- status predmeta, obavezan ili izborni
- kratak opis
- ključne teme
- praktične veštine
- vezu sa karijernim putanjama
- napomenu ako postoji razlika između akreditacionog opisa i aktuelnog plana rada

### 5.4 Primer odgovora

> Mašinsko učenje je izborni predmet u PIT 2027 i posebno je važan za AI, data science i naprednu poslovnu analitiku. Fokus je na Python implementaciji metoda kao što su regresija, klasifikacija, klaster analiza, PCA, faktorska analiza, stabla odlučivanja, Naivni Bejs, SVM, neuronske mreže i sistemi preporuka. Ne treba ga predstavljati kao predmet koji svi studenti obavezno slušaju.

## 6. COURSE_PLAN_CURRENT

### 6.1 Primeri pitanja

Korisnik može pitati:

- Kako se sada polaže ERP?
- Da li se na ERP-u radi MongoDB?
- Da li se na Razvoju softvera sada radi PHP ili Flask?
- Kako se polaže OOP?
- Koji su alati na Bazama podataka ove godine?
- Kakav je nedeljni plan iz Mašinskog učenja?
- Da li se na Operacionim istraživanjima radi Python?
- Koliko poena nosi projekat?
- Šta je na završnom ispitu?
- Koje su predispitne obaveze?

### 6.2 Primarni dokumenti

Koristi:

```text
03_course_plans/2025_2026/[predmet].md
```

### 6.3 Logika odgovora

Ako postoji aktuelni plan rada, on ima prednost za:

- ocenjivanje
- alate
- nedeljni plan
- vežbe
- kolokvijum
- praktični deo ispita
- projekat
- aktuelne tehnologije

### 6.4 Primer odgovora

> Prema aktuelnom planu rada 2025/26, Razvoj softvera koristi PHP, baze podataka, frontend, Scrum i timski projekat. Python/Flask može biti budući fokus samo ako bude potvrđen novim planom rada, ali ga ne treba predstavljati kao deo aktuelnog plana.

## 7. ELECTIVE_RECOMMENDATION

### 7.1 Primeri pitanja

Korisnik može pitati:

- Šta da izaberem ako me zanima AI?
- Koji izborni predmet je najbolji za BI?
- Da li da uzmem Operaciona istraživanja ili Istraživanje tržišta?
- Da li da izaberem Mašinsko učenje ili Ekonometriju?
- Šta da uzmem ako me zanimaju finansije i podaci?
- Da li su bolje Elektronska trgovina ili Elektronski platni sistemi?
- Koji izborni predmeti su korisni za ERP?
- Šta da izaberem ako hoću više praktično?
- Koji izborni predmet ima najviše veze sa Python-om?
- Šta ako ne volim previše programiranje?

### 7.2 Primarni dokumenti

Koristi:

```text
04_baskets/2027/pit_izborne_korpe_overview.md
04_baskets/2027/pit_data_ai_bi_korpa.md
04_baskets/2027/pit_software_erp_digital_korpa.md
04_baskets/2027/pit_finance_analytics_korpa.md
```

Sekundarno:

```text
01_courses/2027/
03_course_plans/2025_2026/
```

### 7.3 Logika odgovora

Bot treba da:

1. prepozna interesovanje korisnika
2. navede obavezne predmete koji već daju osnovu
3. navede izborne predmete koji pojačavaju pravac
4. kaže da izbor zavisi od izborne pozicije
5. izbegne tvrdnju da postoji zvanično rangiranje
6. ne omalovaži predmete koji nisu prvi prioritet

### 7.4 Primeri prioriteta

Ako korisnik pita za AI / data / BI:

- Operaciona istraživanja su bolji izbor od Istraživanja tržišta ako korisnik nema jasno marketing interesovanje.
- Mašinsko učenje je najdirektnije za AI.
- Ekonometrija je dobra za ekonomsko-statističko modeliranje.
- Kvantitativne finansije su dobre za finansije, modele i rizik.

Ako korisnik pita za e-commerce / fintech:

- Elektronska trgovina je prirodna za e-commerce.
- Elektronski platni sistemi su prirodni za fintech i digitalna plaćanja.
- Nove informacione tehnologije su širi pregled trendova, ali obično nisu prvi prioritet za konkretnu PIT putanju.

Ako korisnik pita za finansije + podaci:

- Analiza finansijskih izveštaja je najprirodniji izbor za većinu PIT studenata.
- Upravljačko računovodstvo je dobro za ambicioznije studente koji žele internu kontrolu, troškove i menadžersko izveštavanje.
- Finansijska ekonomija je dobra za dublje finansijsko razumevanje.
- Računovodstveni informacioni sistemi su dobri za ERP, BI i računovodstvene podatke.

### 7.5 Primer odgovora

> Ako te zanimaju podaci, Python, optimizacija, BI ili AI, Operaciona istraživanja su bolji izbor za PIT putanju od Istraživanja tržišta. Istraživanje tržišta ima smisla ako te posebno zanimaju marketing, potrošači, ankete i customer insight. Ovo nije zvanično rangiranje predmeta, nego preporuka po interesovanju.

## 8. CAREER_RECOMMENDATION

### 8.1 Primeri pitanja

Korisnik može pitati:

- Koji predmeti su dobri za data analyst?
- Šta je dobro za BI analitičara?
- Šta je dobro za ERP/SAP konsultanta?
- Koji predmeti su dobri za developera?
- Šta je korisno za AI konsultanta?
- Šta je dobro za digital transformation?
- Koji predmeti vode ka finansijskom analitičaru?
- Šta da učim ako hoću business analyst putanju?

### 8.2 Primarni dokumenti

Koristi:

```text
04_baskets/2027/pit_data_ai_bi_korpa.md
04_baskets/2027/pit_software_erp_digital_korpa.md
04_baskets/2027/pit_finance_analytics_korpa.md
```

Sekundarno:

```text
01_courses/2027/
03_course_plans/2025_2026/
00_overview/pit_2027_overview.md
```

### 8.3 Logika odgovora

Bot treba da poveže predmete sa karijernim putanjama, ali bez obećavanja posla.

Ispravna formulacija:

> Ovi predmeti ne garantuju posao, ali razvijaju korisnu osnovu za tu putanju.

Bot treba da pomene da su važni i:

- projekti
- praksa
- samostalni rad
- alati
- portfolio
- komunikacija
- razumevanje poslovanja
- dodatno učenje

### 8.4 Primer odgovora za ERP/SAP

> Za ERP/SAP putanju najvažniji predmet je ERP softver, jer daje osnovu za razumevanje poslovnih procesa, SAP modula i integrisanih informacionih sistema. Korisni su i Baze podataka, Razvoj softvera, Poslovna analitika i Poslovna inteligencija. Ovi predmeti ne garantuju posao, ali daju dobru osnovu za dalje učenje i praksu u ERP/SAP oblasti.

## 9. INTEREST_BASED_RECOMMENDATION

### 9.1 Primeri pitanja

Korisnik može pitati:

- Volim podatke, šta da biram?
- Zanima me AI, ali nisam siguran da hoću programiranje.
- Hoću nešto praktično.
- Hoću više biznis nego kodiranje.
- Volim finansije i tehnologiju.
- Zanima me digitalno poslovanje.
- Hoću smer koji ima smisla za budućnost.
- Ne znam da li sam više za BI ili za softver.
- Ne volim matematiku, šta je bolje za mene?
- Volim analitiku, ali ne bih bio čist programer.

### 9.2 Primarni dokumenti

Koristi:

```text
04_baskets/2027/
```

Sekundarno:

```text
00_overview/
01_courses/2027/
03_course_plans/2025_2026/
```

### 9.3 Logika odgovora

Bot treba da prevodi interesovanje korisnika u oblast i predmete.

Ne treba odmah da nameće karijeru.

Primer:

Ako korisnik kaže “volim podatke”, bot može da predstavi:

- Baze podataka
- Analiza podataka
- Poslovna analitika
- Poslovna inteligencija
- Operaciona istraživanja
- Mašinsko učenje

Ako korisnik kaže “hoću više biznis nego kodiranje”, bot može da predstavi:

- Poslovna analitika
- Poslovna inteligencija
- ERP softver
- Menadžment projekata
- Analiza finansijskih izveštaja
- Računovodstveni informacioni sistemi

Ako korisnik kaže “hoću nešto praktično”, bot može da predstavi:

- ERP softver
- Razvoj softvera
- Baze podataka
- Poslovna inteligencija
- Operaciona istraživanja
- Elektronsko poslovanje i veštačka inteligencija

### 9.4 Primer odgovora

> Ako voliš podatke, ali ne želiš nužno čistu programersku karijeru, najvažniji su Baze podataka, Analiza podataka, Poslovna analitika i Poslovna inteligencija. Od izbornih predmeta posebno su korisni Operaciona istraživanja za Python, simulacije i optimizaciju, i Mašinsko učenje ako želiš AI i prediktivne modele.

## 10. JOB_MARKET

### 10.1 Primeri pitanja

Korisnik može pitati:

- Da li se sa ovim smerom može naći posao?
- Koje poslove mogu da radim posle PIT-a?
- Da li će AI pojesti ovaj smer?
- Da li je ovaj smer bolji od drugih za posao?
- Da li je bolje ići na PIT ili nešto drugo?
- Da li studenti mogu da rade u IT-ju?
- Da li je ovo dovoljno za data analyst posao?
- Da li je ovo dovoljno za SAP konsultanta?
- Da li je ovo dovoljno za developera?

### 10.2 Primarni dokumenti

Koristi:

```text
00_overview/pit_2027_overview.md
00_overview/pin_2020_overview.md
00_overview/pin_2020_vs_pit_2027.md
04_baskets/2027/
```

Sekundarno:

```text
01_courses/2027/
03_course_plans/2025_2026/
```

### 10.3 Logika odgovora

Bot treba da bude realističan.

Ne sme da kaže:

- posao je zagarantovan
- smer sigurno vodi do određene plate
- AI neće uticati na profesije
- jedan predmet je dovoljan za karijeru
- smer je beskoristan zbog AI-ja

Treba da kaže:

- smer daje relevantnu osnovu
- tržište traži dodatni rad i projekte
- AI menja poslove, ali ne uklanja potrebu za poslovno-tehničkim profilima
- najotpornije putanje kombinuju poslovanje, podatke, alate, procese i AI

### 10.4 Primer odgovora

> PIT daje korisnu kombinaciju poslovnih, analitičkih i informacionih znanja. To ne garantuje posao, ali može biti relevantna osnova za BI, business analyst, ERP/SAP, data, digital transformation i neke developer putanje. AI će promeniti deo rutinskih poslova, pa je važno da student ne ostane samo na teoriji, nego da gradi praktične projekte, alate, portfolio i sposobnost da koristi AI u radu.

## 11. FALLBACK

### 11.1 Primeri pitanja

Fallback se aktivira kada korisnik pita:

- za predmet koji nema poseban dokument
- za smer koji nije u bazi znanja
- za drugi fakultet
- za detalje koji nisu u planu rada
- za nastavnika ili saradnika
- za administrativno pravilo koje nije dokumentovano
- za rokove, procedure ili formalne uslove koji nisu u bazi
- za praksu, završni rad ili seminarski rad u detaljima
- za sadržaj koji nije potvrđen nijednim dokumentom

### 11.2 Primarni dokumenti

Koristi:

```text
06_policy/pit_navigator_answering_policy.md
05_retrieval_guides/pit_navigator_retrieval_map.md
04_baskets/2027/pit_izborne_korpe_overview.md
00_overview/pit_2027_overview.md
00_overview/pin_2020_vs_pit_2027.md
```

### 11.3 Minimalni fallback odgovor

Koristi ovu formulaciju:

> Za ovo nemam dovoljno precizan dokument u bazi znanja. Mogu da odgovorim na osnovu dostupnog kurikuluma i srodnih dokumenata, ali za tačan sadržaj, ocenjivanje ili aktuelno izvođenje treba proveriti zvanični plan rada ili silabus.

Ako korisnik pita za drugi smer ili drugi fakultet:

> Ne znam tačno strukturu tvog programa ako nije deo ove baze znanja. Mogu da navedem korisne veštine i predmete iz PIT konteksta, ali formalna pravila moraš proveriti u svom kurikulumu.

### 11.4 Nastavnici i saradnici

Ako korisnik pita o nastavnicima:

> Za aktuelne informacije o nastavnicima i saradnicima najbolje je proveriti zvaničnu stranicu fakulteta, raspored nastave ili zvanični silabus. PIT Navigator ne ocenjuje nastavnike i ne daje preporuke na osnovu toga ko drži predmet.

Bot ne sme da komentariše kvalitet nastavnika ili saradnika.

## 12. Primeri mešovitih pitanja

### 12.1 “Da li da biram Mašinsko učenje ako me zanima AI, ali nisam dobar programer?”

Intent:

```text
INTEREST_BASED_RECOMMENDATION
ELECTIVE_RECOMMENDATION
```

Primarni dokumenti:

```text
04_baskets/2027/pit_data_ai_bi_korpa.md
01_courses/2027/masinsko_ucenje.md
03_course_plans/2025_2026/masinsko_ucenje.md
```

Logika:

- Mašinsko učenje je najdirektnije za AI.
- Treba reći da traži rad sa modelima i Python-om.
- Ako korisnik ne voli programiranje, može se pomenuti i poslovna AI strana kroz Elektronsko poslovanje i veštačku inteligenciju, Poslovnu analitiku i BI.
- Ne treba obeshrabriti korisnika, ali treba biti realan.

Primer odgovora:

> Mašinsko učenje je najdirektniji izbor za AI, ali traži spremnost za rad sa Python-om, podacima i modelima. Ako te AI zanima više poslovno nego programerski, važni su i Elektronsko poslovanje i veštačka inteligencija, Poslovna analitika i Poslovna inteligencija. Za ozbiljniju AI putanju, ipak je korisno da postepeno gradiš tehničku osnovu.

### 12.2 “Da li je ERP bolji od Razvoja softvera?”

Intent:

```text
COURSE_EXPLANATION
CAREER_RECOMMENDATION
```

Primarni dokumenti:

```text
01_courses/2027/erp_softver.md
01_courses/2027/razvoj_softvera.md
04_baskets/2027/pit_software_erp_digital_korpa.md
```

Logika:

- Nije “bolji”, nego različit.
- ERP je za poslovne procese, SAP, integrisane sisteme.
- Razvoj softvera je za aplikacije, modeliranje, web, timski razvoj.
- Za ERP/SAP putanju ERP je centralniji.
- Za developer putanju Razvoj softvera je centralniji.

Primer odgovora:

> Nije stvar u tome da je jedan predmet objektivno bolji. ERP softver je važniji ako te zanimaju SAP, poslovni procesi i integrisani informacioni sistemi. Razvoj softvera je važniji ako te zanima izrada aplikacija, modeliranje sistema, baze, web i timski razvoj. Za ERP/SAP putanju ERP je centralniji, a za developer putanju Razvoj softvera.

### 12.3 “Da li je PIN 2020 lošiji jer nema PIT strukturu?”

Intent:

```text
ACCREDITATION_COMPARISON
```

Primarni dokumenti:

```text
00_overview/pin_2020_vs_pit_2027.md
00_overview/pin_2020_overview.md
00_overview/pit_2027_overview.md
```

Logika:

- Ne reći da je PIN lošiji ili zastareo.
- Reći da PIT 2027 formalno modernizuje strukturu.
- Reći da se PIN 2020 osavremenjuje kroz aktuelno izvođenje.

Primer odgovora:

> Ne bih rekao da je PIN 2020 lošiji ili zastareo. PIT 2027 formalno jasnije strukturira modernizaciju kroz predmete kao što su Poslovna analitika, Poslovna inteligencija, UX, Elektronsko poslovanje i veštačka inteligencija i ERP softver. Ali PIN 2020 se u aktuelnom izvođenju osavremenjuje kroz planove rada, alate i praktičnu nastavu.

## 13. Šta bot ne sme da radi u intent klasifikaciji

Bot ne sme da:

- tretira svako pitanje o predmetu kao COURSE_EXPLANATION ako korisnik pita za aktuelno izvođenje
- koristi course dokument ako korisnik pita za ocenjivanje iz aktuelnog plana rada
- koristi tematsku korpu kao formalno pravilo izbora
- kaže da je izborni predmet obavezan
- kaže da je PIT 2027 automatski bolji od PIN 2020
- komentariše nastavnike
- izmišlja detalje za predmete koji nisu obrađeni
- obećava posao ili platu
- izmišlja administrativna pravila

## 14. Izvori i povezani dokumenti

Ovaj dokument je povezan sa:

```text
05_retrieval_guides/pit_navigator_retrieval_map.md
06_policy/pit_navigator_answering_policy.md

00_overview/pin_2020_overview.md
00_overview/pit_2027_overview.md
00_overview/pin_2020_vs_pit_2027.md

01_courses/2027/
03_course_plans/2025_2026/
04_baskets/2027/
```

Napomena: ovaj dokument ne zamenjuje pojedinačne course, course_plan, overview, basket ili policy dokumente. On daje primere pitanja i pokazuje koji dokumenti treba da imaju prioritet u retrieval-u za određene tipove korisničkih namera.