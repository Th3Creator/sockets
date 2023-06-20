import socket
import time

host = 'localhost'
port = 7777
bufferSize = 100000000

def exibir_menu():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        print("Conectado!")

        receber_arquivos(client)

    except Exception as e:
        print("Ocorreu um erro durante a conexão:", str(e))

def exibir_menu():
    while True:
        print("===== Menu =====")
        print("1. Solicitar arquivos")
        print("2. Solicitar tabela de arquivos disponíveis")
        print("3. Sair do programa")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            exibir_menu_solicitacao()
        elif opcao == '2':
            solicitar_tabela_arquivos()
        elif opcao == '3':
            sair()
        else:
            print("Opção inválida. Por favor, tente novamente.")

def exibir_menu_solicitacao():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        print("Conectado!")

        receber_arquivos(client)

    except Exception as e:
        print("Ocorreu um erro durante a conexão:", str(e))

def receber_arquivos(client):
    try:
        nome_arquivo = input("Qual arquivo você deseja solicitar? ")

        client.send(nome_arquivo.encode())

        folderPath = "files_received/"

        with open(folderPath + nome_arquivo, 'w') as arquivo:
            start_time = time.time()

            while True:
                data = client.recv(bufferSize).decode()
                if not data:
                    break

                arquivo.write(data)

            end_time = time.time()
            tempo_gasto = end_time - start_time

        print("Arquivo recebido com sucesso.")
        print("Tempo gasto:", tempo_gasto, "segundos")

        with open(folderPath + nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                print(linha)

        exibir_menu()

    except Exception as e:
        print("Ocorreu um erro durante o recebimento do arquivo:", str(e))

def solicitar_tabela_arquivos():
    print("Função para solicitar a tabela de arquivos disponíveis.")

def sair():
    print("\nEncerrando o programa.")
    raise SystemExit

if __name__ == '__main__':
    exibir_menu()
