import time
import serial
from random import randint

connect = serial.Serial('porta', 9600)

l=[]
i = 0
while True:
    a = randint(0,3)
    l.append(a)
    connect.write(a)
    connect.read()
    time.sleep(1)   
    i+=1
connect.close()
print(l)
