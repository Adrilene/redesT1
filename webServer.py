import socket
import time

listAvailable = ['google','uece', 'alunoonline']

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
		
		print("Conexão de: " + str(addr))
	
		data = conn.recv(2048).decode()
		site = data.split(' ')

		if not data:
			break

		if (site[1] in listAvailable):
			print('Disponível')
			responseRequest = 'HTTP/1.1 200 OK pageFound.html'
		else:
			print('Not Found')
			responseRequest = 'HTTP/1.1 404 Not Found pageNotFound.html'

		conn.send(responseRequest.encode())			
		print('Enviando resposta...')
		time.sleep(0.5)
		print('Enviado!')
		break

	conn.close()

if __name__ == '__main__':
	Main()