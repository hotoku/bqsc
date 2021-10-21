#!/bin/sh -l


poetry run node node_modules/pyright/index.js di_predict tests
echo ::set-output name=exit-code::$?
