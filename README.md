# Fletやってみた

GTUG Girlsのもくもく会にて  
https://gtuggirls.connpass.com/event/273502/

Fletをやってみた  
https://flet.dev/

## やった手順
### 0. エディタ入れる
JetBrainsが好きだからPyCharm入れた

### 1. 仮想環境を作る
```
$ python3 -m venv .venv
```

### 2. 仮想環境をアクティベートする
```
$ source .venv/bin/activate
```

### 3. Pythonの向き先確認
```
$ which python
```

### 4. パッケージ管理できるようにする
```
$ mkdir requirements.txt
```

requirements.txtは以下
```text
flet
```

### 5. requirements.txtの内容をインストールする
```
$ pip install -r requirements.txt
```

### 6. インストールしたパッケージを確認する
```
$ pip freeze
```

### 7. pipの更新をしておく
```
$ pip install --upgrade pip
```

### 8. 実行
```
$ python main.py
```

### 9. Fletやってみる
このチュートリアルにそってやってみた〜  
https://flet.dev/docs/guides/python/getting-started

以下でアプリみたいな画面が立ち上がる
```python
ft.app(target=main)
```

こっちだとブラウザで表示できる
```python
ft.app(target=main, view=ft.WEB_BROWSER, port=8550)
```

以下で画面がアップデートされる
```python
page.update()
```

以下だとTextFieldのアップデートになる
```python
new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
new_task.update()
```

以下で画面にチェックボックスを追加する
```python
page.add(ft.Checkbox(label=new_task.value))
```

Columnで縦に並べられる（Rowは横
```python
greetings = ft.Column()
```
