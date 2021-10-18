from datetime import date, datetime, time
import bqsc

from bqsc.table import typehint


Case1 = bqsc.load("tests/resources/case1.json")


def test_hint():
    case1 = Case1()
    exp = """
class Case1:
    id: Union[int, Sequence[int]]
    name: Union[str, Sequence[str]]
    value: Union[float, Sequence[float]]
    datetime: Union[datetime, Sequence[datetime]]
    date: Union[date, Sequence[date]]
    time: Union[time, Sequence[time]]
    ...
"""
    act = typehint(case1)
    assert act.strip() == exp.strip()
