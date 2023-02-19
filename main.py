import time

import flet as ft


def show_loading(page):
    pass


def show_hello_world(page):
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()


def show_counter(page):
    t = ft.Text()
    page.add(t)

    for i in range(10):
        t.value = f"Step {i}"
        page.update()
        time.sleep(1)


def show_abc(page):
    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )


def show_button(page):
    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )


def show_counter_and_pop(page):
    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0)
        page.update()
        time.sleep(0.3)


def show_text_when_click(page):
    def button_clicked(e):
        page.add(ft.Text("Clicked!"))

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))


def show_checkbox(page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))


def show_disable_field(page):
    first_name = ft.TextField()
    last_name = ft.TextField()
    first_name.disabled = True
    last_name.disabled = True
    page.add(first_name, last_name)


def show_disable_fields(page):
    first_name = ft.TextField()
    last_name = ft.TextField()
    c = ft.Column(controls=[
        first_name,
        last_name
    ])
    c.disabled = True
    page.add(c)


def show_name(page):
    first_name = ft.TextField(label="First name", autofocus=True)
    last_name = ft.TextField(label="Last name")
    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        greetings,
    )


def show_ref_name(page):
    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()

    def btn_click(e):
        greetings.current.controls.append(
            ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!")
        )
        first_name.current.value = ""
        last_name.current.value = ""
        page.update()
        first_name.current.focus()

    page.add(
        ft.TextField(ref=first_name, label="First name", autofocus=True),
        ft.TextField(ref=last_name, label="Last name"),
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        ft.Column(ref=greetings),
    )


def main(page: ft.Page):
    # ローディングを表示！
    # show_loading(page)

    # hello worldを表示！
    # show_hello_world(page)

    # counter的なやつ！
    # show_counter(page)

    # ただ表示するだけ！
    # show_abc(page)

    # ボタン付き！
    # show_button(page)

    # popで値消しつつ表示！
    # show_counter_and_pop(page)

    # ボタンクリックしたら表示されるやつ！
    # show_text_when_click(page)

    # ボタンクリックしたらチェックボックス追加されるやつ！
    # show_checkbox(page)

    # disabledにする！
    # show_disable_field(page)

    # いっぺんにdisabledにする！
    # show_disable_fields(page)

    # 名前入力して表示するやつ！
    # show_name(page)

    # refを使って表示する！（Reactのrefみたいなやつ
    show_ref_name(page)


ft.app(target=main)
# こっちだとブラウザで表示できる
# ft.app(target=main, view=ft.WEB_BROWSER, port=8550)
