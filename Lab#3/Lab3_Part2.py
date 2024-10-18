import RPi.GPIO as GPIO
import time


servopin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servopin, GPIO.OUT)
p = GPIO.PWM(servopin,50)
p.start(0)
time.sleep(2)

try: 
	while(True):
		p.start(12.5)
		time.sleep(5)
		for i in range(0,181,18):
			print('i=',i)
			p.ChangeDutyCycle(2.5 + 5.5 * i / 180)
			time.sleep(0.1)
		for i in range(180,0,-18):
			print('........i=',i)
			p.ChangeDutyCycle(2.5 + 5.5 * i / 180)
			time.sleep(0.1)

except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
