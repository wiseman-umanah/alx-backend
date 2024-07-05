#!/usr/bin/env python3
"""Getting timezone of Users"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from time import datetime
from pytz import UnknownTimeZoneError

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    Configuration for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Select and return best language match based on supported languages
    """
    user = getattr(g, 'user', None)
    if user and user['locale'] in app.config['LANGUAGES']:
        return user['locale']
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
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


def get_user():
    """Get user's id"""
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


def get_current_time_in_timezone(timezone):
    """Get time format from timezone"""
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz)
    return current_time.strftime("%m %d, %Y, %H:%M:%S %p")


@app.before_request
def before_request():
    """Run before each request
    """
    user = get_user()
    g.user = user


@app.route('/')
def index():
    """Home route"""
    timezone = get_timezone()
    tf = get_current_time_in_timezone(timezone)

    return render_template('index.html', tf=tf)


if __name__ == '__main__':
    app.run()
