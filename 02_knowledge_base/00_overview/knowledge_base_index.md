---
id: overview_knowledge_base_index
type: knowledge_base_index
title: PIT Navigator, indeks knowledge base dokumenata
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
  - knowledge base index
  - PIT Navigator
  - indeks dokumenata
  - struktura baze znanja
  - overview
  - course
  - course_plan
  - baskets
  - retrieval guides
  - policy
---

# PIT Navigator, indeks knowledge base dokumenata

## 1. Svrha dokumenta

Ovaj dokument je centralni indeks knowledge base strukture za PIT Navigator.

Cilj je da se jasno vidi:

- koji folderi postoje
- koji dokumenti postoje
- čemu služi svaki tip dokumenta
- koji dokumenti su primarni za koji tip pitanja
- šta nije obrađeno kao poseban dokument
- gde se nalaze retrieval i policy pravila

Ovaj dokument ne sadrži detalje pojedinačnih predmeta. On služi kao mapa baze znanja.

## 2. Glavna struktura knowledge base-a

Knowledge base je organizovan ovako:

```text
02_knowledge_base/
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

## 3. README.md

Fajl `README.md` služi kao kratko uputstvo za korišćenje PIT Navigator knowledge base-a.

Koristi se za:

- brzo razumevanje strukture baze
- orijentaciju po folderima
- objašnjenje razlike između overview, course, course_plan, basket, retrieval i policy dokumenata
- brzu proveru statusa v1 knowledge base-a

## 4. Folder 00_overview

Folder:

```text
02_knowledge_base/
  00_overview/
```

Svrha foldera:

Ovaj folder sadrži osnovne dokumente o modulu, akreditacijama i opštoj strukturi PIT Navigatora.

Koristi se kada korisnik pita:

- šta je PIT
- šta je PIN
- šta se promenilo između 2020 i 2027
- šta je novo u PIT 2027
- da li je PIN 2020 zastareo
- kakva je opšta logika smera
- koje oblasti pokriva poslovno-informatički profil

## 4. Dokumenti u 00_overview

### 4.1 pin_2020_overview.md

Svrha:

Opšti pregled modula PIN 2020, odnosno Poslovna informatika u akreditaciji 2020.

Koristi se za:

- objašnjenje stare akreditacije
- opšti opis PIN profila
- prikaz kontinuiteta poslovno-informatičkog profila
- zaštitu od pogrešne interpretacije da je PIN 2020 zastareo
- povezivanje PIN 2020 sa aktuelnim planovima rada

Važno pravilo:

Bot ne sme da kaže da je PIN 2020 loš, zastareo ili manje vredan. Treba da kaže da se PIN 2020 u aktuelnom izvođenju osavremenjuje kroz planove rada, alate, primere i praktičnu nastavu.

### 4.2 pit_2027_overview.md

Svrha:

Opšti pregled modula PIT 2027, odnosno Poslovne informacione tehnologije u akreditaciji 2027.

Koristi se za:

- objašnjenje novog modula
- prikaz modernizovane strukture
- objašnjenje obaveznih i izbornih predmeta
- povezivanje PIT 2027 sa data, BI, AI, ERP, software i digital business putanjama

Važno pravilo:

Bot treba da predstavi PIT 2027 kao formalno modernizovan i jasnije strukturisan nastavak poslovno-informatičkog profila, ali ne sme da kaže da je PIT 2027 objektivno bolji za svakog studenta.

### 4.3 pin_2020_vs_pit_2027.md

Svrha:

Direktno poređenje PIN 2020 i PIT 2027.

Koristi se za:

- pitanja o razlikama između stare i nove akreditacije
- pitanja o modernizaciji
- pitanja o tome šta je novo
- pitanja o tome šta je ostalo slično
- pitanja o tome da li je PIN 2020 zastareo

Važno pravilo:

Bot treba da kaže da PIT 2027 formalno jasnije strukturira modernizaciju kroz nove obavezne predmete i izborne pozicije, ali da PIN 2020 ne treba predstavljati kao zastareo.

### 4.4 knowledge_base_index.md

Svrha:

Ovaj dokument. Centralni indeks knowledge base strukture.

Koristi se za:

- pregled svih foldera i dokumenata
- orijentaciju u knowledge base-u
- proveru šta postoji, a šta nije obrađeno
- završnu QA proveru strukture

## 5. Folder 01_courses/2027

Folder:

```text
02_knowledge_base/
  01_courses/
    2027/
