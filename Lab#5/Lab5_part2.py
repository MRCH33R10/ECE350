import RPi.GPIO as GPIO
import time

# GPIO pin setup
IN1 = 11    # pin11  
IN2 = 12
IN3 = 13
IN4 = 15
CLK = 16    # Rotary encoder CLK pin
DT = 18     # Rotary encoder DT pin

# Initialize counter
counter = 0
last_state = None

def setStep(w1, w2, w3, w4):
    GPIO.output(IN1, w1)
    GPIO.output(IN2, w2)
    GPIO.output(IN3, w3)
    GPIO.output(IN4, w4)

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

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location  
    GPIO.setup(IN1, GPIO.OUT)      # Set pin's mode is output  
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)
    GPIO.setup(CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    global counter, last_state
    last_state = GPIO.input(CLK)
    
    while True:
        current_state = GPIO.input(CLK)
        time.sleep(0.1)
        if current_state != last_state:  # Confirm state change
            if GPIO.input(DT) != current_state:
                counter += 1
                forward(0.003, 1)  
            else:
                counter -= 1
                backward(0.003, 1)
            print(f"Counter: {counter}")
        # else:
        #     if counter > 0:
        #         forward(0.003, 512) 
        #         stop()
        #         counter -= 1
        #     elif counter < 0:
        #         backward(0.003, 512)
        #         stop()
        #         counter += 1
                    
        last_state = current_state
        time.sleep(0.01)

def destroy():
    GPIO.cleanup()             # Release resource  

if __name__ == '__main__':     # Program start from here  
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.  
        destroy()
