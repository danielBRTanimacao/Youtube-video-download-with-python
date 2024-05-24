from flask import Blueprint, render_template, request
from pytube import YouTube
from pytube.exceptions import RegexMatchError, AgeRestrictedError, VideoUnavailable

home_route = Blueprint('home', __name__)

@home_route.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        q = request.form['q']
        try:
            yt = YouTube(q)
            title_video = yt.title
            url_thumb = yt.thumbnail_url
            list_videos = yt.streams
            return render_template('index.html', list_videos=list_videos, title_video=title_video, url_thumb=url_thumb, url=q)
        except RegexMatchError:
            return render_template('index.html', error="Erro: URL invalida!")
        except AttributeError:
            return render_template('index.html', error="Erro: atributo invalido na URL, tente novamente!")
        except AgeRestrictedError:
            return render_template('index.html', error="Erro: vídeo bloqueado por idade, tente novamente!")
        except VideoUnavailable:
            return render_template('index.html', error="Erro: vídeo invalido, tente novamente!")
    return render_template('index.html')

@home_route.route('/download', methods=['POST'])
def download():
    r = request.form['r']
    v = request.form['v']
    yt = YouTube(v)
    stream = yt.streams.get_by_itag(r)
    stream.download()
    return render_template('index.html')
# tentar salvar o link aqui para baixar