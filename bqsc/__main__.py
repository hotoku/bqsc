from typing import Optional, Sequence, Union
import glob
import os


import click

from .load import load


@click.command()
@click.option("--pyi_path", type=click.Path(file_okay=False, writable=True))
@click.argument("json_dir", type=click.Path(file_okay=False, readable=True))
def main(pyi_path: Optional[str], json_dir: str):
    ret = """from typing import Sequence, Union
from datetime import date, datetime, time

"""
    Sequence
    for js in glob.glob(os.path.join(json_dir, "**.json")):
        Table = load(js)
        table = Table()
        ret += table._typehint() + "\n" * 2

    print(ret)


if __name__ == "__main__":
    main()
