# PIT Navigator frontend site

Ovaj folder sadrži frontend prototip za PIT Navigator chat stranicu.

Struktura:

```text
04_frontend_site/
  pit-navigator.html
  pit-navigator.css
  pit-navigator.js
  README.md
```

Za lokalni test backend treba pokrenuti iz `03_implementation/`:

```bash
cd 03_implementation
python -m uvicorn api.main:app --reload --host 127.0.0.1 --port 8000
```

Za lokalni statički server može se koristiti:

```bash
python -m http.server 5500
```

Stranicu zatim otvoriti na:

```text
http://127.0.0.1:5500/pit-navigator.html
```

Za lokalni test potrebno je servirati fajlove zajedno sa postojećim `layout/` folderom sajta.

`API_URL` može da se override-uje kroz `window.PIT_CONFIG` u `pit-navigator.html`.
`STREAM_API_URL` može posebno da se override-uje ako streaming endpoint nije izveden iz istog URL-a.

Podrazumevano `API_URL` trenutno pokazuje na `http://127.0.0.1:8000/chat`. Pre produkcije treba ga zameniti produkcionim API URL-om.
Podrazumevano `STREAM_API_URL` pokazuje na `http://127.0.0.1:8000/chat/stream`.

Conversation history se čuva u browser `localStorage`.

Lokalno se čuva najviše poslednjih 50 poruka.

Backend-u se šalje najviše poslednjih 6 poruka.

Za deploy se fajlovi iz ovog foldera kopiraju u root statičkog sajta `pin.ekof.bg.ac.rs`.
