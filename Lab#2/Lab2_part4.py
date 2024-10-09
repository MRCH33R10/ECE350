#Controlling an LED using a switch and turning an active buzzer on when button is pressed 

import RPi.GPIO as GPIO
import time

tmeARR = [1.00, 0.95, 0.90, 0.85, 0.80, 0.75, 0.70, 0.65, 0.60, 0.55, 0.50, 0.45, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05, 0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00]

#(LedPin1, BzrPin, LedPin2)
OutLowArr = [11, 12]

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
for i in OutLowArr:  
  GPIO.setup(i, GPIO.OUT)   # Set LedPin's mode as output
  GPIO.setup(i, GPIO.LOW)   #Set BzrPin's output to low-turn LED off at start

try:
	while True:
		for i in range(1,99):
			for w in range(10):
				GPIO.output(OutLowArr[1], GPIO.HIGH)
				GPIO.output(OutLowArr[0], GPIO.HIGH)
				time.sleep(i/20000)
				GPIO.output(OutLowArr[1], GPIO.LOW)
				GPIO.output(OutLowArr[0], GPIO.LOW)
				time.sleep((100-i)/20000)
		for i in range(1,99):
			for w in range(10):
				GPIO.output(OutLowArr[1], GPIO.HIGH)
				GPIO.output(OutLowArr[0], GPIO.HIGH)
				time.sleep((100-i)/20000)
				GPIO.output(OutLowArr[1], GPIO.LOW)
				GPIO.output(OutLowArr[0], GPIO.LOW)
				time.sleep(i/20000)	
        
except KeyboardInterrupt:               #set up keyboard interrupt ctrl C
	for y in OutLowArr:  
		GPIO.output(y, GPIO.LOW) # LED off
		GPIO.output(y, GPIO.LOW) # Buzzer off		
	GPIO.cleanup()                          #cleanup all used GPIO pins
	print ("Ending program")                #print end of program to terminal
  


