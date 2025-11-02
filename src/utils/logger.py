"""
logger.py — tiny wrapper to ensure logging is set up once.
"""

import logging
from config.logging_config import setup_logging

def get_logger(name: str):
    setup_logging()
    return logging.getLogger(name)
