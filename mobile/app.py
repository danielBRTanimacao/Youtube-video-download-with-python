import flet as ft

from utils.validators import url_validator

def main(page: ft.Page):
    page.title = "Python vídeo downloader"
    title_principal = ft.Row(
        [
            ft.Icon(ft.icons.PLAY_ARROW, size=35, color="red"),
            ft.Text(
                "Youtube vídeo downloader",
                size=30,
                weight=ft.FontWeight.BOLD,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    
    def submit_link(e):
        if not url_input.value or not url_validator(url_input.value):
            url_input.error_text = "Cole aqui uma URL valida!"
            page.update()
        else:
            link_video = url_input.value
            page.clean()
            page.add(
                ft.Text(f"Link do video: {link_video}")
            )

    url_input = ft.TextField(label="URL youtube")

    page.add(
        ft.Container(
        title_principal,
        padding=15,
        alignment=ft.alignment.center
        ),
        url_input,
        ft.Container(
            ft.ElevatedButton(
                "Enviar",
                on_click=submit_link,
                style=ft.ButtonStyle(
                    padding=ft.padding.symmetric(10, 150)
                )
            ),
            alignment=ft.alignment.center,
        )
    )

ft.app(target=main)