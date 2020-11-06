# routes.py
from flask import Flask

my_app = Flask(__name__)

@my_app.route("/")
def hello():
    return "Hello World"

if __name__ == "__main__":
    my_app.run()