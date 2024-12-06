#!/usr/bin/env python3

from tools.sf_installer import SF_Installer

installer = SF_Installer(
    name='pipower3',
    friendly_name='PiPower 3',

    # - Setup install command description if needed, default to "Installer for {friendly_name}""
    # description='Installer for PiPower 3',

    # - Setup venv options if needed, default to []
    venv_options=[
        '--system-site-packages',
    ],

    # - Setup Work Dir if needed, default to /opt/{name}
    # work_dir='/opt/pipower3',

    # - Setup log dir if needed, default to /var/log/{name}
    # log_dir='/var/log/pipower3',

    # - Install from apt
    apt_dependencies=[
    ],

    # - Install from pip
    pip_dependencies=[
        'pip',
    ],

    # - Install python source code from git
    python_source={
        'pipower3': './',
        'spc': 'git+http://github.com/sunfounder/spc.git',
    },

    # - Setup config txt
    # config_txt = {
    #     'dtparam=spi': 'on',
    #     'dtparam=i2c_arm': 'on',
    #     'dtoverlay=gpio-ir,gpio_pin': '13',
    # },

    # - Autostart settings
    # - Set service filenames
    service_files = ['pipower3.service'],
    # - Set bin files
    bin_files = ['pipower3'],

    # - Copy device tree overlay to /boot/overlays
    dtoverlay = ['sunfounder-pipower3.dtbo'],
)
installer.install()
