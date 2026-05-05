---
id: policy_pit_navigator_qa_checklist
type: qa_checklist
title: PIT Navigator, QA checklist za knowledge base
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
  - QA checklist
  - quality assurance
  - PIT Navigator
  - provera dokumenata
  - RAG
  - frontmatter
  - policy
  - retrieval
  - izborne korpe
  - course documents
---

# PIT Navigator, QA checklist za knowledge base

## 1. Svrha dokumenta

Ovaj dokument služi kao kontrolna lista za proveru kvaliteta PIT Navigator knowledge base-a pre korišćenja u RAG sistemu.

Checklist se koristi za proveru:

- strukture foldera
- frontmatter-a
- tačnosti statusa predmeta
- razlike između akreditacije i aktuelnog plana rada
- tretmana izbornih predmeta
- tretmana PIN 2020 i PIT 2027
- zabrane komentarisanja nastavnika
- fallback pravila
- izvora
- konzistentnosti naziva predmeta
- čistoće Markdown formata

Ovaj dokument ne sadrži sadržaj predmeta, već pravila za proveru dokumenata.

## 2. Glavno QA pravilo

Dokument je spreman za RAG tek kada:

1. ima ispravan frontmatter
2. ima jasan tip dokumenta
3. ima jasan izvor
4. ne meša akreditacioni opis i aktuelno izvođenje
5. jasno razlikuje obavezne i izborne predmete
6. ne sadrži komentare o nastavnicima i saradnicima
7. ne izmišlja informacije koje nisu u izvorima
8. ima zaštitne formulacije gde su potrebne
9. ima pravilno zatvorene Markdown code block-ove
10. završava se jasnom sekcijom o izvorima ili napomenom

## 3. Provera strukture foldera

Očekivana struktura:

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

Checklist:

- [ ] Folder `00_overview/` postoji
- [ ] Folder `01_courses/2027/` postoji
- [ ] Folder `03_course_plans/2025_2026/` postoji
- [ ] Folder `04_baskets/2027/` postoji
- [ ] Folder `05_retrieval_guides/` postoji
- [ ] Folder `06_policy/` postoji
- [ ] Dokumenti nisu pomešani između foldera
- [ ] Course dokumenti za PIT 2027 nisu u folderu za aktuelne planove rada
- [ ] Aktuelni planovi rada nisu u folderu `01_courses/2027/`
- [ ] Policy i retrieval dokumenti nisu pomešani sa course dokumentima

## 4. Provera frontmatter-a

Svaki dokument treba da ima YAML frontmatter na početku.

Minimum:

```yaml
---
id:
type:
title:
last_updated:
keywords:
---
```

Za course dokumente treba proveriti:

- [ ] `id` postoji
- [ ] `type: course`
- [ ] `title` postoji
- [ ] `course_code` postoji kada je dostupan
- [ ] `accreditation: 2027`
- [ ] `module: PIT`
- [ ] `status` jasno kaže da li je predmet obavezan ili izborni
- [ ] `espb` postoji kada je dostupan
- [ ] `semester` postoji kada je dostupan
- [ ] `source_file` postoji
- [ ] `source_status` postoji
- [ ] `related_intents` postoji
- [ ] `keywords` postoji

Za course_plan dokumente treba proveriti:

- [ ] `id` postoji
- [ ] `type: course_plan`
- [ ] `academic_year: 2025/2026`
- [ ] `implementation_context` postoji
- [ ] `related_accreditation` postoji
- [ ] `source_file` postoji
- [ ] `source_status: aktuelni_plan_rada_2025_2026`
- [ ] `related_intents` postoji
- [ ] `keywords` postoji

Za basket dokumente treba proveriti:

- [ ] `type: thematic_basket` ili odgovarajući tip
- [ ] `basket_type: tematska`, ako je tematska korpa
- [ ] `basket_purpose: preporuka_po_interesovanju`, ako je preporuka
- [ ] `formal_basket: false`, ako nije formalna kurikulumska korpa
- [ ] `source_file` postoji
- [ ] `related_intents` postoji
- [ ] `related_courses_core` postoji kada je relevantno
- [ ] `related_courses_elective` postoji kada je relevantno
- [ ] `keywords` postoji

