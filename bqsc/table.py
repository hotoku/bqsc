from typing import Any, Dict, Iterable, Sequence
from .table_info import TableInfo
from .column_info import ColumnInfo

_type_map: Dict[str, type] = {
    "string": str,
    "integer": int,
    "float": float,
    "boolean": bool
}


class NotDefinedColumn(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"{name} is not defined.")


class TypeMismatch(Exception):
    def __init__(self, name: str, value: Any, expected: type) -> None:
        super().__init__(
            f"column: {name}, expected: {expected}, given: {value}")


class Table:
    def __init__(self, tinfo: TableInfo, cinfos: Sequence[ColumnInfo]) -> None:
        self.table_info = tinfo
        self.column_infos = list(cinfos)
        self.column_names = [c.name for c in self.column_infos]
        self.column_types = {
            c.name: _type_map[c.type.lower()] for c in self.column_infos
        }

    def __setattr__(self, name: str, value: Any) -> None:
        if name not in self.column_names:
            raise NotDefinedColumn(name)

        if isinstance(value, Iterable):
            it = iter(value)
            v = next(it)
        else:
            v = value

        if not self.type_check(name, v):
            raise TypeMismatch(name, v, self.column_types[name])

        super().__setattr__(name, v)

    def type_check(self, name: str, value: Any) -> bool:
        ty = self.column_types[name]
        return isinstance(value, ty)
