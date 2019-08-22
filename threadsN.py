import time
import threading

fd_primos = open('VALORES_PRIMOS.TXT', 'w')
fd_nprimos = open('VALORES_NAO_PRIMOS.TXT','w')
fd_tempo = open('TEMPO_GASTO.txt', 'w')

def primos(var):
  cont = 0
  for div in range(1, var+1):
    if var%div == 0:
      cont += 1
  if cont == 2 and var > 1:
    fat = var
    num_fat =  threading.Thread(target=fatorial, args=(fat, ), name='p2')
    num_fat.start()
    var = str(var) +" - "+ str(num_fat) +'\n'
    fd_primos.write(var)
  else:
    var = str(var) + '\n'
    fd_nprimos.write(var)
    

def fatorial(fat):
  total = 1
  for f in range(1, fat+1):
    total = total * f
  return(total)
  
num = int(input("Digite um valor: "))

inicio = time.time()
for var in range (1, num+1):
  num_vez = threading.Thread(target=primos, args=(var, ), name='p1')
  num_vez.start()

termino = time.time()

tempo = termino-inicio
tempo = str(tempo)+" segundos"

fd_tempo.write(tempo)
