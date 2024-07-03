#!/usr/bin/env python3
"""Change your get_locale function to use a
user’s preferred local if it is supported.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

SUPPORTED_LOCALES = ['fr', 'en']


def get_locale() -> str:
    """Get locale for user

    Returns:
        str: The language format
    """
    lang = request.args.get('locale')
    if lang in SUPPORTED_LOCALES:
        return lang
    user = getattr(g, 'user', None)
    if user and user['locale'] in SUPPORTED_LOCALES:
        return user['locale']

    return request.accept_languages.best_match(SUPPORTED_LOCALES)


babel = Babel(app, locale_selector=get_locale)


def get_user():
    """Get user's id"""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Run before each request
    """
    g.user = get_user()


@app.route('/')
def index():
    """Index route"""
    home_title = _('home_title')
    home_header = _('home_header')
    return render_template('5-index.html',
                           home_title=home_title, home_header=home_header)


if __name__ == '__main__':
    app.run()
