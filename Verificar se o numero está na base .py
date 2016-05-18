#Inicio do trabalho , função que verifica se o numero digitado está na base correta , ainda pode ter erros , mas foi o melhor que
#pude fazer até agora.

def verifica_base(numero,base):
    if base=='16':
        if'8'in numero or '9'in numero or 'A'in numero or 'B'in numero or 'C'in numero or 'D' in numero or 'E'in numero or 'F' in numero:
            print('Base 16 correta!')
            return True
        else:
            print('Base incorreta!')
            return False
    if base=='8':
        if '5' in numero or '6' in numero or '7' in numero:
            print('Base 8 correta!')
            return True
        else:
            print('Base incorreta!')
            return False
    if base=='5':
        if '4'in numero or '3'in numero or '2' in numero:
            print('Base 5 correta!')
            return True
        else:
            print('Base incorreta!')
            return False
    if base=='2':
        if '0' in numero or '1' in numero:
            print('Base 2 correta!')
            return True
        else:
            print('Base incorreta!')
            return False
    if base=='10':
        if numero.isnumeric()==True:
            print('Base correta!')
            return True
        else:
            print('Base incorreta!')
            return False

#só para testar a função:
numero=str(input('insira o numero que deseja converter: '))
baseN=input('Insira a base do número que deseja converter:')
baseR=input('insira a base para ser convertida:')

if verifica_base(numero,baseN) is True:
    print("Parabens")
