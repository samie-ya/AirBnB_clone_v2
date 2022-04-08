#!/usr/bin/python3
"""This script will create 5 simple flask web application"""

from flask import Flask, render_template
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
    """This function is called when there is no text"""
    return "Python is cool"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """This function will go to the number n given"""
    return "%d is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def calling_template(n):
    """This function will call an html template and add the value of n"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
