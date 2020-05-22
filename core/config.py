import os
import yaml
from collections import namedtuple

from .models import Config, RequestAuth


def _read_yaml_file(filename, cls):
    core_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(core_dir, "..", filename)

    with open(file_path, mode="r", encoding="UTF-8") as file:
        config = yaml.safe_load(file)
        return cls(**config)


def read_config():
    try:
        return _read_yaml_file("config.yaml", Config)
    except IOError:
        print("Error: couldn't file the configuration file `config.yaml`")
        exit()


def read_reqauth():
    try:
        return _read_yaml_file(".twitterauth", RequestAuth)
    except IOError:
        print(
            "It seems like you have not authorized the application.\n"
            "In order to use your twitter data, please run the auth.py first."
        )
