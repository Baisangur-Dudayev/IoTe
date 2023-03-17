import time
import wiringpi

print("start")
pin1 = 3
pin2 = 4 
pin3 = 6 
pin4 = 9 
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin1, 1)
wiringpi.pinMode(pin2, 1)
wiringpi.pinMode(pin3, 1)
wiringpi.pinMode(pin4, 1)

while True:
    
    wiringpi.digitalWrite(pin1,1)
    wiringpi.digitalWrite(pin2,0)
    wiringpi.digitalWrite(pin3,1)
    wiringpi.digitalWrite(pin4,0)
    time.sleep(1)
    wiringpi.digitalWrite(pin1,0)
    wiringpi.digitalWrite(pin2,1)
    wiringpi.digitalWrite(pin3,0)
    wiringpi.digitalWrite(pin4,1)
    time.sleep(1)

