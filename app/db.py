import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "app_data.sqlite"

def get_connection():
    """Establish SQLite connection and return Row factory cursor."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def search_products(query: str):
    """Search products by name or description with partial match."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM products WHERE name LIKE ? OR description LIKE ? LIMIT 5",
        (f"%{query}%", f"%{query}%"),
    )
    rows = cur.fetchall()
    conn.close()
    return rows