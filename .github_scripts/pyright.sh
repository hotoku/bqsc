#!/bin/sh -l


poetry run node node_modules/pyright/index.js ${GITHUB_REPOSITORY_NAME_SLUG} tests
echo ::set-output name=exit-code::$?
