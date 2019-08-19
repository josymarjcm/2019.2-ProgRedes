import time

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
    var = str(var) + '\n'
    fd_primos.write(var)
    fator=fatorial(fat)
    return("é PRIMO",fator)
  else:
    var = str(var) + '\n'
    fd_nprimos.write(var)
    return ("")

def fatorial(fat):
  total = 1
  for f in range(1, fat+1):
    total = total * f
  return (total)

num = int(input("Digite um valor: "))

inicio = time.time()
for var in range (1, num+1):
  print(var,primos(var))

termino = time.time()

tempo = termino-inicio
tempo = str(tempo)+" segundos"

fd_tempo.write(tempo)
