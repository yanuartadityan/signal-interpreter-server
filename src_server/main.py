from routes import signal_interpreter_app

if __name__ == '__main__':
    signal_interpreter_app.debug = True
    signal_interpreter_app.run("127.0.0.1", port=5000)