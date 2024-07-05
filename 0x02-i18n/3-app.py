#!/usr/bin/env python3
"""Parametrize templates
with gettext
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

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
    """Select best language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])



@app.route('/')
def index():
    """index route"""
    home_title = _('home_title')
    home_header = _('home_header')
    return render_template('3-index.html',
                           home_title=home_title, home_header=home_header)


if __name__ == '__main__':
    app.run()
