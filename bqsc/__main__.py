from typing import Optional
import glob
import os


import click

from .load import load


@click.command()
@click.option("--pyi_path", type=click.Path(file_okay=False, writable=True))
@click.argument("json_dir", type=click.Path(file_okay=False, readable=True))
def main(pyi_path: Optional[str], json_dir: str):
    for js in glob.glob(os.path.join(json_dir, "**.json")):
        ty = load(js)
        print(ty._typehint())


if __name__ == "__main__":
    main()
