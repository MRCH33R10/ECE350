#Controlling an LED using a switch and turning an active buzzer on when button is pressed 

import RPi.GPIO as GPIO
import time

BzrPin = 12    # pin12 Buzzer Pin
tmeARR = [0.1, 0.9, 0.4, 0.6, 0.9, 0.1, 0.1, 0.9, 0.4, 0.6, 0.9, 0.1]
freqARR = [200,400,600,200,400,600]
IO = 1
GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(BzrPin, GPIO.OUT)  # Set BzrPin's mode as output
GPIO.setup(BzrPin, GPIO.LOW)  # Set BzrPin's output to low-turn buzzer off at start



#Poll the input of the BtnPin continuously to detect if its state is high or low. If low, button is pressed 
# so turn on the LED by applying a high value to LEDPin to turn LED on and apply a high value to BzrPin to turn
# on the buzzer. Otherwise output low value from both pins to keep both LED and buzzer off. 
#Print status of LED on the screen to the user 
try:
	while True:
		for i in tmeARR:
			if IO == 1:
				GPIO.setup(BzrPin, GPIO.HIGH)
			else:
				GPIO.setup(BzrPin, GPIO.LOW)
      			time.sleep(i)
      			IO = IO ^ 1
    		for x in freqARR:
      			for y in range(x):
        			GPIO.setup(BzrPin, GPIO.HIGH)
        			time.sleep(.9/x)
        			GPIO.setup(BzrPin, GPIO.LOW)
        			time.sleep(.1/x)
        
except KeyboardInterrupt:               #set up keyboard interrupt ctrl C
	GPIO.output(BzrPin, GPIO.LOW) # Buzzer off
	GPIO.cleanup()                          #cleanup all used GPIO pins
	print ("Ending program")                #print end of program to terminal
  

