from .version import __version__

def main():
    from spc.spc import SPC
    import argparse
    import time
    spc = SPC()
    parser = argparse.ArgumentParser(description='PiPower 3')
    parser.add_argument('command', nargs='?', help='Command')
    parser.add_argument('-sp', '--shutdown-percentage', nargs='?', default='', help='Set shutdown percentage, leave empty to read')
    parser.add_argument('-pp', '--power-off-percentage', nargs='?', default='', help='Set power off percentage, leave empty to read')
    parser.add_argument('-iv', '--input-voltage', action='store_true', help='Read input voltage')
    parser.add_argument('-ov', '--output-voltage', action='store_true', help='Read output voltage')
    parser.add_argument('-bv', '--battery-voltage', action='store_true', help='Read battery voltage')
    parser.add_argument('-bp', '--battery-percentage', action='store_true', help='Read battery percentage')
    parser.add_argument('-bs', '--battery-source', action='store_true', help='Read battery source')
    parser.add_argument('-ii', '--is-input-plugged_in', action='store_true', help='Read is input plugged in')
    parser.add_argument('-ib', '--is-battery-plugged_in', action='store_true', help='Read is battery plugged in')
    parser.add_argument('-ic', '--is-charging', action='store_true', help='Read is charging')
    parser.add_argument('-ao', '--always-on', action='store_true', help='Read always on')
    parser.add_argument('-sr', '--shutdown-request', action='store_true', help='Read shutdown request')
    parser.add_argument('-bi', '--board-id', action='store_true', help='Read board id')
    parser.add_argument('-psv', '--power_source-voltage', action='store_true', help='Read power source voltage')
    parser.add_argument('-a', '--all', action='store_true', help='All')

    args = parser.parse_args()

    if args.command == 'start':
        import os
        from pipower3.logger import Logger

        log = Logger('pipower3')
        log.info('Starting PiPower 3 service')
        last_shutdown_request = None
        last_is_usb_plugged_in = None
        last_is_charging = None
        while True:
            shutdown_request = spc.read_shutdown_request()
            is_usb_plugged_in = spc.read_is_input_plugged_in()
            is_charging = spc.read_is_charging()
            if shutdown_request != last_shutdown_request:
                if shutdown_request == spc.SHUTDOWN_REQUEST_NONE:
                    continue
                elif shutdown_request == spc.SHUTDOWN_REQUEST_BUTTON:
                    log.info("Shutdown request: Button")
                    os.system("sudo shutdown -h now")
                elif shutdown_request == spc.SHUTDOWN_REQUEST_LOW_BATTERY:
                    log.info("Shutdown request: Low battery")
                    os.system("sudo shutdown -h now")
                last_shutdown_request = shutdown_request
            if is_usb_plugged_in != last_is_usb_plugged_in:
                if is_usb_plugged_in:
                    log.info("USB plugged in")
                else:
                    log.info("USB unplugged")
                last_is_usb_plugged_in = is_usb_plugged_in
            if is_charging != last_is_charging:
                if is_charging:
                    log.info("Charging")
                else:
                    log.info("Not charging")
                last_is_charging = is_charging
            time.sleep(1)
            
    if args.command == "stop":
        import os
        from pipower3.logger import Logger
        log = Logger('PiPower 3')
        log.info('Stopping PiPower 3 service')
        os.system('kill -9 $(pgrep -f "pipower3 start")')
        os.system('kill -9 $(pgrep -f "pipower3-service start")')

    if args.shutdown_percentage != '':
        if args.shutdown_percentage == None:
            print(f"Shutdown battery percentage: {spc.read_shutdown_percentage()}%")
        else:
            if int(args.shutdown_percentage) < 10:
                print("Failed, shutdown battery percentage minimal is 10%")
            elif int(args.shutdown_percentage) > 100:
                print("Failed, shutdown battery percentage maximal is 100%")
            else:
                spc.write_shutdown_percentage(int(args.shutdown_percentage))
                time.sleep(0.5)
                if spc.read_shutdown_percentage() == int(args.shutdown_percentage):
                    print(f"Success, shutdown battery percentage: {spc.read_shutdown_percentage()}%")
    if args.power_off_percentage != '':
        if args.power_off_percentage == None:
            print(f"Power off battery percentage: {spc.read_power_off_percentage()}%")
        else:
            if int(args.power_off_percentage) < 5:
                print("Failed, power off battery percentage minimal is 5%")
            elif int(args.power_off_percentage) > 100:
                print("Failed, power off battery percentage maximal is 100%")
            else:
                spc.write_power_off_percentage(int(args.power_off_percentage))
                time.sleep(0.5)
                if spc.read_power_off_percentage() == int(args.power_off_percentage):
                    print(f"Success, power off battery percentage: {spc.read_power_off_percentage()}%")
    if args.input_voltage:
        print(f"Input voltage: {spc.read_input_voltage()} mV")
    if args.output_voltage:
        print(f"Output voltage: {spc.read_output_voltage()} mV")
    if args.battery_voltage:
        print(f"Battery voltage: {spc.read_battery_voltage()} mV")
    if args.battery_percentage:
        print(f"Battery percentage: {spc.read_battery_percentage()} %")
    if args.battery_source:
        power_source = spc.read_power_source()
        print(f"Power source: {power_source} ({'Battery' if power_source == spc.BATTERY else 'External'})")
    if args.is_input_plugged_in:
        print(f"Input plugged in: {spc.read_is_input_plugged_in()}")
    if args.is_battery_plugged_in:
        print(f"Battery plugged in: {spc.read_is_battery_plugged_in()}")
    if args.is_charging:
        print(f"Charging: {spc.read_is_charging()}")
    if args.always_on:
        print(f"Always on: {spc.read_always_on()}")
    if args.shutdown_request:
        shutdown_request = spc.read_shutdown_request()
        shutdown_request_str = 'None'
        if shutdown_request == spc.SHUTDOWN_REQUEST_NONE:
            shutdown_request_str = 'None'
        elif shutdown_request == spc.SHUTDOWN_REQUEST_LOW_BATTERY:
            shutdown_request_str = 'Low battery'
        elif shutdown_request == spc.SHUTDOWN_REQUEST_BUTTON:
            shutdown_request_str = 'Button'
        else:
            shutdown_request_str = 'Unknown'
        print(f"Shutdown request: {shutdown_request} - {shutdown_request_str}")
    if args.board_id:
        print(f"Board id: {spc.read_board_id()}")
    if args.power_source_voltage:
        print(f"Power source voltage: {spc.read_power_source_voltage()} mV")
    if args.all:
        while True:
            data_buffer = spc.read_all()
            print(f"Input voltage: {data_buffer['input_voltage']} mV")
            print(f"Input current: {data_buffer['input_current']} mA")
            print(f"Raspberry Pi voltage: {data_buffer['output_voltage']} mV")
            print(f"Raspberry Pi current: {data_buffer['output_current']} mA")
            print(f"Battery voltage: {data_buffer['battery_voltage']} mV")
            print(f"Battery current: {data_buffer['battery_current']} mA")
            print(f"Battery capacity: {data_buffer['battery_capacity']} mAh")
            print(f"Battery percentage: {data_buffer['battery_percentage']} %")
            print(f"Power source: {data_buffer['power_source']} ({'Battery' if data_buffer['power_source'] == spc.BATTERY else 'External'})")
            print(f"Input plugged in: {data_buffer['is_input_plugged_in']}")
            print(f"Battery plugged in: {data_buffer['is_battery_plugged_in']}")
            print(f"Charging: {data_buffer['is_charging']}")
            print(f"Fan power: {data_buffer['fan_power']} %")
            shutdown_request_str = 'None'
            if data_buffer['shutdown_request'] == spc.SHUTDOWN_REQUEST_NONE:
                shutdown_request_str = 'None'
            elif data_buffer['shutdown_request'] == spc.SHUTDOWN_REQUEST_LOW_BATTERY:
                shutdown_request_str = 'Low battery'
            elif data_buffer['shutdown_request'] == spc.SHUTDOWN_REQUEST_BUTTON:
                shutdown_request_str = 'Button'
            else:
                shutdown_request_str = 'Unknown'
            print(f"Shutdown request: {data_buffer['shutdown_request']} - {shutdown_request_str}")
            print(f'Board id: {spc.read_board_id()}')
            print(f"Always on: {spc.read_always_on()}")
            print(f"Power source voltage: {spc.read_power_source_voltage()} mV")
            print(f"Shutdown percentage: {spc.read_shutdown_percentage()} %")
            print(f"Power off percentage: {spc.read_power_off_percentage()} %")
