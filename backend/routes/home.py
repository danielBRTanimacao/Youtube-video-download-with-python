from flask import Blueprint, render_template, request
from pytube import YouTube
from pytube.exceptions import RegexMatchError

home_route = Blueprint('home', __name__)

@home_route.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        q = request.form['q'].strip()
        try:
            yt = YouTube(q)
            title_video = yt.title
            url_thumb = yt.thumbnail_url
            list_videos = yt.streams
            return render_template('index.html', list_videos=list_videos, title_video=title_video, url_thumb=url_thumb)
        except RegexMatchError:
            return render_template('index.html', error="Erro: URL invalida!")
        except AttributeError:
            return render_template('index.html', error="Erro: atributo invalido na URL, tente novamente!")
    return render_template('index.html')