import socket
import time

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    host = 'localhost'
    port = 9999

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    bufferSize = 1024

    while True:
        try:
            fileName = input("Digite o nome do arquivo (ou 'sair' para encerrar): ")
            if fileName == 'sair':
                break

            client.sendto(fileName.encode(), (host, port))
            folderPath = "files_reiceved/"

            with open(folderPath + fileName, 'w') as file:
                start_time = time.time()
                while True:
                    data, address = client.recvfrom(bufferSize)
                    line = data.decode()
                    print(line)
                    if line == "END":
                        break
                    file.write(line)

            print("Arquivo recebido com sucesso.")

        except Exception as e:
            print("Ocorreu um erro durante a transmissão do arquivo:", str(e))

    client.close()

    print("Conexão encerrada.")

if __name__ == '__main__':
    main()