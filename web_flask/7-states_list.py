#!/usr/bin/python3
"""
in this file SQLALchemy is gonna be used to establishes conversations
between the program and the databases.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    function that will display the states list
    :return: display HTML with the stated sorted
    """
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_connection(exception):
    """
    close the database
    """
    storage.close()


if __name__ == '__main__':
    app.run()
