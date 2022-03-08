from typing import Sequence, Union
from datetime import date, datetime, time, timedelta

from bqsc import Table

class MyTable(Table):
    col_str: Union[str, Sequence[str]]
    col_int: Union[int, Sequence[int]]
    col_float: Union[float, Sequence[float]]
    ...


