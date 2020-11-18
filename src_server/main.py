import argparse
from signal_interpreter_server.src_server.json_parser import SignalParser
from signal_interpreter_server.src_server.routes import signal_interpreter_app


def main():
    p = argparse.ArgumentParser()
    p.add_argument('-f', '--file_path', help="Specified path to the signal database file" , required=False, default="signal_interpreter_server/signal_database.json")
    parsed = p.parse_args()

    # create SignalParser obj
    signalParserObj = SignalParser(parsed.file_path)

    # enable debug mode, pass variable
    signal_interpreter_app.debug = False
    signal_interpreter_app.config['signal_db'] = signalParserObj
    signal_interpreter_app.run("127.0.0.1", port=5000)

def init_app():
    if __name__ == '__main__':
        main()

# run app
init_app()