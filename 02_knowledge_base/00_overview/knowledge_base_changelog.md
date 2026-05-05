---
id: overview_knowledge_base_changelog
type: changelog
title: PIT Navigator, changelog knowledge base-a
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
  - changelog
  - versioning
  - PIT Navigator
  - v1
  - knowledge base
  - izmene
  - verzionisanje
  - status
---

# PIT Navigator, changelog knowledge base-a

## 1. Svrha dokumenta

Ovaj dokument beleži razvoj PIT Navigator knowledge base-a kroz verzije.

Cilj je da se jasno zna:

- šta je urađeno u verziji v1.0
- koji folderi i dokumenti postoje
- koje odluke su namerno donete
- šta nije obrađeno u ovoj verziji
- šta treba proveravati pri budućim izmenama
- koja su moguća buduća unapređenja

Ovaj dokument ne sadrži detalje pojedinačnih predmeta. On služi za verzionisanje i održavanje knowledge base-a.

## 2. Trenutna verzija

```text
Version: v1.0
Status: ready_for_initial_rag_testing
Last updated: 2026-05-04
```

Verzija v1.0 predstavlja prvu funkcionalnu verziju PIT Navigator knowledge base-a i označena je kao spremna za početno RAG testiranje.

Ova verzija je dovoljna za početno RAG testiranje jer sadrži:

- overview dokumente
- PIT 2027 course dokumente za glavne predmete
- aktuelne planove rada 2025/26 za obrađene predmete
- izborne korpe i preporuke
- referencu za izborne predmete bez posebnog course dokumenta
- retrieval mapu
- intent primere
- answering policy
- QA checklist
- indeks knowledge base-a
- README kao ulaznu orijentaciju za korišćenje baze

## 3. Glavna struktura v1.0

U verziji v1.0 knowledge base je organizovan ovako:

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

## 4. Dokumenti završeni u verziji v1.0

### 4.1 README.md

Status:

```text
QA_STATUS: ready
```

Svrha:

README.md daje kratko uputstvo za korišćenje knowledge base-a i služi kao ulazna orijentacija za strukturu foldera i tipove dokumenata.

### 4.2 Overview dokumenti

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
knowledge_base_index.md
knowledge_base_changelog.md
```

Status:

```text
QA_STATUS: ready
```

Svrha:

- opšti pregled PIN 2020
- opšti pregled PIT 2027
- poređenje PIN 2020 i PIT 2027
- centralni indeks strukture
- verzionisanje knowledge base-a

## 5. PIT 2027 course dokumenti završeni u v1.0

Folder:

```text
02_knowledge_base/
  01_courses/
    2027/
```

Dokumenti:

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

Status:

```text
QA_STATUS: ready
```

Svrha:

Ovi dokumenti pokrivaju glavne predmete PIT 2027 koji su važni za:

- data
- AI
- BI
- software
- ERP
- digital business
- UX
- poslovnu analitiku
- razvoj softvera
- operaciona istraživanja
- mašinsko učenje

Važna napomena:

Operaciona istraživanja i Mašinsko učenje su izborni predmeti u PIT 2027 i ne smeju se predstavljati kao predmeti koje svi studenti nužno slušaju.

## 6. Aktuelni planovi rada završeni u v1.0

Folder:

```text
02_knowledge_base/
  03_course_plans/
    2025_2026/
```

Dokumenti:

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

Status:

```text
QA_STATUS: ready
```

Svrha:

Ovi dokumenti pokrivaju aktuelno izvođenje predmeta u školskoj godini 2025/26.

Koriste se za pitanja o:

- ocenjivanju
- alatima
- nedeljnom planu
- kolokvijumima
- završnom ispitu
- vežbama
- projektima
- trenutnom izvođenju predmeta

Važna napomena:

Aktuelni plan rada ima prednost za operativna pitanja.

Akreditacioni course dokument ima prednost za formalni opis PIT 2027.

## 7. Izborne korpe završene u v1.0

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
pit_minor_electives_reference.md
```

Status:

```text
QA_STATUS: ready
```

Svrha:

Ovi dokumenti pokrivaju:

- formalne izborne pozicije PIT 2027
- preporuke po interesovanjima
- data / AI / BI putanju
- software / ERP / digital putanju
- finance analytics putanju
- izborne predmete bez posebnog course dokumenta

Važna napomena:

Tematske korpe nisu formalne kurikulumske korpe. One su preporuke po interesovanju.

Bot ne sme da kaže da postoji zvanično rangiranje izbornih predmeta ako ono nije navedeno u kurikulumu.

## 8. Retrieval dokumenti završeni u v1.0

Folder:

```text
02_knowledge_base/
  05_retrieval_guides/
```

