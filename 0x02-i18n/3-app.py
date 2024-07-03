#!/usr/bin/env python3
"""Parametrize templates
with gettext
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'


def get_locale():
    """Find best language for user"""
    return request.args.get('lang',
                            request.accept_languages.best_match(['fr', 'en']))


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    """index route"""
    home_title = _('home_title')
    home_header = _('home_header')
    return render_template('3-index.html',
                           home_title=home_title, home_header=home_header)


if __name__ == '__main__':
    app.run()
