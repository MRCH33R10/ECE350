import RPi.GPIO as GPIO
import time

LedPin1 = 11 # pin11
LedPin2 = 13 # pin11

GPIO.setmode(GPIO.BOARD)       # Number pins according to physical location
GPIO.setup(LedPin1, GPIO.OUT)   # Set pin mode as output
GPIO.output(LedPin1, GPIO.HIGH) # Set pin to high (+3.3V) to turn LED off 
GPIO.setup(LedPin2, GPIO.OUT)   # Set pin mode as output
GPIO.output(LedPin2, GPIO.HIGH) # Set pin to high (+3.3V) to turn LED off 

try:
	while True:
		print ('...led on')
		GPIO.output(LedPin1, GPIO.LOW)  
    GPIO.output(LedPin2, GPIO.HIGH) 
		time.sleep(5)
		print ('led off...')
		GPIO.output(LedPin1, GPIO.HIGH)
    GPIO.output(LedPin2, GPIO.LOW)  
		time.sleep(5)
		
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the next two lines will be executed:
	GPIO.output(LedPin1, GPIO.HIGH)     # turn LED off
  GPIO.output(LedPin2, GPIO.HIGH)     # turn LED off
	GPIO.cleanup()                     # Release resource
