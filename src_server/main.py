"""
main.py
"""
import argparse
from signal_interpreter_server.src_server.json_parser import SignalParser
from signal_interpreter_server.src_server.routes import signal_interpreter_app


def main():
    """
    main
    """
    parser_p = argparse.ArgumentParser()
    parser_p.add_argument('-f', '--file_path',
                            help="Specified path to the signal database file",
    required=False, default="signal_interpreter_server/signal_database.json")
    parsed = parser_p.parse_args()

    # create SignalParser obj
    signal_parser_obj = SignalParser(parsed.file_path)

    # enable debug mode, pass variable
    signal_interpreter_app.debug = False
    signal_interpreter_app.config['signal_db'] = signal_parser_obj
    signal_interpreter_app.run("127.0.0.1", port=5000)

def init_app():
    """
    init_app
    """
    if __name__ == '__main__':
        main()

# run app
init_app()
