#!/usr/bin/python3
"""This script will create 5 simple flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)

new_list = []
for state_id, state in storage.all(State).items():
    new_list.append(state)


@app.route("/states_list", strict_slashes=False)
def states():
    """This function will display html that conatins states"""
    return render_template('7-states_list.html', name=new_list)


@app.teardown_appcontext
def close(exception):
    """This function closes the application"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
