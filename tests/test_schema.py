import bqsc


def test_schema():
    cls = bqsc.load("tests/resources/case1.json")
    assert cls.__name__ == "Case1"
