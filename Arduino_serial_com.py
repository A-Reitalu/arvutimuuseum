import serial
import time

ser = serial.Serial('/dev/ttyACM0',115200,timeout=1)
time.sleep(3)

ser.write(b'monitor\r\n')
time.sleep(0.5)

ser.write(b'm 0\r\n')
time.sleep(0.5)

ser.write(b's 1\r\n')
time.sleep(0.5)

ser.write(b'r 0,1\r\n')
time.sleep(0.5)



#ser.write(b'dir\r\n')
#time.sleep(0.5)

while True:
    line = ser.readline()
    if line:
        print(line.decode('utf-8').strip())
        empty = 0
    else:
        empty += 1
        if empty >= 3:
            break 
ser.close()