Dokumenti:

```text
pit_navigator_retrieval_map.md
pit_navigator_intent_examples.md
```

Status:

```text
QA_STATUS: ready
```

Svrha:

Ovi dokumenti definišu:

- koji dokumenti se koriste za koji tip pitanja
- kako razlikovati intent-e
- kako razlikovati course i course_plan pitanja
- kako postupati kod izbornih preporuka
- kako postupati kod fallback pitanja
- kako postupati kod mešovitih pitanja

## 9. Policy dokumenti završeni u v1.0

Folder:

```text
02_knowledge_base/
  06_policy/
```

Dokumenti:

```text
pit_navigator_answering_policy.md
pit_navigator_qa_checklist.md
```

Status:

```text
QA_STATUS: ready
```

Svrha:

Ovi dokumenti definišu:

- pravila odgovaranja
- zabrane
- fallback formulacije
- QA proveru
- pravila za nastavnike i saradnike
- pravila za karijere i tržište rada
- pravila za PIT 2027 i PIN 2020
- pravila za aktuelni plan rada i akreditacioni opis
- pravila za izborne predmete

## 10. Ključne odluke u v1.0

### 10.1 PIT 2027 je primarni sloj za izborne korpe

U verziji v1.0 izborne korpe se prave samo za PIT 2027.

PIN 2020 se ne mapira detaljno kroz posebne izborne korpe.

Razlog:

- PIT 2027 je ciljna nova struktura
- izborne pozicije su jasnije definisane
- PIN 2020 se koristi kroz overview, comparison i aktuelne planove rada
- izbegava se nepotrebno dupliranje posla

### 10.2 PIN 2020 se ne predstavlja kao zastareo

Jedna od glavnih policy odluka je da se PIN 2020 ne sme nazivati zastarelim.

Ispravna formulacija:

> PIT 2027 formalno modernizuje i jasnije strukturira poslovno-informatički profil. To ne znači da je PIN 2020 zastareo, jer se aktuelno izvođenje predmeta osavremenjuje kroz planove rada, alate, primere i praktičnu nastavu.

### 10.3 Aktuelni planovi rada imaju prednost za operativna pitanja

Ako korisnik pita kako se predmet trenutno izvodi, koristi se:

```text
03_course_plans/2025_2026/
```

Ako korisnik pita za formalni opis PIT 2027, koristi se:

```text
01_courses/2027/
```

### 10.4 Praksa, završni rad i seminarski radovi se ne obrađuju kao posebni dokumenti

U v1.0 namerno ne pravimo posebne dokumente za:

- praksu
- završni rad
- seminarske radove
- letnju školu

Za ove teme bot može dati samo opšti odgovor ako je potvrđeno kurikulumom, uz upućivanje na zvanična fakultetska uputstva za procedure i rokove.

### 10.5 Nastavnici i saradnici se ne komentarišu

U v1.0 bot ne sme da:

- ocenjuje nastavnike
- ocenjuje saradnike
- preporučuje predmet zbog nastavnika
- odvraća od predmeta zbog nastavnika
- koristi lična imena u preporukama

Za aktuelne informacije korisnik se upućuje na zvanični raspored, silabus ili stranicu fakulteta.

### 10.6 Izborni predmeti se ne predstavljaju kao obavezni

Posebno važi za:

- Operaciona istraživanja
- Mašinsko učenje
- Elektronsku trgovinu
- Elektronske platne sisteme
- Nove informacione tehnologije
- sve ostale predmete iz izbornih pozicija

Bot mora jasno reći da izborni predmeti zavise od izborne pozicije i pravila izbora.

## 11. Šta je namerno izostavljeno u v1.0

U ovoj verziji nisu urađeni posebni course dokumenti za sve izborne predmete.

Predmeti koji su pokriveni kroz kratku referencu, a ne kroz posebne course dokumente:

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

Razlog:

- nisu svi predmeti jednako važni za prvu verziju
- cilj je bio izbeći preveliko dupliranje posla
- tematske korpe i minor electives reference daju dovoljno konteksta za preporuke
- detalji se mogu dodati kasnije ako korisnici često pitaju za neki predmet

## 12. Status predmeta u v1.0

### 12.1 Predmeti sa posebnim PIT 2027 course dokumentom

```text
Baze podataka
Poslovna analitika
Poslovna inteligencija
Korisničko iskustvo i dizajn
Elektronsko poslovanje i veštačka inteligencija
Analiza podataka
Objektno orijentisano programiranje
Razvoj softvera
ERP softver
Operaciona istraživanja
Mašinsko učenje
```

### 12.2 Predmeti sa aktuelnim planom rada 2025/26

