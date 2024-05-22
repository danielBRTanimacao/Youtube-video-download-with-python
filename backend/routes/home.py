from flask import Blueprint, render_template, request
from pytube import YouTube

home_route = Blueprint('home', __name__)

@home_route.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        q = request.form['q']
        try:
            yt = YouTube(q)
            title_video = yt.title
            url_thumb = yt.thumbnail_url
            list_ofv = yt.streams.filter(file_extension='mp4', progressive=False)
            return render_template('index.html', list_videos=list_ofv, title_video=title_video, url_thumb=url_thumb)
        except:
            return render_template('index.html', error="URL invalida!")
    return render_template('index.html')