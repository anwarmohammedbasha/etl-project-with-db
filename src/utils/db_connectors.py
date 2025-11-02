"""
db_connectors.py — Generic SQLite helper
"""
import sqlite3
from contextlib import contextmanager

@contextmanager
def sqlite_connection(db_path):
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()
