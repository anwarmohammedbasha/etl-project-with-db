"""
cleaner.py — Cleans and validates data
"""
from utils.logger import get_logger

logger = get_logger(__name__)

def clean_data(raw_data: dict) -> dict:
    logger.info("Cleaning raw data...")
    # Example: fill missing comments
    if "customer_reviews" in raw_data:
        df = raw_data["customer_reviews"]
        df["comment"] = df["comment"].fillna("N/A")
        raw_data["customer_reviews"] = df
    return raw_data
