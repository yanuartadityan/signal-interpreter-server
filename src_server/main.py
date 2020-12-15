"""
main.py
"""
import argparse
import logging
from signal_interpreter_server.src_server.json_parser import SignalParser
from signal_interpreter_server.src_server.routes import signal_interpreter_app


# !TODO 2020/12/14: catch all possible exceptions and logs
logger = logging.getLogger(__name__)

SERVER_IP_ADDR = "127.0.0.1"
SERVER_PORT = 5000

def main():
    """
    main
    """
    parser_p = argparse.ArgumentParser()
    parser_p.add_argument(
        '-f',
        '--file_path',
        help="Specified path to the signal database file",
        required=False,
        default="signal_interpreter_server/signal_database.json")
    parsed = parser_p.parse_args()

    # log
    logger.debug("Start")
    logger.debug("Entered arguments")

    # create SignalParser obj
    signal_parser_obj = SignalParser(parsed.file_path)

    # enable debug mode, pass variable
    signal_interpreter_app.debug = False
    signal_interpreter_app.config['signal_db'] = signal_parser_obj
    signal_interpreter_app.run(SERVER_IP_ADDR, port=SERVER_PORT)

    # log
    logger.info("Starting the server at: ")
    logger.info("\tIP Address: %s", SERVER_IP_ADDR)
    logger.info("\tPort: %d", SERVER_PORT)


def init_app():
    """
    init_app
    """
    if __name__ == '__main__':
        main()


# run app
init_app()
