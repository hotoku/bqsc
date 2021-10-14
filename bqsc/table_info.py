from typing import Dict, Iterable, Any
from datetime import date, datetime, time

from .column_info import ColumnInfo
from .type_map import TYPE_MAP


class TableInfo:
    def __init__(self, cinfos: Iterable[ColumnInfo]) -> None:
        self.column_infos = list(cinfos)
        self.column_names = [c.name for c in self.column_infos]
        self.column_types = {
            c.name: TYPE_MAP[c.type.lower()] for c in self.column_infos
        }

    def type_check(self, name: str, value: Any) -> bool:
        ty = self.column_types[name]
        return isinstance(value, ty)
