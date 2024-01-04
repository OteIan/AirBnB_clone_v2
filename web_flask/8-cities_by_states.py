#!/usr/bin/python3
""" A route to /cities_by_state """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def db_close(exception):
    """
    Teardown method to close the database connection.

    Parameters:
    - exception: An exception object if an exception occurred during processing
    """
    storage.close()


@app.route("/states_list")
def states_list():
    """
    Route: /states_list

    Renders a template displaying a list of states.

    Example:
    $ curl http://127.0.0.1:5000/states_list
    Output: HTML page displaying a list of states
    """
    data = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template("7-states_list.html", states=data)


@app.route("/cities_by_state")
def cities_by_state():
    """
    Route: /cities_by_state

    Renders a template displaying a list of states and their cities.

    Example:
    $ curl http://127.0.0.1:5000/cities_by_state
    Output: HTML page displaying a list of states and their cities
    """
    data = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template("8-cities_by_states.html", states=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
