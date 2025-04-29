import RPi.GPIO as GPIO
import time

# Define pins
IN1 = 17
IN2 = 27
ENA = 24

GPIO.setmode(GPIO.BCM)

# Setup pins
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

# Set up PWM on ENA at 1 kHz
pwm = GPIO.PWM(ENA, 1000)
pwm.start(0)  # Start with 0% duty

try:
    while True:
        # Move head in one direction
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        for duty in range(0, 50, 2):  # ramp up to 50%
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.05)

        for duty in range(50, -1, -2):  # ramp down
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.05)

        # Stop movement
        pwm.ChangeDutyCycle(0)
        time.sleep(0.2)

        # Move head in the opposite direction
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        for duty in range(0, 50, 2):
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.05)

        for duty in range(50, -1, -2):
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.05)

        time.sleep(0.2)

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()