import time
import wiringpi

print("start")
pin1 = 3

wiringpi.wiringPiSetup()
wiringpi.pinMode(pin1, 1)



while True:
    #S
    wiringpi.digitalWrite(pin1,1)
    time.sleep(.5)
    wiringpi.digitalWrite(pin1,0)
    time.sleep(.5)
    wiringpi.digitalWrite(pin1,1)
    time.sleep(.5)
    wiringpi.digitalWrite(pin1,0)
    time.sleep(.5)
    wiringpi.digitalWrite(pin1,1)
    time.sleep(.5)
    wiringpi.digitalWrite(pin1,0)
    time.sleep(.5)

    #O
    wiringpi.digitalWrite(pin1,1)
    time.sleep(1.5)
    wiringpi.digitalWrite(pin1,0)
    time.sleep(.5)
    wiringpi.digitalWrite(pin1,1)
    time.sleep(1.5)
    wiringpi.digitalWrite(pin1,0)
    time.sleep(.5)
    wiringpi.digitalWrite(pin1,1)
    time.sleep(1.5)
    wiringpi.digitalWrite(pin1,0)
    time.sleep(.5)
    #S
    wiringpi.digitalWrite(pin1,1)
    time.sleep(.5)
    wiringpi.digitalWrite(pin1,0)
    time.sleep(.5)
    wiringpi.digitalWrite(pin1,1)
    time.sleep(.5)
    wiringpi.digitalWrite(pin1,0)
    time.sleep(.5)
    wiringpi.digitalWrite(pin1,1)
    time.sleep(.5)
    wiringpi.digitalWrite(pin1,0)
    time.sleep(1.5)

