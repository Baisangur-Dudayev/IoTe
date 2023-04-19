import time
import wiringpi 
import sys

def controlLEDs(sig1, sig2, cnt, wait):
	
	time.sleep(wait)

#SETUP
print("Start")
pin2 = 2
pin5 = 5
pause_time = 2           # you can change this to slow down/speed up
wiringpi.wiringPiSetup() 

# Set pins as a softPWM output
wiringpi.softPwmCreate(pin2, 0, 100)
wiringpi.softPwmCreate(pin5, 0, 100)

try:
	while True:
		wiringpi.softPwmWrite(pin2, 0)
		wiringpi.softPwmWrite(pin5, 100)
		time.sleep(10)
		wiringpi.softPwmWrite(pin2, 0)
		wiringpi.softPwmWrite(pin5, 0)
		time.sleep(2)
		wiringpi.softPwmWrite(pin2, 100)
		wiringpi.softPwmWrite(pin5, 0)
		time.sleep(10)
		wiringpi.softPwmWrite(pin2, 0)
		wiringpi.softPwmWrite(pin5, 0)
		time.sleep(2)

except KeyboardInterrupt:
	wiringpi.softPwmWrite(pin2, 0)            # stop the white PWM output
	wiringpi.softPwmWrite(pin5, 0)            # stop the white PWM output
	print("\nDone")