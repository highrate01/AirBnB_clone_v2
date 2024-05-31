#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """return Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """C is fun"""
    underscore = text.replace('_', ' ')
    return "C {}".format(underscore)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """return default value if param is not passed"""
    underscore = text.replace('_', ' ')
    return "Python {}".format(underscore)


@app.route('/number/<n>', strict_slashes=False)
def number_route(n):
    """display a number"""
    try:
        n = int(n)
        return f"{n} is a number"
    except ValueError:
        pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
