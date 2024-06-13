.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Use with Raspberry Pi Pico and ESP32 Boards
====================================================
If you are using the PiPower 3 to power your Raspberry Pi Pico or ESP32 Board, you can connect the Raspberry Pi Pico or ESP32 Board to the PiPower 3's Type A output port or use two jump wires.

Connect the board's I2C interface using a jumper. If no operation is required before powering off, directly connect the **SDSIG** jumper cap to the GND. If operations are necessary before shutdown, remove the jumper cap and connect the intermediate wire to an IO port on the Raspberry Pi Pico or ESP32 Board. This is used to notify PiPower 3 that it has completed shutdown and can power off.

We provide a library that allows you to monitor input and output voltages, battery voltage and percentage, power source, charging status, and other internal data.

#. Download the library from GitHub. You can quickly download it using the link below or visit: https://github.com/sunfounder/micropython_spc.

    * :download:`micropython_spc <https://github.com/sunfounder/micropython_spc/archive/refs/heads/main.zip>`

#. After downloading and unzipping, upload the ``spc`` folder to your Raspberry Pi Pico or ESP32 Board. Thonny is recommended for this purpose.

    .. image:: img/micropython_upload.png
        :align: center

#. Once uploaded, you can run a few examples from the ``micropython_spc-main`` folder to see the effects:

    * ``example_pipower_3_read_all.py``: Use this example if you need to read all data at once and process them individually.
    * ``example_pipower_3_read_individual.py``: If you only need to read certain data, this example provides individual data retrieval instructions.
    * ``example_pipower_3_set_shutdown_percentage.py``: This example teaches how to set a shutdown battery percentage. This will send a shutdown signal to the host when the battery is not charging and falls below the set percentage. It will power off only after the host has shut down and received a power-off signal. Typically used with SBCs like Raspberry Pi. For microcontrollers, remove the **SDSIG** jumper cap and connect the intermediate wire to a pin. After safely shutting down upon receiving the shutdown signal, pull this pin high to power off PiPower 3.
    * ``example_pipower_3_shutdown_when_request.py``: This example shows how to handle operations after receiving a shutdown signal. Remove the **SDSIG** jumper cap and connect the intermediate wire to a pin.

Micropython Library API Documentation:

https://github.com/sunfounder/micropython_spc?tab=readme-ov-file#api
