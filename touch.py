import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbering
button_pin = 23
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Pull-down resistor

# Debounce variables
button_state = False
debounce_time = 0.2  # Debounce time in seconds

try:
    while True:
        if GPIO.input(button_pin) == GPIO.HIGH:
            if not button_state: # Check if the button state has changed
                button_state = True
                print("Button Pressed")
                time.sleep(debounce_time) # Wait for debounce time

        else:
            button_state = False  # Reset the button state when the button is released

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Exiting...")
