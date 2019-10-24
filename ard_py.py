import time
#import serial
from random import randint

#connect = serial.Serial('COM4', 9600)
acertos=0
n = 1
l=[]
l2=[]
while True:
    for n_s in range(0, n):
        a = randint(4,7)
        l.append(a)
        a = str(a)
    
    print(l)
    time.sleep(1)
    print("Verificando a sequência: ")
    time.sleep(1)
    #for n_r in range(0, n):
    b = int(input())
    #    l2.append(b)
    #    b = str(b)#
    
    if len(l) ==b : 
        print("Você acertou!")
        acertos+=len(l)
    else:
        print("Você errou!")
        print("Seus acertos foram: ", acertos)
        break
    
#connect.close()
       
