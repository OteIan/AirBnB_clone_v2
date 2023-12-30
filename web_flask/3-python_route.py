#!/usr/bin/python3
"""
Flask web application

This is a simple Flask web application that defines the following routes:
1. '/' - Returns a greeting message.
2. '/hbnb' - Returns "HBNB".
3. '/c/<text>': display "C" followed by the value of the text variable
4. '/python/<text>' - Displays "Python" followed by the value of the 'text'
variable.Defaults to "is cool"
"""
from flask import Flask
from markupsafe import escape  # Prevents HTML injections
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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route: /c/<text>

    Displays "C" followed by the value of the 'text' variable.

    Example:
    $ curl http://127.0.0.1:5000/c/<text>
    Output: C <text>
    """
    text = escape(text.replace('_', ' '))
    return f'C {text}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_text(text='is cool'):
    """
    Route: /python/<text> and /python

    Displays "Python" followed by the value of the 'text' variable.
    Defaults to "is cool" if 'text' is not provided.

    Example:
    $ curl http://127.0.0.1:5000/python
    Output: Python is cool

    $ curl http://127.0.0.1:5000/python/programming
    Output: Python programming
    """
    text = escape(text.replace('_', ' '))
    return f'Python {text}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
