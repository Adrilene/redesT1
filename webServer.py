'''
	Universidade Estadual do Ceará
	Ciência da Computação
	Redes de Computadores
	Prof: Bruno Araújo Lima
	Alunos: Adrilene Pessoa da Fonseca - 1381145
			Ricardo de Carvalho Oliveira Filho - 1368080
'''

import socket

def Main():
	#endereço e porta específicos (iguais do client)
	host = "127.0.0.2"
	port = 5000

	#Configura o socket e inicia no host e porta específica
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverSocket.bind((host,port))

	#espera requests no socket
	serverSocket.listen(1)
	print('Pronto para conexão...')

	while True:
		
		#recebe a conexão de um endereço ( client)
		conn, addr = serverSocket.accept()
		
		print("Conexão de: {}\n".format(str(addr)))
	
		try:
			#lê o request recebido e o exibe
			data = conn.recv(2048).decode()
			print('Request recebido:\n'+ data)
			filename = data.split(' ')[1]   #recupera o nome do arquivo

			#abre o arquivo que foi solicitado e 'avisa' que foi encontrado
			f = open(filename[0:])
			outputdata = f.read()
			print('\nArquivo disponível!')
			conn.send(('HTTP/1.1 200 OK\r\n\r\n').encode())

			#envia o arquivo para o cliente
			for i in range(0, len(outputdata)):  
				conn.send((outputdata[i]).encode())
			conn.send(("\r\n").encode())

			#tendo enviado, fecha a conexão
			print('Enviado! Fechando Conexão...')
			conn.close()
			serverSocket.close()
			break

		except IOError:
			#caso o arquivo solicitado não tenha sido encontrado, avisa ao cliente
			print('\nArquivo não disponível!')
			conn.send(('HTTP/1.1 404 Not Found\r\n\r\n').encode())
			
			#envia o arquivo NotFound
			f = open('pageNotFound.html')
			outputdata = f.read()

			for i in range(0, len(outputdata)):  
				conn.send((outputdata[i]).encode())
			conn.send(("\r\n").encode())

			print('Fechando conexão...')
			conn.close()
			serverSocket.close()
			break
	serverSocket.close()

if __name__ == '__main__':
	Main()