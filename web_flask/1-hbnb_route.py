#!/usr/bin/python3
"""display Hello HBNB / root
   display HBNB /hbnb root
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="1000")
