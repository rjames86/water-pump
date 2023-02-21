import RPi.GPIO as GPIO
from time import sleep

from meross import turn_off as turn_off_fans, turn_on as turn_on_fans
from timing import timing

GPIO.setmode(GPIO.BOARD)

NEW = 3
OLD = 5

class WaterPump:
    def __init__(self, pin_num):
        self.pin_num = pin_num
        GPIO.setup(pin_num, GPIO.OUT, initial=GPIO.HIGH)

    def on(self):
        GPIO.output(self.pin_num, GPIO.LOW)    
    
    def off(self):
        GPIO.output(self.pin_num, GPIO.HIGH)    

old_water = WaterPump(OLD)
new_water = WaterPump(NEW)


input("Press enter to begin...")

# First turn off the fans
turn_off_fans()
old_water.on()

input("Press enter to stop pump...")
old_water.off()

input("Press enter to start pumping in new water...")
new_water.on()

input("Press enter to stop pump...")
turn_on_fans()

GPIO.cleanup()