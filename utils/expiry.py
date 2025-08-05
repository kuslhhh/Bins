from datetime import datetime, timedelta

EXPIRY_MAP = {
    "1h": timedelta(hours=1),
    "24h": timedelta(hours=24),
    "7d": timedelta(days=7),
    "31d": timedelta(days=31)
}

def calc_expiry(choice: str) -> datetime:
    return datetime.utcnow() + EXPIRY_MAP.get(choice, timedelta(days=7))