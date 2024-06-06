Use with Raspberry Pi
========================

Download and Install the ``pipower3`` Module
-------------------------------

Download the code from GitHub and install:

.. code-block:: shell
    
    git clone https://github.com/sunfounder/pipower3

    cd pipower3
    sudo python3 install.py

After installation, you will be prompted to reboot. Enter ``Y`` and press enter to reboot. After rebooting, the safe shutdown service will automatically start. If the button is pressed for 2 seconds or if the battery is low, the Raspberry Pi will shut down and notify PiPower 3 to power off.

Set Shutdown Percentage
--------------------------------

PiPower 3 sends a "LOW BATTERY" shutdown request through I2C to the host when there is no external power and the battery voltage drops below the shutdown percentage. The host can read the shutdown request signal through I2C, and if "LOW BATTERY" is detected, it can process the shutdown. 

After shutting down, pulling the ``SDSIG`` high will power off the PiPower. This implements the low battery shutdown feature of PiPower 3.

.. note::

    If you are use Raspberry Pi 5, if the power used is greater than 3A, the battery will not be able to sustain power for long. It is recommended to set the shutdown Percentage to 100%, i.e., notify the Raspberry Pi to shut down immediately when external power is disconnected, to protect the Raspberry Pi and data.

You can set the shutdown percentage using the command, for example, set it to 30%. When the battery level is below 30%, PiPower3 will power off the Raspberry Pi after it shuts down.

.. code-block:: shell
    
    pipower3 -sp 30 

View the Basic Configurations
----------------------------------------

You can use the ``pipower3`` command to view the current information, detailed usage tutorial as follows:

.. code-block::

    usage: pipower3-service [-h] [-sp [SHUTDOWN_PERCENTAGE]] [-pp [POWER_OFF_PERCENTAGE]] [-so SHUTDOWN_OVERRIDE] [-iv] [-ov] [-bv] [-bp] [-bs] [-ii] [-ib] [-ic] [-ao] [-sr] [-bi]
                            [-psv] [-a]
                            [command]

    PiPower 3

    positional arguments:
    command               Command

    options:
    -h, --help            show this help message and exit
    -sp [SHUTDOWN_PERCENTAGE], --shutdown-percentage [SHUTDOWN_PERCENTAGE]
                            Set shutdown percentage, leave empty to read
    -iv, --input-voltage  Read input voltage
    -ov, --output-voltage
                            Read output voltage
    -bv, --battery-voltage
                            Read battery voltage
    -bp, --battery-percentage
                            Read battery percentage
    -bs, --battery-source
                            Read battery source
    -ii, --is-input-plugged_in
                            Read is input plugged in
    -ic, --is-charging    Read is charging
    -do, --default-on     Read default on
    -sr, --shutdown-request
                            Read shutdown request
    -a, --all             All

Configure with Python
-------------------------------

PiPower 3 uses the ``spc`` library, which allows you to get data and set parameters in Python. The ``spc`` library is installed in a virtual environment, so you need to first enter the virtual environment.

.. code-block:: shell

    source /opt/pipower3/venv/bin/activate

If you do not want to enter the virtual environment, you can reinstall ``spc`` to the system, which needs to be confirmed with ``--break-system`` due to possible conflicts with other libraries:

.. code-block:: shell

    sudo pip3 install --break-system git+http://github.com/sunfounder/spc.git

Or if you want to install it in your own virtual environment, simply run the install command after entering your virtual environment:

.. code-block:: shell

    pip3 install git+http://github.com/sunfounder/spc.git

Now you can run examples:

.. code-block:: shell

    cd ~/pipower3/examples

.. code-block:: shell

    python3 read_all.py

* ``read_all.py``: Use this example if you need to read all data at once and process them individually.
* ``read_individual.py``: If you only need to read certain data, this example provides individual data retrieval instructions.
* ``set_shutdown_percentage.py``: This example teaches how to set a Shutdown battery percentage, which sends a shutdown signal to the host when there is no charging and the battery falls below this value. After the host shuts down, it receives a power-off signal before powering off. Typically used with SBCs like Raspberry Pi. Microcontrollers needing to use this feature should remove the SDSIG jumper cap and connect the middle wire to a pin. After receiving the shutdown signal and safely shutting down, pull this pin high to power off PiPower 3.
* ``shutdown_when_request``: This example shows how to handle operations after receiving a shutdown signal. Remove the SDSIG jumper cap and connect the middle wire to a pin.

Python Library API Documentation:

https://github.com/sunfounder/spc?tab=readme-ov-file#api

