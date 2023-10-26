from machine import Pin
import utime

led = Pin(8, Pin.OUT)
led.low()

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)