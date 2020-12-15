""" test_mock_server.py 
to mock server side
"""
import pytest

from signal_interpreter_server.src_server.routes import signal_interpreter_app

@pytest.fixture
def signal_interpreter_app_instance():
    """ mock server """
    signal_interpreter_app.testing = True
    return signal_interpreter_app.test_client()
