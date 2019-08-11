#Aluno: Josymar Cortez de Melo
import socket

host = '10.0.0.106'
port = 55454

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.bind((host, port))
tcp_socket.listen(5)

print('Aguardando Mensagens...\n\n')
con, cliente = tcp_socket.accept()
print('Conectado por: ', cliente)

    
arq = con.recv(512)
arq = arq.decode('utf-8')

fdin = open(arq,'w')
while True:                
    msg = con.recv(4096)
    msg = msg.decode('utf-8')
    fdin.write(msg)
    if not msg: break
    'print(cliente, ": ", msg)'
