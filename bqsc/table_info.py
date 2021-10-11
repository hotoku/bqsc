from typing import Dict, Iterable, Any

from .column_info import ColumnInfo


class TableInfo:
    _type_map: Dict[str, type] = {
        "string": str,
        "integer": int,
        "float": float,
        "boolean": bool
    }

    def __init__(self, cinfos: Iterable[ColumnInfo]) -> None:
        self.column_infos = list(cinfos)
        self.column_names = [c.name for c in self.column_infos]
        self.column_types = {
            c.name: self._type_map[c.type.lower()] for c in self.column_infos
        }

    def type_check(self, name: str, value: Any) -> bool:
        ty = self.column_types[name]
        return isinstance(value, ty)
