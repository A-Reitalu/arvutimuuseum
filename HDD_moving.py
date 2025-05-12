import RPi.GPIO as GPIO
import time

MOTOR_HEAD1 = 17 #22
MOTOR_HEAD2 = 27 #23
ENA = 24 #25
MOTOR_SPIN3 = 22 #17
MOTOR_SPIN4 = 23 #27
ENB = 25 #25

GPIO.setmode(GPIO.BCM)

GPIO.setup(MOTOR_HEAD1, GPIO.OUT)
GPIO.setup(MOTOR_HEAD2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(MOTOR_SPIN3, GPIO.OUT)
GPIO.setup(MOTOR_SPIN4, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

PWM_A = GPIO.PWM(ENA, 1000)
PWM_A.start(0) # Start with 0% duty cycle
#PWM_B = GPIO.PWM(ENB, 1000)
#PWM_B.start(0)

def MoveHDD():
    try:
        while True:
            # Motor forward
            GPIO.output(MOTOR_HEAD1, GPIO.HIGH)
            GPIO.output(MOTOR_HEAD2, GPIO.LOW)
            PWM_A.ChangeDutyCycle(30)
            print("Motor running forward...")
            time.sleep(1)

            # Motor stop
            GPIO.output(MOTOR_HEAD1, GPIO.LOW)
            GPIO.output(MOTOR_HEAD2, GPIO.LOW)
            PWM_A.ChangeDutyCycle(0)
            print("Motor stopped.")
            time.sleep(2)

            # Motor backward (if you want to test direction)
            GPIO.output(MOTOR_HEAD1, GPIO.LOW)
            GPIO.output(MOTOR_HEAD2, GPIO.HIGH)
            PWM_A.ChangeDutyCycle(30)
            print("Motor running backward...")
            time.sleep(1)

            # Motor stop
            GPIO.output(MOTOR_HEAD1, GPIO.LOW)
            GPIO.output(MOTOR_HEAD2, GPIO.LOW)
            PWM_A.ChangeDutyCycle(0)
            print("Motor stopped.")
            time.sleep(2)

    except KeyboardInterrupt:
        # Graceful exit
        print("Stopping motor.")
        GPIO.output(MOTOR_HEAD1, GPIO.LOW)
        GPIO.output(MOTOR_HEAD2, GPIO.LOW)
        GPIO.cleanup()


