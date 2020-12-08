"""
# test_json_parser.py
"""
import json
from unittest import TestCase
from unittest.mock import patch, mock_open
from signal_interpreter_server.src_server.json_parser import SignalParser


class TestParser(TestCase):
    """
    TestParser class
    """
    @staticmethod
    @patch('signal_interpreter_server.src_server.json_parser.SignalParser.load_file')
    def test_constructor(mock_signals):
        """
        test_constructor
        """
        mock_signals.return_value = {
            "services": [
                {
                    "title": "ECU Reset",
                    "id": "11"
                },
                {
                    "title": "Security Access",
                    "id": "27"
                }
            ]
        }
        parser_obj = SignalParser("whatever")
        assert parser_obj.signals == mock_signals.return_value

    @staticmethod
    @patch('signal_interpreter_server.src_server.json_parser.SignalParser.get_signal_title')
    def test_get_signal_by_id(mock_signal_title):
        """
        test_get_signal_by_id
        """
        db_path = "signal_interpreter_server/signal_database.json"
        mock_signal_title.return_value = "ECU Reset"
        parser_obj = SignalParser(db_path)
        assert parser_obj.get_signal_by_id("Whatever") == "ECU Reset"

    def test_load_file(self):
        """
        test_load_file
        """
        # provide valid signal database
        valid_database = {
            "services": [
                    {
                        "title": "ECU Reset",
                        "id": "11"
                    },
                    {
                        "title": "Security Access",
                        "id": "27"
                    }
                ]
        }

        # dump the valid JSON to IO-type read_data.
        read_data = json.dumps(valid_database)

        # fetch IO-type data to mock_open and assign to mock_fn_open
        mock_fn_open = mock_open(read_data=read_data)
        with patch('builtins.open', mock_fn_open):
            result = SignalParser.load_file("random_filename")
        self.assertEqual(valid_database, result)


    def test_get_signal_title(self):
        """
        test_get_signal_title
        """
        ok_signal_list = {
                "services": [
                    {
                        "title": "ECU Reset",
                        "id": "11"
                    },
                    {
                        "title": "Security Access",
                        "id": "27"
                    }
                ]
            }

        notok_signal_list = {
                "services": [
                    {
                        "title": "ECU Reset",
                        "ids": "11"
                    },
                    {
                        "title": "Security Access",
                        "ids": "27"
                    }
                ]
            }

        self.assertEqual(SignalParser.get_signal_title(ok_signal_list, "11"), "ECU Reset")
        self.assertEqual(SignalParser.get_signal_title(notok_signal_list, "15"), None)
