import json
import time
import os
from pkg_resources import resource_filename

from .logger import create_get_child_logger
from .utils import merge_dict, log_error
from .shutdown_service import ShutdownService
from .version import __version__

get_child_logger = create_get_child_logger('pipower3')
log = get_child_logger('main')
__package_name__ = __name__.split('.')[0]
CONFIG_PATH = resource_filename(__package_name__, 'config.json')

PMDashboard = None
try:
    from pm_dashboard.pm_dashboard import PMDashboard
except ImportError:
    pass

PERIPHERALS = [
    "storage", 
    "cpu", 
    "network", 
    "memory", 
    "history", 
    "log", 
    "input_voltage", 
    "output_voltage", 
    "battery_voltage", 
    "battery_percentage", 
    "power_source", 
    "is_input_plugged_in", 
    "is_charging", 
    "shutdown_percentage", 
    "default_on", 
]
DEVICE_INFO = {
    'name': 'PiPower 3',
    'id': 'pipower3',
    'peripherals': PERIPHERALS,
    'version': __version__,
}
AUTO_DEFAULT_CONFIG = {
    'temperature_unit': 'C',
}
DASHBOARD_SETTINGS = {
    "database": "pipower3",
    "interval": 1,
    "spc": True,
}

class PiPower3:
    # @log_error
    def __init__(self):
        self.log = log
        self.config = {
            'auto': AUTO_DEFAULT_CONFIG,
        }
        if not os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, 'w') as f:
                json.dump(self.config, f, indent=4)
        else:
            with open(CONFIG_PATH, 'r') as f:
                config = json.load(f)
            merge_dict(self.config, config)

        self.shutdown_service = ShutdownService(get_logger=get_child_logger)
        if PMDashboard is None:
            self.pm_dashboard = None
            self.log.warning('PM Dashboard not found, skipping')
        else:
            self.pm_dashboard = PMDashboard(device_info=DEVICE_INFO,
                                            settings=DASHBOARD_SETTINGS,
                                            config=self.config,
                                            peripherals=PERIPHERALS,
                                            get_logger=get_child_logger)
            self.pm_dashboard.set_on_config_changed(self.update_config)

    @log_error
    def update_config(self, config):
        merge_dict(self.config, config)
        with open(CONFIG_PATH, 'w') as f:
            json.dump(self.config, f, indent=4)

    @log_error
    @staticmethod
    def update_config_file(config):
        current = None
        with open(CONFIG_PATH, 'r') as f:
            current = json.load(f)
        merge_dict(current, config)
        with open(CONFIG_PATH, 'w') as f:
            json.dump(current, f, indent=4)

    @log_error
    def start(self):
        self.shutdown_service.start()
        if self.pm_dashboard:
            self.pm_dashboard.start()
            self.log.info('PmDashboard started')
        while True:
            time.sleep(1)

    @log_error
    def stop(self):
        self.shutdown_service.stop()
        if self.pm_dashboard:
            self.pm_dashboard.stop()
