"""
json_parser.py
"""
import json


class SignalParser:
    """
    SignalParser class
    """
    def __init__(self, filepath):
        """
        __init__ (constructor)
        """
        self.signals = SignalParser.load_file(filepath)

    def get_signal_by_id(self, signal_id):
        """
        get_signal_by_id
        """
        title = SignalParser.get_signal_title(self.signals, signal_id)
        return title

    @staticmethod
    def load_file(filepath):
        """
        load_file
        """
        with open(filepath) as json_file:
            signal_dict = json.load(json_file)
        return signal_dict

    @staticmethod
    def get_signal_title(signal_list, signal_id):
        """
        get_signal_title
        """
        if isinstance(signal_list, dict):
            if "id" in signal_list:
                if signal_list["id"] == signal_id:
                    return signal_list["title"]

            for k in signal_list:
                value = SignalParser.get_signal_title(signal_list[k], signal_id)
                if value is not None:
                    return value

        elif isinstance(signal_list, list):
            for j in signal_list:
                value = SignalParser.get_signal_title(j, signal_id)
                if value is not None:
                    return value

        return None
