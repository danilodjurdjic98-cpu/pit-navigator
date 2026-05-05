# PIT Navigator, struktura baze znanja i inventar dokumenata

## 0. Odnos prema strukturi baze znanja

Ovaj dokument privremeno objedinjuje dve stvari:
1. osnovnu strukturu buduće baze znanja
2. inventar sirovih dokumenata koje trenutno imamo

Kasnije, ako projekat poraste, ovaj dokument se može razdvojiti na:
- `05_knowledge_base_structure.md`
- `06_document_inventory.md`

Za prvu verziju PIT Navigatora dovoljno je da ostane jedan objedinjeni dokument.

---

## 1. Svrha dokumenta

Ovaj dokument evidentira sve sirove izvore koje koristimo za izradu baze znanja PIT Navigatora.

Cilj je da uvek znamo:

- koji dokument imamo
- gde se čuva
- koju akreditaciju pokriva
- šta iz njega koristimo
- da li je dovoljan za prvu verziju
- šta kasnije treba očistiti u `.md` dokumente

---

## 2. Trenutna struktura sirovih dokumenata

```text
pit-navigator/
  01_raw_documents/
    akreditacija_2020/
      knjiga_predmeta_pin_2020.pdf
      nastavni_plan_pin_2020.pdf

    akreditacija_2027/
      knjiga_predmeta_pit_2027.pdf
      nastavni_plan_pit_2027.pdf
```

---

## 3. Dokumenti za akreditaciju 2020, PIN

### 3.1 `nastavni_plan_pin_2020.pdf`

Putanja:

01_raw_documents/akreditacija_2020/nastavni_plan_pin_2020.pdf

Šta dokument pokriva:

stari naziv modula / smera, Poslovna informatika, PIN
raspored predmeta po godinama i semestrima
ESPB bodove
fond časova
obavezne predmete
izborne blokove
pravila izbora u izbornim blokovima, ako su navedena

Za šta ga koristimo:

pregled strukture stare akreditacije
poređenje PIN 2020 i PIT 2027
identifikaciju predmeta koje treba očistiti u bazi znanja
identifikaciju izbornih blokova stare akreditacije

Status:

Dovoljan za prvu verziju kao izvor strukture PIN 2020.

### 3.2 `knjiga_predmeta_pin_2020.pdf`

Putanja:

01_raw_documents/akreditacija_2020/knjiga_predmeta_pin_2020.pdf

Šta dokument pokriva:

opise predmeta stare akreditacije
ciljeve predmeta
ishode učenja
sadržaj predmeta
metode izvođenja nastave
literaturu
način ocenjivanja

Za šta ga koristimo:

izradu očišćenih .md dokumenata za predmete iz akreditacije 2020
izvlačenje veština po predmetima
povezivanje predmeta sa karijernim putanjama
poređenje starih i novih predmeta

**Prioritetni predmeti za čišćenje:**

**Obavezni predmeti modula PIN 2020:**

- Diskretna matematika
- Analiza podataka
- Veb dizajn
- Baze podataka
- Objektno orijentisano programiranje
- Informacioni sistemi i poslovna analitika
- Elektronsko poslovanje
- Razvoj softvera
- Menadžment projekata
- ERP softver
- Stručna praksa

**Karakteristični izborni predmeti PIN 2020:**

- Nove informacione tehnologije
- Elektronska trgovina
- Elektronski platni sistemi
- Digitalni marketing
- Mašinsko učenje
- Primenjena napredna analitika
- Ekonometrija
- Operaciona istraživanja
- Računovodstveni informacioni sistemi
- Kvantitativne finansije
- Istraživanje tržišta

Napomena: izborni predmeti iz šire ekonomije, finansija, računovodstva, marketinga ili kvantitativnih oblasti ulaze u bazu znanja ako su dostupni studentima PIN modula kroz izborne blokove, ali imaju niži prioritet za opšte preporuke.

Status:

Dovoljan za prvu verziju kao izvor sadržaja predmeta PIN 2020.

**Napomena za obradu predmeta iz akreditacije 2020:**

Knjiga predmeta PIN 2020 koristi se kao osnovni akreditacioni izvor, ali za izradu pojedinačnih dokumenata o predmetima iz akreditacije 2020 treba, kad god je moguće, koristiti i trenutne planove rada predmeta.

Razlog je što su sadržaji, alati, primeri, literatura i način izvođenja nastave mogli biti osavremenjeni nakon akreditacije.

**Pravilo za obradu:**

- za strukturu predmeta, status, semestar i ESPB koristi se akreditacioni dokument
- za aktuelni sadržaj, alate, literaturu i praktične aktivnosti traže se trenutni planovi rada
- ako trenutni plan rada nije dostupan, koristi se knjiga predmeta uz napomenu da je izvor akreditacioni dokument

## 4. Dokumenti za akreditaciju 2027, PIT

### 4.1 `nastavni_plan_pit_2027.pdf`

Putanja:

01_raw_documents/akreditacija_2027/nastavni_plan_pit_2027.pdf

Šta dokument pokriva:

novi naziv modula / smera, Poslovne informacione tehnologije, PIT
raspored predmeta po godinama i semestrima
ESPB bodove
fond časova
obavezne predmete
izborne blokove PIT
pravila izbora u izbornim blokovima, ako su navedena

Za šta ga koristimo:

pregled strukture nove akreditacije
poređenje PIN 2020 i PIT 2027
identifikaciju novih i izmenjenih predmeta
identifikaciju izbornih blokova PIT 2027

Status:

Dovoljan za prvu verziju kao izvor strukture PIT 2027.

### 4.2 `knjiga_predmeta_pit_2027.pdf`

Putanja:

01_raw_documents/akreditacija_2027/knjiga_predmeta_pit_2027.pdf

