import time
import threading

fd_primos = open('VALORES_PRIMOS.TXT', 'w')
fd_nprimos = open('VALORES_NAO_PRIMOS.TXT','w')
fd_tempo = open('TEMPO_GASTO.TXT', 'w')
fd_fibonacci = open('NUMEROS_FIBONACCI.TXT', 'w')


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
    
    nfibonacci = threading.Thread(target=fibonacci, args=(var, ), name='p3')
    nfibonacci.start()
    var = str(var) + '\n'
    fd_nprimos.write(var)

def fibonacci(var):
  gerAt = 1
  gerPa = 1
  n=2
  if var>2:
    while n<var:
      gerAt += gerPa
      gerPa = gerAt - gerPa
      n+=1
    wrt = str(gerAt) + '\n'
    fd_fibonacci.write(wrt)
  else:
    wrt = '1' + '\n'
    return(fd_fibonacci.write(wrt))

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
