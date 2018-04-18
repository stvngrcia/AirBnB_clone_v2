#!/usr/bin/python3
from flask import Flask
from models import storage, State
from flask import render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exceptions):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    state_obj = storage.all("State")
    states = list()
    for state, value in state_obj.items():
        states.append(value)
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    state_obj = storage.all("State")
    city_obj = storage.all("City")
    states = list()
    cities = list()
    for state, value in state_obj.items():
        states.append(value)
    for city, value in city_obj.items():
        cities.append(value)
    return render_template("8-cities_by_states.html",
                           states=states,
                           cities=cities)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def show_states(id=None):
    state_obj = storage.all("State")
    city_obj = storage.all("City")
    states = list()
    cities = list()
    for state, value in state_obj.items():
        states.append(value)
    for city, value in city_obj.items():
        cities.append(value)

    state_id = "State.{}".format(id)
    if id is not None and state_id not in state_obj:
        states = None
    return render_template("9-states.html",
                           states=states,
                           cities=cities,
                           id=id)


@app.route("/hbnb_filters", strict_slashes=False)
def display_filters():
    state_obj = storage.all("State")
    city_obj = storage.all("City")
    amenities_objs = storage.all("Amenity")
    states = list()
    cities = list()
    amenities = list()
    for state, value in state_obj.items():
        states.append(value)
    for city, value in city_obj.items():
        cities.append(value)
    for amenity, value in amenities_objs.items():
        amenities.append(value)

    return render_template("10-hbnb_filters.html",
                           states=states,
                           cities=cities,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