```

Svrha foldera:

Ovaj folder sadrži course dokumente za predmete iz PIT 2027 akreditacije.

Koristi se kada korisnik pita za:

- formalni opis predmeta u PIT 2027
- status predmeta, obavezan ili izborni
- ESPB
- semestar
- cilj predmeta
- ishode učenja
- ključne teme
- vezu predmeta sa karijerama
- šta predmet pokriva u novoj akreditaciji

Važno pravilo:

Ako korisnik pita za “PIT 2027”, “nova akreditacija”, “novi smer” ili formalni opis predmeta, prednost imaju dokumenti iz `01_courses/2027/`.

Ako korisnik pita za “trenutno”, “ove godine”, “kako se polaže”, “plan rada” ili “šta se sada radi”, prednost imaju dokumenti iz `03_course_plans/2025_2026/`.

## 6. Dokumenti u 01_courses/2027

### 6.1 baze_podataka.md

Svrha:

Opis predmeta Baze podataka u PIT 2027.

Koristi se za:

- SQL i baze podataka
- organizaciju podataka
- vezu sa softverom, BI, ERP i data putanjama
- osnovu za sve dalje data i software predmete

### 6.2 poslovna_analitika.md

Svrha:

Opis predmeta Poslovna analitika u PIT 2027.

Koristi se za:

- poslovnu analitiku
- donošenje odluka na osnovu podataka
- business analyst putanju
- vezu između podataka, poslovnog problema i preporuke

### 6.3 poslovna_inteligencija.md

Svrha:

Opis predmeta Poslovna inteligencija u PIT 2027.

Koristi se za:

- BI
- dashboarde
- KPI pokazatelje
- poslovno izveštavanje
- vizualizaciju poslovnih podataka
- business / BI analyst putanju

### 6.4 korisnicko_iskustvo_i_dizajn.md

Svrha:

Opis predmeta Korisničko iskustvo i dizajn u PIT 2027.

Koristi se za:

- UX
- UI
- korisničke interfejse
- digitalne proizvode
- korisnički put
- vezu između tehnologije i korisničkih potreba

### 6.5 elektronsko_poslovanje_i_vestacka_inteligencija.md

Svrha:

Opis predmeta Elektronsko poslovanje i veštačka inteligencija u PIT 2027.

Koristi se za:

- AI u digitalnom poslovanju
- chatbotove
- preporuke
- AI servise
- e-commerce
- digitalne platforme
- poslovne web scenarije

Važna napomena:

Ovaj predmet nije isto što i Mašinsko učenje. Elektronsko poslovanje i veštačka inteligencija je više usmereno na poslovne i digitalne AI primene, dok je Mašinsko učenje usmerenije na modele i algoritme.

### 6.6 analiza_podataka.md

Svrha:

Opis predmeta Analiza podataka u PIT 2027.

Koristi se za:

- obradu podataka
- statističku analizu
- interpretaciju podataka
- data analyst i business analyst osnovu
- pripremu za BI, poslovnu analitiku i mašinsko učenje

### 6.7 objektno_orijentisano_programiranje.md

Svrha:

Opis predmeta Objektno orijentisano programiranje u PIT 2027.

Koristi se za:

- OOP
- Java
- klase i objekte
- nasleđivanje
- polimorfizam
- enkapsulaciju
- developer osnovu
- tehničku osnovu za Razvoj softvera

### 6.8 razvoj_softvera.md

Svrha:

Opis predmeta Razvoj softvera u PIT 2027.

Koristi se za:

- razvoj poslovnih aplikacija
- modeliranje sistema
- web aplikacije
- baze podataka
- agilni razvoj
- Scrum
- timski projekat
- developer i business analyst putanju

Važna napomena:

Ako se pominje budući fokus ka Python/Flask-u ili AI-assisted development-u, to treba predstaviti samo kao radni predlog dok nije potvrđeno aktuelnim planom rada.

### 6.9 erp_softver.md

Svrha:

Opis predmeta ERP softver u PIT 2027.

Koristi se za:

- ERP
- SAP
- poslovne procese
- integrisane informacione sisteme
- ERP / SAP konsultantsku putanju
- vezu između poslovnih procesa, podataka i izveštavanja

### 6.10 operaciona_istrazivanja.md

Svrha:

Opis predmeta Operaciona istraživanja u PIT 2027.

Koristi se za:

- Python
- NumPy
- SciPy
- pandas
- Matplotlib
- simulacije
- optimizaciju
- preskriptivnu analitiku
- data / AI / BI putanju

Važna napomena:

Predmet je izborni u PIT 2027. Ne sme se predstaviti kao predmet koji svi studenti obavezno slušaju.

### 6.11 masinsko_ucenje.md

Svrha:

Opis predmeta Mašinsko učenje u PIT 2027.

Koristi se za:

- AI
- machine learning
- Python
- klasifikaciju
- regresiju
- klasterizaciju
- PCA
- faktorsku analizu
- stabla odlučivanja
- SVM
- neuronske mreže
- sisteme preporuka
- AI i data science putanju

Važna napomena:

Predmet je izborni u PIT 2027. Ne sme se predstaviti kao predmet koji svi studenti obavezno slušaju.

## 7. Folder 03_course_plans/2025_2026

Folder:

```text
02_knowledge_base/
  03_course_plans/
    2025_2026/
