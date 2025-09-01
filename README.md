# Bins — Backend for binsh

## What this project does

Bins is a lightweight backend that lets users create, store, and share text snippets via short, shareable URLs. It supports creating, reading, updating, and deleting snippets, optional expiration times, and simple visibility controls (public/private). The API is organized for clarity so you can hook a frontend to it quickly or extend features like syntax metadata, analytics, or rate-limiting.

## Tech stack

* Python 3.10+
* FastAPI
* Uvicorn (ASGI server)
* Prisma ORM (with Postgres)
* asyncpg

## Quick local setup

1. Clone the repo

```bash
git clone <https://github.com/kuslhhh/Bins.git>
cd <Bins>
```

2. Create & activate a virtual environment

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create a `.env` in the project root with:

```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/bins_db
PORT: 3000
```

5. Ensure Postgres is running (local or Docker or you can get one on [neon.tech](https://console.neon.tech/)).

6. Prisma: generate client and run migrations

```bash
prisma generate 
prisma migrate dev --name init
```

7. Run the app (dev)

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

Open `http://localhost:5000/bin` to see the API (Swagger UI).

---

### Test `web/index.html` — quick options

**1) With backend (FastAPI)** — serves static files at `/bin`

```bash
# dev
uvicorn main:app --reload --host 0.0.0.0 --port 5000
# open:
http://localhost:5000/bin/   
```
**2) Frontend-only (fast)** 

```bash
# serve 
npx serve web/index.html
# open:
http://localhost:3000
```