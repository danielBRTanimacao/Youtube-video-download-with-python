import flet as ft

from utils.validators import url_validator

def main(page: ft.Page):
    page.title = "Youtube vídeo downloader"
    
    def submit_link(e):
        if not url_input.value or not url_validator(url_input.value):
            url_input.error_text = "Cole aqui uma URL valida!"
            page.update()
        else:
            link_video = url_input.value
            page.clean()
            page.add(ft.Text(f"Link do video: {link_video}"))

    url_input = ft.TextField(label="URL youtube")

    page.add(url_input, ft.ElevatedButton("Enviar", on_click=submit_link))

ft.app(target=main)