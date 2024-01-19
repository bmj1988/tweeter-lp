# !!START
from flask import (Flask, render_template, redirect)
from .config import Config
from .tweets import tweets
from random import randint
from .form.sample_form import Tweet
from datetime import date

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

@app.route('/new', methods=['GET', 'POST'])
def new_tweet():
    form = Tweet()
    id = len(tweets)

    if form.validate_on_submit():
        tweets.append({
        "id": id,
        "author":form.data["author"],
        "date": date.today(),
        "tweet":form.data["tweet"],
        "likes": 0})
        return redirect('/',302)
    if form.errors:
        return form.errors
    return render_template('new_tweet.html', form=form)
