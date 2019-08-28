import json
import xml.etree.ElementTree as ET
import requests
from xml.dom import minidom

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

		# Imprimindo o resultado Bruto (RAW)
		print (dados_cep)
		print('')
		print('')
		print('CEP: {0} / Cidade: {1} / Estado: {2}'.format(dados_cep['cep'], dados_cep['localidade'], dados_cep['uf']))
		# Imprimindo o dado tratado

		#for i in range(len(dados_cep)):
	   	#	print('CEP: {0} / Cidade: {1} / Estado: {2}'.format(dados_cep[i]['cep'], dados_cep[i]['logradouro'], dados_cep[i]['bairro']))
		break
	elif formato_retorno.lower()=="xml":
		arqxml = open('arqxml.xml', 'w')
		dados_cep = getInformacoes()
		arqxml.write(dados_cep)
		
		print(arqxml)
		'''arq = minidom.parseString(arqxml)

		itemlist = arq.getElementsByTagName('cep')
		itemlist2 = arq.getElementsByTagName('localidade')
		itemlist3 = arq.getElementsByTagName('uf') 

		print('CEP: {0} / Cidade: {1} / Estado: {2}'.format(itemlist, itemlist2, itemlist3))
    	#print('CEP: {0} / Cidade: {1} / Estado: {2}'.format(root.get('cep'), root.get('localidade'), root.get('uf')))
		'''
		break
	else:
		print("Formato inválido.")
