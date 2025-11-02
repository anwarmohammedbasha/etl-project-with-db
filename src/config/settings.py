# src/config/settings.py
import os
from pathlib import Path

def _clean(name, default=""):
    return str(os.getenv(name, default)).strip().strip('"').strip("'")

BASE_DIR = Path(__file__).resolve().parent.parent

# data dirs (still used for CSVs)
DATA_DIR = _clean("DATA_DIR", str(BASE_DIR / "data" / "source"))
PROCESSED_DIR = _clean("PROCESSED_DIR", str(BASE_DIR / "data" / "processed"))

# mysql only
MYSQL_HOST = _clean("MYSQL_HOST", "127.0.0.1")
MYSQL_PORT = int(_clean("MYSQL_PORT", "3306"))
MYSQL_USER = _clean("MYSQL_USER", "root")
MYSQL_PASSWORD = _clean("MYSQL_PASSWORD", "")
MYSQL_DB = _clean("MYSQL_DB", "anwar_coffee_db")

# logging
LOG_PATH = _clean("LOG_PATH", str(BASE_DIR / "etl.log"))
