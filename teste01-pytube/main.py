import os
import tkinter as tk
from time import sleep
from pytube import YouTube

LINK_ = 'https://www.youtube.com/shorts/wS5guAl4T64'

class Aplication:
    def __init__(self, link_youtube: str = None) -> None:
        while True: 
            try: # Adiciona a URl youtube a class Youtube
                self._yt = YouTube(link_youtube)
            except BaseException as error:
                print(f'Ocorreu um erro {error}')
            else:
                break
        # Cria a janela principal
        self.root = tk.Tk()
        self._screen()
        self._title_(f'Titulo do vídeo: ---> {self._yt.title} <---')
        # executa loop
        self.root.mainloop()
    
    def _screen(self) -> None:
        self.title = self.root.title('Youtube vídeo downloader')
        self.root.geometry('700x500')

    def _title_(self, text_: str) -> None:
        label = tk.Label(self.root, text=text_)
        label.pack(pady=20, padx=20)
        # print('==='*20)
        # print(text)
        # print('==='*20)    
    
    def _download_video(self, streams):
        pass

    def _download_audio(self):
        pass


if __name__ == '__main__':
    # App(input('link youtube: '))
    Aplication(LINK_)