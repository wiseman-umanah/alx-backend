#!/usr/bin/env python3
"""
get_locale function with the
babel.localeselector decorator
"""
from flask import Flask, render_template
from flask_babel import Babel
from flask import request


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


@app.route("/", strict_slashes=False)
def home():
    """Home route"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
