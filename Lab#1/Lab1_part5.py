import RPi.GPIO as GPIO
import time

sel = [3,5,7,11,13]
selorder = [1,2,3,4,5,4,3,2,1]

GPIO.setmode(GPIO.BOARD)       # Number pins according to physical location
for i in sel:
  GPIO.setup(i, GPIO.OUT)   # Set pin mode as output
  GPIO.output(i, GPIO.HIGH) # Set pin to high (+3.3V) to turn LED off 

try:
	while True:
    for x in selorder:
      GPIO.output(sel[x-1], GPIO.LOW) #On
      time.sleep(1)
      GPIO.output(sel[x-1], GPIO.HIGH) #Off
      time.sleep(1)
      
      
    
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the next two lines will be executed:
	GPIO.output(LedPin1, GPIO.HIGH)     # turn LED off
	GPIO.output(LedPin2, GPIO.HIGH)     # turn LED off
	GPIO.cleanup()                     # Release resource
