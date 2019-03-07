import socket
import time
import webbrowser

page = 'empty'

def messageRequest():
    site = input('Insira o Site: ')
    request = 'GET {} HTTP/1.1\nHost: www.{}.com\nConnection: close\nUser-agent: Chrome/70.0\nAccept-language:pt\n'.format(site,site)
     
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
			time.sleep(1)
			clientSocket.close()
			break

		print('Conectado!\n')

		mrequest = messageRequest()
		clientSocket.send(mrequest.encode())
		print('Aguardando resposta...')
		time.sleep(1)

		response = clientSocket.recv(2048).decode()

		print('\nResposta do Server: ')
		print(response)
		if(response.split(' ')[1] == 200):
			page = response.split(' ')[3].split('\n')[0]
		else:
			page = response.split(' ')[4]

		break

	print('\nEncerrando conexão...')
	clientSocket.close()

	if(page != 'empty'):
		print('\nAbrindo página...')
		webbrowser.open(page, new=0, autoraise=True)

if __name__ == '__main__':
    Main()


