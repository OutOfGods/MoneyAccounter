from ui_controller import *
from keys_controller import *

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('configuration.ini')

    if 'Controller' in config:
        if config['Controller']['Type'] == 'ui':
            controller = UIController()
        elif config['Controller']['Type'] == 'keys':
            controller = KeysController()
