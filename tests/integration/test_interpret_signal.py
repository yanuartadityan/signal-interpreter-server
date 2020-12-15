""" 
test_interpret_signal.py
"""
import os
import sys

from unittest.mock import patch
import pytest

from signal_interpreter_server.src_server.routes import signal_interpreter_app
from signal_interpreter_server.src_server.main import main
from signal_interpreter_server.tests.integration.server_mock import signal_interpreter_app_instance


curr_dir = os.path.abspath(os.path.dirname(__file__))
fixture_path = os.path.join(curr_dir, "fixtures", "test_parametrize.json")


@pytest.mark.parametrize("payload, status_code, exp_response", [
    ({"signal": "11"}, 200, {"title": "ECU Reset"}),
    ({"signal": "27"}, 200, {"title": "Security Access"}),
    ({"signal": "99"}, 200, {"title": None}),
    ({"signal": "11f"}, 200, {"title": None})
])
@patch.object(sys, "argv", ["signal_interpreter_server", "--file_path", fixture_path])
def test_interpret_signal(payload, status_code, exp_response, signal_interpreter_app_instance):
    with patch.object(signal_interpreter_app, "run"):
        with signal_interpreter_app_instance as client:
            main()
            response = client.post("/", json=payload)
            assert response.get_json() == exp_response
            assert response.status_code == status_code
