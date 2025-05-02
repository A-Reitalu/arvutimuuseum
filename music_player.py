import serial
import time
import subprocess

# === Configuration ===
SERIAL_PORT = '/dev/ttyACM0'     # Adjust if needed
BAUDRATE = 115200
TRIGGER_FILE = 'CRZYFROG.raw'
AUDIO_FILE = '/music/CRZYFROG.wav'

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
        if TRIGGER_FILE.lower() in line.lower():
            found = True
    if "A:>" in line or (time.time() - start > 5):  # End when prompt returns or timeout
        break

ser.close()

# === Play audio if file is found ===
if found:
    print("Trigger file found! Playing sound...")
    subprocess.run(['aplay', AUDIO_FILE])
else:
    print("Trigger file NOT found.")