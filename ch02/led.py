import RPi.GPIO as rg
import time

rg.setmode(rg.BCM)

ledPlusPin = 27

rg.setup(ledPlusPin, rg.OUT)

try:
    while True:
        rg.output(ledPlusPin, rg.LOW)
        time.sleep(1)
        rg.output(ledPlusPin, rg.HIGH)
        time.sleep(1)
except KeyboardInterrupt:
    rg.cleanup()
