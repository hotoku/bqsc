from typing import Sequence, Union
from datetime import date, datetime, time


class Prediction:
    product_code: Union[int, Sequence[int]]
    year: Union[int, Sequence[int]]
    week: Union[int, Sequence[int]]
    forward_week_num: Union[int, Sequence[int]]
    value: Union[float, Sequence[float]]
    exec_id: Union[str, Sequence[str]]
    exec_date: Union[date, Sequence[date]]
    ...


class ValidationSummary:
    exec_id: Union[str, Sequence[str]]
    model: Union[str, Sequence[str]]
    exec_md_week: Union[str, Sequence[str]]
    all: Union[bool, Sequence[bool]]
    mape_for_model: Union[float, Sequence[float]]
    mape_std: Union[float, Sequence[float]]
    mape_min: Union[float, Sequence[float]]
    mape_25per: Union[float, Sequence[float]]
    mape_50per: Union[float, Sequence[float]]
    mape_75per: Union[float, Sequence[float]]
    mape_max: Union[float, Sequence[float]]
    exec_start: Union[datetime, Sequence[datetime]]
    duration: Union[time, Sequence[time]]
    exec_end: Union[datetime, Sequence[datetime]]
    debug: Union[bool, Sequence[bool]]
    commit_hash: Union[str, Sequence[str]]
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


