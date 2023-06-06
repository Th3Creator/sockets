import socket # https://pythontic.com/modules/socket/introduction
import time # https://pythontic.com/modules/datetime/introduction

client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

"""

    host: ip onde o servidor está... no caso é tudo na minha máquina local
    port: tem que ser a mesma porta que o servidor tá lá
    bufferSize: buffer para a recepção de dados

"""
host = 'localhost' 
port = 7777 
bufferSize = 100000000 

"""

    vai fazer a conexão com o ip da máquina passada e qual porta vai se comunicar

"""
client.connect(( host, port ))
print("conectado!")


"""
    Toda essa parte acima é padrão... 

    O que vem após a conexão é o que o professor quer, quer seria:
        
        - pedir o arquivo pro servidor
        - receber esse arquivo e "ser remontados e salvos como arquivos de texto cliente"*
        - imprimir o tempo gasto desse envio
        - imprimir a quantidade total de linhas desse arquivo
        - notificar ao servidor se quer mais um arquivo ou pode fechar conexão
"""


# tentando dar uma adiantada: 
try:

    """

    nameFile: ler o arquivo que deseja que o servidor te mande

    """
    nameFile = str(input('qual arquivo deseja pedir?')) 

    """

        transforma o str em bytes para poder ser transmitido
        encode(): faz o processo de codificação, transformando os dados em bytes para poder ser transmitidos

    """
    client.send( nameFile.encode() ) # 

    folder_path = "files_reiceved/"

    # Cria o arquivo para salvar os dados recebidos
    with open( folder_path + nameFile, 'w' ) as file:
        start_time = time.time()

        # Recebe os dados do servidor e escreve no arquivo
        while True:
            data = client.recv( bufferSize ).decode()
            if not data:
                break
            file.write(data)

        end_time = time.time()
        elapsed_time = end_time - start_time

        print("Arquivo recebido com sucesso.")
        print("Tempo gasto:", elapsed_time, "segundos")

        # Contar a quantidade de linhas do arquivo
        with open( folder_path + nameFile, 'r' ) as file:
            lines = file.readlines()
            line_count = len(lines)
            print("Quantidade de linhas:", line_count)

except Exception as e:
    print("Ocorreu um erro durante o recebimento do arquivo:", str(e))

client.close()