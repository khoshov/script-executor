import os

from core.models import AppConfiguration


def get_scripts_list():
    config = AppConfiguration.get_solo()
    return os.popen(f'ls {config.scripts_path}').read().split()


def get_executable_path(filename):
    config = AppConfiguration.get_solo()
    return os.path.join(config.scripts_path, filename)
