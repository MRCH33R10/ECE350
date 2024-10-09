#Controlling an LED using a switch and turning an active buzzer on when button is pressed 

import RPi.GPIO as GPIO
import time

tmeARR = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

#(LedPin1, BzrPin, LedPin2)
OutLowArr = [11, 12]

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
for i in OutLowArr:  
  GPIO.setup(i, GPIO.OUT)   # Set LedPin's mode as output
  GPIO.setup(i, GPIO.LOW)   #Set BzrPin's output to low-turn LED off at start

try:
	while True:
		for i in range(1,200):
			for x in range(200): #100Hz
				GPIO.output(OutLowArr[1], GPIO.HIGH)
				GPIO.output(OutLowArr[0], GPIO.HIGH)
				time.sleep(1/i)
				GPIO.output(OutLowArr[1], GPIO.LOW)
				GPIO.output(OutLowArr[0], GPIO.LOW)
				time.sleep(1-1/i)
        			
        
except KeyboardInterrupt:               #set up keyboard interrupt ctrl C
	for y in OutLowArr:  
		GPIO.output(y, GPIO.LOW) # LED off
		GPIO.output(y, GPIO.LOW) # Buzzer off
		GPIO.cleanup()                          #cleanup all used GPIO pins
		print ("Ending program")                #print end of program to terminal
  


