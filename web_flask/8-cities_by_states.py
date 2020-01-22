#!/usr/bin/python3
"""
import cities by state
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def city_by_state():
    """
    function that will display the cities by state
    :return: display HTML with the state and it respective cities (sorted)
    """
    states = storage.all("State").values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_connection(exception):
    """
    close the database
    """
    storage.close()


if __name__ == '__main__':
    app.run()
