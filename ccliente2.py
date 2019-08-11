import socket
HOST = '10.0.0.106' #ip do server
PORT = 55454 # porta do server




while True:	
	nomeArquivo = input('Digite o nome do arquivo: ')
	nomeArquivo = nomeArquivo.encode('utf-8')
	try :
		tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcp_socket.connect((HOST, PORT))
	
		fd = open(nomeArquivo, "r")
		tcp_socket.send(nomeArquivo)
		
		while True:
	 
		    msg = fd.readline()

		    msg = msg.encode('utf-8')
		    
		    tcp_socket.send(msg)

		    if not msg: break
	except:
		print("Arquivo não encontrado!")
		tcp_socket.close()
	

tcp_socket.close()


