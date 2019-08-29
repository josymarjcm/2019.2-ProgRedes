import json
import xml.etree.ElementTree as ET
import requests
from xml.dom import minidom
from xml.etree.ElementTree import Element, ElementTree 

while True:
	
	# Variaveis a serem passadas como parâmetros das URLs da API
	numero_cep      = 59170000#int(input("Digite o cep: "))
	formato_retorno = 'xml'#input("Digite o formato: ")

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
		print('CEP: {0} / Cidade: {1} / Estado: {2}'.format(dados_cep['cep'], dados_cep['localidade'], dados_cep['uf']))

	   	#	print('CEP: {0} / Cidade: {1} / Estado: {2}'.format(dados_cep[i]['cep'], dados_cep[i]['logradouro'], dados_cep[i]['bairro']))
		break
	elif formato_retorno.lower()=="xml":
		arqxml = open('arqxml.xml', 'w')
		#Montando o XML de Retorno
		dados_cep = getInformacoes() 

		arqxml.write(dados_cep)
		arqxml.close()

		'''tree = ElementTree(file="arqxml.xml")
		r = tree.getroot()
		cep = r.find('cep')'''

		#fxml = open('Dados_cep.txt', 'w')
		arqxml = open('arqxml.xml', 'r')
		cont = 0
		for i in range(12):
			cont+=1
			linha = arqxml.readline()
			#print(linha)
			if cont == 3:
				cep1 = "<cep>"
				cep2 = "</cep>"
				linha = linha.replace(cep1, "")
				linha = linha.replace(cep2, "")
				fxml1 = linha
			elif cont == 7:
				localidade1 = "<localidade>"
				localidade2 = "</localidade>"
				linha = linha.replace(localidade1, "")
				linha = linha.replace(localidade2, "")
				fxml2 = linha
			elif cont == 8:
				uf1 = "<uf>"
				uf2 = "</uf>"
				linha = linha.replace(uf1,"")
				linha = linha.replace(uf2,"")
				fxml3 = linha
		print(f'CEP:{fxml1}Estado:{fxml3}Cidade{fxml2}')
		#print('CEP:    {0}Estado: {1}Cidade: {2} '.format(fxml1, fxml3, fxml2))
				#fxml.write(linha)
		#arqxml.write(dados_cep)'''
		
		
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


