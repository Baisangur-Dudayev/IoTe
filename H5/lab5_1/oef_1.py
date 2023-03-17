import time
import wiringpi as wp

print("start")
wp.wiringPiSetup()

pin1 = 3

wp.pinMode(pin1,1)

while True:
    wp.digitalWrite(pin1,1)
   