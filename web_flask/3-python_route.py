#!/usr/bin/python3
"""This script will create 4 simple flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """This function will use url with slash and give the result"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """This function will redirect to hbnb and display return"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def with_C(text):
    """This functio will display c followed by text value"""
    return "C %s" % text.replace("_", " ")


@app.route("/python/<text>", strict_slashes=False)
def with_python(text):
    """This function will display python and the text given"""
    return "Python %s" % text.replace("_", " ")


@app.route("/python", strict_slashes=False)
def python_without_text():
    """THis function is called when there is no text"""
    return "Python is cool"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