```

Svrha foldera:

Ovaj folder sadrži aktuelne planove rada za školsku godinu 2025/26.

Koristi se kada korisnik pita:

- šta se sada radi
- kako se sada polaže
- koji alati se koriste
- kakav je nedeljni plan
- šta se radi na vežbama
- kakav je kolokvijum
- kakav je završni ispit
- koji projekti postoje
- kakve su predispitne obaveze

Važno pravilo:

Aktuelni plan rada ima prednost za operativna pitanja.

Akreditacioni course dokument ima prednost za formalni opis u PIT 2027.

## 8. Dokumenti u 03_course_plans/2025_2026

### 8.1 baze_podataka.md

Svrha:

Aktuelni plan rada za Baze podataka u školskoj godini 2025/26.

Koristi se za:

- aktuelno izvođenje
- alate
- teme po nedeljama
- ocenjivanje
- praktične vežbe

### 8.2 veb_dizajn.md

Svrha:

Aktuelni plan rada za Veb dizajn u školskoj godini 2025/26.

Koristi se za:

- trenutno izvođenje Veb dizajna
- web tehnologije
- praktične teme
- ocenjivanje
- vežbe

Napomena:

Veb dizajn je deo PIN 2020 / aktuelnog izvođenja, a ne poseban obavezan predmet PIT 2027 u istoj formi.

### 8.3 elektronsko_poslovanje.md

Svrha:

Aktuelni plan rada za Elektronsko poslovanje u školskoj godini 2025/26.

Koristi se za:

- trenutno izvođenje Elektronskog poslovanja
- digitalno poslovanje
- e-commerce
- aktuelne teme i ocenjivanje

Napomena:

Za PIT 2027 postoji poseban predmet `Elektronsko poslovanje i veštačka inteligencija`.

### 8.4 analiza_podataka.md

Svrha:

Aktuelni plan rada za Analizu podataka u školskoj godini 2025/26.

Koristi se za:

- trenutno izvođenje Analize podataka
- alate i metode
- ocenjivanje
- praktičan rad sa podacima

### 8.5 objektno_orijentisano_programiranje.md

Svrha:

Aktuelni plan rada za Objektno orijentisano programiranje u školskoj godini 2025/26.

Koristi se za:

- trenutno izvođenje OOP-a
- Java / OOP teme
- ocenjivanje
- vežbe
- praktične zadatke

### 8.6 razvoj_softvera.md

Svrha:

Aktuelni plan rada za Razvoj softvera u školskoj godini 2025/26.

Koristi se za:

- trenutno izvođenje Razvoja softvera
- PHP
- baze podataka
- frontend
- Scrum
- timski projekat
- ocenjivanje

Važna napomena:

Ako postoji radni predlog za budući fokus ka Python/Flask-u, bot ne sme da kaže da se to trenutno radi dok ne bude potvrđeno novim planom rada.

### 8.7 erp_softver.md

Svrha:

Aktuelni plan rada za ERP softver u školskoj godini 2025/26.

Koristi se za:

- SAP ERP
- SAP module
- SD, MM, WM, FI, HCM
- MongoDB
- PyMongo
- Python
- Tkinter
- Big Data
- mini ERP dashboard
- ocenjivanje
- aktuelno izvođenje

### 8.8 operaciona_istrazivanja.md

Svrha:

Aktuelni plan rada za Operaciona istraživanja u školskoj godini 2025/26.

Koristi se za:

- Python
- NumPy
- Monte Carlo simulacije
- MIP
- Matplotlib
- pandas
- optimizaciju
- ocenjivanje
- nedeljni plan

### 8.9 masinsko_ucenje.md

Svrha:

Aktuelni plan rada za Mašinsko učenje u školskoj godini 2025/26.

Koristi se za:

- Python
- klaster analizu
- PCA
- faktorsku analizu
- klasifikaciju
- stabla odlučivanja
- Naivni Bejs
- logističku regresiju
- neuronske mreže
- RNN
- istraživački rad na realnom skupu podataka
- ocenjivanje

## 9. Folder 04_baskets/2027

Folder:

```text
02_knowledge_base/
  04_baskets/
    2027/
