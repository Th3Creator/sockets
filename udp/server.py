import socket
import time
import os

host = 'localhost'
port = 9999
bufferSize = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((host, port))

print("Aguardando conexão...")

while True:
    data, address = server.recvfrom(bufferSize)
    print("\nConectado com sucesso!")

    nameFile = data.decode()
    if nameFile == "sair":
        break

    folderPath = "../files/"

    if not os.path.isfile(folderPath + nameFile):
        error_message = "ERROR: Arquivo não encontrado.".encode()
        server.sendto(error_message, address)
        print("Arquivo não encontrado.")
        continue
    with open(folderPath + nameFile, 'r') as file:
        startTime = time.time()
        for line in file:
            server.sendto(line.encode(), address)
        server.sendto("END".encode(), address)

    endTime = time.time()
    elapsedTime = endTime - startTime
    elapsedTimeFormatted = "{:.2f}".format(elapsedTime)

    print("Arquivo transmitido com sucesso.")
    print("Tempo gasto: {} segundos".format(elapsedTimeFormatted))

server.close()
