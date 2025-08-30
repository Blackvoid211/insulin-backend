\# Insulin Backend (minimal)



\## Run locally

1\. Create \& activate virtualenv:

&nbsp;  python -m venv .venv

&nbsp;  source .venv/bin/activate   # macOS / Linux

&nbsp;  .venv\\Scripts\\activate      # Windows



2\. Install dependencies:

&nbsp;  pip install -r requirements.txt



3\. Create .env (copy .env.example) and set:

&nbsp;  DATABASE\_URL=sqlite:///./test.db

&nbsp;  JWT\_SECRET=your\_secret

&nbsp;  ALLOWED\_ORIGINS=http://localhost:3000



4\. Create tables \& seed:

&nbsp;  python scripts/test\_db\_conn.py   # if present (creates tables)

&nbsp;  python scripts/seed\_foods.py



5\. Start dev server:

&nbsp;  python -m uvicorn app.main:app --reload



APIs:

\- GET /health

\- POST /auth/register

\- POST /auth/login

\- GET /foods



