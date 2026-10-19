# Instrukcije za izradu vežbi iz Razvoja softvera 2026/27

## Svrha i granice

Za stil objašnjavanja i njegovo povezivanje sa ovim instrukcijama koristiti [Sačuvan stil prezentacija i vežbi](STIL_PREZENTACIJA_I_VEZBI.md), zasnovan na materijalima iz 2025. Ovaj dokument ostaje merodavan za metodiku i obim nastave.

Ovaj dokument određuje kako pripremati vežbe i prateće materijale. Važeći predlog rasporeda tema ostaje neizmenjen. Instrukcije nisu novi plan nastave i ne daju osnov za samostalno pomeranje ili dodavanje tema.

Prve nedelje nema vežbi. Šest dogovorenih početnih tema obuhvata analizu procesa, modelovanje i Git/GitHub. Programerski deo vežbi usmeren je na Flask, Jinja2, forme i SQLAlchemy. MongoDB se ne obrađuje na vežbama.

## Način rada na času

Vežbe se pripremaju prema 4C/ID pristupu, uz što manje frontalnog izlaganja i dovoljno vremena da studenti sami rešavaju zadatke uz materijale i pomoć nastavnika.

Okvirno se može planirati pola raspoloživog vremena za objašnjenje i demonstraciju, a pola za studentski rad. To nije obavezna podela: uvodni deo treba skratiti kad god je moguće i preostalo vreme prepustiti studentima. Objašnjenja mogu biti raspoređena u kratke celine tokom rada, umesto jednog dugog predavanja na početku.

Ako termin traje 90 minuta, polazni okvir je:

- 5 minuta: poslovni problem, očekivani rezultat i kratko povezivanje sa prethodnim vežbama.
- 20–25 minuta: objašnjenje pristupa i demonstracija ključnog dela rešenja.
- 45–50 minuta: studentski rad uz materijale, obilazak i kratka objašnjenja po potrebi.
- 10 minuta: provera rezultata, analiza tipičnih grešaka i kratak osvrt.

Vremena su smernice. Zadatak mora biti realno rešiv u vremenu namenjenom studentskom radu. Ne planirati puno gradivo za ceo termin, pa vežbanje ostaviti samo ako preostane vremena.

## Primena četiri komponente 4C/ID

### 1. Celoviti zadaci za učenje

Svake vežbe imaju razumljiv poslovni problem i vidljiv rezultat. Zadatke organizovati od jednostavnijih ka složenijim, uz povezivanje znanja i veština.

U programerskom delu celovit zadatak može biti prikaz dostupnih knjiga: zahtev korisnika, Flask ruta, priprema podataka i prikaz kroz Jinja2. Celovit zadatak ne znači da studenti svaki put pišu celu aplikaciju od nule. Delovi koje još nisu učili mogu biti pripremljeni u početnom projektu.

U delu modelovanja koristiti opis poslovnog sistema i tražiti odgovarajući model uz obrazloženje odluka. Na Git vežbama rezultat je smislen postupak čuvanja i objavljivanja promene projekta.

Za zadatke slične složenosti postepeno smanjivati pomoć: objašnjen primer, dopunjavanje delimičnog rešenja, zatim samostalna varijanta. Kada se uvede nova klasa složenijih zadataka, ponovo obezbediti potrebnu podršku.

### 2. Podržavajuće informacije

Pripremiti kratka objašnjenja koja pomažu studentima da razumeju problem i izaberu postupak rešavanja:

- kako su delovi sistema povezani;
- kojim redosledom analizirati zahtev;
- zašto se koristi određeni model ili rešenje;
- kako proveriti da li rezultat odgovara poslovnom zahtevu.

Za Flask, na primer, prikazati tok zahtev → ruta → obrada podataka → šablon → odgovor. Ovi materijali treba da budu dostupni tokom rada, uz ponovno korišćenje na narednim vežbama.

### 3. Proceduralne informacije

Obezbediti kratka uputstva dostupna baš kada studentu zatrebaju: pokretanje aplikacije, struktura rute, sintaksa Jinja petlje, čitanje polja forme ili čuvanje promene u bazi.

