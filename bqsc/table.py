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
        super().__setattr__("_table_info", TableInfo(cinfos))

    def __setattr__(self, name: str, value: Any) -> None:
        info: TableInfo = self._table_info  # type: ignore
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

    def _typehint(self) -> str:
        info: TableInfo = self._table_info  # type: ignore
        ret = f"""
class {type(self).__name__}:
"""
        for col in info.column_infos:
            ret += "    " + col._typehint() + "\n"
        ret += "    ..."
        return ret
