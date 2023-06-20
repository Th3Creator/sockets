import socket # https://pythontic.com/modules/socket/introduction
import time # https://pythontic.com/modules/datetime/introduction

"""

    host: o ip onde toda comunicação vai acontecer, coloquei localhost porquê vai ser tudo na minha máquina
    port: a porta onde toda comunicação entre o cliente/servidor vai acontecer
    bufferSize: buffer para a recepção de dados 

"""
host = 'localhost'  
port = 7777 
bufferSize = 1024 

"""

    socket.socket(): invocando o método socket que chama o construtor dela passando dois parâmetros:
    (família de protocologo, tipo de protocologo (SOCK_STREM = tcp; SOCK_DGRAM = udp))

"""
server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

"""

    bind(): o método bind é responsável por associar uma porta a um host, no caso eu associei a porta 7777 a minha máquina local

"""
server.bind(( host, port ))

def sendFiles(connection, communicationInterruption):
        try:
            """

            nameFile: o nome do arquivo que o cliente pediu para o servidor
            bufferSize: vai ser quantos bytes você quer receber, o n° 1024 já é o suficente
            decode(): o decode é pra transformar os bytes em string, isso se dá porque toda vez que você envia algo na rede,
            é necessário que você transforma aquele dado em bytes e quando chega é necessário fazer o processo inverso para 
            poder visualizar o que foi enviado, basicamente transforma bytes em string
            encode(): faz o processo de codificação, transformando os dados em bytes para poder ser transmitidos

            """
            nameFile = connection.recv( bufferSize ).decode() 

            folderPath = "../files/"

            with open( folderPath + nameFile, 'r' ) as file:
                
                startTime = time.time()

                for line in file:
                    connection.send( line.encode() )

                endTime = time.time()
                elapsedTime = endTime - startTime
                elapsedTimeFormatted = "{:.2f}".format(elapsedTime)

            print("Arquivo transmitido com sucesso.")
            print("Tempo gasto:", elapsedTimeFormatted, "segundos")    
            
            if communicationInterruption == "sair":
                connection.close()
                sair()

            connection.close()
            main()


        except Exception as e:
            print("Ocorreu um erro durante a transmissão do arquivo:", str(e))

def sair():
    print("Encerrando o programa.")
    raise SystemExit

def main():
    
    """

        listen(): transforma o servidor em modo de escuta, ou seja, tá esperando que alguém faça uma comunicação

    """
    server.listen()
    print("aguardando conexão...") # 

    """

        connection: a conexão com o cliente
        address: endereço do cliente conectado

    """
    connection, address = server.accept()
    print("\nconectado com sucesso!")

    communicationInterruption = connection.recv( bufferSize ).decode()
    print(communicationInterruption)

    # se a communicationInterruption  for igual a sair, ele vai embora do programa

    sendFiles(connection, communicationInterruption)

if __name__ == '__main__':
    main()