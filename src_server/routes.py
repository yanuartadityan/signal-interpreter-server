# routes.py
"""
routes.py
"""
import logging
from flask import Flask, request, abort
from signal_interpreter_server.src_server.exceptions import JsonParserError

signal_interpreter_app = Flask(__name__)
logger = logging.getLogger(__name__)


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    """
    interpret_signal
    """
    # get data
    try:
        data = request.get_json()
        logger.info("JSON received: %s", data)
    # triggered when the json is not correct
    except JsonParserError as err:
        logging.exception("Error in parsing request to json: %s", err)
        abort(404, description=f"Aborting request. Parsing error of the json")

    try:
        # create a parser, and use it to get signal value
        signal_ps = signal_interpreter_app.config.get('signal_db')
        signal_name = signal_ps.get_signal_by_id(data["signal"])
        return {
            "title": signal_name
        }
    # triggered when data["signal"] couldn't find key to the dictionary
    except KeyError as err:
        logger.exception("Received key input error %s", err)
        abort(400, description=f"{data['signal']} did not return correct values. Key error!")
