import serial
import time

ser = serial.Serial('COM6', 9600)
time.sleep(10)
while True:
    line = ser.readline()
    print(line)

