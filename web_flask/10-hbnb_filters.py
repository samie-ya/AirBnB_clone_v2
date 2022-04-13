#!/usr/bin/python3
"""This script will create 5 simple flask web application"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def states():
    """This function will display html that conatins our web static"""
    from models.state import State
    from models.amenity import Amenity
    from models.city import City
    city_dict = storage.all(City)
    state_dict = storage.all(State)
    amenity_dict = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=state_dict,
                           amenities=amenity_dict, cities=city_dict)


@app.teardown_appcontext
def close(exception):
    """This function closes the application"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)
