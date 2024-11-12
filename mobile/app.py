import flet as ft

def main(page: ft.Page):
    page.title = "Youtube vídeo downloader"
    
    def submit_link(e):
        if not txt_name.value:
            txt_name.error_text = "Cole aqui uma URL valida!"
            page.update()
        else:
            link_video = txt_name.value
            page.clean()
            page.add(ft.Text(f"Link do video: {link_video}"))

    txt_name = ft.TextField(label="URL youtube")

    page.add(txt_name, ft.ElevatedButton("Enviar", on_click=submit_link))

ft.app(target=main)