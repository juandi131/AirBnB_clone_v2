#!/usr/bin/python3
"""endpoint (route) will be to return the status of your API"""
from flask import Flask, jsonify
from flask_cors import CORS
from api.v1.views import app_views
from models import storage
from os import getenv

app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    call storage.close()
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    return a json formatted 404 error
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    API_HOST = getenv("HBNB_API_HOST", "0.0.0.0")
    API_PORT = getenv("HBNB_API_PORT", "5000")
    app.run(host=API_HOST, port=API_PORT, threaded=True)
