from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Dict, List

from yaml import safe_load


def load_yaml_config(config_path: Path) -> Dict:
    """Load YAML config file and return a parsed, ready to consume, dictionary
    :param config_path: location of the config file
    :return: config dictionary
    """
    with config_path.open(mode='r') as stream:
        config = safe_load(stream)
    return config


def parse_arguments(arguments_list: List) -> Namespace:
    """Parse arguments list"""
    parser = ArgumentParser(__name__)
    parser.add_argument('--config_path', type=Path, help='config path')
    parser.add_argument('--input_file', type=Path, help='file input path')

    return parser.parse_args(arguments_list)
