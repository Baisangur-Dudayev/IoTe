import time
import wiringpi
import sys

# Set up GPIO 1 as output
wiringpi.wiringPiSetup()
wiringpi.pinMode(1, wiringpi.OUTPUT)

# Endless loop to measure capacitance repeatedly
while True:
    # Set GPIO 1 output to low and wait 0.1 seconds
    wiringpi.digitalWrite(1, wiringpi.LOW)
    time.sleep(0.1)

    # Set up GPIO 1 as input
    wiringpi.pinMode(1, wiringpi.INPUT)

    # Wait for input to go high and record start time
    start_time = time.time()
    while wiringpi.digitalRead(1) == wiringpi.LOW:
        time.sleep(0.01)

    # Record stop time and calculate interval
    stop_time = time.time()
    interval = stop_time - start_time

    # Print the interval
    print("Interval: ", interval)