#!/usr/bin/python
import RPi.GPIO as GPIO
import time
pin_number = 22
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_number, GPIO.OUT)
while True:
    GPIO.output(pin_number, True)
    time.sleep(1)
    GPIO.output(pin_number, False)
    time.sleep(1)
