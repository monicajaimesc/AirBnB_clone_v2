#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask


app = Flask(__name__)

# specify URL
@app.route("/", strict_slashes=False)
def Hello_route():
    """
    define first route

    :return: url return a string
    """
    # what that URL returns
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    define second route
    :return: url returns a second string
    """
    return "HBNB"


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    app.run()