Šta dokument pokriva:

opise predmeta nove akreditacije
ciljeve predmeta
ishode učenja
sadržaj predmeta
metode izvođenja nastave
literaturu
način ocenjivanja

Za šta ga koristimo:

izradu očišćenih .md dokumenata za predmete iz akreditacije 2027
izvlačenje veština po predmetima
povezivanje predmeta sa karijernim putanjama
promociju modernizovanog PIT profila
poređenje starih i novih predmeta

**Prioritetni predmeti za čišćenje:**

**Obavezni predmeti modula PIT 2027:**

- Baze podataka
- Poslovna analitika
- Diskretna matematika
- Korisničko iskustvo i dizajn
- Analiza podataka
- Objektno orijentisano programiranje
- Razvoj softvera
- Poslovna inteligencija
- Menadžment projekata
- Stručna praksa
- Elektronsko poslovanje i veštačka inteligencija
- ERP softver

**Karakteristični izborni predmeti PIT 2027:**

- Teorija verovatnoće
- Linearna algebra
- Menadžment odnosa sa kupcima
- Računovodstveni informacioni sistemi
- Analiza finansijskih izveštaja
- Upravljačko računovodstvo
- Osnovi poslovnih finansija
- Istraživanje tržišta
- Operaciona istraživanja
- Mašinsko učenje
- Ekonometrija
- Kvantitativne finansije
- Ekonomska statistika
- Elektronska trgovina
- Nove informacione tehnologije
- Elektronski platni sistemi

Napomena: obavezni predmeti PIT 2027 imaju najviši prioritet za prvu verziju baze znanja. Izborni predmeti se uključuju zato što ih studenti realno mogu birati, ali se u recommendation matrix-u rangiraju prema vezi sa karijernom putanjom.

Status:

Dovoljan za prvu verziju kao izvor sadržaja predmeta PIT 2027.

## 5. Radni izvod iz nastavnih planova

Iz nastavnih planova za PIN 2020 i PIT 2027 izdvojeni su obavezni predmeti, izborni blokovi i glavne promene između stare i nove akreditacije.

Detaljni spiskovi predmeta po semestrima neće se čuvati u ovom dokumentu, već će biti obrađeni u očišćenim dokumentima baze znanja:

```text
02_knowledge_base/
  00_overview/
    pin_2020_overview.md
    pit_2027_overview.md
    pin_2020_vs_pit_2027.md
```

---

### 5.1 Ključne promene PIN 2020 → PIT 2027

Radni zaključci iz nastavnih planova:

- stari modul se vodi kao PIN, odnosno Poslovna informatika
- novi modul se vodi kao PIT, odnosno Poslovne informacione tehnologije
- PIT 2027 uvodi predmet Poslovna analitika kao poseban obavezan predmet
- PIT 2027 uvodi predmet Korisničko iskustvo i dizajn, koji širi raniji fokus Veb dizajna ka UX-u, korisničkom putu i digitalnim interfejsima
- PIT 2027 uvodi predmet Poslovna inteligencija kao poseban obavezan predmet
- Elektronsko poslovanje iz PIN 2020 menja se u Elektronsko poslovanje i veštačka inteligencija u PIT 2027
- izborne opcije su u PIT 2027 organizovane granularnije, kroz sedam izbornih blokova PIT
- Analiza podataka ostaje važan predmet, ali se u PIT 2027 pomera u 6. semestar i nosi 7 ESPB
- PIT 2027 jače naglašava poslovnu analitiku, BI, UX, AI, ERP, baze podataka i razvoj softvera

### 5.2 Pravilo za izborne predmete iz drugih oblasti

Neki izborni blokovi uključuju predmete koji nisu strogo poslovno-informatički, ali su dostupni studentima PIN/PIT modula.

Takvi predmeti treba da uđu u bazu znanja ako su deo izbornih blokova u nastavnom planu.

Razlog:

- student ih realno može birati
- mogu biti relevantni za specifična interesovanja
- bot treba da objasni opcije koje su studentu dostupne
- recommendation matrix može dati niži prioritet predmetima koji su manje povezani sa glavnim PIT karijernim putanjama

Pravilo:

- obavezni PIT/PIN predmeti imaju najviši prioritet za čišćenje
- izborni predmeti iz direktno povezanih oblasti, kao što su BI, ERP, AI, podaci, softver i elektronsko poslovanje, imaju srednji do visok prioritet
- izborni predmeti iz šire ekonomije, finansija, računovodstva, marketinga ili turizma ulaze u bazu, ali sa nižim prioritetom za preporuke, osim ako korisnik pita baš za tu oblast

Primer:

Ako korisnik pita za BI analitiku, bot prvo koristi Baze podataka, Poslovnu analitiku, Analizu podataka, Poslovnu inteligenciju i ERP softver.

Ako korisnik pita za finansijsku analitiku, bot može pomenuti predmete kao što su Analiza finansijskih izveštaja, Osnovi poslovnih finansija, Ekonometrija ili Kvantitativne finansije, ako su dostupni u izbornim blokovima.

## 6. Zaključak

Za prvu verziju PIT Navigatora trenutno imamo dovoljno sirovih izvora za:

- staru akreditaciju 2020, PIN
- novu akreditaciju 2027, PIT
- strukturu predmeta
- izborne blokove
- opise predmeta
- poređenje starog i novog programa
- početno mapiranje predmeta prema karijernim putanjama

Trenutno ne treba tražiti nove PDF dokumente za akreditacije.

Sledeći korak je izrada strukture za očišćenu bazu znanja u folderu:

```text
02_knowledge_base/
```

Prvo treba napraviti preglede:

```text
02_knowledge_base/
  00_overview/
    pin_2020_overview.md
    pit_2027_overview.md
    pin_2020_vs_pit_2027.md
```
