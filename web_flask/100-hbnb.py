#!/usr/bin/python3
"""This script will create 5 simple flask web application"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def states():
    """This function will display html that contains our web static"""
    from models.state import State
    from models.amenity import Amenity
    from models.place import Place
    from models.city import City
    from models.user import User
    city_dict = storage.all(City)
    state_dict = storage.all(State)
    amenity_dict = storage.all(Amenity)
    place_dict = storage.all(Place)
    user_dict = storage.all(User)
    return render_template('100-hbnb.html', states=state_dict,
                           amenities=amenity_dict, places=place_dict,
                           cities=city_dict, users=user_dict)


@app.teardown_appcontext
def close(exception):
    """This function closes the application"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
