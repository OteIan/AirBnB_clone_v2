#!/usr/bin/python3
"""
Flask web application

This is a simple Flask web application that defines two routes:
1. '/' - Returns a greeting message.
2. '/hbnb' - Returns "HBNB".
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Route: /

    Returns a greeting message.

    Example:
    $ curl http://127.0.0.1:5000/
    Output: Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route: /hbnb

    Returns the string "HBNB".

    Example:
    $ curl http://127.0.0.1:5000/hbnb
    Output: HBNB
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
