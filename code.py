# Created by Alexander James
# Created on Oct. 2023
# Uses the Pi Pico to blink an LED on a breabboard

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP8)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)