```

Svrha foldera:

Ovaj folder sadrži dokumente za izborne predmete, tematske korpe i preporuke po interesovanjima.

Koristi se kada korisnik pita:

- šta da izaberem
- koji izborni predmet je korisniji
- šta ako me zanima AI
- šta ako me zanima BI
- šta ako me zanima ERP
- šta ako me zanimaju finansije i podaci
- šta ako me zanima e-commerce
- šta ako me zanima fintech
- šta ako želim više biznis nego kodiranje
- koje predmete da biram za određenu karijeru

Važno pravilo:

Ovi dokumenti nisu formalno rangiranje predmeta. Oni su preporuke po interesovanjima i karijernim putanjama.

## 10. Dokumenti u 04_baskets/2027

### 10.1 pit_izborne_korpe_overview.md

Svrha:

Pregled izbornih pozicija PIT 2027 i osnovna logika preporuka.

Koristi se za:

- formalni pregled izbornih pozicija
- objašnjenje da izborni predmeti nisu obavezni za sve
- pravila preporučivanja
- praktičnu logiku izbora po semestrima
- zaštitne formulacije

### 10.2 pit_data_ai_bi_korpa.md

Svrha:

Tematska korpa za data, AI i BI putanje.

Koristi se za korisnike koje zanimaju:

- podaci
- AI
- BI
- poslovna analitika
- poslovna inteligencija
- mašinsko učenje
- operaciona istraživanja
- Python
- optimizacija
- simulacije
- prediktivna i preskriptivna analitika

### 10.3 pit_software_erp_digital_korpa.md

Svrha:

Tematska korpa za software, ERP i digitalne putanje.

Koristi se za korisnike koje zanimaju:

- programiranje
- razvoj softvera
- ERP / SAP
- digitalno poslovanje
- e-commerce
- fintech
- UX
- poslovne web aplikacije
- digitalna transformacija

### 10.4 pit_finance_analytics_korpa.md

Svrha:

Tematska korpa za finance analytics putanje.

Koristi se za korisnike koje zanimaju:

- finansije i podaci
- finansijska analitika
- BI u finansijama
- ERP / SAP i finansijski podaci
- analiza finansijskih izveštaja
- računovodstveni informacioni sistemi
- ekonometrija
- kvantitativne finansije
- mašinsko učenje u finansijama

### 10.5 pit_minor_electives_reference.md

Svrha:

Kratka referenca za izborne predmete koji nemaju poseban course dokument.

Koristi se kada korisnik pita za:

- Elektronsku trgovinu
- Elektronske platne sisteme
- Nove informacione tehnologije
- Menadžment odnosa sa kupcima
- Računovodstvene informacione sisteme
- Analizu finansijskih izveštaja
- Upravljačko računovodstvo
- Finansijsku ekonomiju
- Ekonometriju
- Kvantitativne finansije
- Ekonomska statistiku
- Istraživanje tržišta
- Marketing
- Organizaciju
- druge izborne predmete bez pojedinačnog course dokumenta

Važno pravilo:

Za ove predmete bot sme da da širi kontekst i preporuku po interesovanju, ali ne sme da izmišlja detaljan sadržaj, ocenjivanje ili aktuelni plan rada.

## 11. Folder 05_retrieval_guides

Folder:

```text
02_knowledge_base/
  05_retrieval_guides/
