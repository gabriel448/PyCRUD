from ybusca import buscar
from zcadastro import cadastrar
from xupdate import update
from wdelete import deletar
import os
import time

i = True
while i:
    os.system('cls')
    print('Cadastro de cliente')
    print('\n1. Cadastrar')
    print('2. Buscar')
    print('3. Atualizar dados')
    print('4. Deletar dados')
    print('4. Sair\n')
    act = input('Digite a acao desejada: ').strip()
    if act == '1':
        os.system('cls')
        cadastrar()
        continue
    elif act == '2':
        os.system('cls')
        buscar()
        continue
    elif act == '3':
        os.system('cls')
        update()
        continue
    elif act == '4':
        os.system('cls')
        deletar()
    elif act == '5':
        print('sessao encerrada')
        time.sleep(1)
        break
    else:
        print('Comando invalido, digite o numero de uma das opcoes [1, 2, 3, 4, 5]')
        input('Digite qualquer tecla pra continuar....')
        continue
