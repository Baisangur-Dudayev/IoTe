import time
import wiringpi

print("start")
blu_pin = 3
Pin_pin = 4 
Yel_pin = 6 
Ora_pin = 9 
wiringpi.wiringPiSetup()
wiringpi.pinMode(blu_pin, 1)
wiringpi.pinMode(Pin_pin, 1)
wiringpi.pinMode(Yel_pin, 1)
wiringpi.pinMode(Ora_pin, 1)

while True:
    wiringpi.digitalWrite(blu_pin,1)
    time.sleep(.1)
    wiringpi.digitalWrite(blu_pin,0)
    wiringpi.digitalWrite(Pin_pin,1)
    time.sleep(.1)
    wiringpi.digitalWrite(Pin_pin,0)
    wiringpi.digitalWrite(Yel_pin,1) 
    time.sleep(.1)
    wiringpi.digitalWrite(Yel_pin,0)

    wiringpi.digitalWrite(Ora_pin, 1)
    time.sleep(.1)
    wiringpi.digitalWrite(Ora_pin, 0)
