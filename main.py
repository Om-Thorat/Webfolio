from flask import Flask,render_template,Response,redirect
import spotipy
from spotipy import util
from pathlib import Path
import re
import base64
from PIL import Image
import requests
from io import BytesIO


cwd = Path.cwd()
cwd = re.sub(r"\\",r"/",str(cwd))
CLIENT_ID = 'xxxx'
CLIENT_SECRET = 'xxxx'
username = "aqowup3436r3wevile0yvclmk"
scope = "user-read-playback-state user-read-recently-played"
redirect_uri = "http://127.0.0.1:5000/spotify/"
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

def spotify():
    token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET, redirect_uri,cache_path=f"{cwd}/static/token.txt")
    sp = spotipy.Spotify(auth=token)
    try:
        current = (sp.current_playback())
        songname = (current['item']['name'])
        artist = (current['item']['artists'][0]['name'])
        cover = (current['item']['album']['images'][0]['url'])
        return ["now playing",songname,cover,artist]
    except:
        print("huh")
        current = sp.current_user_recently_played(limit=1)
        songname = (current['items'][0]['track']['name'])
        artist = (current['items'][0]['track']['artists'][0]['name'])
        cover = (current['items'][0]['track']['album']['images'][0]['url'])
        return ["last played",songname,cover,artist]

@app.route('/spotify')
def cool():   
        info = spotify()
        response = requests.get(info[2])
        img = Image.open(BytesIO(response.content))
        img.save("./tmp/haha",format="JPEG")
        with open("./tmp/haha","rb") as img_file:
            imgstr = base64.b64encode(img_file.read()).decode()
        aight = """
<svg width="500px" height="190px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<style>
.main{
display: flex;
flex-direction: row;
align-items: center;
background: #6666CC;
border-radius: 20px;
}
img{
padding:20px;
border-radius:50px;
filter: drop-shadow(2px 4px 6px #393972);
}
.info{
display: flex;
flex-direction: column;
}
.song{
    color: #FFFF00;
    font-size: x-large;
}
.artist{
    color: #CCFFFF;
}</style>
<g>
<rect xmlns="http://www.w3.org/2000/svg"/>
<g>
<foreignObject width="500px" height="190px">
<div xmlns="http://www.w3.org/1999/xhtml">
<div class="main">
<img class="pic" src="data:image/jpg;base64,%s" width="150px"></img>
<div class="info" xmlns="http://www.w3.org/1999/xhtml"><a xmlns="http://www.w3.org/1999/xhtml" class="song" >%s</a><a class="artist" xmlns="http://www.w3.org/1999/xhtml">by %s</a></div>
</div>
</div>
</foreignObject>
</g>
</g>
</svg>
"""%(imgstr,info[1],info[3])
        return Response(aight,mimetype='image/svg+xml')

@app.route('/spotifyinfo')
def info():
    return spotify()
@app.errorhandler(404)
def NotFound(e):
    return render_template('404.html')
# app.run(debug=True)