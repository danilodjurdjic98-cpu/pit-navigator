from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.config import load_settings  # noqa: E402
from src.generator import generate_answer  # noqa: E402
from src.intent_classifier import classify  # noqa: E402
from src.prompt_builder import build_messages, collect_source_paths  # noqa: E402
from src.retriever import Retriever  # noqa: E402


@dataclass(frozen=True)
class EvalQuestion:
    question: str
    expected: str
    must_include: tuple[str, ...] = ()
    nice_to_include: tuple[str, ...] = ()
    must_not_include: tuple[str, ...] = ()
    primary_source: str = "01_courses/2027/poslovna_informatika.md"


QUESTIONS: list[EvalQuestion] = [
    EvalQuestion("Šta je Poslovna informatika u PIT 2027?", "Treba da objasni da je formalni predmet koji povezuje poslovanje, IT, informacione sisteme, podatke i digitalno poslovanje.", ("PIT 2027", "poslovanje", "informacione"), ("SQL", "ERP", "Power BI")),
    EvalQuestion("Koja je uloga Poslovne informatike u novoj akreditaciji?", "Treba da istakne orijentacionu formalnu ulogu predmeta u PIT 2027 i vezu poslovanja sa informacionim tehnologijama.", ("PIT 2027", "informacione tehnologije"), ("poslovni informacioni sistemi",)),
    EvalQuestion("Da li Poslovna informatika povezuje poslovanje i IT?", "Treba da odgovori potvrdno i objasni da predmet spaja poslovne aktivnosti i informacione tehnologije.", ("poslovanje", "IT"), ("informacioni sistemi",)),
    EvalQuestion("Koje oblasti pokriva Poslovna informatika?", "Treba da navede ključne oblasti: baze/SQL, programski alati, Power BI ako je deo koncepta, poslovni IS, e-poslovanje, ERP, cloud i big data.", ("SQL", "ERP"), ("Power BI", "cloud", "big data")),
    EvalQuestion("Koji je cilj predmeta Poslovna informatika?", "Treba da kaže da je cilj razumevanje kako IT i informacioni sistemi podržavaju poslovanje, procese, podatke i odluke.", ("cilj", "poslovanje"), ("podacima", "odluka")),
    EvalQuestion("Koje ishode učenja student treba da stekne na Poslovnoj informatici?", "Treba da sažme ishode: razumevanje IT-a u poslovanju, IS, SQL/baze, programskih alata, ERP-a i digitalnog poslovanja.", ("ishod", "SQL"), ("ERP", "digitalno poslovanje")),
    EvalQuestion("Da li je Poslovna informatika više tehnički ili poslovni predmet?", "Treba da kaže da je predmet spoj poslovnog i tehničkog pogleda, ne čisto jedno ili drugo.", ("poslov", "tehn"), ("spaja", "povezuje")),
    EvalQuestion("Da li Poslovna informatika uvodi studente u informacione sisteme?", "Treba da potvrdi i objasni poslovne informacione sisteme i podršku procesima/odlukama.", ("informacioni sistemi", "poslov"), ("proces", "odluk")),
    EvalQuestion("Kako Poslovna informatika pomaže razumevanju poslovnih procesa?", "Treba da poveže informacione sisteme sa podrškom poslovnim procesima, informacijama i odlučivanjem.", ("proces", "informacioni sistemi"), ("odluka",)),
    EvalQuestion("Šta su poslovni informacioni sistemi u kontekstu ovog predmeta?", "Treba da objasni sisteme koji podržavaju procese, informacije i odluke u organizacijama.", ("poslovni informacioni sistemi", "proces"), ("odluka",)),
    EvalQuestion("Da li Poslovna informatika uključuje baze podataka?", "Treba da odgovori da uključuje osnove baza podataka, relacije, tipove podataka i SQL.", ("baze podataka", "SQL"), ("relacije",)),
    EvalQuestion("Zašto je SQL važan u Poslovnoj informatici?", "Treba da objasni da SQL omogućava rad sa poslovnim podacima i povezuje predmet sa bazama, BI, analitikom i ERP-om.", ("SQL", "podac"), ("BI", "ERP")),
    EvalQuestion("Da li se na Poslovnoj informatici uči SQL?", "Treba da kaže da formalni opis uključuje SQL, ali za aktuelno izvođenje treba proveriti plan rada 2025/26.", ("SQL",), ("2025/26", "plan rada")),
    EvalQuestion("Kakva je veza između Poslovne informatike i baza podataka?", "Treba da kaže da predmet daje osnovu za razumevanje baza i rada sa poslovnim podacima.", ("baze", "podac"), ("SQL",)),
    EvalQuestion("Da li Poslovna informatika priprema za predmete iz baza podataka?", "Treba da kaže da daje osnovu i orijentaciju, ali nije zamena za detaljan predmet Baze podataka.", ("osnov", "baze"), ("ne", "zamena")),
    EvalQuestion("Da li Poslovna informatika uključuje relacije i tipove podataka?", "Treba da potvrdi da opis uključuje relacije, tipove podataka i DBMS kontekst.", ("relacije", "tipove podataka"), ("SQL",)),
    EvalQuestion("Da li Poslovna informatika obuhvata sisteme za upravljanje bazama podataka?", "Treba da potvrdi osnove sistema za upravljanje bazama podataka.", ("sistem", "baz"), ("SQL",)),
    EvalQuestion("Kako se SQL iz Poslovne informatike povezuje sa BI-jem?", "Treba da objasni da SQL omogućava pripremu/rad sa podacima za analitiku, BI i Power BI.", ("SQL", "BI"), ("Power BI", "analitika")),
    EvalQuestion("Da li je SQL u ovom predmetu dovoljan za data engineering karijeru?", "Treba da kaže da predmet daje osnovu, ali nije dovoljan sam za kompletnu data engineering karijeru.", ("SQL", "osnov"), ("nije dovoljan", "karijer")),
    EvalQuestion("Da li je Poslovna informatika korisna ako me zanimaju podaci?", "Treba da preporuči predmet kao dobru osnovu za podatke, SQL, BI i analitiku, bez preterivanja.", ("podac", "SQL"), ("BI", "analitika")),
    EvalQuestion("Da li Poslovna informatika uključuje Javu?", "Treba da kaže da je Java relevantna prema dostupnom aktuelnom planu, ali da 2027 opis nije potvrda svih operativnih detalja.", ("Java",), ("plan rada", "2025/26")),
    EvalQuestion("Šta se iz Jave pominje u Poslovnoj informatici?", "Treba da navede tipove podataka, stringove, uslove, petlje, nizove i unos podataka.", ("Java", "tipove podataka"), ("petlje", "nizove")),
    EvalQuestion("Da li je Java u Poslovnoj informatici namenjena rešavanju poslovnih problema?", "Treba da potvrdi da programski alati služe za rešavanje poslovnih problema.", ("Java", "poslovnih problema"), ("program",)),
    EvalQuestion("Da li Poslovna informatika uvodi programske jezike?", "Treba da kaže da uvodi programske jezike i programske alate za poslovne probleme.", ("program", "poslov"), ("Java",)),
    EvalQuestion("Da li je Poslovna informatika isto što i Razvoj softvera?", "Treba da razgraniči: Poslovna informatika daje širu osnovu, Razvoj softvera je posebna softverska putanja.", ("nije", "Razvoj softvera"), ("osnov", "šir")),
    EvalQuestion("Da li Poslovna informatika sama po sebi pravi developera?", "Treba da kaže da ne garantuje niti sama čini kompletnu developersku pripremu, već daje osnovu.", ("ne", "developer"), ("osnov", "ne garantuje")),
    EvalQuestion("Kako se programiranje u Poslovnoj informatici razlikuje od čistog programiranja?", "Treba da naglasi poslovni kontekst i rešavanje poslovnih problema programskim alatima.", ("poslov", "program"), ("problem",)),
    EvalQuestion("Da li je Poslovna informatika dobra ako nikad nisam programirao?", "Treba da kaže da može biti uvod/orijentacija, ali bez garancije težine i bez tvrdnji o nastavnom tempu.", ("uvod", "osnov"), ("program",)),
    EvalQuestion("Da li Poslovna informatika može da pomogne za kasnije učenje Razvoja softvera?", "Treba da kaže da može pomoći kao osnova, ali nije zamena za predmet Razvoj softvera.", ("osnov", "Razvoj softvera"), ("nije zamena",)),
    EvalQuestion("Da li Poslovna informatika obuhvata unos podataka u programima?", "Treba da potvrdi da se u Java osnovama pominje rad sa unosom podataka.", ("unos", "podat"), ("Java",)),
    EvalQuestion("Da li Poslovna informatika uključuje Power BI?", "Treba da kaže da Power BI važi ako se zadrži koncept iz aktuelnog plana, ne kao bezuslovna 2027 potvrda.", ("Power BI", "ako"), ("2025/26", "plan")),
    EvalQuestion("Šta se u Power BI delu Poslovne informatike radi?", "Treba da navede import iz SQL baze, vizualizacije, filtere, slicere, interaktivne grafike i dashboarde.", ("Power BI", "SQL"), ("dashboard", "filter")),
    EvalQuestion("Kako se Poslovna informatika povezuje sa poslovnom analitikom?", "Treba da poveže podatke, SQL, Power BI, BI i donošenje odluka.", ("analitika", "podac"), ("Power BI", "SQL")),
    EvalQuestion("Da li Poslovna informatika ima veze sa poslovnom inteligencijom?", "Treba da potvrdi vezu kroz BI, Power BI, SQL i rad sa poslovnim podacima.", ("poslovnom inteligencijom", "BI"), ("Power BI", "SQL")),
    EvalQuestion("Da li je Power BI u Poslovnoj informatici sigurno deo PIT 2027?", "Treba da bude oprezan: ako se zadrži koncept iz aktuelnog plana; poseban 2027 izvor nije dostupan.", ("Power BI", "ako"), ("nije", "potvr")),
    EvalQuestion("Da li se kroz Poslovnu informatiku prave dashboardi?", "Treba da kaže da se dashboardi pominju u Power BI delu ako se zadrži aktuelni koncept izvođenja.", ("dashboard", "Power BI"), ("ako",)),
    EvalQuestion("Da li Poslovna informatika pomaže za BI analitičara?", "Treba da kaže da daje osnovu za BI analitiku kroz podatke, SQL i Power BI, ali ne garantuje posao.", ("BI", "osnov"), ("ne garantuje",)),
    EvalQuestion("Da li je Poslovna informatika dovoljna za BI karijeru?", "Treba da kaže da nije dovoljna sama, već je osnova uz druge predmete i dalje učenje.", ("nije dovoljna", "BI"), ("osnov",)),
    EvalQuestion("Kako se Power BI povezuje sa SQL bazama u ovom predmetu?", "Treba da objasni import podataka iz SQL baze i vizualizacije/dashboards.", ("Power BI", "SQL"), ("vizualizacije",)),
    EvalQuestion("Da li se u Poslovnoj informatici rade sliceri i filteri?", "Treba da potvrdi da se pominju filteri i sliceri u Power BI delu ako ostane aktuelni koncept.", ("filter", "slicer"), ("Power BI", "ako")),
    EvalQuestion("Da li Poslovna informatika uključuje elektronsko poslovanje?", "Treba da potvrdi i navede e-poslovanje, e-trgovinu, e-bankarstvo, e-novac i internet bankarstvo.", ("elektronsko poslovanje",), ("elektronska trgovina", "bankarstvo")),
    EvalQuestion("Koja je veza Poslovne informatike i elektronske trgovine?", "Treba da kaže da predmet pokriva e-trgovinu kao oblast digitalnog poslovanja.", ("elektronska trgovina", "digital"), ("poslovanje",)),
    EvalQuestion("Da li se pominje elektronsko bankarstvo?", "Treba da potvrdi da se pominju elektronsko bankarstvo, e-novac i internet bankarstvo.", ("elektronsko bankarstvo",), ("internet bankarstvo", "novac")),
    EvalQuestion("Da li Poslovna informatika objašnjava digitalne servise?", "Treba da kaže da ishodi uključuju digitalne servise i e-poslovanje.", ("digital", "servis"), ("elektronsko poslovanje",)),
    EvalQuestion("Kako informacione tehnologije menjaju poslovne modele u ovom predmetu?", "Treba da objasni kroz e-poslovanje, e-trgovinu, bankarstvo, ERP, cloud i big data.", ("poslovne modele", "informacione tehnologije"), ("elektrons", "cloud")),
    EvalQuestion("Da li je elektronsko poslovanje poseban predmet ili deo Poslovne informatike?", "Treba da kaže da se e-poslovanje pominje kao oblast u Poslovnoj informatici, a može postojati i poseban predmet u programu.", ("elektronsko poslovanje", "oblast"), ("poseban predmet",)),
    EvalQuestion("Da li se Poslovna informatika bavi internet bankarstvom?", "Treba da potvrdi da je internet bankarstvo navedeno u oblasti elektronskog poslovanja.", ("internet bankarstvo",), ("elektronsko poslovanje",)),
    EvalQuestion("Da li Poslovna informatika obuhvata elektronski novac?", "Treba da potvrdi da se elektronski novac pominje.", ("elektronski novac",), ("elektronsko poslovanje",)),
    EvalQuestion("Kako e-poslovanje u ovom predmetu pomaže razumevanju digitalnog poslovanja?", "Treba da poveže e-poslovanje sa promenama u uslugama, modelima i digitalnim servisima.", ("e-poslovanje", "digital"), ("uslug", "model")),
    EvalQuestion("Da li Poslovna informatika pokriva digitalnu trgovinu?", "Treba da odgovori kroz elektronsku trgovinu kao deo digitalnog poslovanja.", ("elektronska trgovina", "digital"), ("poslovanje",)),
    EvalQuestion("Da li Poslovna informatika uključuje ERP sisteme?", "Treba da potvrdi i objasni ERP kao integrisani poslovni softver i poslovne procese.", ("ERP", "integrisani"), ("poslovni softver",)),
    EvalQuestion("Šta je ERP u kontekstu Poslovne informatike?", "Treba da objasni ERP sisteme, integrisani softver, komponente i implementaciju ERP-a.", ("ERP", "integrisani"), ("komponente", "implementacija")),
    EvalQuestion("Da li Poslovna informatika uvodi integrisani poslovni softver?", "Treba da potvrdi kroz ERP i integrisani poslovni softver.", ("integrisani poslovni softver", "ERP"), ()),
    EvalQuestion("Da li se u Poslovnoj informatici uče komponente ERP sistema?", "Treba da kaže da opis uvodi komponente ERP sistema.", ("ERP", "komponente"), ()),
    EvalQuestion("Da li se pominje implementacija ERP-a?", "Treba da potvrdi da se pominje implementacija ERP-a.", ("implementacija", "ERP"), ()),
    EvalQuestion("Da li je Poslovna informatika korisna za SAP/ERP konsultanta?", "Treba da kaže da daje osnovu za ERP/SAP putanju, ali ne garantuje posao ni sertifikat.", ("ERP", "SAP"), ("ne garantuje", "osnov")),
    EvalQuestion("Da li Poslovna informatika garantuje SAP posao?", "Treba jasno da kaže da ne garantuje posao.", ("ne", "garantuje"), ("SAP", "posao")),
    EvalQuestion("Kako se ERP povezuje sa poslovnim procesima u Poslovnoj informatici?", "Treba da poveže ERP sa integracijom poslovnih procesa i softverskom podrškom organizaciji.", ("ERP", "proces"), ("integr",)),
    EvalQuestion("Da li Poslovna informatika može biti uvod u ERP softver?", "Treba da kaže da može biti osnova/uvod za ERP teme i predmet ERP softver.", ("uvod", "ERP"), ("osnov",)),
    EvalQuestion("Da li je ERP u Poslovnoj informatici dovoljan za ERP konsultantski rad?", "Treba da kaže da nije dovoljan sam, nego daje osnovu uz druge predmete i praksu.", ("nije dovoljan", "ERP"), ("osnov",)),
    EvalQuestion("Da li Poslovna informatika uključuje cloud computing?", "Treba da potvrdi cloud computing kao savremenu temu digitalnog poslovanja.", ("cloud", "digital"), ()),
    EvalQuestion("Da li se u Poslovnoj informatici pominje big data?", "Treba da potvrdi big data kao savremenu temu.", ("big data",), ("digital",)),
    EvalQuestion("Kako se cloud i big data uklapaju u Poslovnu informatiku?", "Treba da kaže da su savremene teme poslovnih informacionih tehnologija i digitalnog poslovanja.", ("cloud", "big data"), ("savremene", "digital")),
    EvalQuestion("Da li Poslovna informatika pokriva savremene tehnologije?", "Treba da navede cloud computing, big data, ERP, Power BI ako je deo koncepta, i digitalno poslovanje.", ("savremene", "tehnologije"), ("cloud", "big data")),
    EvalQuestion("Da li Poslovna informatika govori o digitalnoj transformaciji?", "Treba da je poveže sa informacionim sistemima, ERP-om, cloud/big data i digitalnim poslovanjem.", ("digital", "transform"), ("ERP", "cloud")),
    EvalQuestion("Da li je Poslovna informatika dobar predmet za digitalnu transformaciju i AI interesovanja?", "Treba da kaže da daje osnovu za digitalnu transformaciju i podatke, ali AI zahteva i druge predmete.", ("digital", "AI"), ("osnov", "drugi predmeti")),
    EvalQuestion("Da li se u Poslovnoj informatici uči veštačka inteligencija?", "Treba da ne preuveliča: dokument povezuje sa digitalnim poslovanjem i karijerama, ali AI nije centralno potvrđena oblast ovog predmeta.", ("AI", "nije"), ("ne", "central")),
    EvalQuestion("Da li big data u Poslovnoj informatici znači da ću naučiti data science?", "Treba da kaže da big data postoji kao savremena tema, ali predmet ne daje kompletnu data science obuku.", ("big data", "ne"), ("data science", "kompletn")),
    EvalQuestion("Kako cloud computing pomaže poslovnim informacionim tehnologijama?", "Treba da objasni cloud kao savremenu podršku digitalnim poslovnim sistemima, bez izmišljanja detalja.", ("cloud", "poslov"), ("digital",)),
    EvalQuestion("Da li je Poslovna informatika tehnološki moderan predmet?", "Treba da kaže da formalni opis uključuje savremene teme, uz ogradu da 2027 operativni detalji nisu potvrđeni.", ("savremene", "2027"), ("nisu potvr",)),
    EvalQuestion("Sa kojim predmetima je Poslovna informatika povezana?", "Treba da navede baze, razvoj softvera, ERP, poslovnu analitiku, BI, e-poslovanje i AI.", ("Baze", "ERP"), ("BI", "Razvoj softvera")),
    EvalQuestion("Da li Poslovna informatika pomaže za Baze podataka?", "Treba da kaže da daje osnovu za baze i SQL.", ("osnov", "baze"), ("SQL",)),
    EvalQuestion("Da li Poslovna informatika pomaže za Poslovnu analitiku?", "Treba da kaže da pomaže kroz podatke, SQL, Power BI i donošenje odluka.", ("poslovna analitika", "SQL"), ("Power BI",)),
    EvalQuestion("Da li Poslovna informatika pomaže za Poslovnu inteligenciju?", "Treba da potvrdi vezu sa BI, podacima, SQL-om i dashboardima.", ("poslovna inteligencija", "SQL"), ("dashboard",)),
    EvalQuestion("Da li Poslovna informatika pomaže za Elektronsko poslovanje i veštačku inteligenciju?", "Treba da kaže da je korisna osnova za e-poslovanje i digitalne teme, ali ne sme tvrditi da sama uči AI.", ("elektronsko poslovanje", "osnov"), ("AI",)),
    EvalQuestion("Da li je Poslovna informatika korisna za business analitičara?", "Treba da kaže da je korisna osnova za business/BI analitiku, bez garancije posla.", ("business", "analiti"), ("ne garantuje",)),
    EvalQuestion("Da li je Poslovna informatika korisna za data inženjera?", "Treba da kaže da daje osnovu kroz podatke i SQL, ali data engineering zahteva dodatne predmete i praksu.", ("data", "SQL"), ("dodat", "nije dovolj")),
    EvalQuestion("Da li je Poslovna informatika korisna za developera?", "Treba da kaže da daje uvodnu osnovu kroz programske alate/Java, ali nije kompletna developerska priprema.", ("developer", "osnov"), ("nije", "komplet")),
    EvalQuestion("Da li je Poslovna informatika korisna za konsultanta za digitalnu transformaciju?", "Treba da potvrdi relevantnost kroz IS, ERP, digitalno poslovanje, cloud i podatke.", ("digitalnu transformaciju", "ERP"), ("cloud", "podac")),
    EvalQuestion("Da li Poslovna informatika garantuje posao?", "Treba jasno da kaže da predmet ne garantuje posao, već daje osnovu i orijentaciju.", ("ne garantuje", "posao"), ("osnov",)),
    EvalQuestion("Da li ovaj predmet sam dovoljan za BI, data, ERP ili software karijeru?", "Treba jasno da kaže da nije dovoljan sam i da su potrebni drugi predmeti/učenje/praksa.", ("nije dovoljan", "karijer"), ("BI", "ERP")),
    EvalQuestion("Da li mogu na osnovu Poslovne informatike da izaberem karijerni pravac?", "Treba da kaže da može pomoći kao orijentacija za pravce, ne kao garancija.", ("orijentacija", "karijer"), ("ne garantuje",)),
    EvalQuestion("Koje karijere se najviše povezuju sa Poslovnom informatikom?", "Treba da navede business/BI analitičara, ERP/SAP konsultanta, developera, data inženjera i digitalnu transformaciju.", ("BI", "ERP"), ("developer", "data")),
    EvalQuestion("Šta ako me zanimaju i poslovanje i tehnologija?", "Treba da preporuči Poslovnu informatiku kao prirodnu osnovu za spoj poslovanja i tehnologije.", ("poslovanje", "tehnolog"), ("osnov",)),
    EvalQuestion("Da li Poslovna informatika spada u PIT 2027?", "Treba da potvrdi da je dokument formalni course opis u PIT 2027 kontekstu.", ("PIT 2027", "Poslovna informatika"), ("formalni",)),
    EvalQuestion("Da li su operativni detalji Poslovne informatike za PIT 2027 potvrđeni?", "Treba da kaže da nisu potvrđeni posebnim 2027 izvorom.", ("nisu", "potvr"), ("2027",)),
    EvalQuestion("Da li ovaj dokument potvrđuje nedeljni raspored Poslovne informatike?", "Treba da kaže da ne potvrđuje nedeljni raspored.", ("ne", "nedeljni raspored"), ("potvr",)),
    EvalQuestion("Da li ovaj dokument potvrđuje nastavnike na Poslovnoj informatici?", "Treba da kaže da ne potvrđuje nastavnike i ne komentariše ih.", ("ne", "nastavnik"), ("potvr",)),
    EvalQuestion("Da li ovaj dokument potvrđuje kolokvijume i bodove za Poslovnu informatiku?", "Treba da kaže da ne potvrđuje precizne bodove, kolokvijume ili ispitne uslove za PIT 2027.", ("ne", "kolokvij"), ("bod", "PIT 2027")),
    EvalQuestion("Koji dokument treba koristiti za pitanje kako se Poslovna informatika trenutno izvodi?", "Treba da uputi na aktuelni course_plan 2025/26.", ("2025/26", "plan rada"), ("03_course_plans",)),
    EvalQuestion("Kako se polaže Poslovna informatika?", "Treba da koristi ili uputi na aktuelni plan rada 2025/26, a ne formalni 2027 opis.", ("2025/26", "plan rada"), ("pola",)),
    EvalQuestion("Da li se način ocenjivanja iz 2025/26 automatski prenosi na PIT 2027?", "Treba jasno da kaže da se ne sme automatski prenositi.", ("ne", "automatski"), ("2025/26", "2027")),
    EvalQuestion("Da li je plan rada 2025/26 isto što i formalni opis PIT 2027?", "Treba da razgraniči aktuelni plan rada i formalni 2027 opis.", ("nije", "2025/26"), ("formalni", "2027")),
    EvalQuestion("Da li je sadržaj za PIT 2027 izveden iz plana rada 2025/26?", "Treba da potvrdi da je izveden iz dostupnog aktuelnog plana jer poseban 2027 izvor nije dostupan.", ("izveden", "2025/26"), ("poseban 2027", "nije dostupan")),
    EvalQuestion("Da li treba oprezno tumačiti opis Poslovne informatike za 2027?", "Treba da kaže da je orijentacioni formalni opis, ne potvrda svih operativnih detalja.", ("orijentacioni", "operativ"), ("nije potvr",)),
    EvalQuestion("Da li Poslovna informatika u PIT 2027 sigurno ima iste kolokvijume kao 2025/26?", "Treba da kaže da to nije potvrđeno i da ne treba tvrditi automatsko poklapanje.", ("nije potvr", "kolokvij"), ("2025/26",)),
    EvalQuestion("Da li se aktuelno izvođenje predmeta proverava u course plan dokumentu?", "Treba da potvrdi da za trenutno izvođenje prednost ima course_plan 2025/26.", ("course_plan", "2025/26"), ("prednost",)),
    EvalQuestion("Da li Poslovna informatika u PIT 2027 ima potvrđen ESPB broj u ovom dokumentu?", "Treba da kaže da ESPB nije potvrđen u ovom dokumentu.", ("ESPB", "nije potvr"), ()),
    EvalQuestion("Da li je godina i semestar Poslovne informatike potvrđena u ovom dokumentu?", "Treba da kaže da godina i semestar nisu potvrđeni.", ("godina", "semestar"), ("nije potvr",)),
    EvalQuestion("Da li se status predmeta u ovom dokumentu vodi kao potvrđen?", "Treba da kaže da je status označen kao nije potvrđeno.", ("status", "nije potvr"), ()),
    EvalQuestion("Šta bot ne sme da tvrdi o Poslovnoj informatici?", "Treba da navede zabrane: bez potvrđenih operativnih detalja, bez garantovanja posla, bez ocene nastavnika.", ("ne sme", "garantuje posao"), ("nastavnik", "operativ")),
    EvalQuestion("Da li bot sme da kaže da su operativni detalji PIT 2027 potvrđeni?", "Treba da kaže da ne sme ako poseban izvor nije naveden.", ("ne sme", "operativni detalji"), ("2027", "potvr")),
    EvalQuestion("Da li bot sme da ocenjuje kvalitet nastavnika na Poslovnoj informatici?", "Treba da kaže da ne sme ocenjivati nastavnike.", ("ne sme", "nastavnik"), ("kvalitet",)),
    EvalQuestion("Da li bot sme da kaže da je predmet dovoljan za kompletnu software karijeru?", "Treba da kaže da ne sme i da je predmet osnova, ne kompletna priprema.", ("ne sme", "dovoljan"), ("software", "karijer")),
    EvalQuestion("Da li bot sme da obeća posao posle Poslovne informatike?", "Treba da kaže da ne sme obećati posao.", ("ne sme", "posao"), ("garant",)),
    EvalQuestion("Kako bot treba ukratko da objasni Poslovnu informatiku studentu?", "Treba da da kratak studentski opis: predmet povezuje poslovanje, IT, podatke, programske alate i digitalno poslovanje.", ("poslovanje", "IT"), ("podat", "digitalno")),
    EvalQuestion("Koja je najbolja kratka definicija Poslovne informatike u ovom kontekstu?", "Treba da definiše predmet kao spoj poslovanja, informacionih sistema i digitalnih tehnologija u PIT 2027.", ("spoj", "poslovanja"), ("informacioni sistemi", "PIT 2027")),
    EvalQuestion("Da li je Poslovna informatika dobar uvodni predmet za PIT?", "Treba da kaže da jeste dobra osnova/orijentacija za poslovno-informatički profil.", ("uvod", "PIT"), ("osnov",)),
    EvalQuestion("Koja je razlika između formalnog opisa i aktuelnog izvođenja Poslovne informatike?", "Treba da objasni da formalni opis opisuje PIT 2027 okvir, a aktuelno izvođenje 2025/26 plan rada.", ("formalni opis", "aktuelno izvođenje"), ("2027", "2025/26")),
    EvalQuestion("Ako pitam šta se radi sada na Poslovnoj informatici, koji izvor je prioritet?", "Treba da kaže da je prioritet aktuelni plan rada 2025/26.", ("sada", "2025/26"), ("prioritet",)),
    EvalQuestion("Ako pitam šta je predmet u novoj akreditaciji, koji izvor je prioritet?", "Treba da kaže da je prioritet formalni PIT 2027 opis.", ("nova akreditacija", "PIT 2027"), ("formalni",)),
]


