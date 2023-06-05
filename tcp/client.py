import socket # https://pythontic.com/modules/socket/introduction

client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

host = 'localhost' # ip onde o servidor está... no caso é tudo na minha máquina local
port = 7777 # tem que ser a mesma porta
bufferSize = 1024 # buffer para a recepção de dados

client.connect(( host, port ))
# vai fazer a conexão com o ip da máquina passada e qual porta vai se comunicar

print("Conectando...")

"""
    Toda essa parte acima é padrão... 

    O que vem após a conexão é o que o professor quer, quer seria:
        
        - pedir o arquivo pro servidor
        - receber esse arquivo
        - imprimir o tempo gasto desse envio
        - imprimir a quantidade total de linhas desse arquivo
        - notificar ao servidor se quer mais um arquivo ou pode fechar conexão
"""

# tratamento de exceção 
