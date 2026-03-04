import flet as ft

def main(page: ft.Page):
    page.title = "Contador Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Control que muestra el número
    txt_numero = ft.TextField(
        value="0",
        text_align=ft.TextAlign.RIGHT,
        width=100
    )

    def restar(e):
        txt_numero.value = str(int(txt_numero.value) - 1)
        page.update()

    def sumar(e):
        txt_numero.value = str(int(txt_numero.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(icon=ft.Icons.REMOVE, on_click=restar),
                    txt_numero,
                ft.IconButton(icon=ft.Icons.ADD, on_click=sumar),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)