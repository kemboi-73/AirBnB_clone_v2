#!/usr/bin/python3
"""Starts a simple  Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Routing to root(/), strict_slashes ensure
    the URL works with or without the '/'
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
