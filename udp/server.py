import socket
import sys
import os
from threading import Thread

HOST = '127.0.0.1'  # endereço IP
PORT = 20001        # Porta utilizada pelo servidor
BUFFER_SIZE = 1024  # tamanho do buffer para recepção dos dados

def send_file(file_name, client_address):
    try:
        # Verifica se o arquivo existe
        if os.path.isfile(file_name):
            # Envia a confirmação para o cliente
            server_socket.sendto('Arquivo encontrado'.encode(), client_address)

            # Lê o arquivo e envia linha por linha para o cliente
            with open(file_name, 'r') as file:
                for line in file:
                    server_socket.sendto(line.encode(), client_address)

            # Envia um indicador de finalização para o cliente
            server_socket.sendto(b'Fim', client_address)
            print(f'O arquivo "{file_name}" foi enviado para {client_address[0]}:{client_address[1]}')
        else:
            # Envia uma mensagem de erro para o cliente
            server_socket.sendto('Arquivo não encontrado'.encode(), client_address)
            print(f'O arquivo "{file_name}" não foi encontrado.')

    except Exception as error:
        print(f"Erro ao enviar o arquivo {file_name} para {client_address[0]}:{client_address[1]}")
        print(error)

def main(argv):
    try:
        # Cria um socket UDP
        global server_socket
        server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # Associa o socket ao endereço e porta
        server_socket.bind((HOST, PORT))
        print("Servidor UDP iniciado e ouvindo")

        # Aguarda as mensagens do cliente
        while True:
            bytesAddressPair = server_socket.recvfrom(BUFFER_SIZE)
            message = bytesAddressPair[0]
            address = bytesAddressPair[1]

            # Verifica se a mensagem contém um nome de arquivo
            file_name = message.decode()
            if file_name.startswith('FILE:'):
                file_name = file_name[5:]  # Remove o prefixo 'FILE:' da mensagem

                # Cria uma nova thread para lidar com o envio do arquivo
                thread = Thread(target=send_file, args=(file_name, address))
                thread.start()
            else:
                client_msg = "Mensagem do cliente: {}".format(message.decode())
                client_ip = "Client IP Address: {}".format(address)
                print(client_msg)
                print(client_ip)
                # Envia a mesma mensagem de volta para o cliente
                server_socket.sendto(message, address)

    except Exception as error:
        print("Erro na execução do servidor!!")
        print(error)

    finally:
        server_socket.close()


if __name__ == "__main__":
    main(sys.argv[1:])