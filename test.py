#!/home/don/mypy/bin/python3

import time
import smbus
import sys

DEVICE_BUS = 1
DEVICE_ADDR = 0x10

RELAY1 = 1
RELAY2 = 2
RELAY3 = 3
RELAY4 = 4

bus = smbus.SMBus(DEVICE_BUS)

try:
    while True:
        bus.write_byte_data(DEVICE_ADDR, RELAY1, 0x00)
        time.sleep(1)
        bus.write_byte_data(DEVICE_ADDR, RELAY2, 0x00)
        time.sleep(1)
        bus.write_byte_data(DEVICE_ADDR, RELAY3, 0x00)
        time.sleep(1)
        bus.write_byte_data(DEVICE_ADDR, RELAY4, 0x00)
        time.sleep(1)

        bus.write_byte_data(DEVICE_ADDR, RELAY1, 0xFF)
        time.sleep(1)
        bus.write_byte_data(DEVICE_ADDR, RELAY2, 0xFF)
        time.sleep(1)
        bus.write_byte_data(DEVICE_ADDR, RELAY3, 0xFF)
        time.sleep(1)
        bus.write_byte_data(DEVICE_ADDR, RELAY4, 0xFF)
        time.sleep(1)

except KeyboardInterrupt as e:
    bus.write_byte_data(DEVICE_ADDR, RELAY1, 0x00)
    bus.write_byte_data(DEVICE_ADDR, RELAY2, 0x00)
    bus.write_byte_data(DEVICE_ADDR, RELAY3, 0x00)
    bus.write_byte_data(DEVICE_ADDR, RELAY4, 0x00)
    sys.exit()
