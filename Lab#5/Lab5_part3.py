import RPi.GPIO as GPIO
import time

# GPIO pin setup
RoAPin = 16    # Rotary encoder CLK pin
RoBPin = 18    # Rotary encoder DT pin
ButtonPin = 22 # Rotary encoder button pin
IN1 = 11       # Stepper motor pin
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
    GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button with pull-up resistor
    GPIO.setup(IN1, GPIO.OUT)      # Set pin's mode is output  
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)

def stop():
    setStep(0, 0, 0, 0)

def forward(delay, steps):    
    for i in range(steps):
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 0, 0, 1)
        time.sleep(delay)

def backward(delay, steps):
    for i in range(steps):
        setStep(0, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(1, 0, 0, 0)
        time.sleep(delay)

def halfStepForward(delay, steps):
    for i in range(steps):
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        setStep(1, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 0, 1, 1)
        time.sleep(delay)
        setStep(0, 0, 0, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)

def halfStepBackward(delay, steps):
    for i in range(steps):
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 0, 1, 1)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(1, 1, 0, 0)
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
            globalCounter -= 1
        if (Last_RoB_Status == 1) and (Current_RoB_Status == 0):
            globalCounter += 1

def loop():
    global globalCounter
    tmp = 0  # Rotary Temporary

    while True:
        if GPIO.input(ButtonPin) == GPIO.LOW:  # Button pressed
            globalCounter = 0
            print("Global counter reset to 0")
            time.sleep(0.5)  # Debounce delay

        rotaryDeal()
        if tmp != globalCounter:
            print('globalCounter = %d' % globalCounter)
            tmp = globalCounter

        if globalCounter == 1:
            print("Full-step drive mode")
            forward(0.01, 1)
        elif globalCounter == -1:
            print("Half-step drive mode")
            halfStepForward(0.01, 1)
        elif globalCounter == 0:
            stop()

        time.sleep(0.01)

def destroy():
    GPIO.cleanup()  # Release resource

if __name__ == '__main__':  # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
        destroy()
