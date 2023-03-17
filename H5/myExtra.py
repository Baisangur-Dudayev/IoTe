import time
import wiringpi

wiringpi.wiringPiSetup()
print("start")

pins = [3, 4, 6, 9]

for pin in pins:
   wiringpi.digitalWrite(pin, wiringpi.LOW)
