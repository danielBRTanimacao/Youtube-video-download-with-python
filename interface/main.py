# import os
import tkinter as tk
import pytube
import os
from tkinter import messagebox
from pytube import YouTube

# maybe i'll refactor 
LINK_ = 'https://www.youtube.com/shorts/wS5guAl4T64'

class Functions: #funções do app
    def send_link(self) -> None:
        youtube_video_link = self.link_entry.get()
        self.link_entry.delete(0)
        # recebe o link de entrada
        # Adiciona a URl youtube a class >>> Youtube <<<
        try:
            self.yt = YouTube(youtube_video_link)
            name_title_video = self.yt.title
            self.options_download(name_title_video) # function recebe titulo do vídeo
        except pytube.exceptions.RegexMatchError:
            messagebox.showerror('Error link', 'Erro por favor tente de novo!')

    def options_download(self, _title_video: str) -> None:
        # elimina todos os textos e labels anteriores
        self.send_.destroy()
        self.link_entry.destroy()
        self.label_title.destroy()
        # inicia uma nova caixa com os tipos de downloads disponiveis
        self.label_correct_link = tk.Label(self.frame1, text=f'Titulo do vídeo {_title_video}')
        self.label_correct_link.pack(pady=40, padx=40)
        self.download_video()
        self.download_audio()
    
    def download_video(self):
        self.label_resolution = tk.Label(self.frame1, text=self.yt.streams.get_highest_resolution())
        self.label_resolution.pack(pady=40, padx=40)
    
    def download_audio(self):
        self.label_audio = tk.Label(self.frame1, text=self.yt.streams.filter(only_audio=True).first())
        self.label_audio.pack(pady=40, padx=40)
        # baixa o arquivo
        out_file = self.yt.download()
        # salva o arquivo em mp3
        base, ext = os.path.splitext(out_file) 
        new_file = base + '.mp3'
        os.rename(out_file, new_file) 


class Aplication(Functions):
    def __init__(self) -> None:
        self.root = tk.Tk()
        self._screen() # tela principal junto a configurações basicas
        self._screen_frames() # caixa principal da tela
        self._send_link_widgets()
        # executa loop
        self.root.mainloop()
    
    def _screen(self) -> None:
        self.title = self.root.title('Youtube vídeo downloader')
        self.root.configure(background='#801811')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)
    
    def _screen_frames(self) -> None:
        self.frame1 = tk.Frame(self.root, bd=4, bg='#ad372f',
                               highlightbackground='#fff', highlightthickness=6)
        self.frame1.place(relx=.02, rely=.05, relwidth=.96, relheight=.9)
    
    def _send_link_widgets(self) -> None:
        # Botão para enviar o link str
        self.send_ = tk.Button(self.frame1, text='Enviar', bd=2, bg='#c7310c', fg='#fff', command=self.send_link)
        self.send_.place(relx=.44, rely=.45, relwidth=.15, relheight=.15)
        # entrada link
        self.link_entry = tk.Entry(self.frame1)
        self.link_entry.place(relx=.2, rely=.2, relwidth=.6, relheight=.1)
        # label entrada 
        self.label_title = tk.Label(self.frame1, text='Coloque aqui abaixo o link do vídeo')
        self.label_title.pack(pady=45, padx=20)


if __name__ == '__main__':
    Aplication()
