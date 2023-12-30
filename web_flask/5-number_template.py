#!/usr/bin/python3
"""
Flask web application

This is a simple Flask web application that defines the following routes:
1. '/' - Returns a greeting message.
2. '/hbnb' - Returns "HBNB".
3. '/c/<text>': display "C" followed by the value of the text variable
4. '/python/<text>' - Displays "Python" followed by the value of the 'text'
\t\t\tvariable.Defaults to "is cool"
5. '/number/<int:n>' - Displays the provided integer 'n' with a message
\t\t\t'is an integer'
6. '/number_template/<int:n>' - Renders an HTML template displaying the
\t\t\tprovided integer 'n'
"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """
    Route: /number/<int:n>

    Displays the provided integer 'n' with a message.

    Example:
    $ curl http://127.0.0.1:5000/number/89
    Output: 89 is a number
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_n(n):
    """
    Route: /number_template/<int:n>

    Renders an HTML template displaying the provided integer 'n'.

    Example:
    $ curl http://127.0.0.1:5000/number_template/89
    Output: HTML page displaying "Number: 89"
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
