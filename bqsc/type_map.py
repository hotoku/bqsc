from typing import Dict
from datetime import date, datetime, time, timedelta


TYPE_MAP: Dict[str, type] = {
    "string": str,
    "integer": int,
    "int64": int,
    "float": float,
    "float64": float,
    "boolean": bool,
    "date": date,
    "datetime": datetime,
    "time": time,
    "interval": timedelta
}
