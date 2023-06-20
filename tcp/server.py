import socket # https://pythontic.com/modules/socket/introduction
import time # https://pythontic.com/modules/datetime/introduction
import os

"""

    host: o ip onde toda comunicação vai acontecer, coloquei localhost porquê vai ser tudo na minha máquina
    port: a porta onde toda comunicação entre o cliente/servidor vai acontecer
    bufferSize: buffer para a recepção de dados 

"""
host = 'localhost'  
port = 7777 
bufferSize = 1024 

server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

server.bind(( host, port ))

def sendFilesText( connection ):
        try:
            nameFile = connection.recv( bufferSize ).decode() 

            folderPath = "../files/"

            with open( folderPath + nameFile, 'r' ) as file:
                
                startTime = time.time()

                for line in file:
                    connection.send( line.encode() )

                endTime = time.time()
                elapsedTime = endTime - startTime
                elapsedTimeFormatted = "{:.2f}".format(elapsedTime)

            os.system('cls') or None
            print("\nArquivo", nameFile, "transmitido com sucesso.")
            print("\nTempo gasto:", elapsedTimeFormatted, "segundos")    
            
            time.sleep(5)

            connection.close()
            main()

        except Exception as e:
            print("Ocorreu um erro durante a transmissão do arquivo:", str(e))

def exit():
    os.system('cls') or None
    print("\nPrograma encerrado.")
    raise SystemExit

def main():
    os.system('cls') or None

    server.listen()
    print("\naguardando conexão...") # 

    connection, address = server.accept()

    option = connection.recv( bufferSize ).decode()

    if option == '1':
        sendFilesText( connection )
    elif option == '2':

        # client.send( option.encode() )
        print("tabela disponível...")
    elif option == '3':

        exit()
    else:

        connection.close()
        main()

if __name__ == '__main__':
    main()