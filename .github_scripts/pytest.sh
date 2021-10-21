#!/bin/sh -l


. .venv/bin/activate
export PYTHONPATH=$(pwd)
pytest
echo ::set-output name=exit-code::$?
