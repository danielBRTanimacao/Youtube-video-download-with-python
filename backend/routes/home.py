from flask import Blueprint, render_template, request
from pytube import YouTube

home_route = Blueprint('home', __name__)

@home_route.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        q = request.form['q']
        yt = YouTube(q)
    return render_template('index.html')