import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#botar seu ip em locahost 8888 e a porta
#put your ip in locahost 8888 and the port
server.bind(('localhost', 8888))

server.listen()
cliente, end = server.accept()

terminado = False

while not terminado:
    msg = cliente.recv(1024).decode('utf-8')
    if msg == 'tt':
        terminado = True
    else:
        print(msg)

    cliente.send(input('Mensagem: ').encode('utf8'))

cliente.close()
server.close()