Koristiti sažete kartice, male primere i uputstva za česte greške. Ne zatrpavati početak časa svim naredbama. Kako studenti ovladavaju postupkom, smanjivati detaljnost koraka i upućivati ih na sažet podsetnik.

### 4. Vežbanje pojedinačnih postupaka

Kratke dodatne zadatke koristiti kada je potrebno učvrstiti ponavljajuću radnju, na primer pisanje uslova, Jinja petlje, pretvaranje unosa u broj ili jednostavan filter upita.

Takva vežba dolazi nakon upoznavanja postupka u celovitom zadatku. Ne mora biti zaseban blok na svakom času i ne treba da potisne rad na poslovnom problemu.

## Paket materijala za svake vežbe

Pripremiti sledeće povezane delove, u obimu koji odgovara temi:

1. **Vodič za nastavnika:** cilj, predznanje, raspodela vremena, ključna demonstracija, očekivane teškoće i kriterijumi uspeha.
2. **Studentski zadatak:** scenario, početno stanje, konkretni zahtevi i očekivani rezultat. Jasno razdvojiti obavezni zadatak i opciono proširenje.
3. **Kratko konceptualno objašnjenje:** ono što studenti moraju razumeti da bi donosili odluke, uz shemu ili primer kada pomažu.
4. **Proceduralni podsetnik:** najpotrebnija sintaksa, komande i koraci za te vežbe.
5. **Početni materijal:** opis sistema, delimičan model ili pripremljen projekat i podaci, zavisno od teme.
6. **Postepeni nagoveštaji:** prvo pitanje koje usmerava razmišljanje, zatim konkretniji trag, pa delimičan primer ako je potreban.
7. **Rešenje za nastavnika:** ispravno rešenje sa kratkim objašnjenjem ključnih odluka, odvojeno od početnog studentskog materijala.
8. **Provera rezultata:** nekoliko konkretnih test-slučajeva ili kriterijuma koje student može sam da primeni.

Nije potrebno praviti osam zasebnih datoteka. Kratke delove objediniti radi lakšeg korišćenja. Nazivi, putanje i način pokretanja moraju biti jasni i međusobno usklađeni.

## Oblikovanje studentskog rada

- Nastavnik pokazuje obrazac i objašnjava razmišljanje, a student rešava sličan, smisleno izmenjen problem.
- Studentski rad ne svoditi na prepisivanje prikazanog koda ili zamenu naziva promenljivih.
- Menjati podatke, poslovni uslov ili traženi prikaz kako bi student morao da primeni naučeno.
- Koristiti kontinuitet poznatog poslovnog sistema, uz povremene slične primere za proveru prenosa znanja.
- Osnovni zadatak mora biti dostižan prosečnom studentu uz pripremljenu podršku. Bržim studentima ponuditi kratko proširenje bez novih obaveznih tehnologija.
- Za svake vežbe obezbediti ispravno početno stanje, tako da nezavršen prethodni zadatak ne blokira nastavak rada.
- Kada student zastane, prvo koristiti pitanje ili nagoveštaj, a zatim konkretniju pomoć.
- Na kraju proveriti i rezultat i razumevanje: student treba da objasni tok podataka ili obrazloži odluku, ne samo da pokaže da aplikacija radi.

## Povezanost sa praktičnim ispitom

Referentni primer je „Knjižara”, u datoteci `../../planovi rada/Predlog ispita/ZADATAK.md`. Studenti na tom ispitu dobijaju modele, pripremljenu bazu i kostur Flask aplikacije.

Kroz zadatke, u okviru postojećeg rasporeda, ponavljati:

- GET rutu, filtriranje i sortiranje podataka;
- prosleđivanje podataka šablonu i Jinja prikaz tabele;
- HTML formu, padajuću listu, POST zahtev i čitanje unosa;
- proveru poslovnog uslova, poput raspoloživog stanja;
- ažuriranje postojećeg i kreiranje povezanog zapisa;
- čuvanje promena i preusmeravanje korisnika.

