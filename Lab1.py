
#Adeept Lesson 1
#Blinking LED
#Modified by Pelin Kurtay

import RPi.GPIO as GPIO
import time

LedPin = 11# pin11

GPIO.setmode(GPIO.BOARD)       # Number pins according to physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(LedPin, GPIO.HIGH) # Set pin to high (+3.3V) to turn LED off 

try:
	while True:
		print ('...led on')
		GPIO.output(LedPin, GPIO.LOW)  # LED on
		time.sleep(0.5)
		print ('led off...')
		GPIO.output(LedPin, GPIO.HIGH) # LED off
		time.sleep(0.5)
		
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the next two lines will be executed:
	GPIO.output(LedPin, GPIO.HIGH)     # turn LED off
	GPIO.cleanup()                     # Release resource
	
	
