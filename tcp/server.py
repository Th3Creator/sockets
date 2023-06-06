import socket # https://pythontic.com/modules/socket/introduction

"""

    socket.socket(): invocando o método socket que chama o construtor dela passando dois parâmetros:
    (família de protocologo, tipo de protocologo (SOCK_STREM = tcp; SOCK_DGRAM = udp))

"""
server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

"""

    host: o ip onde toda comunicação vai acontecer, coloquei localhost porquê vai ser tudo na minha máquina
    port: a porta onde toda comunicação entre o cliente/servidor vai acontecer
    bufferSize: buffer para a recepção de dados 

"""
host = 'localhost'  
port = 7777 
bufferSize = 1024 

"""

    bind(): o método bind é responsável por associar uma porta a um host, no caso eu associei a porta 7777 a minha máquina local

"""
server.bind(( host, port ))

"""

    listen(): transforma o servidor em modo de escuta, ou seja, tá esperando que alguém faça uma comunicação

"""
server.listen()
print("aguardando conexão...")

"""

    connection: a conexão com o cliente
    address: endereço do cliente conectado

"""
connection, address = server.accept()
print("\nconectado com sucesso!")

"""

    nameFile: o nome do arquivo que o cliente pediu para o servidor
    bufferSize: vai ser quantos bytes você quer receber, o n° 1024 já é o suficente
    decode(): o decode é pra transformar os bytes em string, isso se dá porque toda vez que você envia algo na rede,
    é necessário que você transforma aquele dado em bytes e quando chega é necessário fazer o processo inverso para 
    poder visualizar o que foi enviado, basicamente transforma bytes em string

"""
nameFile = connection.recv( bufferSize ).decode()  

"""
    Toda essa parte acima é padrão... 

    O que vem após a conexão é o que o professor quer, que seria:
        
        - verificar se existe o arquivo que o cliente pediu na pasta "files"
        - abrir e ler esse arquivo
        - a transmissão deverá ser feita linha a linha*
        - codificar o arquivo, ou seja, transformar em bytes para poder enviar
        - verificar se chegou no final do arquivo
        - informar ao cliente o tempo gasto no envio do arquivo

        # obs: cronometrar todo esse processo para poder notificar ao cliente 
"""






# tratamento de exceção aqui...
# tentando dar uma adiantada:


"""

    with open(): essa função abre o arquivo e garante após isso que ele seja fechado
    for data in file: lê esse arquivo e envia esse arquivo para o cliente
    readlines: vai ler todo o arquivo e enviar para o cliente
    
"""
with open( nameFile, 'rb' ) as file: # , 
     
    for data in file.readlines(): # 
        connection.send( data )

print("arquivo enviado!")