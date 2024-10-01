#Controlling an LED using a switch and turning an active buzzer on when button is pressed 

import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11 LED Pin
BzrPin = 12    # pin12 Buzzer Pin
BtnPin = 13    # pin13 Button Pin
#(LedPin1, BzrPin, LedPin2)
OutLowArr = [11, 15, 12]
# (BtPin1, BtPin2)
BtnArr = [13, 16]

IO1 = 0
IO2 = 0

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
for i in OutLowArr:  
  GPIO.setup(i, GPIO.OUT)   # Set LedPin's mode as output
  GPIO.setup(i, GPIO.LOW)   #Set BzrPin's output to low-turn LED off at start
for x in 
  GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode as input, and pull



#Poll the input of the BtnPin continuously to detect if its state is high or low. If low, button is pressed 
# so turn on the LED by applying a high value to LEDPin to turn LED on and apply a high value to BzrPin to turn
# on the buzzer. Otherwise output low value from both pins to keep both LED and buzzer off. 
#Print status of LED on the screen to the user 
try:
	while True:
		if	GPIO.input(BtnArr[0]) == GPIO.LOW:
        		IO1 = IO1 ^ 1
		if	GPIO.input(BtnArr[1]) == GPIO.LOW:
        		IO2 = IO2 ^ 1



      	if IO1 == 1 or IO2 == 1:
        	GPIO.output(OutLowArr[IO2], GPIO.HIGH)  # turn led on
        	GPIO.output(OutLowArr[IO1], GPIO.LOW)  # turn led on
		GPIO.output(OutLowArr[2], GPIO.LOW) # buzzer off
		print("...SINGLE LED ON")
      	elif IO1 == 1 and IO2 == 1:
        	GPIO.output(OutLowArr[2], GPIO.HIGH)
        	GPIO.output(OutLowArr[1], GPIO.HIGH)
        	GPIO.output(OutLowArr[0], GPIO.HIGH)
		print("...BOTH LED ON")
      	else:
        	GPIO.output(OutLowArr[0], GPIO.LOW) # led off
		GPIO.output(OutLowArr[1], GPIO.LOW) # led off
		GPIO.output(OutLowArr[2], GPIO.LOW) # buzzer off
		print("ALL LED OFF...")


except KeyboardInterrupt:               #set up keyboard interrupt ctrl C
  	for y in OutLowArr:  
		GPIO.output(y, GPIO.LOW) # LED off
		GPIO.output(y, GPIO.LOW) # Buzzer off
	GPIO.cleanup()                          #cleanup all used GPIO pins
	print ("Ending program")                #print end of program to terminal
  
