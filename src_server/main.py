import argparse
from signal_interpreter_server.src_server.routes import signal_interpreter_app


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('-f', '--file_path', help="Specified path to the signal database file" , required=False, default="signal_interpreter_server/signal_database.json")
    parsed = p.parse_args()

    # enable debug mode, pass variable
    signal_interpreter_app.debug = True 
    signal_interpreter_app.config['signal_db'] = parsed.file_path
    signal_interpreter_app.run("127.0.0.1", port=5000)