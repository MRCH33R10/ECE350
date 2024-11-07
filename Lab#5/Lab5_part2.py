import RPi.GPIO as GPIO
import time

RoAPin = 16    # pin11
RoBPin = 18    # pin12
IN1 = 11    # pin11  
IN2 = 12
IN3 = 13
IN4 = 15

globalCounter = 0
stepcounter = 0

flag = 0
Last_RoB_Status = 0
Current_RoB_Status = 0

def setStep(w1, w2, w3, w4):
	GPIO.output(IN1, w1)
	GPIO.output(IN2, w2)
	GPIO.output(IN3, w3)
	GPIO.output(IN4, w4)
def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(RoAPin, GPIO.IN)    # input mode
	GPIO.setup(RoBPin, GPIO.IN)	
	GPIO.setup(IN1, GPIO.OUT)      # Set pin's mode is output  
	GPIO.setup(IN2, GPIO.OUT)
	GPIO.setup(IN3, GPIO.OUT)
	GPIO.setup(IN4, GPIO.OUT)
def stop():
	setStep(0, 0, 0, 0)
def forward(delay, steps):    
	for i in range(0, steps):
		setStep(1, 0, 0, 0)
		time.sleep(delay)
		setStep(0, 1, 0, 0)
		time.sleep(delay)
		setStep(0, 0, 1, 0)
		time.sleep(delay)
		setStep(0, 0, 0, 1)
		time.sleep(delay)
def backward(delay, steps):
	for i in range(0, steps):
		setStep(0, 0, 0, 1)
		time.sleep(delay)
		setStep(0, 0, 1, 0)
		time.sleep(delay)
		setStep(0, 1, 0, 0)
		time.sleep(delay)
		setStep(1, 0, 0, 0)
		time.sleep(delay)
def rotaryDeal():
	global flag
	global Last_RoB_Status
	global Current_RoB_Status
	global globalCounter
	Last_RoB_Status = GPIO.input(RoBPin)
	while(not GPIO.input(RoAPin)):
		Current_RoB_Status = GPIO.input(RoBPin)
		flag = 1
	if flag == 1:
		flag = 0
		if (Last_RoB_Status == 0) and (Current_RoB_Status == 1):
			globalCounter = globalCounter - 1
			if stepcounter > 0:
				backward(0.003, 800)  # 512 steps --- 360 angle  
				stop()                 # stop  
				stepcounter -= 1
		if (Last_RoB_Status == 1) and (Current_RoB_Status == 0):
			globalCounter = globalCounter + 1
			if stepcounter < 4:
				forward(0.003, 800)  # 512 steps --- 360 angle  
				stop()                 # stop  
				stepcounter += 1	
	else:
		if globalCounter > 0:
			globalCounter -= 1
		elif globalCounter < 0:
			globalCounter += 1


def loop():
	global globalCounter
	tmp = 0	# Rotary Temperary

	while True:
		rotaryDeal()
		if tmp != globalCounter:
			print('globalCounter = %d' % globalCounter)
			tmp = globalCounter

def destroy():
	GPIO.cleanup()             # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
