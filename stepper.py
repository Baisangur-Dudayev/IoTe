import time
import wiringpi

print("start")
blu_pin = 2
Pin_pin = 3
Yel_pin = 4
Ora_pin = 6
wiringpi.wiringPiSetup()
wiringpi.pinMode(blu_pin, 1)
wiringpi.pinMode(Pin_pin, 1)
wiringpi.pinMode(Yel_pin, 1)
wiringpi.pinMode(Ora_pin, 1)

#MAIN
while True:
    wiringpi.digitalWrite(blu_pin,1)
    time.sleep(2)
    wiringpi.digitalWrite(blu_pin,0)
    wiringpi.digitalWrite(Pin_pin,1)
    time.sleep(0.01)
    wiringpi.digitalWrite(Pin_pin,0)
    wiringpi.digitalWrite(Yel_pin,1) 
    time.sleep(2)
    wiringpi.digitalWrite(Yel_pin,0)

    wiringpi.digitalWrite(Ora_pin, 1)
    time.sleep(2)
    wiringpi.digitalWrite(Ora_pin, 0)

