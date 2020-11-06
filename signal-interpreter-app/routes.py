# routes.py
from flask import Flask

signal_interpreter_app = Flask(__name__)

@signal_interpreter_app.route("/")
def hello():
    return "Hello World"

@signal_interpreter_app.route("/member/")
def ricardo_introduction():
    return "This is member's page"