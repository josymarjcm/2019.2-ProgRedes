import time
import serial
from random import randint

connect = serial.Serial('COM10', 9600)

l=[]
i = 0
while i<100:
    a = randint(0,3)
    l.append(a)
    a = str(a)

    connect.write('a'.encode())
    #connect.read()
    time.sleep(2)   
    i+=1
connect.close()
print(l)
