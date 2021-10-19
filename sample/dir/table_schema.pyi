from typing import Sequence, Union
from datetime import date, datetime, time


class Prediction:
    product_code: Union[int, Sequence[int]]
    year: Union[int, Sequence[int]]
    week: Union[int, Sequence[int]]
    forward_week_num: Union[int, Sequence[int]]
    value: Union[float, Sequence[float]]
    exec_id: Union[str, Sequence[str]]
    ...


class Validation:
    product_code: Union[int, Sequence[int]]
    year: Union[int, Sequence[int]]
    week: Union[int, Sequence[int]]
    forward_week_num: Union[int, Sequence[int]]
    type: Union[str, Sequence[str]]
    value: Union[float, Sequence[float]]
    exec_id: Union[str, Sequence[str]]
    ...