```text
Baze podataka
Veb dizajn
Elektronsko poslovanje
Analiza podataka
Objektno orijentisano programiranje
Razvoj softvera
ERP softver
Operaciona istraživanja
Mašinsko učenje
```

### 12.3 Predmeti pokriveni kroz minor electives reference

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

## 13. Poznate granice v1.0

Knowledge base v1.0 ne pokriva detaljno:

- sve izborne predmete kroz course dokumente
- sve planove rada za buduće školske godine
- administrativne procedure za praksu
- administrativne procedure za završni rad
- aktuelne informacije o nastavnicima i saradnicima
- zvanične rokove
- sve moguće kombinacije izbornih predmeta
- stvarne tržišne podatke o zapošljavanju
- plate
- garancije zaposlenja
- pojedinačne preferencije svakog studenta

Za ove slučajeve koristi se fallback ili upućivanje na zvanične izvore.

## 14. Moguća unapređenja posle v1.0

Buduća unapređenja mogu uključiti:

- posebne course dokumente za najčešće tražene izborne predmete
- aktuelne planove rada za naredne školske godine
- test set pitanja za evaluaciju RAG-a
- dokument sa očekivanim odgovorima za evaluaciju
- dodatni changelog za v1.1, v1.2 i dalje
- automatsku QA proveru Markdown formata
- dodatne karijerne mape
- posebnu mapu alata i tehnologija po predmetima
- dokument za poređenje PIT-a sa drugim modulima, ako se kasnije doda dovoljno izvora
- ažuriranje preporuka kada se promene planovi rada

## 15. Pravila za buduće izmene

Pri svakoj budućoj izmeni treba proveriti:

- da li je promenjen izvor
- da li se promenio status predmeta
- da li se promenio plan rada
- da li se promenio naziv predmeta
- da li se promenila izborna pozicija
- da li treba ažurirati povezane basket dokumente
- da li treba ažurirati retrieval mapu
- da li treba ažurirati intent examples
- da li treba ažurirati answering policy
- da li treba ažurirati knowledge_base_index
- da li treba dodati novu stavku u changelog

## 16. Preporučeni format budućih changelog unosa

Za buduće verzije koristiti format:

```text
## Version vX.Y, YYYY-MM-DD

Status:
Scope:
Changed:
Added:
Removed:
Not changed:
Notes:
```

Primer:

```text
## Version v1.1, 2026-09-15

Status: updated_course_plans
Scope: course_plan update for academic year 2026/2027

Changed:
- updated ERP softver plan rada
- updated Razvoj softvera plan rada

Added:
- 03_course_plans/2026_2027/erp_softver.md
- 03_course_plans/2026_2027/razvoj_softvera.md

Removed:
- nothing

Not changed:
- PIT 2027 course documents remain unchanged

Notes:
- 2025/26 plans remain archived for historical comparison
```

## 17. Minimalni QA status v1.0

Trenutni status:

```text
QA_STATUS: ready_for_initial_rag_testing
```

Značenje:

- dokumenti su strukturno spremni
- ključne zaštitne formulacije postoje
- izborni predmeti su odvojeni od obaveznih
- PIN 2020 nije predstavljen kao zastareo
- aktuelni planovi rada su odvojeni od PIT 2027 course dokumenata
- postoje retrieval i policy dokumenti
- postoji QA checklist

Pre pune produkcije preporučuje se:

- testiranje retrieval-a na realnim pitanjima
- ručna provera nekoliko odgovora po intent-u
- provera da RAG pravilno razlikuje `course` i `course_plan`
- provera da RAG ne vraća samo minor electives reference kada postoji detaljan course dokument

## 18. Sledeći korak posle ovog changelog-a

Nakon changelog-a, preporučeni sledeći korak je:

```text
02_knowledge_base/
  05_retrieval_guides/
    pit_navigator_test_questions.md
```

Svrha tog dokumenta:

- napraviti test pitanja za svaki intent
- proveriti koji dokument treba da se povuče
- definisati očekivane elemente odgovora
- proveriti da bot ne krši policy pravila

## 19. Izvori i povezani dokumenti

Ovaj changelog je povezan sa:

```text
00_overview/knowledge_base_index.md
06_policy/pit_navigator_qa_checklist.md
06_policy/pit_navigator_answering_policy.md
05_retrieval_guides/pit_navigator_retrieval_map.md
05_retrieval_guides/pit_navigator_intent_examples.md
04_baskets/2027/pit_minor_electives_reference.md
```

Napomena: ovaj dokument je namenjen održavanju i verzionisanju knowledge base-a. Ne koristi se kao primarni izvor za odgovore o predmetima, već kao evidencija šta je urađeno, šta je namerno izostavljeno i kako treba voditi buduće izmene.
