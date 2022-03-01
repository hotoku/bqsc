from typing import Dict, List, Optional, TextIO, Type, Union
from pathlib import Path
import re
import json
import glob
import os
import subprocess as sp
from io import StringIO
import logging


from .table_info import TableInfo
from .column_info import ColumnInfo
from .table import Table

LOGGER = logging.getLogger(__name__)


def snake_to_camel(s: str) -> str:
    return "".join([x.title() for x in s.split("_")])


def load(fp: TextIO, name: str) -> Type[Table]:
    content = "".join(fp.readlines())
    return loads(content, name)


def load_file(s: Union[str, Path]) -> Type[Table]:
    path = Path(s)
    file = path.as_posix().split("/")[-1]
    body = re.sub(r".json$", "", file)
    name = snake_to_camel(body)
    with open(path) as fp:
        return load(fp, name)


def load_bq(project: Optional[str], dataset: str, table: str) -> Type[Table]:
    cmd = [
        "bq", "show"
    ]
    if project is not None:
        cmd += [f"--project_id={project}"]
    cmd += [
        "--schema",
        f"--format=prettyjson",
        f"{dataset}.{table}"
    ]
    ret = sp.run(
        cmd,
        text=True,
        stdout=sp.PIPE,
        stderr=sp.PIPE
    )
    if ret.returncode != 0:
        raise RuntimeError(
            f"command: {' '.join(cmd)} failed. stdout={ret.stdout}, stderr={ret.stderr}")
    return loads(ret.stdout, snake_to_camel(table))


def loads(s: str, name: str) -> Type[Table]:
    obj = json.loads(s)
    return from_schema(obj, name)


def from_schema(ls: List[Dict[str, str]], name) -> Type[Table]:
    cols = [
        ColumnInfo.create(d) for d in ls
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


Schema = List[Dict[str, str]]


def read_schema_file(file_path: Union[str, Path]) -> Schema:
    with open(str(file_path)) as f:
        return json.load(f)
