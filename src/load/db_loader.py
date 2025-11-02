# src/load/db_loader.py
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from utils.logger import get_logger
from config import settings

logger = get_logger(__name__)

def _server_engine():
    url = URL.create(
        "mysql+pymysql",
        username=settings.MYSQL_USER,
        password=settings.MYSQL_PASSWORD,
        host=settings.MYSQL_HOST,
        port=settings.MYSQL_PORT,
        database=None,  # connect to server, not a specific DB
    )
    return create_engine(url, pool_pre_ping=True)

def _db_engine():
    url = URL.create(
        "mysql+pymysql",
        username=settings.MYSQL_USER,
        password=settings.MYSQL_PASSWORD,
        host=settings.MYSQL_HOST,
        port=settings.MYSQL_PORT,
        database=settings.MYSQL_DB,
    )
    return create_engine(url, pool_pre_ping=True)

def ensure_database_exists():
    logger.info(f"Ensuring database `{settings.MYSQL_DB}` exists…")
    create_sql = text(
        f"CREATE DATABASE IF NOT EXISTS `{settings.MYSQL_DB}` "
        "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
    )
    with _server_engine().connect() as conn:
        conn.execute(create_sql)
        conn.commit()

def load_data(data_dict: dict):
    logger.info(f"Connecting to MySQL at {settings.MYSQL_HOST}:{settings.MYSQL_PORT}")
    ensure_database_exists()
    engine = _db_engine()
    with engine.begin() as conn:
        for name, df in data_dict.items():
            df.to_sql(name, conn, if_exists="replace", index=False)
            logger.info(f"Loaded table {name} ({len(df)} rows) into {settings.MYSQL_DB}")
    logger.info("✅ Data successfully loaded into MySQL.")
