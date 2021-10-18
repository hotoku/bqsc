from typing import Any, Iterable

import pandas as pd

from .table_info import TableInfo


class NotDefinedColumn(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"{name} is not defined.")


class TypeMismatch(Exception):
    def __init__(self, name: str, value: Any, expected: type) -> None:
        super().__init__(
            f"column: {name}, expected: {expected}, given: {value}")


class Table:
    _table_info: TableInfo

    def __setattr__(self, name: str, value: Any) -> None:
        if name not in self._table_info.column_names:
            raise NotDefinedColumn(name)

        if isinstance(value, Iterable):
            it = iter(value)
            v = next(it)
        else:
            v = value

        if not self._table_info.type_check(name, v):
            raise TypeMismatch(name, v, self._table_info.column_types[name])

        super().__setattr__(name, v)


def typehint(table: Table) -> str:
    ret = f"""
class {type(table).__name__}:
"""
    for col in table._table_info.column_infos:
        ret += "    " + col.typehint() + "\n"
    ret += "    ..."
    return ret
