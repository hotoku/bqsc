from typing import Type, Union
from pathlib import Path
import re
import json

from .column_info import ColumnInfo
from .table import Table


def snake_to_camel(s: str) -> str:
    return "".join([x.title() for x in s.split("_")])


def load(s: Union[str, Path]) -> Type:
    path = Path(s)
    file = path.as_posix().split("/")[-1]
    body = re.sub(r".json$", "", file)
    name = snake_to_camel(body)
    with open(path) as fp:
        content = "".join(fp.readlines())
    return loads(content, name)


def loads(s: str, name: str) -> Type:
    obj = json.loads(s)
    cols = [
        ColumnInfo.create(d) for d in obj
    ]

    def __init__(self):
        Table.__init__(self, cols)

    return type(name, (Table,), {
        "__init__": __init__
    })
