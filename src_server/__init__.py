"""
init logger
"""
import os
import logging.config
import yaml

curr_dir = os.path.abspath(os.path.dirname(__file__))
config_file_path = os.path.join(curr_dir, '..', '..', 'cfg', 'log_config.yaml')

with open(config_file_path, 'r') as yfile:
    config = yaml.safe_load(yfile.read())
    logging.config.dictConfig(config)
