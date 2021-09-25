#!/bin/sh

if [ -e docs/conf.py ]; then
    sphinx-apidoc -f -o docs/ src/app_name  # 2回目以降
else
    sphinx-apidoc -F -o docs/ src/app_name  # 初回実行
fi

sphinx-build -b singlehtml ./docs ./docs/_build
