import socket
import time

def solicitar_entrada_usuario():
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
            folderPath = "files_received/"

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


def solicitar_tabela_arquivos():
    # Lógica para solicitar tabela de arquivos disponíveis
    print("Função para solicitar a tabela de arquivos disponíveis.")


def sair_programa():
    print("Programa encerrado.")
    exit()


def exibir_menu():
    while True:
        print("===== Menu =====")
        print("1. Solicitar arquivos")
        print("2. Solicitar tabela de arquivos disponíveis")
        print("3. Sair do programa")

        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            solicitar_entrada_usuario()
        elif opcao == '2':
            solicitar_tabela_arquivos()
        elif opcao == '3':
            sair_programa()
        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == '__main__':
    exibir_menu()