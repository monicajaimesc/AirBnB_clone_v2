#!/usr/bin/python3
"""
list states and cities of the states
"""
from models import storage
from models import *
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """
    function that will display a State object (founded by its id)
    :return: display HTML with the state and it respective cities (sorted)
    """
    states = storage.all("State").values()
    return render_template("9-states.html", states=states, id=id)


@app.teardown_appcontext
def close_connection(exception):
    """
    close the database
    """
    storage.close()


if __name__ == '__main__':
    app.run()