```

Svrha foldera:

Ovaj folder sadrži pravila za retrieval, intent mapiranje i izbor pravog dokumenta.

Koristi se kao sistemski sloj za RAG ponašanje.

## 12. Dokumenti u 05_retrieval_guides

### 12.1 pit_navigator_retrieval_map.md

Svrha:

Glavna retrieval mapa.

Koristi se za:

- mapiranje intent-a na dokumente
- izbor između overview, course, course_plan, basket i policy dokumenata
- rešavanje konflikata između akreditacionih dokumenata i aktuelnih planova rada
- fallback pravila
- pravila za PIT 2027 vs PIN 2020

### 12.2 pit_navigator_intent_examples.md

Svrha:

Primeri korisničkih pitanja i očekivanog retrieval-a.

Koristi se za:

- prepoznavanje intent-a
- razlikovanje sličnih pitanja
- primere mešovitih pitanja
- primer očekivane logike odgovora
- izbegavanje pogrešnog retrieval-a

## 13. Folder 06_policy

Folder:

```text
02_knowledge_base/
  06_policy/
```

Svrha foldera:

Ovaj folder sadrži pravila odgovaranja i zaštitne formulacije.

Koristi se za:

- opšta pravila ponašanja bota
- zabrane
- fallback odgovore
- pravila za nastavnike i saradnike
- pravila za posao i karijere
- pravila za PIN 2020 vs PIT 2027
- pravila za izborne predmete
- pravila za radne predloge

## 14. Dokumenti u 06_policy

### 14.1 pit_navigator_answering_policy.md

Svrha:

Glavni policy dokument za odgovaranje.

Koristi se za:

- pravila tona
- pravila za preporuke
- pravila za karijere
- pravila za tržište rada i AI
- zabranu komentarisanja nastavnika
- zabranu izmišljanja sadržaja
- fallback formulacije
- zaštitne formulacije za PIN 2020
- razliku između akreditacionog opisa i aktuelnog plana rada

## 15. Dokumenti koje ne pravimo kao posebne dokumente

Za ovu verziju PIT Navigatora ne pravimo posebne dokumente za:

- praksu
- završni rad
- seminarske radove
- letnju školu

Ako korisnik pita o njima, bot može da odgovori samo opšte, ako je potvrđeno kurikulumom.

Za detalje treba uputiti korisnika na zvanična fakultetska uputstva.

## 16. Predmeti koji nemaju poseban course dokument

Neki izborni predmeti nemaju poseban course dokument.

Za njih se koristi:

```text
04_baskets/2027/pit_minor_electives_reference.md
```

i relevantne tematske korpe.

Primeri takvih predmeta:

```text
Menadžment odnosa sa kupcima
Poresko planiranje
Finansijska i aktuarska matematika
Linearna algebra
Teorija verovatnoće
Računovodstveni informacioni sistemi
Marketing
Organizacija
Finansijska ekonomija
Međunarodne finansije
Monetarna ekonomija
Makroekonomski modeli
Ekonomija i biznis u turizmu
Analiza finansijskih izveštaja
Upravljačko računovodstvo
Osnovi poslovnih finansija
Istraživanje tržišta
Ekonometrija
Kvantitativne finansije
Ekonomska statistika
Elektronska trgovina
Nove informacione tehnologije
Elektronski platni sistemi
```

Bot ne sme da izmišlja detalje za ove predmete ako ne postoje u dokumentima.

## 17. Primarni dokument po tipu pitanja

### 17.1 Pitanje o modulu uopšteno

Primarno koristi:

```text
00_overview/pit_2027_overview.md
00_overview/pin_2020_overview.md
```

Ako je pitanje o razlikama:

```text
00_overview/pin_2020_vs_pit_2027.md
```

### 17.2 Pitanje o konkretnom predmetu u PIT 2027

Primarno koristi:

```text
01_courses/2027/[predmet].md
```

### 17.3 Pitanje o trenutnom izvođenju predmeta

Primarno koristi:

```text
03_course_plans/2025_2026/[predmet].md
```

### 17.4 Pitanje o izbornim predmetima

Primarno koristi:

```text
04_baskets/2027/pit_izborne_korpe_overview.md
04_baskets/2027/[relevantna_tematska_korpa].md
```

### 17.5 Pitanje o predmetu bez course dokumenta

Primarno koristi:

```text
04_baskets/2027/pit_minor_electives_reference.md
```

### 17.6 Pitanje o retrieval logici

Primarno koristi:

```text
05_retrieval_guides/pit_navigator_retrieval_map.md
05_retrieval_guides/pit_navigator_intent_examples.md
```

### 17.7 Pitanje o tome kako bot treba da odgovori

Primarno koristi:

```text
06_policy/pit_navigator_answering_policy.md
```

## 18. Ključna pravila za ceo knowledge base

Bot mora da poštuje sledeće:

- ne izmišljati sadržaj predmeta
- ne tvrditi da su izborni predmeti obavezni
- ne tvrditi da izbor predmeta garantuje posao
- ne tvrditi da jedan predmet pokriva celu karijeru
- ne komentarisati nastavnike i saradnike
- ne preporučivati predmete zbog nastavnika
- ne omalovažavati predmete koji nisu prioritetni
- ne tvrditi da je PIN 2020 zastareo
- ne tvrditi da je PIT 2027 objektivno bolji za svakog studenta
- razlikovati akreditacioni opis od aktuelnog plana rada
- razlikovati formalne izborne pozicije od tematskih korpi
- za nedovoljno obrađene predmete koristiti fallback
- za praksu, završni rad i seminarske radove ne praviti posebne analize

## 19. Minimalni fallback odgovor

Ako nema dovoljno informacija, bot treba da kaže:

> Za ovo nemam dovoljno precizan dokument u bazi znanja. Mogu da odgovorim na osnovu dostupnog kurikuluma i srodnih dokumenata, ali za tačan sadržaj, ocenjivanje ili aktuelno izvođenje treba proveriti zvanični plan rada ili silabus.

Ako korisnik pita za drugi smer ili drugi fakultet:

> Ne znam tačno strukturu tvog programa ako nije deo ove baze znanja. Mogu da navedem korisne veštine i predmete iz PIT konteksta, ali formalna pravila moraš proveriti u svom kurikulumu.

## 20. Status knowledge base-a

U ovoj fazi knowledge base pokriva:

- overview PIN 2020
- overview PIT 2027
- poređenje PIN 2020 i PIT 2027
- glavne PIT 2027 course dokumente
- aktuelne planove rada za obrađene predmete 2025/26
- izborne korpe PIT 2027
- kratku referencu za manje obrađene izborne predmete
- retrieval mapu
- intent primere
- answering policy

Ova verzija je dovoljna za prvu funkcionalnu verziju PIT Navigatora.

## 21. Sledeća moguća unapređenja

U budućnosti se mogu dodati:

- posebni course dokumenti za najtraženije izborne predmete ako korisnici često pitaju za njih
- ažurirani planovi rada za naredne školske godine
- dodatni primeri pitanja iz realnih korisničkih razgovora
- test pitanja za evaluaciju retrieval-a
- dokument za QA proveru odgovora
- dokument za verzionisanje i changelog knowledge base-a

## 22. Izvori i povezani dokumenti

Ovaj indeks se oslanja na kompletnu strukturu:

```text
00_overview/
01_courses/2027/
03_course_plans/2025_2026/
04_baskets/2027/
05_retrieval_guides/
06_policy/
```

Posebno povezani dokumenti:

```text
00_overview/pin_2020_overview.md
00_overview/pit_2027_overview.md
00_overview/pin_2020_vs_pit_2027.md

04_baskets/2027/pit_izborne_korpe_overview.md
04_baskets/2027/pit_data_ai_bi_korpa.md
04_baskets/2027/pit_software_erp_digital_korpa.md
04_baskets/2027/pit_finance_analytics_korpa.md
04_baskets/2027/pit_minor_electives_reference.md

05_retrieval_guides/pit_navigator_retrieval_map.md
05_retrieval_guides/pit_navigator_intent_examples.md

06_policy/pit_navigator_answering_policy.md
```

Napomena: ovaj dokument je indeks. Za konkretne odgovore bot treba da koristi odgovarajući primarni dokument iz foldera `00_overview`, `01_courses/2027`, `03_course_plans/2025_2026`, `04_baskets/2027`, `05_retrieval_guides` ili `06_policy`, u skladu sa intent-om korisničkog pitanja.