Posebno vežbati povezivanje koraka u jednu funkcionalnost. Ne učiti samo jedno rešenje napamet: koristiti slične zadatke sa drugačijim zahtevima.

Materijali služe kao podrška učenju. Pred kraj vežbanja uključiti kraći samostalan zadatak sa smanjenom podrškom, u skladu sa stvarno dogovorenim uslovima ispita. Ne pretpostavljati da su materijali sa vežbi dozvoljeni na ispitu.

## Provera pre korišćenja materijala

- Tema prati postojeći plan i ne uvodi nepotrebno novo gradivo.
- Veći deo aktivnosti traži rad studenta, a ne pasivno praćenje.
- Obavezni zadatak može da se završi u predviđenom vremenu uz dostupnu pomoć.
- Predznanje je jasno; nepoznati tehnički delovi su pripremljeni ili objašnjeni.
- Početni projekat se pokreće prema priloženom uputstvu, a rešenje zadovoljava zahteve.
- Primeri i test-podaci pokrivaju i uspešan slučaj i relevantan neuspešan slučaj.
- Nagoveštaji pomažu postepeno, bez trenutnog otkrivanja celog rešenja.
- Završna provera otkriva da li student razume postupak.

## Dogovor o models.py i povezivanju sa bazom

Ovaj dogovor dopunjuje 11. i 13. nedelju u datoteci `Plan vezbe.xlsx`, u koloni „Vežbe stvarno”. Ne menja redosled ostalih tema.

### 11. nedelja — prvi model i povezivanje

Na ovim vežbama studenti sami pišu jednostavan `models.py` i povezuju ga sa Flask aplikacijom, uz pripremljeno uputstvo. Redosled obrade:

1. Razdvojiti odgovornosti: `app.py`, `models.py` i folder `templates`.
2. Objasniti konfiguraciju adrese baze, kreiranje objekta `db` i povezivanje sa aplikacijom preko `db.init_app(app)`.
3. Napisati model `Knjiga`: naziv tabele, kolone, tipovi, primarni ključ i osnovna ograničenja.
4. Razlikovati definiciju modela u Python-u od stvarne tabele u bazi. Pokazati `db.create_all()` u aplikacionom kontekstu. Objasniti da ova naredba ne ažurira automatski strukturu već postojećih tabela.
5. Dodati zapis, sačuvati promenu i pročitati podatke.
6. Povezati ranije napravljenu formu sa upisom u bazu, a postojeći Jinja šablon sa prikazom pročitanih podataka.

Celovit studentski zadatak je prelazak postojeće aplikacije sa podataka u Python listi na bazu. Ne praviti ponovo forme i šablone od nule. Nastavnik kratko demonstrira obrazac, a studenti uz materijal samostalno pišu model i dovršavaju povezivanje i rad sa podacima.

Instalaciju i podešavanje servera baze pripremiti unapred. Termin ne trošiti na administraciju servera. Jednostavno filtriranje i sortiranje uključiti kao kratko proširenje ako ostane vremena; ako osnovni deo potraje, razraditi ih u 14. nedelji.

Očekivani rezultat: student može da objasni vezu model–tabela–zapis i samostalno izvede tok forma → upis u bazu → čitanje → Jinja prikaz.

### 13. nedelja — proširenje modela i relacije

Proširiti `models.py` dodatnim modelima, stranim ključevima i vezom jedan–više. Povezati ih sa izborom zapisa u formi i prikazom povezanih podataka kroz Jinja2. Nadovezati se na model i aplikaciju iz prethodnih vežbi.

## Metodološki izvor

Četiri komponente, celoviti zadaci i postepeno smanjivanje podrške zasnovani su na [zvaničnom opisu 4C/ID modela](https://www.4cid.org/about/) i [sažetom prikazu modela](https://www.4cid.org/wp-content/uploads/2022/06/placemat_graphic_v2022.pdf). Raspodela vremena i organizacija materijala u ovom dokumentu predstavljaju primenu modela za ove vežbe, a ne propisanu minutažu 4C/ID pristupa.


