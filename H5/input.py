import time
import wiringpi
import sys

#SETUP
print("Start")
pinLed = 2
pinSwitch = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(pinLed, 1)		#set pin to  mode 1 (OUTPUT)
wiringpi.pinMode(pinSwitch, 0)		#set pin to mode 0 (OUTPUT)

#infinite loop - stop using CTRL-C
while True:
	if(wiringpi.digitalRead(pinSwitch) == 0): #input is active low
		print("Button Pressed")
		time.sleep(0.3) #anti bouncing
		wiringpi.digitalWrite(pinLed, 1)
	else:
		print("Button released")
		time.sleep(0.3) #anti bouncing
		wiringpi.digitalWrite(pinLed, 0)
