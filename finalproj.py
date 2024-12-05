import time
import RPi.GPIO as GPIO
import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import subprocess
import datetime
import os

# Set GPIO mode to BCM (Broadcom GPIO pin numbering)
GPIO.setmode(GPIO.BCM)

# PIR motion sensor pin
pir_pin = 4
led_pin = 14

clk = 0
# Set PIR sensor pin as input
GPIO.setup(pir_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbering
button_pin = 23
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Pull-down resistor

# Debounce variables
button_state = False
debounce_time = 0.2  # Debounce time in seconds

def blink_led(pin, num_blinks, blink_speed):
    for _ in range(num_blinks):
        GPIO.output(pin, GPIO.HIGH)  # Turn the LED on
        time.sleep(blink_speed)
        GPIO.output(pin, GPIO.LOW)  # Turn the LED off
        time.sleep(blink_speed)

# Function to record video using OpenCV with USB camera
def record_video(filename, duration=10):
    cap = cv2.VideoCapture(0)  # Open the camera (index 0 typically corresponds to the first connected USB camera)
    
    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return

    # Set video parameters: lower frame rate (10 fps) and resolution (640x480)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 10)  # Reduce frame rate to 10 FPS to avoid overloading

    # Generate a timestamped filename
    filename = datetime.datetime.now().strftime("/media/nthomp8/B33F-EA9A/VideoLog/%Y-%m-%d_%H-%M-%S.avi")
    # print(f"Recording video to file: {filename}")

    # Set codec for video output (MJPEG codec for AVI file)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # 'MJPG' codec
    out = cv2.VideoWriter(filename, fourcc, 10.0, (640, 480))  # Write to an .avi file

    if not out.isOpened():
        print("Error: VideoWriter initialization failed.")
        cap.release()
        return

    print(f"Recording started for {duration} seconds.")
    start_time = time.time()  # Start time
    frame_count = 0

    try:
        while time.time() - start_time < duration:
            ret, frame = cap.read()
            if ret:
                out.write(frame)
                frame_count += 1
                # Removed cv2.imshow - no need to display live feed
            else:
                print("Error: Unable to read frame.")
                break
    except Exception as e:
        print(f"Exception during video recording: {e}")
    finally:
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        elapsed_time = time.time() - start_time
        print(f"Recording stopped after {elapsed_time:.2f} seconds. Total frames captured: {frame_count}")

        # Convert the recorded video to .mp4 format using ffmpeg
        mp4_filename = filename.replace('.avi', '.mp4')
        convert_video_to_mp4(filename, mp4_filename)

# Function to convert AVI video to MP4 using ffmpeg
def convert_video_to_mp4(input_filename, output_filename):
    try:
        # print(f"Converting {input_filename} to {output_filename}")
        subprocess.run(['ffmpeg', '-i', input_filename, '-c:v', 'libx264', '-c:a', 'aac', '-strict', 'experimental', output_filename], check=True) #Added check=True for error handling
        # print(f"Conversion successful: {output_filename}")
        os.remove(input_filename) #remove the avi file
    except subprocess.CalledProcessError as e:
        print(f"Error during video conversion: {e}")
    except FileNotFoundError:
        print(f"ffmpeg not found. Make sure it's installed and in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred during conversion: {e}")


# Function to send email with video attachment
def send_email(video_filename):
    # Sender and recipient email addresses
    fromaddr = "youremail@example.com"  # Replace with your email
    toaddr = "receiveremail@example.com"  # Replace with recipient's email
    
    # Use the generated App Password instead of your regular password
    app_password = "YOUR_APP_PASSWORD"  # Replace with your App Password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Motion Detected: Video Attached"
    
    # Attach the video file
    try:
        with open(video_filename, "rb") as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(video_filename)}')
        msg.attach(part)
    except FileNotFoundError:
        print(f"Error: The file {video_filename} was not found.")
        return

    # Connect to SMTP server and send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail SMTP server
        server.starttls()
        server.login(fromaddr, app_password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()


# Main function to control the flow of the program
def main():
    while True:
        if GPIO.input(button_pin) == GPIO.HIGH:
            if not button_state: # Check if the button state has changed
                button_state = True
                clk += 1
                time.sleep(debounce_time) # Wait for debounce time
        # Check for motion using the PIR sensor
        if clk == 1:
            blink_led(led_pin, 5, 0.5)
            
            if GPIO.input(pir_pin) == GPIO.HIGH:
                print("Motion detected!")

                # Record video when motion is detected
                video_filename = "motion_video.mp4" #changed to mp4 to avoid double conversion
                record_video(video_filename)
                
                # Pause for 10 seconds before checking motion again
                time.sleep(10)
            else:
                print("No motion detected.")

        time.sleep(1)  # Check for motion every 1 second

# Run the program
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        GPIO.cleanup()
