import serial
import time

ser = serial.Serial('/dev/ttyACM0',115200,timeout=1)

time.sleep(2)

ser.write(b'monitor\r')
time.sleep(0.5)
ser.write(b'm 0\r')
ser.write(b'x\r')
time.sleep(0.5)
ser.write(b'dir\r')

while True:
    line = ser.readline()
    if not line:
        break
    print(line.decode('utf-8').strip())

ser.close()