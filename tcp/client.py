import socket # https://pythontic.com/modules/socket/introduction

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






# tratamento de exceção aqui...
# tentando dar uma adiantada:

"""

    nameFile: ler o arquivo que deseja que o servidor te mande
    escolquer o nome do arquivo que deseja visualizar do servidor

"""
nameFile = str(input('qual arquivo deseja pedir?')) # 

"""

    transforma o str em bytes para poder ser transmitido
    encode(): faz o processo de codificação, transformando os dados em bytes para poder ser transmitidos

"""
client.send( nameFile.encode() ) # 


# preparar para receber os dados do servidor após requesição
with open( nameFile, 'wb') as file:
    while 1:
        data = client.recv( bufferSize )

        if not data:
            break

        file.write( data )

        # saber quando o servidor vai parar de enviar os dados

print("tudo recebido...")

# recebe o arquivo
# ler o arquivo e exibir a quantidade de linhas
# exibir também o tempo gasto no envio