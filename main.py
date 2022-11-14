from flask import Flask,render_template
import spotipy
from spotipy import util
from pathlib import Path
import re

cwd = Path.cwd()
cwd = re.sub(r"\\",r"/",str(cwd))
CLIENT_ID = 'XXXX'
CLIENT_SECRET = 'XXXX'
username = "aqowup3436r3wevile0yvclmk"
scope = "user-read-playback-state user-read-recently-played"
redirect_uri = "http://127.0.0.1:5000/spotify/"
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/spotify')
def spotify():
    token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET, redirect_uri,cache_path=f"{cwd}/static/token.txt")
    sp = spotipy.Spotify(auth=token)
    try:
        current = (sp.current_playback())
        songname = (current['item']['name'])
        artist = (current['item']['artists'][0]['name'])
        cover = (current['item']['album']['images'][0]['url'])
        return ['Now Playing',songname,artist,cover]
    except:
        current = sp.current_user_recently_played(limit=1)
        songname = (current['items'][0]['track']['name'])
        artist = (current['items'][0]['track']['artists'][0]['name'])
        cover = (current['items'][0]['track']['album']['images'][0]['url'])
        return ["last Played",songname,artist,cover]