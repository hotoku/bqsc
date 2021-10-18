from datetime import date, datetime, time, timedelta
import bqsc
from bqsc.table import NotDefinedColumn, TypeMismatch


Case1 = bqsc.load("tests/resources/case1.json")


def test_set():
    table = Case1()
    table.id = [1, 2]
    table.name = ["dog", "cat"]
    table.value = [1.1, 2.2]
    table.datetime = [datetime(2020, 1, 1), datetime(2020, 1, 2)]
    table.date = [date(2020, 1, 1), date(2020, 1, 2)]
    table.time = [time(0, 0, 1), time(0, 0, 2)]
    table.timedelta = [timedelta(days=1), timedelta(days=2)]


def test_mismatch():
    table = Case1()
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

    try:
        table.datetime = "a"
    except TypeMismatch:
        pass

    try:
        table.date = "a"
    except TypeMismatch:
        pass

    try:
        table.time = "a"
    except TypeMismatch:
        pass

    try:
        table.timedelta = "a"
    except TypeMismatch:
        pass


def test_no_definition():
    table = Case1()
    try:
        table.hoge = "x"
        assert False
    except NotDefinedColumn:
        pass
