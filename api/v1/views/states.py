#!/usr/bin/python3
"""State Model View"""

from models import storage
from models.state import State
from flask import Flask, jsonify, request
from api.v1.views import app_views
from flask import Flask, abort


app = Flask(__name__)


@app_views.route("/states/", methods=["GET"], strict_slashes=False)
def get_all_states():
    """Return all States"""
    all_states_arr = [obj.to_dict() for obj in storage.all(State).values()]
    return jsonify(all_states_arr)
@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def get_state_by_id(state_id):
    """Retrieves a State object"""
    state = storage.get(State, state_id)

    if state is None:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_state_by_id(state_id):
    """DELETE route to delete a State"""
    obj = storage.get(State, state_id)

    if obj is None:
        return abort(404)

    storage.delete(obj)
    storage.save()
    return jsonify({}), 200


@app_views.route("/states/", methods=["POST"], strict_slashes=False)
def create_state():
    """Creates a State"""
    if request.is_json:
        data = request.get_json()

        if "name" not in data:
            return "Missing name", 400

        new_obj = State(**data)
        storage.new(new_obj)
        storage.save()
        return jsonify(new_obj.to_dict()), 201

    return "Not a JSON", 400


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_state(state_id):
    """Updates a State object"""
    obj = storage.get(State, state_id)

    if obj is None:
        abort(404)

    if request.is_json:
        data = request.get_json()
        ignore_keys = ["id", "created_at", "updated_at"]

        for key, prop in data.items():
            if key not in ignore_keys:
                setattr(obj, key, prop)

        storage.save()
        return jsonify(obj.to_dict()), 200

    return "Not a JSON", 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
