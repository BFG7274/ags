
import logging
import os
import sys
import yaml


class config:
    def __init__(self, path):
        self.path = path

    def getAgsConfig(self):
        if not os.path.exists(path):
            logging.ERROR(f"Can not find config file: {path}")
            sys.exit(1)
        f = open(path)
        y = yaml.load(f, Loader=yaml.CLoader)
        ags_config = y['ags']
        return ags_config


path = 'config.yaml'
if os.getenv('AGS_CONFIG'):
    path = os.environ['AGS_CONFIG']
conf = config(path).getAgsConfig()
