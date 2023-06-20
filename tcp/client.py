import socket
import time
import os

host = 'localhost'
port = 7777
bufferSize = 100000000

def menu(client):
    while True:
        os.system('cls') or None

        print("\n===== Menu =====")
        print("\n1. Solicitar arquivos de texto")
        print("\n2. Solicitar tabela de arquivos disponíveis no servidor")
        print("\n3. Sair do programa")

        option = input("\nDigite o número da opção desejada: ")

        if option == '1':

            client.send( option.encode() )
            receiveFilesText( client )
        elif option == '2':

            # client.send( option.encode() )
            print("tabela disponível...")
        elif option == '3':

            client.send( option.encode() )
            exit()
        else:

            os.system('cls') or None
            print("\nOpção inválida. Por favor, tente novamente.")
            time.sleep(3)

def receiveFilesText(client):
    try:
        os.system('cls') or None

        nome_arquivo = input("\nEscreva o nome do arquivo de texto que deseja solicitar ex:(small.txt) ")

        client.send(nome_arquivo.encode())

        os.system('cls') or None
        print("\nverifique o tempo informado pelo servidor...")

        folderPath = "files_received/"

        # escrita das linhas recebidas
        with open(folderPath + nome_arquivo, 'w') as arquivo:
            
            while True:
                data = client.recv( bufferSize ).decode()

                if not data:
                    break

                arquivo.write(data)             

        os.system('cls') or None
        print("\niniciando a contagem de linhas...")
        time.sleep(3)

        # leitura e impressão das linhas
        with open(folderPath + nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                print(linha)

        client.close()
        main()

    except Exception as e:
        print("Ocorreu um erro durante o recebimento do arquivo:", str(e))

def exit():
    os.system('cls') or None
    print("\nPrograma encerrado.")
    raise SystemExit

def main():

    client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    client.connect(( host, port ))
    print("conectado!") # tirar isso daqui

    menu(client)
 
if __name__ == '__main__':
    main()