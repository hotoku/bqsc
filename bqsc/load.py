from typing import Dict, Type, Union
from pathlib import Path
import re
import json
import glob
import os

from .table_info import TableInfo
from .column_info import ColumnInfo
from .table import Table


def snake_to_camel(s: str) -> str:
    return "".join([x.title() for x in s.split("_")])


def load(s: Union[str, Path]) -> Type[Table]:
    path = Path(s)
    file = path.as_posix().split("/")[-1]
    body = re.sub(r".json$", "", file)
    name = snake_to_camel(body)
    with open(path) as fp:
        content = "".join(fp.readlines())
    return loads(content, name)


def loads(s: str, name: str) -> Type[Table]:
    obj = json.loads(s)
    cols = [
        ColumnInfo.create(d) for d in obj
    ]
    nulls = {
        col.name: None for col in cols
        if col.mode.upper() == "NULLABLE"
    }

    tinfo = TableInfo(cols)
    return type(name, (Table,), {
        "_table_info": tinfo,
        **nulls
    })


def load_dir(json_dir: Union[str, Path]) -> Dict[str, Type[Table]]:
    ls = [load(js) for js in glob.glob(os.path.join(json_dir, "**.json"))]
    return {
        t.__name__: t for t in ls
    }
