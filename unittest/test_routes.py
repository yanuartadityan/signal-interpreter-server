"""
test_routes.py
"""
from signal_interpreter_server.src_server.routes import signal_interpreter_app
from signal_interpreter_server.src_server.json_parser import SignalParser


def test_interpret_signal():
    """
    test_interpret_signal
    """
    signal_interpreter_app.testing = True
    signal_interpreter_app.config['signal_db'] = SignalParser("signal_interpreter_server/signal_database.json")

    # correct pass
    with signal_interpreter_app.test_client() as client:

        payload = {
            "signal": "27"
        }
        response = client.post("/", json=payload)

        assert response.get_json() == {"title": "Security Access"}
        assert response.status_code == 200

        # incorrect pass
        payload = {
            "signal": "10"
        }
        response = client.post("/", json=payload)

        assert response.get_json() == {"title": None}
        assert response.status_code == 200
