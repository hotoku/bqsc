import numpy as np

import bqsc
from bqsc.table import dataframe


Case2 = bqsc.load("tests/resources/case2.json")


def test_dataframe():
    case2 = Case2()
    case2.id = [1, 2]
    case2.value = [1.0, 2.0]
    case2.label = "a"
    df = dataframe(case2)
    assert np.all(df.id == [1, 2])
    assert np.all(df.value == [1.0, 2.0])
    assert np.all(df.label == ["a", "a"])


def test_dataframe2():
    case2 = Case2()
    case2.id = [1, 2, 3]
    case2.value = [1.0, 2.0]
    case2.label = "a"
    try:
        dataframe(case2)
        assert False, "test_dataframe2"
    except ValueError:
        pass


def test_required():
    case2 = Case2()

    try:
        dataframe(case2)
        assert False, "test_required"
    except AttributeError:
        pass


def test_nullable():
    case2 = Case2()
    case2.id = [1, 2]
    case2.value = [1.0, 2.0]
    dataframe(case2)
