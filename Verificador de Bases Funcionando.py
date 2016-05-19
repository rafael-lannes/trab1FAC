#Função que verifica se o número e a base existe. A função usa a biblioteca Regular Expressions do Python Padrão.
import re #Chamando a biblioteca
def verifica_base02(numero,base):
    if base=='2':
        if not re.match("^[0-1]*$", numero): #re.match("padrão na tabela ASCII",string) no caso 0 e 1 apenas.
            print('Numero inválido')         #Print temporario apenas para intuito de debug.
            return False
        else:
            print('Número Válido')
            return True
    if base=='5':
        if not re.match("^[0-4]*$", numero):
            print('Numero inválido')
            return False
        else:
            print('Número Válido')
            return True
    if base=='8':
        if not re.match("^[0-7]*$", numero):
            print('Numero inválido')
            return False
        else:
            print('Número Válido')
            return True
    if base=='10':
        if not re.match("^[0-9]*$", numero):
            print('Numero inválido')
            return False
        else:
            print('Número Válido')
            return True
    if base=='16':
        if not re.match("^[0-9,A-F]*$", numero):
            print('Numero inválido')
            return False
        else:
            print('Número Válido')
            return True

