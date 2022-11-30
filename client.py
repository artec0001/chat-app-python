import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#botar seu ip em locahost 8888 e a porta
#put your ip in locahost 8888 and the port
client.connect(('localhost', 8888))

terminado = False
print('Digite tt para terminar o chat')

while not terminado:
    client.send(input('Mensagem').encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == 'tt':
        terminado = True
    else:
        print(msg)
client.close()