#!/usr/bin/python3
# coding=utf-8
"""
starts flask four application, display python
"""

from flask import Flask


app = Flask(__name__)


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


@app.route("/python/", defaults={"text": 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python_(text):
    """
    define four routine with python
    :param text: variable that will be passed
    :return: Python ”, followed by the value of the text variable
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run()
