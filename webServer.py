import socket
import time
from datetime import datetime

listAvailable = ['google','uece']
today = datetime.today()

def Main():
	host = "127.0.0.2"
	port = 5000

	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverSocket.bind((host,port))

	serverSocket.listen(1)
	print('Pronto para conexão...')

	while True:
		
		try:
			conn, addr = serverSocket.accept()
		except socket.error:
			break			
		
		print("Conexão de: {}\n".format(str(addr)))
	
		data = conn.recv(2048).decode()
		print('Request recebido:\n'+ data)
		site = data.split(' ')

		if not data:
			break

		if (site[1] in listAvailable):
			print('\nDisponível')
			responseRequest = 'HTTP/1.1 200 OK pageFound.html\nConnection: close\nDate: {}\nServer: {}\nLast-Modified: diadiadiadiada\nContent-Length: 6821\nContent-Type: text/html\n'.format(today.ctime(),host)
		else:
			print('\nNot Found')
			responseRequest = 'HTTP/1.1 404 Not Found pageNotFound.html'

		conn.send(responseRequest.encode())			
		print('\nEnviando resposta...')
		time.sleep(1)
		print('\nEnviado!')
		break

	conn.close()

if __name__ == '__main__':
	Main()