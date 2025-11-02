"""
aggregate.py — Business logic transformations
"""
import pandas as pd
from utils.logger import get_logger

logger = get_logger(__name__)

def transform_data(cleaned: dict) -> dict:
    logger.info("Applying business transformations...")

    sales = cleaned["sales"]
    products = cleaned["products"]
    staff = cleaned["staff"]
    salary = cleaned["salary"]

    # Merge product info into sales
    sales = sales.merge(products[["product_id", "product_name", "unit_price"]],
                        on="product_id", how="left")
    sales["total_sale_price"] = sales["unit_price"] * sales["quantity"]

    # Merge staff and salary
    dim_staff = staff.merge(salary, on="staff_id", how="left")

    cleaned["sales"] = sales
    cleaned["dim_staff"] = dim_staff
    return cleaned
