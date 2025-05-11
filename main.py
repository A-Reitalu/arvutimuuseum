import RPi.GPIO as GPIO
import threading
import time
import serial
import music_player

floppy_liigutamise_nupp = 21
Kõlari_eksponaadi_nupp = 16
HDD_liigutamise_nupp = 20
# HDD_mootor1 = 17
# HDD_mootor2 = 27
# HDD_mootor_PWM = 24 
# HDD_pea1 = 22
# HDD_pea2 = 23
# HDD_pea_PWM = 25

def button_callback(channel):
    print(f"Button toggled on GPIO {channel}")

GPIO.setmode(GPIO.BCM)
# #nupud:
GPIO.setup(floppy_liigutamise_nupp, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Kõlari_eksponaadi_nupp, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(HDD_liigutamise_nupp, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(floppy_liigutamise_nupp, GPIO.BOTH, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(Kõlari_eksponaadi_nupp, GPIO.BOTH, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(HDD_liigutamise_nupp, GPIO.BOTH, callback=button_callback, bouncetime=200)
# #HDD mootori liigutamine:
# GPIO.setup(HDD_mootor1, GPIO.OUT)
# GPIO.setup(HDD_mootor2, GPIO.OUT)
# GPIO.setup(HDD_mootor_PWM, GPIO.OUT)
# PWM_mootor = GPIO.PWM(HDD_mootor_PWM, 1000)
# #PWM_mootor.start(0)
# #HDD pea liigutamine:
# GPIO.setup(HDD_pea1, GPIO.OUT)
# GPIO.setup(HDD_pea2, GPIO.OUT)
# GPIO.setup(HDD_pea_PWM, GPIO.OUT)
# PWM_pea = GPIO.PWM(HDD_pea_PWM, 1000)
#PWM_pea.start(0)

def main():
    try:
        input("Press Enter to exit\n")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()