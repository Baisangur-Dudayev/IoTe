import time
import wiringpi
import sys

wiringpi.wiringPiSetup()
wiringpi.pinMode(1, wiringpi.INPUT)

while True:
    if wiringpi.digitalRead(1) == wiringpi.LOW:
        print("Dark")
        time.sleep(0.5)
    else:
        print("Light")
        time.sleep(0.5)
       
