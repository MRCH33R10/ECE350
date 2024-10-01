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
for x in 
  GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode as input, and pull

try:
	while True:
    		for i in tmeARR:
			for x in range(100): #100Hz
      				GPIO.setup(OutlowArr[1], GPIO.HIGH)
				GPIO.output(OutlowArr[0], GPIO.HIGH)
        			time.sleep(i/100)
      				GPIO.setup(OutlowArr[1], GPIO.HIGH)
				GPIO.output(OutlowArr[0], GPIO.HIGH)
        			time.sleep((1-i)/100)
        			
        
except KeyboardInterrupt:               #set up keyboard interrupt ctrl C
	GPIO.output(BzrPin, GPIO.LOW) # Buzzer off
	GPIO.cleanup()                          #cleanup all used GPIO pins
	print ("Ending program")                #print end of program to terminal
  


