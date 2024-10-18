import RPi.GPIO as GPIO
import time


servopin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servopin, GPIO.OUT)
p = GPIO.PWM(servopin,50)
p.start(0)
time.sleep(1)

try: 
	while(True):
		for i in range(0,181,10):
			print('i=',i)
			p.ChangeDutyCycle(2.5 + 10 * i / 180)
			time.sleep(0.2)
			p.ChangeDutyCycle(0)
			time.sleep(0.5)

		for i in range(180,0,-10):
			print('........i=',i)
			p.ChangeDutyCycle(2.5 + 10 * i / 180)
			time.sleep(0.2)
			p.ChangeDutyCycle(0)
			time.sleep(0.5)

except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
