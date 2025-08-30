# scripts/verify_db.py
import sqlite3
conn = sqlite3.connect("test.db")
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cur.fetchall())
conn.close()
