from dataclasses import dataclass
from typing import Sequence

from .column_info import ColumnInfo


@dataclass
class TableInfo:
    name: str
    columns: Sequence[ColumnInfo]
