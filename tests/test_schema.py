import bqsc
from bqsc.table import NotDefinedColumn, TypeMismatch


def test_set():
    table = bqsc.load("tests/resources/case1.json")
    table.id = [1, 2]
    table.name = ["dog", "cat"]
    table.value = [1.1, 2.2]


def test_mismatch():
    table = bqsc.load("tests/resources/case1.json")
    try:
        table.id = "a"
        assert False
    except TypeMismatch:
        pass

    try:
        table.name = 1
        assert False
    except TypeMismatch:
        pass

    try:
        table.value = "a"
        assert False
    except TypeMismatch:
        pass


def test_no_definition():
    table = bqsc.load("tests/resources/case1.json")
    try:
        table.hoge = "x"
        assert False
    except NotDefinedColumn:
        pass
