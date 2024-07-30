#!/usr/bin/env python3
''' 1-app.py file '''

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    ''' configurations for the app '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    ''' Render index template '''
    return render_template('1-index.html')


if __name__ == '__main__':
    ''' Running the the flask server '''
    app.run()
