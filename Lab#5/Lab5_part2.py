import RPi.GPIO as GPIO
import time

# GPIO pin setup
CLK = 16    # Rotary encoder CLK pin
DT = 18     # Rotary encoder DT pin

# Initialize counter and last state
counter = 0
last_state = None
debounce_time = 0.01  # Debounce time in seconds

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    global counter, last_state
    last_state = GPIO.input(CLK)
    
    while True:
        current_state = GPIO.input(CLK)
        if current_state != last_state:
            time.sleep(debounce_time)  # Debounce
            if GPIO.input(CLK) == current_state:  # Confirm state change
                if GPIO.input(DT) != current_state:
                    counter += 1  # Clockwise
                else:
                    counter -= 1  # Counterclockwise
                print(f"Counter: {counter}")
        last_state = current_state
        time.sleep(0.01)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