def normalize(text: str) -> str:
    return text.lower().replace("š", "s").replace("đ", "dj").replace("č", "c").replace("ć", "c").replace("ž", "z")


def select_context_results(settings: Any, results: list[Any]) -> list[Any]:
    context_results: list[Any] = []
    total_chars = 0

    for result in results:
        if result.score < settings.min_retrieval_score:
            continue
        chunk_text = getattr(result, "original_chunk_text", "") or getattr(result, "contextual_chunk_text", "") or ""
        if context_results and total_chars + len(chunk_text) > settings.max_total_context_chars:
            continue
        context_results.append(result)
        total_chars += len(chunk_text)
        if len(context_results) >= settings.max_context_chunks:
            break

    return context_results


def score_answer(item: EvalQuestion, answer: str, sources: list[str]) -> tuple[int, str]:
    answer_norm = normalize(answer)
    must_hits = sum(1 for phrase in item.must_include if normalize(phrase) in answer_norm)
    nice_hits = sum(1 for phrase in item.nice_to_include if normalize(phrase) in answer_norm)
    forbidden_hits = [phrase for phrase in item.must_not_include if normalize(phrase) in answer_norm]
    has_primary = any(item.primary_source in source for source in sources)

    score = 6
    if item.must_include:
        score += round(2 * must_hits / len(item.must_include))
    if item.nice_to_include:
        score += min(1, nice_hits)
    if has_primary:
        score += 1
    if forbidden_hits:
        score -= min(3, len(forbidden_hits) + 1)
    if not answer.strip() or "LLM generation error" in answer:
        score = 1
    score = max(1, min(10, score))

    notes: list[str] = []
    missing = [phrase for phrase in item.must_include if normalize(phrase) not in answer_norm]
    if has_primary:
        notes.append("primarni izvor je pogođen")
    else:
        notes.append("primarni izvor nije među korišćenim izvorima")
    if missing:
        notes.append("nedostaje ili nije dovoljno eksplicitno: " + ", ".join(missing[:4]))
    if forbidden_hits:
        notes.append("sadrži rizičnu tvrdnju: " + ", ".join(forbidden_hits))
    if not missing and not forbidden_hits:
        notes.append("odgovor pokriva suštinu očekivanja")

    return score, "; ".join(notes)


