import socket # https://pythontic.com/modules/socket/introduction
import time # https://pythontic.com/modules/datetime/introduction

"""

    host: ip onde o servidor está... no caso é tudo na minha máquina local
    port: tem que ser a mesma porta que o servidor tá lá
    bufferSize: buffer para a recepção de dados

"""
host = 'localhost' 
port = 7777 
bufferSize = 100000000 

def receiveFiles( client, communicationInterruption ):
        try:

            """

                nameFile: ler o arquivo que deseja que o servidor te mande

            """
            nameFile = str(input('\nqual arquivo deseja pedir?')) 

            """

                transforma o str em bytes para poder ser transmitido
                encode(): faz o processo de codificação, transformando os dados em bytes para poder ser transmitidos
                decode(): o decode é pra transformar os bytes em string, isso se dá porque toda vez que você envia algo na rede,
                é necessário que você transforma aquele dado em bytes e quando chega é necessário fazer o processo inverso para 
                poder visualizar o que foi enviado, basicamente transforma bytes em string
                
            """
            client.send( nameFile.encode() ) 
            # toda essa parte daqui pra cima, colocar no menu

            folderPath = "files_reiceved/"

            # Cria o arquivo para salvar os dados recebidos
            with open( folderPath + nameFile, 'w' ) as file:

                start_time = time.time()

                # Recebe os dados do servidor e escreve no arquivo
                while True:

                    data = client.recv( bufferSize ).decode()
                    # b.o tá aqui
                    if not data:
                        break

                    file.write( data )

                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    
            print("Arquivo recebido com sucesso.")
            print("Tempo gasto:", elapsed_time, "segundos")

            # Contar a quantidade de linhas do arquivo
            with open( folderPath + nameFile, 'r' ) as file:
                    
                for line in file:
                    print( line )  

            if communicationInterruption == "sair":
                client.close()
                sair()

            main()

        except Exception as e:
            print("Ocorreu um erro durante o recebimento do arquivo:", str(e))

def sair():
    print("\nEncerrando o programa.")
    raise SystemExit

def main():

    client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    """

        vai fazer a conexão com o ip da máquina passada e qual porta vai se comunicar

    """
    client.connect(( host, port ))
    print("conectado!") # tirar isso daqui

    # menu


    communicationInterruption = str(input("Digite 'sair' caso deseja sair do programa ou outra tecla par continuar: "))

    if communicationInterruption == "sair":
        sair()

    client.send( communicationInterruption.encode() )

    receiveFiles( client, communicationInterruption )
    
if __name__ == '__main__':
    main()