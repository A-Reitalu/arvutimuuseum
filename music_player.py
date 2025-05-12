import serial
import time
import subprocess


def search_and_play():
    Trigger_words = ["CRZYFROG","BADPIGS","DAISYBEL","HLGEHALL"]
    # === Configuration ===
    SERIAL_PORT = '/dev/ttyACM0'
    BAUDRATE = 115200

    # === Connect to Arduino ===
    ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)
    time.sleep(3)  # Wait for Arduino to reboot
    
    # === Send "dir" command to list floppy files ===
    ser.write(b'dir\r\n')

    # === Read response ===
    print("Checking for trigger file on floppy...")
    found = False
    start = time.time()
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print(line)
            if any(trigger in line for trigger in Trigger_words):
                found = True
                song = line.split()[0]
                print(song)
                break
        if line == "A:>" or (time.time() - start > 5):  # End when prompt returns or timeout
            break

    ser.close()

    # === Play audio if file is found ===
    if found:
        print("Trigger file found! Playing sound...")
        subprocess.run(['aplay', f"./music/{song}.wav"])
    else:
        print("Trigger file NOT found.")

if __name__ == "__main__":
    search_and_play()