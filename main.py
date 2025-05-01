import RPi.GPIO as GPIO
import threading
import time
import serial

floppy_liigutamise_nupp = 14
Kõlari_eksponaadi_nupp = 15
HDD_liigutamise_nupp = 18
HDD_mootor1 = 17
HDD_mootor2 = 27
HDD_mootor_PWM = 24 
HDD_pea1 = 22
HDD_pea2 = 23
HDD_pea_PWM = 25

#peame blokeerima floppy liigutamise eksponaadi selleks ajaks, kui sealt helifaile loetakse:
floppy_lugemise_block = threading.lock()

GPIO.setmode(GPIO.BCM)
#nupud:
GPIO.setup(floppy_liigutamise_nupp, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Kõlari_eksponaadi_nupp, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(HDD_liigutamise_nupp, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#HDD mootori liigutamine:
GPIO.setup(HDD_mootor1, GPIO.OUT)
GPIO.setup(HDD_mootor2, GPIO.OUT)
GPIO.setup(HDD_mootor_PWM, GPIO.OUT)
PWM_mootor = GPIO.PWM(HDD_mootor_PWM, 1000)
#PWM_mootor.start(0)
#HDD pea liigutamine:
GPIO.setup(HDD_pea1, GPIO.OUT)
GPIO.setup(HDD_pea2, GPIO.OUT)
GPIO.setup(HDD_pea_PWM, GPIO.OUT)
PWM_pea = GPIO.PWM(HDD_pea_PWM, 1000)
#PWM_pea.start(0)


def main():
    pass

if __name__ == "__main__":
    main()