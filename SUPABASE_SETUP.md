# Supabase Setup

## 1) Install dependency

Already added in `requirements.txt`:

```
supabase>=2.0.0
```

## 2) Create tables and policies

In Supabase SQL editor, run file `SUPABASE_SCHEMA.sql`.

## 3) Streamlit secrets (do not hardcode keys)

Create `.streamlit/secrets.toml` locally and add in Streamlit Cloud Secrets:

```
SUPABASE_URL = "https://<your-project-ref>.supabase.co"
SUPABASE_ANON_KEY = "<anon-key>"
```

For personal single-user apps, anon key is sufficient if policies allow. Never commit the `service_role` key to code or secrets for a client-facing app.

## 4) Environment variables (optional local dev)

Alternatively set env vars:

- `SUPABASE_URL`
- `SUPABASE_ANON_KEY`

## 5) How it works in the app

- On startup, the app checks for Supabase secrets.
- If configured, it loads initial data from Supabase into local CSVs/session.
- On each write (profile update, meal/workout logs), it upserts to Supabase.
- If not configured, it falls back to CSV/session only.

## 6) Migrating existing CSV data

- Start the app once without Supabase to generate CSVs.
- Configure secrets.
- Any next save operation will upsert your local data to Supabase.
- Or manually import by loading CSVs and inserting in the Supabase SQL editor.
