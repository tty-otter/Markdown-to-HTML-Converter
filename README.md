Markdown to HTML Converter

概要

このプロジェクトは、Markdown ファイルを HTML ファイルに変換するシンプルなコマンドラインツールです。

Python とオープンソースライブラリ python-markdown を使用しており、初心者でもコードの流れを追いやすい構成になっています。

⸻

特徴
	•	Markdown（.md）ファイルを HTML に変換
	•	コマンドラインから実行可能
	•	表（table）記法に対応
	•	出力先が不正な場合のフォールバック処理あり
	•	小規模・学習用途に適した設計

⸻

動作環境
	•	Python 3.9 以上（推奨: Python 3.12）
	•	Linux / macOS / Windows

⸻

使用しているライブラリ

python-markdown

Markdown 形式のテキストを HTML に変換するためのオープンソースライブラリです。
	•	PyPI: https://pypi.org/project/Markdown/

⸻

インストール方法

1. Python と pip の準備

Debian / Ubuntu 系 Linux の場合：

sudo apt update
sudo apt install python3 python3-pip

仮想環境（venv）を使用している場合は、pip が有効になっていることを確認してください。

⸻

2. python-markdown のインストール

pip install markdown


⸻

使い方

コマンド形式

python3 markdownToHTMLConverter.py markdown <input_filepath> <output_filepath>

実行例

python3 markdownToHTMLConverter.py markdown sample.md output.html

	•	sample.md : 変換元の Markdown ファイル
	•	output.html : 変換後の HTML ファイル

⸻

対応している Markdown 記法
	•	見出し（#〜#####）
	•	太字・リスト
	•	番号付きリスト
	•	水平線
	•	テーブル（tables 拡張を有効化）

⸻

エラー処理について
	•	入力ファイルが存在しない場合はエラーメッセージを表示
	•	出力先に書き込めない場合は output.html を自動生成
	•	引数が不正な場合は使用例を表示

⸻

ファイル構成例

.
├── markdownToHTMLConverter.py
├── sample.md
├── output.html
└── README.md


⸻

学習目的でのポイント
	•	sys.argv を使ったコマンドライン引数処理
	•	try / except による例外処理
	•	関数分割による責務の明確化
	•	外部ライブラリ（pip）の利用方法

⸻

ライセンス

このプロジェクトは学習目的のサンプルコードです。
自由に改変・利用してください。

⸻

シェア

「Markdown to HTML Converter」をぜひシェアしてください。# Markdown-to-HTML-Converter
