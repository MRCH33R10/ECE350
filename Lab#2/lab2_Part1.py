#Controlling an LED using a switch and turning an active buzzer on when button is pressed 

import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11 LED Pin
BzrPin = 12    # pin12 Buzzer Pin
BtnPin = 13    # pin13 Button Pin

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode as output
GPIO.setup(LedPin, GPIO.LOW)   #Set BzrPin's output to low-turn LED off at start
GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode as input, and pull
GPIO.setup(BzrPin, GPIO.OUT)  # Set BzrPin's mode as output
GPIO.setup(BzrPin, GPIO.LOW)  # Set BzrPin's output to low-turn buzzer off at start



#Poll the input of the BtnPin continuously to detect if its state is high or low. If low, button is pressed 
# so turn on the LED by applying a high value to LEDPin to turn LED on and apply a high value to BzrPin to turn
# on the buzzer. Otherwise output low value from both pins to keep both LED and buzzer off. 
#Print status of LED on the screen to the user 
try:
	while True:
			if	GPIO.input(BtnPin) == GPIO.LOW:
				GPIO.output(LedPin, GPIO.HIGH)  # turn led on
				GPIO.output(BzrPin, GPIO.HIGH) # turn buzzer on
				print("...LED ON")
			else:
				GPIO.output(LedPin, GPIO.LOW) # led off
				GPIO.output(BzrPin, GPIO.LOW) # buzzer off
				print("LED OFF...")
				


except KeyboardInterrupt:               #set up keyboard interrupt ctrl C
	GPIO.output(LedPin, GPIO.LOW) # LED off
	GPIO.output(BzrPin, GPIO.LOW) # Buzzer off
	GPIO.cleanup()                          #cleanup all used GPIO pins
	print ("Ending program")                #print end of program to terminal
  
