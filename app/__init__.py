# !!START
from flask import Flask, render_template
from .config import Config
from .tweets import tweets
from random import randint

app = Flask(__name__)

app.config.from_object(Config)
# !!END

@app.route('/')
def index():
    idx = randint(0, len(tweets))
    randomTweet = tweets[idx]
    return render_template('index.html', tweet=randomTweet)

@app.route('/feed')
def feed():
    return render_template('feed.html', tweets=tweets)
