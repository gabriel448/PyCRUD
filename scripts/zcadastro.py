import json
import os
CAMINHO_ARQUIVO = 'zclientes.json'

class Clientes:
    def __init__(self,name, age, height):
        self.nome = name
        self.idade = age
        self.altura = height

def salvar(cadastros, caminho):
    with open (caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(cadastros, arquivo, ensure_ascii = False, indent = 2)
    return

def carregar(cadastros, caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        salvar(cadastros, caminho)
        return carregar(cadastros, caminho)

def check(age, height):
    try:
        x = int(age)
        y = float(height)
        z = int(search_code)
        return False
    except:
        return True
        
    

if __name__ == '__main__':
    cadastros = carregar({}, CAMINHO_ARQUIVO)

    clients_count = None

    i = 0
    while True:
        clients_count = len(cadastros.keys())
        print(f'Bem-Vindo ao cadastro de clientes!      clientes cadastrados: {clients_count}')
        print()
        search_code = input('Digite um codigo de busca para este cliente: ')
        client_name = input('Digite o nome do cliente: ')
        client_age = input('Digite a idade do cliente: ')
        client_height = input('Digite a altura(metros) do cliente: ')

        if check(client_age, client_height):
            os.system('cls')
            print('altura, idade ou codigo de busca invalido(s).','Verifique se os mesmos sao numeros.', sep='\n')
            print()
            continue

        cliente = Clientes(f'{client_name}',int(client_age), float(client_height))
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

    
    