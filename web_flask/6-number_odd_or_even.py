#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from markupsafe import escape

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display a number"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a template"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display a HTML page stating whether n is odd or even"""
    odd_or_even = "odd" if n % 2 else "even"
    return render_template('6-number_odd_or_even.html',
                           number=n, parity=odd_or_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
