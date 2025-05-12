import serial
import time

def send_and_read(cmd,ser):
    ser.write(cmd.encode())
    time.sleep(0.2)
    while ser.in_waiting:
        print(ser.readline().decode(errors="ignore").strip())


def move_floppys():
    SERIAL_PORT = '/dev/ttyACM0'
    BAUDRATE = 115200

    # === Connect to Arduino ===
    ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)
    time.sleep(3)  # Wait for Arduino to reboot
    
    send_and_read('monitor\r\n',ser)

    for i in range(1,79,19):
        send_and_read(f"r {i},1\r\n",ser)
        time.sleep(1)
        
    #switch the drive and turn off its motor:
    send_and_read('s 1\r\n',ser)
    time.sleep(0.5)
    send_and_read('m 0\r\n',ser)
    time.sleep(0.5)

    for i in range(1,39,9):
        send_and_read(f"r {i},1\r\n",ser)
        time.sleep(2)

    ser.close()

if __name__ == "__main__":
    move_floppys()