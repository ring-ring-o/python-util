# python utils
- pythonや関連ライブラリで使用するちょっとした処理をまとめておくプロジェクト
- 基本的にはコピペで利用する

## 実行方法
- 実際に実行する場合は以下の手順で環境を作成する

1. プロジェクトルートでdevcontainerを起動する
2. 仮想環境の作成と依存関係の解決を行う
```bash
rye sync
```
3. pythonモジュールを実行する
```bash
rye run python src/pydantic-helper.py
```
3. 仮想環境を有効にする
```bash
. ./venv/bin/activate
```
