# import os
import tkinter as tk
from time import sleep
from pytube import YouTube

LINK_ = 'https://www.youtube.com/shorts/wS5guAl4T64'

class Functions: #funções do app
    def send_link(self) -> None:
        youtube_video_link = self.link_entry.get()
        # adquiri o link de entrada
        try: # Adiciona a URl youtube a class Youtube
            self.yt = YouTube(youtube_video_link)
            name_video = self.yt.title
            self.label_text_ = tk.Label(self.frame1, text=f'Titulo do vídeo: {name_video}').pack(pady=45, padx=20)
        except BaseException:
            self.label_text_ = tk.Label(self.frame1, text=f'Ocorreu um erro! por favor tente de novo...').pack(pady=45, padx=20)


class Aplication(Functions):
    def __init__(self) -> None:
        # Adiciona a URl youtube a class Youtube
        self.root = tk.Tk()
        self._screen()
        self._screen_frames()
        self._title_('Coloque aqui abaixo o link do vídeo')
        self._send_link_widgets()
        # executa loop
        self.root.mainloop()
    
    def _screen(self) -> None:
        self.title = self.root.title('Youtube vídeo downloader')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)
    
    def _screen_frames(self) -> None:
        self.frame1 = tk.Frame(self.root, bd=4, bg='#dfe3ee',
                               highlightbackground='#759fe6', highlightthickness=3)
        self.frame1.place(relx=.02, rely=.05, relwidth=.96, relheight=.46)

    def _title_(self, text_: str) -> None:
        label = tk.Label(self.frame1, text=text_)
        label.pack(pady=45, padx=20)
    
    def _send_link_widgets(self) -> None:
        self.send_ = tk.Button(self.frame1, text='Enviar', bd=2, bg='#591C21', fg='white', command=self.send_link)
        self.send_.place(relx=.44, rely=.52, relwidth=.1, relheight=.15)
        # entrada link
        self.link_entry = tk.Entry(self.frame1)
        self.link_entry.place(relx=.2, rely=.33, relwidth=.6, relheight=.15)

        # self._yt = YouTube(LINK_)
        # self._title_(f'Titulo do vídeo: ---> {self._yt.title} <---')


if __name__ == '__main__':
    Aplication()