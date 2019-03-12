'''
	Universidade Estadual do Ceará
	Ciência da Computação
	Redes de Computadores
	Prof: Bruno Araújo Lima
	Alunos: Adrilene Pessoa da Fonseca - 1381145
			Ricardo de Carvalho Oliveira Filho - 1368080
'''

import socket 

#Função que monta a mensagem a ser passada como request, seguindo o padrão HTTP
def messageRequest():
    file = input('Insira nome arquivo: ')
    request = 'GET {} HTTP/1.1\n'.format(file)
     
    return request

def Main():

	#Define a porta e o endereço (iguais do server)
	host = '127.0.0.2'
	port = 5000
		
	#Inicia o socket com uma conexão TCP
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	while True:
		print('Disponível?')
		
		#verifica se a conexão é feita
		try:
			clientSocket.connect((host, port))
		except:
			print('Server offline')
			break

		print('Conectado!\n')
		
		#Tendo conectado, envia o request para o socket
		mrequest = messageRequest()
		clientSocket.send(mrequest.encode())
		print('Aguardando resposta...')

		#Recebe a resposta do Server e imprime
		response = clientSocket.recv(2048).decode()
		print('\nResposta do Server: ')
		print(response)

		break

	#Depois de feita, encerra a conexão
	print('\nEncerrando conexão...')
	clientSocket.close()

if __name__ == '__main__':
    Main()