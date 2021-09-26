# template-python-simple

[![CircleCI](https://circleci.com/gh/mozkzki/template-python-simple/tree/main.svg?style=svg)](https://circleci.com/gh/mozkzki/template-python-simple/tree/main)
[![codecov](https://codecov.io/gh/mozkzki/template-python-simple/branch/main/graph/badge.svg?token=BRB5vsPkO2)](https://codecov.io/gh/mozkzki/template-python-simple)
[![Maintainability](https://api.codeclimate.com/v1/badges/df50bbce59225073a577/maintainability)](https://codeclimate.com/github/mozkzki/template-python-simple/maintainability)

Python開発用テンプレート。

| ツール種類 | ツール名 |
|--|--|
| 依存関係管理 | [Poetry](https://python-poetry.org/) |
| テストフレームワーク | [pytest](https://docs.pytest.org/en/6.2.x/) |
| リンター | [flake8](https://flake8.pycqa.org/en/latest/) |
| フォーマッター | [black](https://github.com/psf/black) |
| 型チェック | [mypy](https://mypy.readthedocs.io/en/stable/) |

## 実行方法

```sh
python ./src/app.py
# or
make start
```

※ Poetryはタスクランナー機能がないのでmakeで代用

## 開発方法

### [Poetry](https://cocoatomo.github.io/poetry-ja/basic-usage/)導入

開発環境に無ければ入れる。使い方まとめは[こちら](https://github.com/mozkzki/poetry-sample/blob/main/README.md)。

#### Mac / Linux

```bash
> curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

#### Windows (※Powershellで導入)

```Powershll
> (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

### 依存パッケージの一括インストール

```sh
poetry install
```

### 仮想環境に入る

lintやunit testは仮想環境に入って実行する。出るのは`exit`。

```sh
poetry shell
```

### とりあえず一通り動確したい時

```sh
make lint
make ut
make start
```

### Unit Test

全部実行

```sh
pytest
pytest -v # verbose
pytest -s # 標準出力を出す (--capture=noと同じ)
pytest -ra # サマリーを表示 (テストをpassしたもの以外)
pytest -rA # サマリーを表示 (テストをpassしたものも含む)
```

指定して実行  
(テストファイル名, パッケージ名, テストクラス名, メソッド名, 割と何でも拾ってくれる。部分一致でも。)

```sh
pytest -k app
pytest -k test_app.py
pytest -k my
```

マーカーを指定して実行

```sh
pytest -m 'slow'
pytest -m 'not slow'
```

カバレッジレポートも作成

```sh
pytest -v --capture=no --cov-config .coveragerc --cov=src --cov-report=xml --cov-report=term-missing .
# or
make ut
```

VSCodeでコードカバレッジを見るには、Coverage Gutters (プラグイン) を入れる。表示されない場合は、コマンドパレットで`Coverage Gutters: Display Coverage`する。

- [VSCodeでカバレッジを表示する（pytest-cov）](https://zenn.dev/tyoyo/articles/769df4b7eb9398)

### Lint

```sh
flake8 --max-line-length=100 --ignore=E203,W503 ./src ./tests
# or
make lint
```

### Create API Document (Sphinx)

```sh
make doc
```

### Update dependency modules

dependabot (GitHub公式) がプルリクを挙げてくるので確認してマージする。

- 最低でもCircleCIが通っているかは確認
- CircleCIでは、最新の依存モジュールでtestするため`poetry update`してからtestしている
- dependabotは`pyproject.toml`と`poetry.lock`を更新してくれる

## 参考

- [基本的な使い方 - Poetry documentation (ver. 1.1.6 日本語訳)](https://cocoatomo.github.io/poetry-ja/basic-usage/)
- [Configuration — pytest documentation](https://docs.pytest.org/en/6.2.x/customize.html)
- [Usage and Invocations — pytest documentation](https://docs.pytest.org/en/6.2.x/usage.html)
