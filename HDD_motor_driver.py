import RPi.GPIO as GPIO
import time

# L298N pin definitions
MOTOR_IN3 = 22  # Choose your GPIO pin numbers (BCM numbering)
MOTOR_IN4 = 23

# Setup
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(MOTOR_IN3, GPIO.OUT)
GPIO.setup(MOTOR_IN4, GPIO.OUT)

try:
    while True:
        # Motor forward
        GPIO.output(MOTOR_IN3, GPIO.HIGH)
        GPIO.output(MOTOR_IN4, GPIO.LOW)
        print("Motor running forward...")
        time.sleep(3)

        # Motor stop
        GPIO.output(MOTOR_IN3, GPIO.LOW)
        GPIO.output(MOTOR_IN4, GPIO.LOW)
        print("Motor stopped.")
        time.sleep(2)

        # Motor backward (if you want to test direction)
        GPIO.output(MOTOR_IN3, GPIO.LOW)
        GPIO.output(MOTOR_IN4, GPIO.HIGH)
        print("Motor running backward...")
        time.sleep(3)

        # Motor stop
        GPIO.output(MOTOR_IN3, GPIO.LOW)
        GPIO.output(MOTOR_IN4, GPIO.LOW)
        print("Motor stopped.")
        time.sleep(2)

except KeyboardInterrupt:
    # Graceful exit
    print("Stopping motor.")
    GPIO.output(MOTOR_IN3, GPIO.LOW)
    GPIO.output(MOTOR_IN4, GPIO.LOW)
    GPIO.cleanup()
