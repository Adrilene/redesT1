import socket
import time
import webbrowser

def messageRequest():
    site = input('insira o arquivo: ')
    request = 'GET ' + site + ' HTTP/1.1'
     
    return request

def Main():
	host = '127.0.0.2'
	port = 5000
		
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	while True:
		print('Disponível?')
		try:
			clientSocket.connect((host, port))
		except:
			print('Server offline')
			clientSocket.close()
			break

		print('Conectado!')

		mrequest = messageRequest()
		clientSocket.send(mrequest.encode())
		print('Aguardando resposta...')
		time.sleep(0.5)

		response = clientSocket.recv(2048).decode()

		print('Resposta do Server: ')
		print(response)

		break

	print('Encerrando conexão...')
	clientSocket.close()

if __name__ == '__main__':
    Main()