import time
import wiringpi

wiringpi.wiringPiSetup()
print("start")

pins = [3, 4, 6, 9]

for pin in pins:
    wiringpi.pinMode(pin, wiringpi.OUTPUT)
    
while True:
    for pin in pins:
        wiringpi.digitalWrite(pin, wiringpi.HIGH)
    time.sleep(.1)
    print("on")

    for pin in pins:
        wiringpi.digitalWrite(pin, wiringpi.LOW)
    print("off")
    time.sleep(.1)
