num = int(input("Digite um número: "))
cont = 0

fdprimos = open('VALORES_PRIMOS.TXT','w')
fdnprimos = open('VALORES_NAO_PRIMOS.TXT','w')

def primos(var):
	if var == 1:
		print(var, "é primo")
		fatorial(var)
	for test in range(1, var+1):
		if var%test==0:
			cont +=1
	if cont==2 and var>1:
		fatorial(var)
		print("é primo", var)
		fdprimos.write(var)
	else:
		fdnprimos.write(var)

def fatorial(test):
	mult = 1
	for pdt in range(1,test+1):
		mult = mult*pdt
	print("fatorial de", var,"é",mult)

for var in range(1, num+1):
	primos(var)
	print(var)