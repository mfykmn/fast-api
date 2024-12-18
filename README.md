# fast-api
## 構成
```bash
.
├── routers
│     * APIエンドポイントをパスとハンドラーの組み合わせで定義する
└── schemas
      * APIのリクエストとレスポンスを、厳密な型と一緒に定義する
```

## 環境構築
* miniconda インストール
  * https://docs.anaconda.com/miniconda/install/#quick-command-line-install
* 仮想環境構築コマンド
  * `$ conda env list`
  * `$ conda create -n fastapi_env python=3.12`
  * `$ conda activate fastapi_env`
  * `$ conda deactivate`
  * `$ conda remove  -n fastapi_env --all`
* vscode
  * インタプリタをPython 3.12.7('fastapi_env')を選択
  * main.py　を右クリック　ターミナルで実行ができる
* webサーバーの起動
    ```bash
    $ pip install -r requirements.txt
    $ uvicorn main:app --reload
    $ curl http://127.0.0.1:8000
    $ open http://127.0.0.1:8000/docs
    ```

## 学習メモ
### ライブラリ
* FastAPI
  * アプリケーションフレームワーク
* Uvicorn
  * ASGI
  * Webサーバー 
* Pydantic
  * データの変換とバリデーション
* httpx
  * 外部APIなどにHTTPリクエストを送るための非同期対応ライブラリ
* SQLAlchemy
  * ORM
* aiosqlite
  * SQLiteデータベースを非同期IOで利用するためのライブラリ

### デコレータ
@app.get("/") みたいなやつ

### 型ヒント(type hints)
Python3.5以降の機能

Python3.8以前とPython3.9からでリストや辞書などの標準コレクションの型ヒント指定方法が変わっている
3.8以前はtypingモジュールを使用する必要があったが3.9からは不要

```python
def add(num1: int, num2: int) -> str:
    results: str = '足し算結果=>'
    return results + str(num1 + num2) 
```

#### Optional型
変数が特定の型を持つかNoneを持つ可能性がある場合に使用
3.5から導入

```python
from typing import Optional
def hoge(param: Optional[int] = None) -> Optional[int]:
```

#### Annotated
3.9以降で導入
型ヒントに追加情報や制約を加える
これだけだと開発者が気をつけるための情報という風に見えるが、ツールやライブラリを連携させて強力なチェックをしたりもできる?(プログラムの実行に影響を与えないのでは？？？) FastAPIの機能と連携できるらしい

```python
from typing import Annotated
def hoge(email: Annotated[str, "有効なメールアドレスの必要がある"]):
```

#### |(パイプ)演算子
3.10から
2つの型のいずれか

```python
def hoge(param: str | None) -> str:
```

'Optinal[str] = None'と 'str | None = None'は同じ
versionが3.10以上なら後者を採用するのがよさそう

### 型判定
```python
if isinstance(value, int):
  return f"値はint型です ${value}"
```

### dict
```python
return [{
  "id": book.id
  "title": book.title
} for book in result]
```

#### 辞書のアンパック
```python
data = {"id": 1, "name": "hogehoge"}
event = Event(**data) // **で展開できる
```

### enumerate
enumerateはリストなどの反復可能なオブジェクトをループする際に、現在のindexと要素の両方を取得できる
```python
for index, existing_book in enumerate(books)
```

### 非同期
asyncio を使う
#### async with
python 3.5 から使える
https://peps.python.org/pep-0492/#asynchronous-context-managers-and-async-with
https://stackoverflow.com/questions/67092070/why-do-we-need-async-for-and-async-with

### DB操作
`engine.begin()`でトランザクションを開始できる
