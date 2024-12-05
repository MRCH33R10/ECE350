import RPi.GPIO as GPIO
from time import sleep

# Use BCM GPIO numbering (recommended for clarity)
GPIO.setmode(GPIO.BCM)  # Changed to BCM
GPIO.setwarnings(False)

# Define the GPIO pin connected to the servo (adjust if needed)
servo_pin = 22  # Example: Change to the actual GPIO pin connected to your servo

# Set up the GPIO pin as output
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM instance (50Hz)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

# Function to control the servo angle (degrees)
def set_servo_angle(angle):
    """Sets the servo angle. Angle should be between 0 and 180 degrees."""
    if not 0 <= angle <= 180:
        raise ValueError("Angle must be between 0 and 180 degrees.")

    # Calculate duty cycle (adjust these values based on your servo's specifics)
    duty_cycle = (angle / 180.0) + 0.05 # Calibration may be needed here

    # Map duty cycle to pulse width (approximately)
    pulse_width = duty_cycle * 20 # 20ms period

    # Set the duty cycle (0 to 100%)
    pwm.ChangeDutyCycle(pulse_width)
    sleep(0.1)

try:
    # Example usage:
    print("Moving servo...")
    set_servo_angle(0)  # Go to 0 degrees
    sleep(1)
    set_servo_angle(90) # Go to 90 degrees
    sleep(1)
    set_servo_angle(180) # Go to 180 degrees
    sleep(1)
    set_servo_angle(90) # Go to 90 degrees
    sleep(1)
    set_servo_angle(0) # Go to 0 degrees
    sleep(1)

except KeyboardInterrupt:
    print("Servo control stopped.")

finally:
    pwm.stop()
    GPIO.cleanup()
