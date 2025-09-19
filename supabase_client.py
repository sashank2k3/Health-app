import os
from typing import Optional, Dict, Any, List

import streamlit as st

try:
	from supabase import create_client, Client
except Exception:  # pragma: no cover
	create_client = None
	Client = None  # type: ignore


SUPABASE_TABLES = {
	"user_profile": "user_profile",
	"weight_log": "weight_log",
	"diet_log": "diet_log",
	"workout_log": "workout_log",
}


def get_supabase_client() -> Optional["Client"]:
	"""Initialize Supabase client from Streamlit secrets.
	Returns None if not configured properly or SDK missing.
	"""
	# Prefer Streamlit secrets
	url = st.secrets.get("SUPABASE_URL", None)
	key = st.secrets.get("SUPABASE_ANON_KEY", None)
	if not url or not key:
		# Allow environment variables fallback for local testing
		url = os.environ.get("SUPABASE_URL")
		key = os.environ.get("SUPABASE_ANON_KEY")

	if not url or not key:
		return None
	if create_client is None:
		return None
	try:
		client: Client = create_client(url, key)
		return client
	except Exception:
		return None


def table_exists(client: "Client", table: str) -> bool:
	try:
		# Lightweight check: attempt a count(*) with limit 1
		client.table(table).select("id", count="exact").limit(1).execute()
		return True
	except Exception:
		return False


def fetch_all(client: "Client", table: str) -> List[Dict[str, Any]]:
	resp = client.table(table).select("*").order("date", desc=False).execute()
	return resp.data or []


def upsert_rows(client: "Client", table: str, rows: List[Dict[str, Any]]) -> None:
	if not rows:
		return
	client.table(table).upsert(rows).execute()


def insert_row(client: "Client", table: str, row: Dict[str, Any]) -> None:
	client.table(table).insert(row).execute()


def delete_by_id(client: "Client", table: str, row_id: Any) -> None:
	client.table(table).delete().eq("id", row_id).execute()
