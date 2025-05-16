import RPi.GPIO as GPIO
import time

MOTOR_HEAD1 = 22
MOTOR_HEAD2 = 23
ENA = 25
MOTOR_SPIN3 = 17
MOTOR_SPIN4 = 27
ENB = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(MOTOR_HEAD1, GPIO.OUT)
GPIO.setup(MOTOR_HEAD2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(MOTOR_SPIN3, GPIO.OUT)
GPIO.setup(MOTOR_SPIN4, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

PWM_A = GPIO.PWM(ENA, 1000)
PWM_A.start(0) # Start with 0% duty cycle
PWM_B = GPIO.PWM(ENB, 1000)
PWM_B.start(100)

def MoveHDD():
    try:
        GPIO.output(MOTOR_SPIN3, GPIO.HIGH)
        GPIO.output(MOTOR_SPIN4, GPIO.LOW)
        while True:
            # Motor forward
            GPIO.output(MOTOR_HEAD1, GPIO.HIGH)
            GPIO.output(MOTOR_HEAD2, GPIO.LOW)
            PWM_A.ChangeDutyCycle(100)
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
            PWM_A.ChangeDutyCycle(100)
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
        GPIO.output(MOTOR_SPIN3, GPIO.LOW)
        GPIO.output(MOTOR_SPIN4, GPIO.LOW)
        GPIO.cleanup()

if __name__ == "__main__":
    MoveHDD()
