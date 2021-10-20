from dataclasses import dataclass
from typing import Iterable, Optional
import glob
import os

import click

from .table import Table, typehint
from .load import load, load_bq


@click.group()
def main():
    pass


def print_typehint(tables: Iterable[Table]):
    ret = """from typing import Sequence, Union
from datetime import date, datetime, time, timedelta

from bqsc import Table
"""

    for t in tables:
        ret += typehint(t) + "\n" * 2
    print(ret)


@main.command()
@click.argument("json_dir", type=click.Path(file_okay=False, readable=True))
def dir(json_dir: str):
    if not os.path.isdir(json_dir):
        raise ValueError(f"{json_dir} is not a directory")
    print_typehint([
        load(js)()
        for js in glob.glob(os.path.join(json_dir, "**.json"))
    ])


@dataclass
class TableRepr:
    project: Optional[str]
    dataset: str
    table: str


def parse_table(s: str) -> TableRepr:
    pos = s.find(":")
    if pos > 0:
        proj = s[:pos]
        s = s[(pos + 1):]
    else:
        proj = None
    pos = s.find(".")
    if pos < 1:
        raise ValueError(
            f"table format should be [project:]dataset.table: given value = {s}")
    ds = s[:pos]
    table = s[(pos+1):]
    return TableRepr(proj, ds, table)


@main.command()
@click.argument("table", type=str)
def bq(table: str):
    rep = parse_table(table)
    ty = load_bq(rep.project, rep.dataset, rep.table)()
    print_typehint([ty])


if __name__ == "__main__":
    main()
