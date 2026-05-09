# 05_server_upload

Ovaj folder sadrži production-ready verziju PIT Navigator frontenda za ručni upload na server.

## Ciljna putanja na serveru

```
/home/azecevic/public_html/pin/pit-navigator/
```

Odgovarajući URL: `https://pin.ekof.bg.ac.rs/pin/pit-navigator/`

## Fajlovi za upload

```
05_server_upload/pit-navigator/
  index.html          ← glavna stranica (pit-navigator.html prilagođena za /pin/pit-navigator/)
  pit-navigator.css   ← stilovi (isti fajl kao u 04_frontend_site/)
  pit-navigator.js    ← logika (isti fajl kao u 04_frontend_site/)
```

## Pre upload-a: obavezno podešavanje API URL-a

U fajlu `index.html`, pronađi sledeći blok na dnu:

```html
<script>
  window.PIT_CONFIG = {
    API_URL: "https://PIT-NAVIGATOR-API-URL/chat",
    STREAM_API_URL: "https://PIT-NAVIGATOR-API-URL/chat/stream"
  };
</script>
```

Zameni `PIT-NAVIGATOR-API-URL` sa produkcionim adresom backend API-ja, na primer:

```javascript
API_URL: "https://pit-api.ekof.bg.ac.rs/chat",
STREAM_API_URL: "https://pit-api.ekof.bg.ac.rs/chat/stream"
```

## Šta NE uploadovati

- `.env` fajlove
- `03_implementation/` folder (Python kod, indeks, logovi)
- `02_knowledge_base/` (knowledge base dokumenti)
- `01_raw_documents/` (sirovi PDF/DOCX)
- `00_project_rules/`, `Plan rada.txt`, `logika pocetak.txt`

## Preduslovi na serveru

- `layout/styles/layout.css` mora postojati na serveru u:
  `/home/azecevic/public_html/layout/styles/layout.css`
  (index.html ga referencira kao `../../layout/styles/layout.css`)

## Backend preduslovi pre deployment-a

1. VPS sa Python 3.11+, uvicorn, FastAPI
2. `.env` fajl sa `GEMINI_API_KEY` (i opcionalno `OPENAI_API_KEY` za fallback)
3. Index izgrađen: `python scripts/build_index.py`
4. `https://pin.ekof.bg.ac.rs` dodat u `allow_origins` u `api/main.py` (već urađeno)
5. HTTPS sertifikat za backend domen
6. Nginx konfigurisana sa `proxy_read_timeout 60s` i rate limiting

## Provera nakon upload-a

1. Otvori `https://pin.ekof.bg.ac.rs/pin/pit-navigator/`
2. Postavi pitanje i proveri da li dobijaju odgovori
3. Proveri `/health` endpoint na backend API-ju
4. Proveri `/health/deep` endpoint — treba da prikaže `"model_loaded": true`
