# これは何？
xlsxのデータを取り込む際に、プログラミングを行わずにjinja2経由でテキストデータに変換するモジュールとコマンドラインツールです。

# 利用例

以下の３つを用意することで利用できます。

ソースデータ(source data): 変換元のデータが入ったxlsxファイル
<img


ソーステンプレート(source template): ソースデータと同じワークシートやセルのレイアウトにしたものにテンプレート変数を埋め込んだxlsxファイル
<img

エクスポートテンプレート(export template):jinja2のテンプレート変数を埋め込んだテキストファイル(htmlやjson, csvなど)

※:jinja2のテンプレートは現在は変数のみ対応です。ドットによるネストやフィルターなどの対応は未確認です。

```html


```

ソーステンプレートとエクスポートテンプレートで利用するテンプレート変数名は同じにすることでマッピングを行い変換されます。

```html
<!--結果をこちらに貼り付ける-->

```

# インストール

venvやvirtualenvなどの仮想環境上での利用をおすすめします

```
pip install xlsx2txt
```

# コマンドの利用方法
```
(env) myworksation: example$ python xlsx2txt-cli.py --help
Usage: xlsx2txt-cli.py [OPTIONS] SRC_TEMPLATE SRC_DATA EXPORT_TEMPLATE

Options:
  --export_filename TEXT  Set export filename
  --help                  Show this message and exit.
```

`--export_filename` はエクスポートしたファイルの名前を指定します。指定しない場合は exported_data.txtというファイル名を作成します。

# ライブラリの利用方法
実際の利用方法を書いていく。
xlsx2txtはライブラリとしても利用できます。

cli

# このコマンド,ライブラリはα版です
α版のためライブラリのAPIやコマンドの仕様は定まっておらず、変更される恐れがあります。

# Future Work

- 各OS向けのバイナリを用意
- データの羅列に対応できるテンプレートの追加
- （何かしらの方法で）GUIフロントエンドを別途用意する
- APIのドキュメントを用意する

# ライセンス
MIT License

# 利用ライブラリ

- 
- click