Za policy i retrieval dokumente treba proveriti:

- [ ] `type` jasno označava dokument
- [ ] `project: PIT Navigator`
- [ ] `related_intents` postoji
- [ ] `keywords` postoji
- [ ] dokument ne glumi course ili basket dokument

## 5. Provera Markdown formata

Checklist:

- [ ] Dokument počinje frontmatter-om
- [ ] Nema spoljašnjih copy-paste oznaka kao inline ili blok oznaka za Markdown eksport
- [ ] Svi Markdown code block-ovi su zatvoreni
- [ ] Naslovi koriste pravilne oznake `#`, `##`, `###`
- [ ] Nema sekcija tipa `8. Naslov` bez `##`
- [ ] Liste su pravilno formatirane sa `-` ili numeracijom
- [ ] Blockquote primeri koriste `>`
- [ ] Dokument nema slučajno ubačene komentare iz razgovora
- [ ] Dokument nema nezatvorene navodnike, YAML blokove ili code block-ove
- [ ] Dokument se završava smislenom napomenom, izvorima ili zaključkom

## 6. Provera naziva predmeta

Nazivi predmeta moraju biti konzistentni.

Tačni nazivi koji se koriste:

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
Veb dizajn
Elektronsko poslovanje
Elektronska trgovina
Elektronski platni sistemi
Nove informacione tehnologije
Računovodstveni informacioni sistemi
Analiza finansijskih izveštaja
Upravljačko računovodstvo
Finansijska ekonomija
Ekonometrija
Kvantitativne finansije
Ekonomska statistika
```

Checklist:

- [ ] Ne koristi se “web dizajn” ako je u dokumentima standardizovano “Veb dizajn”
- [ ] Ne koristi se skraćeni naziv ako može zvanični naziv
- [ ] Ako korisnik koristi skraćenicu, odgovor koristi zvanični naziv
- [ ] `Elektronsko poslovanje` i `Elektronsko poslovanje i veštačka inteligencija` se ne mešaju
- [ ] `Poslovna inteligencija` i `Poslovna analitika` se ne mešaju
- [ ] `Mašinsko učenje` i `Elektronsko poslovanje i veštačka inteligencija` se ne predstavljaju kao isti predmet
- [ ] `ERP softver` i `Razvoj softvera` se ne predstavljaju kao isti predmet
- [ ] `Objektno orijentisano programiranje` i `Razvoj softvera` se ne predstavljaju kao isti predmet

## 7. Provera obaveznih i izbornih predmeta

Bot mora jasno da razlikuje obavezne i izborne predmete.

Checklist:

- [ ] Svaki course dokument ima jasno naznačen status predmeta
- [ ] Izborni predmeti nisu predstavljeni kao obavezni
- [ ] Obavezni predmeti nisu predstavljeni kao izborni
- [ ] Kod tematskih korpi jasno stoji da one nisu formalne korpe
- [ ] Kod izbornih predmeta stoji da zavise od izborne pozicije i pravila izbora
- [ ] Kod Mašinskog učenja stoji da je izborni predmet
- [ ] Kod Operacionih istraživanja stoji da je izborni predmet
- [ ] Kod Elektronske trgovine, Elektronskih platnih sistema i Novih informacionih tehnologija stoji da su izborni predmeti
- [ ] Bot ne sme da kaže da svi studenti slušaju izborni predmet

Ispravna formulacija:

> Obavezni predmeti daju osnovu, a izborni predmeti pojačavaju pravac.

Pogrešna formulacija:

> Svi studenti PIT-a slušaju Mašinsko učenje.

## 8. Provera PIT 2027 i PIN 2020 formulacija

PIT 2027 treba predstaviti kao formalnu modernizaciju.

PIN 2020 ne sme biti predstavljen kao zastareo.

Checklist:

- [ ] Nigde ne piše da je PIN 2020 loš
- [ ] Nigde ne piše da je PIN 2020 zastareo
- [ ] Nigde ne piše da je PIN 2020 manje vredan
- [ ] Nigde ne piše da PIT 2027 automatski znači da PIN 2020 nije relevantan
- [ ] Nigde ne piše da je PIT 2027 objektivno bolji za svakog studenta
- [ ] Modernizacija je predstavljena kao formalno strukturisanje, ne kao prekid
- [ ] Aktuelni planovi rada 2025/26 se koriste kao dokaz da se PIN 2020 osavremenjuje u izvođenju
- [ ] Comparison dokument koristi zaštitne formulacije

Ispravna formulacija:

> PIT 2027 formalno modernizuje i jasnije strukturira poslovno-informatički profil. To ne znači da je PIN 2020 zastareo, jer se aktuelno izvođenje predmeta osavremenjuje kroz planove rada, alate, primere i praktičnu nastavu.

Pogrešna formulacija:

> PIN 2020 je zastareo i PIT 2027 ga zamenjuje jer je bolji.

## 9. Provera akreditacionog opisa i aktuelnog plana rada

Akreditacioni course dokument i aktuelni plan rada nisu isto.

Checklist:

- [ ] `01_courses/2027/` se koristi za formalni opis PIT 2027
- [ ] `03_course_plans/2025_2026/` se koristi za aktuelno izvođenje
- [ ] Ako korisnik pita “kako se sada radi”, koristi se course_plan
- [ ] Ako korisnik pita “šta piše u PIT 2027”, koristi se course dokument
- [ ] Ako postoje razlike, jasno se kaže šta je formalni okvir, a šta aktuelno izvođenje
- [ ] Radni predlozi se ne predstavljaju kao aktuelni plan rada
- [ ] Za Razvoj softvera se ne tvrdi da se trenutno radi Flask ako aktuelni plan navodi PHP
- [ ] Za ERP se mogu pomenuti MongoDB, Python, Tkinter i Big Data samo kada se koristi aktuelni plan koji to potvrđuje

Ispravna formulacija:

> U aktuelnom planu rada 2025/26 naveden je PHP. Python/Flask i AI-assisted development mogu biti budući fokus samo ako budu potvrđeni novim planom rada.

Pogrešna formulacija:

> Na Razvoju softvera se trenutno radi Flask.

## 10. Provera radnih predloga

Radni predlozi nisu zvanični dokumenti.

Checklist:

- [ ] Radni predlog je jasno označen kao radni predlog
- [ ] Radni predlog se ne predstavlja kao aktuelni plan rada
- [ ] Radni predlog se ne predstavlja kao akreditacioni dokument
- [ ] Ako se pominje Python/Flask u Razvoju softvera, jasno je da je to mogući budući fokus
- [ ] Ako se pominje AI-assisted development, jasno je da nije zvaničan deo plana dok se ne potvrdi
- [ ] Nema formulacija koje radni predlog predstavljaju kao obavezu

Ispravna formulacija:

> Postoji radni predlog da se predmet u budućnosti više usmeri ka Python/Flask-u i AI-assisted development-u, ali to ne treba predstavljati kao aktuelni plan rada dok ne bude potvrđeno zvaničnim planom.

## 11. Provera nastavnika i saradnika

Knowledge base ne sme da komentariše nastavnike i saradnike.

Checklist:

- [ ] Nigde se ne ocenjuju nastavnici
- [ ] Nigde se ne ocenjuju saradnici
- [ ] Nigde ne piše da je profesor dobar ili loš
- [ ] Nigde ne piše da predmet treba birati zbog nastavnika
- [ ] Nigde ne piše da predmet treba izbegavati zbog nastavnika
- [ ] Nigde se ne koriste lična imena nastavnika i saradnika u preporukama
- [ ] Ako su imena prisutna u izvorima, ne koriste se u korisničkim odgovorima osim ako je formalno nužno
- [ ] Za aktuelne informacije o nastavnicima korisnik se upućuje na zvanični raspored, silabus ili stranicu fakulteta

Ispravna formulacija:

> Za aktuelne informacije o nastavnicima i saradnicima najbolje je proveriti zvaničnu stranicu fakulteta, raspored nastave ili zvanični silabus. PIT Navigator ne ocenjuje nastavnike i ne daje preporuke na osnovu toga ko drži predmet.

## 12. Provera karijernih preporuka

Bot sme da povezuje predmete sa karijernim putanjama, ali ne sme da obećava posao.

Checklist:

- [ ] Nigde se ne obećava posao
- [ ] Nigde se ne obećava plata
- [ ] Nigde se ne kaže da je jedan predmet dovoljan za karijeru
- [ ] Nigde se ne kaže da smer sam garantuje zaposlenje
- [ ] Karijere su predstavljene kao putanje, ne kao garantovani ishodi
- [ ] U odgovorima se pominje dodatni rad, projekti, praksa, portfolio i alati kada je relevantno
- [ ] AI se predstavlja realno, bez panike i bez lažne sigurnosti

Ispravna formulacija:

> Ovi predmeti ne garantuju posao, ali razvijaju korisnu osnovu za tu putanju.

Pogrešna formulacija:

> Ako izabereš ove predmete, sigurno ćeš naći posao.

## 13. Provera tržišta rada i AI

Odgovori o AI i tržištu rada moraju biti realistični.

Checklist:

- [ ] Bot ne kaže da AI neće uticati na poslove
- [ ] Bot ne kaže da će AI potpuno uništiti smer
- [ ] Bot ne kaže da je smer siguran bez dodatnog rada
- [ ] Bot ne kaže da je smer beskoristan zbog AI-ja
- [ ] Bot ističe kombinaciju poslovanja, podataka, alata, procesa i AI-ja
- [ ] Bot naglašava važnost praktičnog rada i projekata
- [ ] Bot izbegava marketinški prazan ton

Ispravna formulacija:

> AI će promeniti deo poslova, posebno rutinske zadatke. Međutim, PIT profil može ostati relevantan ako student kombinuje poslovno razumevanje, podatke, procese, softver, ERP, BI i sposobnost da koristi AI alate kao podršku u radu.

## 14. Provera izbornih preporuka

Preporuke iz korpi su praktične, ali nisu formalno rangiranje.

Checklist:

- [ ] Preporuke su označene kao preporuke po interesovanju
- [ ] Nigde ne piše da postoji zvanično rangiranje ako ne postoji
- [ ] Nigde se ne omalovažava predmet koji nije prioritetan
- [ ] Nove informacione tehnologije se ne nazivaju lošim predmetom
- [ ] Finansijska i aktuarska matematika se ne naziva lošim predmetom
- [ ] Istraživanje tržišta se ne naziva lošim predmetom
- [ ] Ekonomska statistika se ne naziva lošim predmetom
- [ ] Preporuke su povezane sa interesovanjem korisnika
- [ ] Bot kaže da izbor zavisi od izborne pozicije i pravila izbora

Ispravna formulacija:

> Nove informacione tehnologije mogu biti korisne za širi pregled trendova. Ako student želi konkretniju vezu sa e-commerce-om, fintech-om, softverom, ERP-om ili analitikom, često su direktniji izbori Elektronska trgovina, Elektronski platni sistemi, ERP softver, Razvoj softvera, Mašinsko učenje ili Operaciona istraživanja.

Pogrešna formulacija:

> Nove informacione tehnologije su loš predmet.

## 15. Provera predmeta bez posebnog course dokumenta

Za neke izborne predmete postoji samo kratka referenca.

Checklist:

- [ ] Za takve predmete se koristi `pit_minor_electives_reference.md`
- [ ] Bot ne izmišlja detaljan sadržaj
- [ ] Bot ne izmišlja ocenjivanje
- [ ] Bot ne izmišlja alate
- [ ] Bot ne izmišlja nedeljni plan
- [ ] Bot ne izmišlja nastavnike
- [ ] Bot ne tvrdi da zna aktuelno izvođenje ako nema plan rada
- [ ] Bot daje samo širi kontekst i preporuku po interesovanju
- [ ] Bot upućuje na zvanični silabus ili plan rada za detalje

Fallback formulacija:

> Za taj predmet trenutno nemam poseban course dokument u bazi znanja. Mogu da ga smestim u širi PIT 2027 kontekst i objasnim za koje interesovanje je koristan, ali za detaljan sadržaj, ocenjivanje i aktuelno izvođenje treba proveriti zvanični silabus ili plan rada.

## 16. Provera prakse, završnog rada i seminarskih radova

Za ovu verziju PIT Navigatora ne pravimo posebne dokumente za:

- praksu
- završni rad
- seminarske radove
- letnju školu

Checklist:

- [ ] Ne postoje posebni course dokumenti za praksu
- [ ] Ne postoje posebni course dokumenti za završni rad
- [ ] Ne postoje posebni course dokumenti za seminarske radove
- [ ] Korpe ne obrađuju praksu kao poseban predmet
- [ ] Ako korisnik pita za praksu ili završni rad, bot daje samo opštu informaciju ako je potvrđena kurikulumom
- [ ] Za procedure, rokove i pravila korisnik se upućuje na zvanična fakultetska uputstva

Ispravna formulacija:

> Praksa i završni rad postoje u strukturi studija, ali PIT Navigator ih trenutno ne obrađuje kao posebne knowledge base dokumente. Za tačne procedure, rokove i pravila treba proveriti zvanična fakultetska uputstva.

## 17. Provera izvora

Svaki dokument treba da ima izvor ili povezane dokumente.

Checklist:

- [ ] Dokument ima `source_file` u frontmatter-u kada postoji primarni izvor
- [ ] Dokument ima `source_status`
- [ ] Dokument ima sekciju `Izvori` ili `Izvori i povezani dokumenti`
- [ ] Ako je dokument interpretativni, navodi dokumente na koje se oslanja
- [ ] Ako je dokument course_plan, navodi konkretan aktuelni plan rada
- [ ] Ako je dokument course, navodi knjigu predmeta ili nastavni plan
- [ ] Ako je dokument basket, navodi kurikulum i relevantne course dokumente
- [ ] Ako je dokument policy/retrieval, navodi povezane sistemske dokumente
- [ ] Ne postoji tvrdnja bez jasnog izvora kada je faktualno specifična

## 18. Provera retrieval dokumenata

Retrieval dokumenti moraju jasno mapirati intent na dokumente.

Checklist:

- [ ] `pit_navigator_retrieval_map.md` postoji
- [ ] `pit_navigator_intent_examples.md` postoji
- [ ] PROGRAM_OVERVIEW mapira na overview dokumente
- [ ] ACCREDITATION_COMPARISON mapira na comparison dokument
- [ ] COURSE_EXPLANATION mapira na `01_courses/2027/`
- [ ] COURSE_PLAN_CURRENT mapira na `03_course_plans/2025_2026/`
- [ ] ELECTIVE_RECOMMENDATION mapira na `04_baskets/2027/`
- [ ] CAREER_RECOMMENDATION mapira na tematske korpe
- [ ] FALLBACK mapira na policy, retrieval i overview dokumente
- [ ] Postoje primeri mešovitih pitanja
- [ ] Retrieval dokumenti ne sadrže detaljne lažne course opise

## 19. Provera policy dokumenata

Policy dokumenti moraju pokrivati glavne rizike.

Checklist:

- [ ] `pit_navigator_answering_policy.md` postoji
- [ ] Policy pokriva zabranu komentarisanja nastavnika
- [ ] Policy pokriva zabranu obećavanja posla
- [ ] Policy pokriva zabranu izmišljanja
- [ ] Policy pokriva izborni vs obavezni status
- [ ] Policy pokriva PIT 2027 vs PIN 2020
- [ ] Policy pokriva aktuelni plan rada vs akreditacioni opis
- [ ] Policy pokriva radne predloge
- [ ] Policy pokriva praksu, završni rad i seminarske radove
- [ ] Policy sadrži minimalni fallback odgovor
- [ ] Policy sadrži pravila tona

## 20. Provera indeks dokumenta

Indeks treba da jasno pokazuje šta postoji.

Checklist:

- [ ] `knowledge_base_index.md` postoji
- [ ] Navodi sve glavne foldere
- [ ] Navodi overview dokumente
- [ ] Navodi course dokumente 2027
- [ ] Navodi course_plan dokumente 2025/26
- [ ] Navodi basket dokumente
- [ ] Navodi retrieval dokumente
- [ ] Navodi policy dokumente
- [ ] Navodi šta ne pravimo kao posebne dokumente
- [ ] Navodi predmete bez posebnog course dokumenta
- [ ] Navodi primarne dokumente po tipu pitanja

## 21. Završna ručna provera pre RAG-a

Pre uključivanja u RAG, proći kroz sledeću listu:

- [ ] Otvoriti svaki `.md` fajl i proveriti da počinje frontmatter-om
- [ ] Proveriti da nema spoljašnjih copy-paste oznaka
- [ ] Proveriti da nema nezatvorenih code block-ova
- [ ] Proveriti da nema ličnih komentara iz izrade dokumenta
- [ ] Proveriti da nema imena nastavnika u preporukama
- [ ] Proveriti da nema tvrdnji “predmet je lak/težak”
- [ ] Proveriti da nema tvrdnji “predmet garantuje posao”
- [ ] Proveriti da nema tvrdnji “PIN je zastareo”
- [ ] Proveriti da nema tvrdnji “PIT je objektivno bolji za sve”
- [ ] Proveriti da nema tvrdnji “svi studenti slušaju izborni predmet”
- [ ] Proveriti da su izvori navedeni
- [ ] Proveriti da su obavezni i izborni predmeti jasno razdvojeni
- [ ] Proveriti da su aktuelni planovi rada odvojeni od 2027 course dokumenata
- [ ] Proveriti da su minor electives pokriveni bez izmišljanja detalja

## 22. Minimalni QA status dokumenta

Svaki dokument može dobiti jedan od tri statusa:

```text
QA_STATUS: ready
QA_STATUS: needs_review
QA_STATUS: incomplete
```

Kriterijumi:

### QA_STATUS: ready

Dokument je spreman ako:

- ima frontmatter
- ima jasan izvor
- nema rizične formulacije
- ne meša izvore
- ima zatvorene Markdown blokove
- ima jasnu svrhu
- ima odgovarajuće zaštitne formulacije

### QA_STATUS: needs_review

Dokument treba pregled ako:

- ima sitne nejasnoće
- ima moguće dupliranje
- ima formulacije koje mogu biti preciznije
- nije sasvim jasno da li je nešto obavezno ili izborno
- nije sasvim jasno da li se odnosi na 2027 ili 2025/26

### QA_STATUS: incomplete

Dokument nije spreman ako:

- nema frontmatter
- nema izvor
- ima nezatvoren code block
- meša aktuelni plan rada i akreditacioni opis
- izmišlja detalje
- komentariše nastavnike
- tvrdi da izborni predmet slušaju svi
- tvrdi da predmet garantuje posao
- tvrdi da je PIN 2020 zastareo

## 23. Izvori i povezani dokumenti

Ovaj QA checklist je povezan sa:

```text
00_overview/knowledge_base_index.md

05_retrieval_guides/pit_navigator_retrieval_map.md
05_retrieval_guides/pit_navigator_intent_examples.md

06_policy/pit_navigator_answering_policy.md

04_baskets/2027/pit_izborne_korpe_overview.md
04_baskets/2027/pit_minor_electives_reference.md
```

Napomena: ovaj dokument je interna kontrolna lista za kvalitet knowledge base-a. Ne koristi se kao izvor za sadržaj o predmetima, već kao vodič za proveru da li su dokumenti spremni za korišćenje u PIT Navigator RAG sistemu.
