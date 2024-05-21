from flask import Blueprint, render_template, request
from pytube import YouTube

home_route = Blueprint('home', __name__)

@home_route.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        q = request.form['q']
        yt = YouTube(q)
        list_ofv = yt.streams.filter(file_extension='mp4', progressive="False")
        return render_template('index.html', list_videos=list_ofv)
    return render_template('index.html')