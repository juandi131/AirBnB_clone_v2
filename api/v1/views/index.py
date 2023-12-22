#!/usr/bin/python3
"""Start API!"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route("/status", strict_slashes=False)
def status():
    """Return a JSON"""
    return jsonify({"status": "OK"})