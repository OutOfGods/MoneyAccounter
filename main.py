from ui_controller import *
from keys_controller import *

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('configuration.ini')

    if 'Controller' in config:
        if config['Controller']['Type'] == 'ui':
            controller = UIController()
            controller.app_init()
            controller.ui_setup()
            controller.load_data()
            controller.interface_setup()
            controller.app_run()
        elif config['Controller']['Type'] == 'keys':
            controller = KeysController()
