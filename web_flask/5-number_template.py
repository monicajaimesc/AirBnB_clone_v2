#!/usr/bin/python3
"""
starts a flask web application with number
"""

from flask import Flask
from flask import render_template


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


# @app.route("/number/", defaults={"n": 'is a number'})
@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    web application

    :param n is an integer:
    :return: display a number
    """
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    web application number five
    :return: display a HTML page only if n is an integer
    """
    # Flask will look for templates in the templates folder.
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run()
