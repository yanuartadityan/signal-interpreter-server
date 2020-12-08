# test_main.py
from argparse import ArgumentParser
from unittest import TestCase
from unittest.mock import patch
# from signal_interpreter_server.src_server.main import init_app, main
from src_server.main import init_app, main

class MainTest(TestCase):
    def setup_parser(self):
        self.parser = ArgumentParser()
        self.parser.add_argument('-f', '--file_path')

    def test_main_argument_parser(self):
        self.setup_parser()

        parsed_short = self.parser.parse_args(['-f', 'signal_interpreter_server/signal_database.json'])
        parsed_long = self.parser.parse_args(['--file_path', 'signal_interpreter_server/signal_database.json'])

        self.assertEqual(parsed_short.file_path, 'signal_interpreter_server/signal_database.json')
        self.assertEqual(parsed_long.file_path, 'signal_interpreter_server/signal_database.json')

    @patch('sys.argv', ['test_main', '--file_path', 'signal_interpreter_server/signal_database.json'])
    def test_main(self):
        with patch('signal_interpreter_server.src_server.main.signal_interpreter_app.run') as mock_run:
            main()
            mock_run.assert_called_once()

    @patch('signal_interpreter_server.src_server.main.__name__', '__main__')            
    @patch('sys.argv', ['test_main', '--file_path', 'signal_interpreter_server/signal_database.json'])
    def test_init(self):
        with patch('signal_interpreter_server.src_server.main.main') as mock_main:
            init_app()
            mock_main.assert_called_once()

