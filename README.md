# ChatDev
ChatGPTの可能性を検証してみる

コマンド生成からの実行により、アプリ開発に必要な手順のほぼ全てをChatGPTが実行できることを目指します

- アプリを構成するソースコードのファイル構成を考える
- 構成に従ってフォルダ・ファイルを作成する
- ファイルにソースコードを書き込む
- ソースコードのバグを修正する
- 仕様変更に対応する


# コマンド説明

### use [dir_path]
- ディレクトリを登録します。
- 以降のコマンドでは、ディレクトリを相対パスで書くことが可能になります。
- 同じディレクトリを扱う場合はコマンドでの記述が不要になります。

### createFile [path] [filename]
- 指定したディレクトリに、指定したファイル名で空のファイルを作成します。
- ディレクトリの指定方法は、useコマンドで登録した相対パス、もしくは絶対パスを指定します。

### editFile [filename]
- 指定したファイルに文字を入力します。
- ファイルの指定方法は、useコマンドで登録した相対パス、もしくは絶対パスを指定します。
- saveFileコマンドとの間にあるテキストをそのまま入力します。

# コマンド例
現時点では、config.txtに入れてmain.pyを実行すると実行できます

フォルダは適宜変えてください
```
use D:\Ais\sample_app
createFile run_hello.bat
editFile run_hello.bat
@echo off
python hello.py
pause
saveFile
createFile hello.py
editFile hello.py
print("Hello, World!")
saveFile
```

# Todo
- コマンドのみを出力させるプロンプト文
- コマンドによる「既存のコードがあるファイル」の編集
- 長文への対応（特に大規模なコードを記述するとき、ChatGPTの現性能では途切れがち。何らかのプロンプトなどによる対応が必要）
- フォルダの生成、ファイルコピーなどの機能充実
- コマンド生成を裏手に回したい（言語と実物アプリのみでやりとりしたい）
