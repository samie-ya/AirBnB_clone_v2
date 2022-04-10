#!/usr/bin/python3
"""This script will create 5 simple flask web application"""
from models import storage
from flask import Flask, render_template
import os
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states():
    """This function will display html that conatins states"""
    from models.state import State
    from models.city import City
    city_dict = storage.all(City)
    state_dict = storage.all(State)
    return render_template('8-cities_by_states.html', states=state_dict,
                           cities=city_dict)


@app.teardown_appcontext
def close(exception):
    """This function closes the application"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
