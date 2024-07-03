#!/usr/bin/env python3
"""A Basic Flask app Setup
for / route
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Home route"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
