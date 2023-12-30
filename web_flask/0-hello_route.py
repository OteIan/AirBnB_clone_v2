#!/usr/bin/python3
"""Flask web application"""
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
