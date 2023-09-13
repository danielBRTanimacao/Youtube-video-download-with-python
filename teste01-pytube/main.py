import os
import tkinter as tk
from time import sleep
from pytube import YouTube

LINK_ = 'https://www.youtube.com/shorts/wS5guAl4T64'

class App:
    def __init__(self, link_youtube: str = None):
        # Cria a janela principal e executa loop
        self.root = tk.Tk()
        self.title = self.root.title('Youtube vídeo downloader')
        self.root.mainloop()

        while True: 
            try: # Adiciona a URl youtube a class Youtube
                self._yt = YouTube(link_youtube)
            except BaseException as error:
                print(f'Ocorreu um erro {error}')
            else:
                break
        
    def download_video(self):
        pass

    def download_audio(self):
        pass

if __name__ == '__main__':
    # app = App(input('link youtube: '))
    App(LINK_)