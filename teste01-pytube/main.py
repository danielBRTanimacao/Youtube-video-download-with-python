import os
from time import sleep
from pytube import YouTube

# link_youtube = str(input('Link: '))
link_youtube = 'https://youtu.be/UQ-gEZoed-c?si=R_dn7GzE68-IRMNU'
yt = YouTube(link_youtube)

def title_(text: str) -> None:
    print('==='*20)
    print(text)
    print('==='*20)


def downloading_video(streams_: yt) -> None:
    os.system('cls')
    print('carregando...')
    list_quality_video = streams_.streams.filter(file_extension='mp4').order_by('resolution')
    title_('Escolha a qualidade do vídeo!')
    for numbers, qualitys in enumerate(list_quality_video):
        print(f'Número {numbers+1} Qualidade {qualitys}')
    try:
        choice_resolution = str(input('qualidade do video resolução disponivel: '))
        print('Aguarde.... o download ira ser feito')
        stream_download = streams_.streams.get_by_resolution(choice_resolution)
        stream_download.download()
        print('Download concluido!')
    except BaseException as erro:
        os.system('cls')
        print(f'Ocorreu um erro por favor tente de novo erro {erro}')
        sleep(2)


def downloading_audio(audio_: yt) -> None:
    os.system('cls')
    print('O audio que sera baixado e o de melhor qualidade mp3 disponivel do vídeo')
    audio_download = audio_.streams.filter(only_audio=True).first()
    out_file_download = audio_download.download()
    name_base, out_point = os.path.splitext(out_file_download)
    new_file_download = name_base + '.mp3'
    os.rename(out_file_download, new_file_download)
    print('Download concluido...')
    sleep(2)


if __name__ == '__main__':
    while True:
        title_(f'Titulo do vídeo --> {yt.title}')
        print("Você Deseja baixar o Vídeo ou o Audio digite 'V' ou 'A'")
        question = str(input('Video [V] | Audio [A] | Sair [S]: ')).upper()[0]
        if 'V' in question:
            downloading_video(yt)
        elif 'A' in question:
            downloading_audio(yt)
        elif 'S' in question:
            os.system('cls')
            print('saindo do programa...')
            break
        else:
            os.system('cls')
            print('Por favor tente novamente! o caractere digitado não existe')
            sleep(2)
            continue
