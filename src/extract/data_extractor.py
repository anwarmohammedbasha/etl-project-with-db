"""
data_extractor.py — Reads required CSVs from DATA_DIR with clear errors
"""
import os
import pandas as pd
from utils.logger import get_logger

logger = get_logger(__name__)

REQUIRED_FILES = {
    "products": "products.csv",
    "staff": "staff.csv",
    "salary": "salary.csv",
    "sales": "sales.csv",
    "raw_material_purchases": "raw_material_purchases.csv",
    "daily_expenses": "daily_expenses.csv",
    "customer_reviews": "customer_reviews.csv",
}

def extract_data(data_dir: str) -> dict:
    logger.info(f"Extracting data from {data_dir}")
    missing = []
    data = {}

    for key, filename in REQUIRED_FILES.items():
        path = os.path.join(data_dir, filename)
        if not os.path.exists(path):
            missing.append(filename)
            continue
        try:
            df = pd.read_csv(path)
            if df.empty:
                logger.warning(f"{filename} is present but empty.")
            data[key] = df
            logger.info(f"Loaded {filename} ({len(df)} rows)")
        except Exception as e:
            raise RuntimeError(f"Failed reading {path}: {e}") from e

    if missing:
        raise FileNotFoundError(
            f"Missing required files in {data_dir}: {missing}. "
            f"Ensure your generator writes to this folder or update DATA_DIR."
        )

    return data
