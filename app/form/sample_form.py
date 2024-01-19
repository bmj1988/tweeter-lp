from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

v = [DataRequired()]

class Tweet(FlaskForm):
    author = StringField('author', validators=v)
    tweet = StringField('tweet', validators=v)
    submit = SubmitField('Create Tweet', validators=v)
