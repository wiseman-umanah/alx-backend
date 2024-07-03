#!/usr/bin/env python3
"""Module to force locale with URL parameter"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

SUPPORTED_LOCALES = ['fr', 'en']


def get_locale():
    """Find best language for user from query"""
    lang = request.args.get('locale')
    if lang in SUPPORTED_LOCALES:
        return lang
    return request.accept_languages.best_match(SUPPORTED_LOCALES)


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    """Index route"""
    home_title = _('home_title')
    home_header = _('home_header')
    return render_template('4-index.html',
                           home_title=home_title, home_header=home_header)


if __name__ == '__main__':
    app.run()
