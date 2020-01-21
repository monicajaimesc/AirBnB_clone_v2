#!/usr/bin/python3
# coding=utf-8
"""
script that starts a third Flask web application
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


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    define third route
    :return: “C ” and text variable (replace _ with a space )
    """

    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    app.run()
