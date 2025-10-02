import os
from functions import check, salvar, load, tel_format
from models import Clientes
from dir import CAMINHO_ARQUIVO

if __name__ == '__main__':
    cadastros = load({}, CAMINHO_ARQUIVO)

    clients_count = None

    i = 0
    while True:
        clients_count = len(cadastros.keys())
        print(f'Bem-Vindo ao cadastro de clientes!      clientes cadastrados: {clients_count}')
        print()
        search_code = input('Digite um codigo de busca para este cliente: ')
        client_name = input('Digite o nome do cliente: ')
        client_age = input('Digite a idade do cliente: ')
        client_email = input('Digite o email do cliente: ')
        client_tel = input('Digite o telefone do cliente com o DDD: ')

        if not check(client_age, client_email, client_tel, search_code):
            continue
        
        tel_format = tel_format(client_tel)
        cliente = Clientes(f'{client_name}',int(client_age), f'{client_email}', f'{tel_format}')
        cadastros[f'{search_code}'] = vars(cliente)
        salvar(cadastros, CAMINHO_ARQUIVO)
        i += 1
        
        os.system('cls')
        print(f'Cliente "{client_name}" cadastrado com sucesso.')

        choice = input('Deseja cadastrar outro cliente?: ').lower()
        if choice.startswith('s'):
            os.system('cls')
            continue
        elif choice.startswith('n'):
            os.system('cls')
            print('Ate mais :)')
            print(f'Voce cadastrou {i} clientes nessa sessao.')
            break
        else:
            os.system('cls')
            print('comando invalido.')
            continue

    
    