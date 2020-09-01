#!/usr/bin/python3
"""display Hello HBNB / root
   display HBNB /hbnb root
   display /c/<text>
   display /python/(<text>)
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def print_hello():
    """return text to display using flask"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def print_hbnb():
    """return text to display using flask"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def print_text(text):
    """return text to display using flask"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def print_python(text):
    """return text to display using flask"""
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def print_number(n):
    """return text to display using flask"""
    return "{:d} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
