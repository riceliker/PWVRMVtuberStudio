from flask import Blueprint, jsonify

bp = Blueprint("test", __name__)

@bp.route("/test")
def test():
    return {
        "test": "test is okay.",
        "test_number": 5
    }