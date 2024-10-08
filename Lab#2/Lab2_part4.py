#Controlling an LED using a switch and turning an active buzzer on when button is pressed 

import RPi.GPIO as GPIO
import time


#(LedPin1, BzrPin, LedPin2)
OutLowArr = [11, 12]

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
for i in OutLowArr:  
  GPIO.setup(i, GPIO.OUT)   # Set LedPin's mode as output
  GPIO.setup(i, GPIO.LOW)   #Set BzrPin's output to low-turn LED off at start

try:
	while True:
		GPIO.output(OutLowArr[1], GPIO.LOW)
		GPIO.output(OutLowArr[0], GPIO.LOW)
		for i in range(0,1000):
			GPIO.output(OutLowArr[1], GPIO.HIGH)
			GPIO.output(OutLowArr[0], GPIO.HIGH)
			time.sleep(i/200000)
			GPIO.output(OutLowArr[1], GPIO.LOW)
			GPIO.output(OutLowArr[0], GPIO.LOW)
			time.sleep((1000-i)/100000)

		GPIO.output(OutLowArr[1], GPIO.HIGH)
		GPIO.output(OutLowArr[0], GPIO.HIGH)
		for i in range(1000,0,-1):
			GPIO.output(OutLowArr[1], GPIO.HIGH)
			GPIO.output(OutLowArr[0], GPIO.HIGH)
			time.sleep(i/200000)
			GPIO.output(OutLowArr[1], GPIO.LOW)
			GPIO.output(OutLowArr[0], GPIO.LOW)
			time.sleep((1000-i)/100000)

		GPIO.output(OutLowArr[1], GPIO.HIGH)
		GPIO.output(OutLowArr[0], GPIO.HIGH)
        
except KeyboardInterrupt:               #set up keyboard interrupt ctrl C
	for y in OutLowArr:  
		GPIO.output(y, GPIO.LOW) # LED off
		GPIO.output(y, GPIO.LOW) # Buzzer off		
	GPIO.cleanup()                          #cleanup all used GPIO pins
	print ("Ending program")                #print end of program to terminal
  


