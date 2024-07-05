#!/usr/bin/env python3
"""Module to force locale with URL parameter"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    """
    Configuration for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Find best language for user from query"""
    lang = request.args.get('locale')
    if lang in Config().LANGUAGES:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Index route"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
