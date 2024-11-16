from time import sleep
import flet as ft

from utils.validators import url_validator
from utils.downloader import VideoHandler

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
            def download_video_event(e):
                page.clean()

                pb = ft.ProgressBar(width=400)
                page.add(
                    ft.Text(YT_MANAGER.get_best_av, style="headlineSmall"),
                    ft.Text("Fazendo download do vídeo", style="headlineSmall"),
                    ft.Column([ ft.Text("Doing something..."), pb]),
                )

                for i in range(0, 101):
                    pb.value = i * 0.01
                    sleep(0.1)
                    page.update()

            def download_audio_event(e):
                ...
                
            def download_playlist_event(e):
                ...

            page.clean()    
            link_video = url_input.value
            YT_MANAGER = VideoHandler(link_video)

            page.add(
                ft.Container(
                    ft.Column(
                        [
                            ft.Container(
                                ft.Image(
                                    src=YT_MANAGER.get_thumbnail_url,
                                    width=900,
                                    height=400,
                                    fit=ft.ImageFit.CONTAIN,
                                ),
                                alignment=ft.alignment.center,
                            ),
                            ft.Container(
                                ft.Text(f"Título: {YT_MANAGER.get_title}", size=20),
                                alignment=ft.alignment.center,
                            ),
                            ft.Row(
                                [
                                    ft.ElevatedButton("Baixar vídeo", on_click=download_video_event),
                                    ft.ElevatedButton("Baixar áudio", on_click=download_audio_event),
                                    ft.ElevatedButton("Baixar playlist", on_click=download_playlist_event),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=10,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    alignment=ft.alignment.center,
                )
            )
            page.update()

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