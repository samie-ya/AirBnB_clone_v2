#!/usr/bin/python3
"""This script will create 5 simple flask web application"""
from models import storage
from models.state import State
from models.city import City
import os
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """This function will display html that conatins states"""
    new_list = []
    for state_id, state in storage.all(State).items():
        new_list.append(state)
    return render_template('7-states_list.html', name=new_list)


@app.route("/states/<ids>", strict_slashes=False)
def states_by_id(ids):
    """This function will list cities by the given id"""
    state_name = ""
    city_list = []
    for state_id, state in storage.all(State).items():
        if (str(ids) == state.id):
            state_name = state.name
    if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
        for city_id, city in storage.all(City).items():
            if (str(ids) == city.state_id):
                city_list.append(city)
    else:
        for state_id, state in storage.all(State).items():
            if (str(ids) == state.id):
                for city in state.cities:
                    city_list.append(city)
    return render_template('9-states.html', name=state_name, cities=city_list)


@app.teardown_appcontext
def close(exception):
    """This function closes the application"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
