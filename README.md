# template-python-simple

Pythonツール開発用テンプレート。

## 実行方法

```sh
python ./main/my/app.py
```

もしくは

```sh
make start
```

## 開発方法

### Poetry導入

開発環境に[`Poetry`](https://cocoatomo.github.io/poetry-ja/basic-usage/)が無ければ入れる。使い方まとめは[こちら](https://github.com/mozkzki/poetry-sample/blob/main/README.md)。

Poetryの導入 (Mac, Linux)

```bash
> curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

Poetryの導入 (Windows) ※Powershell

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
pytest -v --capture=no --cov-config .coveragerc --cov=main --cov-report=xml --cov-report=term-missing .
```

もしくは

```sh
make ut
```

VSCodeでコードカバレッジを見るには、Coverage Gutters (プラグイン) を入れる。表示されない場合は、コマンドパレットで`Coverage Gutters: Display Coverage`する。

- [VSCodeでカバレッジを表示する（pytest-cov）](https://zenn.dev/tyoyo/articles/769df4b7eb9398)

### Lint

```sh
flake8 --max-line-length=100 --ignore=E203,W503 ./main
```

もしくは

```sh
make lint
```

## 参考

- [基本的な使い方 - Poetry documentation (ver. 1.1.6 日本語訳)](https://cocoatomo.github.io/poetry-ja/basic-usage/)
- [Configuration — pytest documentation](https://docs.pytest.org/en/6.2.x/customize.html)
- [Usage and Invocations — pytest documentation](https://docs.pytest.org/en/6.2.x/usage.html)
