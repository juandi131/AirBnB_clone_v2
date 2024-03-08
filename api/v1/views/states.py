#!/usr/bin/python3
"""State Model View"""
from models import storage
from models.state import State
from flask import Flask, jsonify, request
from api.v1.views import app_views
from flask import Flask, abort


app = Flask(__name__)


	@@ -16,9 +15,11 @@ def get_all_states():
    """Return all States"""
    all_states_arr = [obj.to_dict() for obj in storage.all(State).values()]
    return jsonify(all_states_arr)
@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def get_state_by_id(state_id):
    """Retrieves a State object"""
    state = storage.get(State, state_id)

    if state is None:
	@@ -30,7 +31,7 @@ def get_state_by_id(state_id):
@app_views.route("/states/<state_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_state_by_id(state_id):
    """DELETE route to delete a State"""
    obj = storage.get(State, state_id)

    if obj is None:
	@@ -43,7 +44,7 @@ def delete_state_by_id(state_id):

@app_views.route("/states/", methods=["POST"], strict_slashes=False)
def create_state():
    """Creates a State"""
    if request.is_json:
        data = request.get_json()

	@@ -60,22 +61,22 @@ def create_state():

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