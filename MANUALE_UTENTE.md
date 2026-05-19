# 📘 Manuale Utente Dettagliato — `pytest-api-framework`

Questo manuale descrive come installare, configurare, eseguire e interpretare i test del progetto `pytest-api-framework`.

---

## 1) Prerequisiti

- **Python 3.10+**
- **pip** aggiornato
- Connessione Internet (per i test live verso `reqres.in`)
- (Opzionale) **Docker**
- (Opzionale) **k6** e **Locust** per performance test

---

## 2) Installazione rapida

```bash
git clone <repo_url>
cd api_test_framework
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

---

## 3) Struttura essenziale del progetto

- `tests/` → suite di test API (smoke, contract, functional, retry, ecc.)
- `core/api_client.py` → client HTTP riusabile con retry, timeout e correlation ID
- `core/endpoints/users_endpoint.py` → endpoint object per dominio utenti
- `conftest.py` → fixture globali (`config`, `logger`, `api_client`)
- `config/config.yaml` → ambiente di default (`default_env`) e mapping ambienti
- `pytest.ini` → opzioni di esecuzione Pytest e marker
- `performance/` → script Locust e k6

---

## 4) Configurazione ambienti

La configurazione attiva viene caricata da `config/config.yaml` tramite fixture `config`.

Esempio:

```yaml
default_env: dev

environments:
  dev:
    base_url: "https://reqres.in/api"
    api_key: "dev-key"
```

### Come cambiare ambiente

In questa versione, l'ambiente si cambia aggiornando il valore:

```yaml
default_env: dev | stage | prod
```

> Nota: il flag CLI `--env=...` **non è implementato** in `conftest.py` al momento.

---

## 5) Eseguire i test

### Tutta la suite
```bash
pytest
```

### Esecuzione verbosa
```bash
pytest -v
```

### Solo contract tests
```bash
pytest -m contract -v
```

### Singolo file
```bash
pytest tests/test_users.py -v
```

### Singolo test
```bash
pytest tests/test_users.py::test_get_single_user -v
```

### Report HTML (già impostato in `pytest.ini`)
Con `addopts`, Pytest genera automaticamente:
- `reports/report.html`

---

## 6) Cosa aspettarsi dai test

- **Status code checks**: verifica codici HTTP corretti
- **Schema/contract checks**: confronto con JSON schema/OpenAPI excerpt
- **Retry robustness**: test della strategia retry del client
- **Smoke/health checks**: validazione base disponibilità endpoint

Se un test fallisce, controllare:
1. endpoint disponibile
2. payload valido
3. eventuali modifiche API esterne
4. log in `logs/`

---

## 7) Logging e troubleshooting

Il client API registra:
- metodo HTTP
- URL
- `X-Correlation-ID`
- tempo risposta (`elapsed_ms`)
- anteprima body risposta

### Diagnostica consigliata

```bash
pytest -v -s
```

`-s` mostra output/print/log in console senza cattura.

---

## 8) Performance tests

### Locust
```bash
locust -f performance/locustfile.py --host=https://reqres.in
```

Aprire poi l'interfaccia web di Locust per avviare il carico.

### k6
```bash
k6 run performance/k6_users.js
```

---

## 9) Esecuzione con Docker

```bash
docker build -t pytest-api-framework .
docker run --rm pytest-api-framework
```

Utile per esecuzioni isolate e consistenti tra ambienti diversi.

---

## 10) FAQ rapida

### I test non partono
- Verificare virtualenv attivo
- Verificare dipendenze installate (`pip install -r requirements.txt`)

### Test instabili o timeout
- Controllare connettività verso `reqres.in`
- Aumentare timeout/retry nel client se necessario

### Il report HTML non compare
- Verificare plugin `pytest-html` installato tramite `requirements.txt`
- Verificare la creazione cartella `reports/`

---

## 11) Buone pratiche operative

- Eseguire sempre almeno smoke + contract prima di push/PR
- Tenere i dati test in `tests/testdata/` separati dalla logica
- Usare naming descrittivo per nuovi test
- Mantenere idempotenza dei test quando possibile

---

## 12) Roadmap suggerita (utente)

Per l'evoluzione del framework:
- aggiungere selezione ambiente da CLI (`--env`)
- introdurre authentication layer (Bearer/JWT/OAuth2)
- consolidare validazione JSON Schema centralizzata
- integrare pipeline CI multi-versione Python