def correction_suggestion(item: EvalQuestion, score: int) -> str:
    if score >= 9:
        return "Nije potrebna ispravka."
    return f"Predlog: odgovor pooštriti ovako: {item.expected}"


def strip_ansi(text: str) -> str:
    return re.sub(r"\x1b\[[0-9;]*m", "", text)


def main() -> None:
    settings = load_settings()
    retriever = Retriever(settings.index_path, settings.embedding_model)
    output_path = PROJECT_ROOT / "data" / "test_results" / "poslovna_informatika_100_qa_analysis.md"

    lines: list[str] = [
        "---",
        "id: poslovna_informatika_100_qa_analysis",
        "type: evaluation_report",
        "title: Poslovna informatika, 100 pitanja i analiza odgovora navigatora",
        "course: Poslovna informatika",
        "scope: PIT 2027 formalni opis i aktuelni plan rada kada je pitanje operativno",
        f"generated_at: {datetime.now().isoformat(timespec='seconds')}",
        "status: draft_for_review",
        "---",
        "",
        "# Poslovna informatika, 100 pitanja i analiza odgovora navigatora",
        "",
        "Format svake stavke: pitanje, odgovor navigatora, analiza sa ocenom od 1 do 10 i predlog ispravke koji možeš da pošalješ nazad za doradu.",
        "",
    ]

    for index, item in enumerate(QUESTIONS[:100], start=1):
        print(f"[{index:03d}/100] {item.question}", flush=True)
        classification = classify(item.question)
        results = retriever.search(
            item.question,
            classification.intents,
            settings.top_k,
            classification.course_names,
        )
        context_results = select_context_results(settings, results)

        if not context_results:
            answer = "Navigator nije vratio dovoljno relevantan kontekst."
            sources: list[str] = []
        else:
            messages = build_messages(
                item.question,
                classification.intents,
                classification.course_names,
                context_results,
            )
            generation_result = generate_answer(messages)
            answer = str(generation_result.get("answer") or "").strip()
            if not answer:
                answer = f"LLM generation error: {generation_result.get('error') or 'Generator nije vratio odgovor.'}"
            sources = collect_source_paths(context_results)

        answer = strip_ansi(answer)
        score, analysis = score_answer(item, answer, sources)
        lines.extend(
            [
                f"## QA_{index:03d}",
                "",
                f"**Pitanje:** {item.question}",
                "",
                "**Odgovor navigatora:**",
                "",
                answer,
                "",
                "**Analiza:**",
                "",
                f"Ocena: {score}/10.",
                "",
                f"Očekivanje: {item.expected}",
                "",
                f"Procena: {analysis}.",
                "",
                f"Predlog ispravke: {correction_suggestion(item, score)}",
                "",
                "**Korišćeni izvori u testu:**",
                "",
            ]
        )
        if sources:
            lines.extend(f"- `{source}`" for source in sources)
        else:
            lines.append("- Nema izvora.")
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {output_path}", flush=True)


if __name__ == "__main__":
    main()
