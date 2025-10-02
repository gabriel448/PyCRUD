from ybusca import buscar
from zcadastro import cadastrar
from xupdate import update
import os
import time

i = True
while i:
    os.system('cls')
    print('Cadastro de cliente')
    print('\n1. Cadastrar')
    print('2. Buscar')
    print('3. Atualizar dados')
    print('4. Sair\n')
    act = input('Digite a acao desejada: ')
    if act.strip() == '1':
        os.system('cls')
        cadastrar()
        continue
    elif act.strip() == '2':
        os.system('cls')
        buscar()
        continue
    elif act.strip() == '3':
        os.system('cls')
        update()
        continue
    elif act.strip() == '4':
        print('sessao encerrada')
        time.sleep(1)
        break
    else:
        print('Comando invalido, digite o numero de uma das opcoes [1, 2, 3]')
        input('Digite qualquer tecla pra continuar....')
        continue
