import socket

HOST = ''  # endereço IP do servidor
PORT =         # Porta utilizada pelo servidor
BUFFER_SIZE =   # tamanho do buffer para recepção dos dados

def receive_file(file_name):
    try:
        # Cria um socket UDP
        client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        server_address = (HOST, PORT)

        # Envia o nome do arquivo para o servidor
        client_socket.sendto(file_name.encode(), server_address)

        # Aguarda a resposta do servidor
        data, _ = client_socket.recvfrom(BUFFER_SIZE)
        response = data.decode()

        if response == 'Arquivo encontrado':
            # Recebe as linhas do arquivo do servidor
            while True:
                data, _ = client_socket.recvfrom(BUFFER_SIZE)
                line = data.decode()
                if line == 'Fim':
                    break
                print(line)

            print(f'O arquivo "{file_name}" foi recebido com sucesso.')

        else:
            print(f'O arquivo "{file_name}" não foi encontrado.')

    except Exception as error:
        print(f"Erro ao receber o arquivo {file_name}")
        print(error)

    finally:
        client_socket.close()

def main():
    file_name = input("Digite o nome do arquivo que deseja receber: ")
    receive_file(file_name)

if __name__ == "__main__":
    main()
