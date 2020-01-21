#!/usr/bin/python3
"""
script that starts a Flask web application
"""""

from flask import Flask

# flask class, name to identify the current app
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_route():
    return "Hello HBNB!"

# application to handle remote requests


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    app.run()
