#!/usr/bin/env python3
"""
get_locale function with the
babel.localeselector decorator
"""
from flask import Flask, render_template
from flask_babel import Babel
from flask import request


app = Flask(__name__)


@babel.localeselector
def get_locale():
    """Select best language"""
    return request.accept_languages.best_match(['en', 'fr'])


babel = Babel(app)


@app.route("/")
def home():
    """Home route"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
