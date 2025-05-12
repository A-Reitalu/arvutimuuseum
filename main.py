import RPi.GPIO as GPIO
import threading
import music_player
import floppy_moving

floppy_liigutamise_nupp = 21
Kõlari_eksponaadi_nupp = 16
HDD_liigutamise_nupp = 20

Floppy_block = threading.Lock()

def button_callback(channel):
    print(f"Button toggled on GPIO {channel}")
    match channel:
        case 21:
            print("floppy liigutamine")
            threading.Thread(target=locked_floppy_moving, daemon=True).start()
        case 20:
            print("HDD liigutamine")
        case 16:
            print("Kõlar")
            leitud, laul = locked_floppy_speaker()
            if leitud:
                threading.Thread(target=music_player.play_song,args=[laul],daemon=True).start()

def locked_floppy_moving():
    with Floppy_block:
        floppy_moving.move_floppys()
        return
    print("floppy draiv on hetkel hõivatud")

def locked_floppy_speaker():
    with Floppy_block:
        return music_player.search_for_song()
    print("floppy draiv on hetkel hõivatud")
    return False, ""

GPIO.setmode(GPIO.BCM)
#nupud:
GPIO.setup(floppy_liigutamise_nupp, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Kõlari_eksponaadi_nupp, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(HDD_liigutamise_nupp, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(floppy_liigutamise_nupp, GPIO.BOTH, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(Kõlari_eksponaadi_nupp, GPIO.BOTH, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(HDD_liigutamise_nupp, GPIO.BOTH, callback=button_callback, bouncetime=200)

def main():
    try:
        input("Press Enter to exit\n")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()