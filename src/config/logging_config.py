"""
logging_config.py — configure logging across the project
Creates the log file if it doesn't exist and logs to both console and file.
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from config.settings import LOG_PATH

def setup_logging():
    # Create parent directory if needed
    log_file = Path(LOG_PATH)
    log_file.parent.mkdir(parents=True, exist_ok=True)

    # Root logger config (idempotent)
    logger = logging.getLogger()
    if logger.handlers:
        # Already configured (avoid duplicate handlers if called twice)
        return

    logger.setLevel(logging.INFO)

    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    # Rotating file handler (approx 5MB, keep 3 backups)
    fh = RotatingFileHandler(str(log_file), maxBytes=5_000_000, backupCount=3, encoding="utf-8")
    fh.setLevel(logging.INFO)
    fh.setFormatter(fmt)
    logger.addHandler(fh)
