import json
import xml.etree.ElementTree as ET
import requests
from xml.dom import minidom
from xml.etree.ElementTree import Element, ElementTree 

while True:
	
	# Variaveis a serem passadas como parâmetros das URLs da API
	numero_cep      = int(input("Digite o cep: "))
	formato_retorno = input("Digite o formato: ")

	# Variaveis a serem passadas como parâmetros das URLs da API
	#
	#
	# Dicionario com as chamadas da API

	urls = { "url_cep_1":"https://viacep.com.br/ws/{0}/{1}".format(numero_cep, formato_retorno)}

	# Função para retorno dos dados gerados pela API
	def getInformacoes():
	    response = requests.get(urls['url_cep_1'], headers='')
	    if response.status_code == 200:
	        return response.content.decode('utf-8')
	    return None

	if formato_retorno.lower()=="json":
		# Montando o JSON de Retorno
		dados_cep = json.loads(getInformacoes())

		print('')
		
		# Imprimindo o dado tratado
		print(' CEP: {0}\n Logradouro: {1}\n Bairro: {2}\n Cidade: {3}\n Estado: {4}\n IBGE: {5}\n'.format(dados_cep['cep'], 
			dados_cep['logradouro'], dados_cep['bairro'], dados_cep['localidade'], dados_cep['uf'], dados_cep['ibge']))

	   	
		break
	elif formato_retorno.lower()=="xml":
		arqxml = open('arqxml.xml', 'w')
		#Montando o XML de Retorno
		dados_cep = getInformacoes() 

		arqxml.write(dados_cep)
		arqxml.close()

		arqxml = open('arqxml.xml', 'r')
		cont = 0
		#Tratando o dado XML:
		for i in range(12):
			cont+=1
			linha = arqxml.readline()
			if cont == 3:
				cep1 = "<cep>"
				cep2 = "</cep>"
				linha = linha.replace(cep1, "")
				linha = linha.replace(cep2, "")
				fxml3 = linha
			elif cont == 4:
				logradouro1 = "<logradouro>"
				logradouro2 = "</logradouro>"
				linha = linha.replace(logradouro1,"")
				linha = linha.replace(logradouro2,"")
				fxml4 = linha
			elif cont == 6:
				bairro1 = "<bairro>"
				bairro2 = "</bairro>"
				linha = linha.replace(bairro1, "")
				linha = linha.replace(bairro2, "")
				fxml6 = linha
			elif cont == 7:
				localidade1 = "<localidade>"
				localidade2 = "</localidade>"
				linha = linha.replace(localidade1, "")
				linha = linha.replace(localidade2, "")
				fxml7 = linha
			elif cont == 8:
				uf1 = "<uf>"
				uf2 = "</uf>"
				linha = linha.replace(uf1,"")
				linha = linha.replace(uf2,"")
				fxml8 = linha
			elif cont == 10:
				ibge1 = "<ibge>"
				ibge2 = "</ibge>"
				linha = linha.replace(ibge1,"")
				linha = linha.replace(ibge2,"")
				fxml10 = linha
		# Imprimindo o dado tratado
		print("")
		print(f' CEP:{fxml3} Logradouro:{fxml4} Bairro:{fxml6} Localidade:{fxml7} Estado:{fxml8} IBGE:{fxml10}')
		
		break
	else:
		print("Formato inválido.")


