# src/main.py
from utils.logger import get_logger
from config.settings import DATA_DIR, MYSQL_DB
from extract.data_extractor import extract_data
from transform.aggregate import transform_data
from load.db_loader import load_data

logger = get_logger(__name__)

def main():
    logger.info("🚀 Starting Anwar Coffee Shop ETL (MySQL)…")
    logger.info(f"Reading CSVs from: {DATA_DIR}")

    raw_data = extract_data(DATA_DIR)
    transformed = transform_data(raw_data)
    load_data(transformed)

    logger.info(f"✅ ETL pipeline complete. Data loaded into MySQL database `{MYSQL_DB}`.")

if __name__ == "__main__":
    main()
