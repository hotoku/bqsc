#!/bin/sh -l


. .venv/bin/activate
pwd
ls
which pytest
which python
python -c "import sys; print(sys.path)"
export PYTHONPATH=$(pwd)
pytest
echo ::set-output name=exit-code::$?
