#!/usr/bin/python3
"""
start web application using Flask
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def print_hello():
    """return text to display"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
