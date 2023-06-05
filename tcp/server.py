import socket # https://pythontic.com/modules/socket/introduction
# faz a importação do módulo socket que vai dar acesso a todas às funções para realizar a comunicação 

server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
# invocando o método socket que chama o construtor dela passando dois parâmetros:
# (família de protocologo, tipo de protocologo (SOCK_STREM = tcp; SOCK_DGRAM = udp)))

host = 'localhost' # o ip onde toda comunicação vai acontecer, coloquei localhost porquê vai ser tudo na minha máquina
port = 7777 # a porta onde toda comunicação entre o cliente/servidor vai acontecer
bufferSize = 1024 # buffer para a recepção de dados 

server.bind(( host, port ))
# o método bind é responsável por associar uma porta a um host, no caso eu associei a porta 7777 a minha máquina local

server.listen()
print("aguardando conexão...")
# transforma o servidor em modo de escuta, ou seja, tá esperando que alguém faça uma comunicação

connection, address = server.accept()
# quando o cliente fizer a conexão, ele automáticamente vai aceitar e retornar esses dois parâmetros
# conexão com o cliente, endereço do cliente

print("\nconectado com sucesso!")

"""
    Toda essa parte acima é padrão... 

    O que vem após a conexão é o que o professor quer, quer seria:
        
        - lê o arquivo que o cliente pediu
        - informar ao cliente o tempo gasto no envio do arquivo
"""

# tratamento de exceção 
