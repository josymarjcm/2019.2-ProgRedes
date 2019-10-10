import time
import serial
from random import randint

connect = serial.Serial('COM4', 9600)

l=[]
while True:
    a = randint(0,3)
    l.append(a)
    a= str(a)
    connect.write(a.encode())
    print(l)
    time.sleep(1)       
connect.close()
