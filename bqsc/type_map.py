from typing import Dict
from datetime import date, datetime, time


TYPE_MAP: Dict[str, type] = {
    "string": str,
    "integer": int,
    "float": float,
    "boolean": bool,
    "date": date,
    "datetime": datetime,
    "time": time
}
