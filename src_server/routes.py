# routes.py
from flask import Flask, request


signal_interpreter_app = Flask(__name__)

@signal_interpreter_app.route("/", methods=["POST"])
def hello():
    return {
        "response": 200,
        "message": "Signal is received"
    }

@signal_interpreter_app.route("/member/", methods=["POST"])
def ricardo_introduction():
    return "This is member's page"

@signal_interpreter_app.route("/post-data/", methods=["POST"])
def handling_signal():
    data = request.get_json()
    return data