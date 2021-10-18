from typing import Optional, Sequence, Union
import glob
import os


import click

from .table import typehint
from .load import load


@click.command()
@click.argument("json_dir", type=click.Path(file_okay=False, readable=True))
def main(json_dir: str):
    ret = """from typing import Sequence, Union
from datetime import date, datetime, time

"""
    for js in glob.glob(os.path.join(json_dir, "**.json")):
        Table = load(js)
        table = Table()
        ret += typehint(table) + "\n" * 2

    print(ret)


if __name__ == "__main__":
    main()
