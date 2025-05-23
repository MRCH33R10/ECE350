import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF, 0X6F00D2, 0xFF5809]

R = 11
G = 12
B = 13

def setup(Rpin, Gpin, Bpin):
  global pins
  global p_R, p_G, p_B
  pins = {'pin_R': Rpin, 'pin_G': Gpin, 'pin_B': Bpin}
  GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
  for i in pins:
    GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode as output
    GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to turn LED off

  p_R = GPIO.PWM(pins['pin_R'], 2000)  # set PWM frequency to 2KHz
  p_G = GPIO.PWM(pins['pin_G'], 2000)
  p_B = GPIO.PWM(pins['pin_B'], 2000)

  p_R.start(100)      # Initial duty Cycle = 100 (All LEDs off)
  p_G.start(100)
  p_B.start(100)

def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def off():
  for i in pins:
    GPIO.output(pins[i], GPIO.HIGH)    # Turn off all leds

def setColor(col):   # For example : col = 0x112233
  R_val = (col & 0xff0000) >> 16 #extract each R,G,B color component from list of colors
  G_val = (col & 0x00ff00) >> 8
  B_val = (col & 0x0000ff) >> 0

  R_val = map(R_val, 0, 255, 0, 100)  #map each RGB color component from 0-255 levels to 0-100
  G_val = map(G_val, 0, 255, 0, 100)
  B_val = map(B_val, 0, 255, 0, 100)

  p_R.ChangeDutyCycle(100-R_val)     # Change duty cycle
  p_G.ChangeDutyCycle(100-G_val)
  p_B.ChangeDutyCycle(100-B_val)

def loop():							#cycle through the 10 different colors in the list with 0.5s between colors
  while True:
    for col in colors:
      setColor(col)
      time.sleep(0.5)

def destroy():
  p_R.stop()
  p_G.stop()
  p_B.stop()
  off()
  GPIO.cleanup()

if __name__ == "__main__":
  try:
    setup(R, G, B)
    loop()
  except KeyboardInterrupt:
    destroy()
