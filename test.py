import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

channel_list = [20,21,26]
GPIO.setup(channel_list, GPIO.OUT)

RELAY1 = 21
RELAY2 = 20
RELAY3 = 26

try:
    while True:
        GPIO.output(RELAY1, GPIO.LOW)
        time.sleep(1)
        GPIO.output(RELAY2, GPIO.LOW)
        time.sleep(1)
        GPIO.output(RELAY3, GPIO.LOW)
        time.sleep(1);
        GPIO.output(RELAY1, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(RELAY2, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(RELAY3, GPIO.HIGH)
        time.sleep(1);

except KeyboardInterrupt:
    # Clean up the GPIO pins on exit
    GPIO.cleanup()
