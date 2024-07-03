#!/usr/bin/env python3
"""Flask setup with Babel
for timezone and lang
"""
from flask import Flask, render_template
from flask_babel import Babel
from flask import request


app = Flask(__name__)


class Config():
    """Config Class for Babel app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


babel = Babel(app)
app.config.from_object = Config()


@app.route("/")
def home():
    """Home route"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
