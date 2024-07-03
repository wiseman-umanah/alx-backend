#!/usr/bin/env python3
"""Getting timezone of Users"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _
import pytz
from pytz.exceptions import UnknownTimeZoneError


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

SUPPORTED_LOCALES = ['fr', 'en']


def get_locale():
    """Get user's locale"""
    user = getattr(g, 'user', None)
    if user and user['locale'] in SUPPORTED_LOCALES:
        return user['locale']
    lang = request.args.get('locale')
    if lang in SUPPORTED_LOCALES:
        return lang
    return request.accept_languages.best_match(SUPPORTED_LOCALES)


def get_timezone():
    """Get timezone"""
    time = request.args.get('timezone')
    if time:
        try:
            pytz.timezone(time)
            return time
        except UnknownTimeZoneError:
            pass

    user = getattr(g, 'user', None)
    if user and user['timezone']:
        try:
            pytz.timezone(user['timezone'])
            return user['timezone']
        except UnknownTimeZoneError:
            pass

    return 'UTC'


babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


def get_user():
    """Get user id"""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Runs before each request"""
    g.user = get_user()


@app.route('/')
def index():
    """Home route"""
    home_title = _('home_title')
    home_header = _('home_header')

    return render_template('7-index.html', home_title=home_title,
                           home_header=home_header)


if __name__ == '__main__':
    app.run()
