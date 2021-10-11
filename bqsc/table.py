from typing import Any, Dict, Iterable, Sequence
import re

from .table_info import TableInfo
from .column_info import ColumnInfo


class NotDefinedColumn(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"{name} is not defined.")


class TypeMismatch(Exception):
    def __init__(self, name: str, value: Any, expected: type) -> None:
        super().__init__(
            f"column: {name}, expected: {expected}, given: {value}")


class Table:
    def __init__(self, cinfos: Sequence[ColumnInfo]) -> None:
        self.table_info_NOSETCHECK = TableInfo(cinfos)

    def __setattr__(self, name: str, value: Any) -> None:
        if re.match(r".+_NOSETCHECK$", name):
            super().__setattr__(name, value)
            return

        info = self.table_info_NOSETCHECK
        if name not in info.column_names:
            raise NotDefinedColumn(name)

        if isinstance(value, Iterable):
            it = iter(value)
            v = next(it)
        else:
            v = value

        if not info.type_check(name, v):
            raise TypeMismatch(name, v, info.column_types[name])

        super().__setattr__(name, v)
