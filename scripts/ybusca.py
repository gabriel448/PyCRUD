from zcadastro import CAMINHO_ARQUIVO
import json
import os
def client_data(dict):
    for chave, valor in dict.items():
        print(f'{chave}: {valor}')
    return

def carregar(caminho):
    with open(caminho, 'r', encoding='utf-8')as arquivo:
        dados = json.load(arquivo)
    return dados

clientes = carregar(CAMINHO_ARQUIVO)

count_clients = None

i=0
while True:
    count_clients = len(clientes.keys())
    print(f'Bem vindo a consulta de informacoes do cliente      clientes cadastrados: {count_clients}')
    print()
    search = input('Digite o codigo de busca do cliente: ')

    os.system('cls')
    print(f'informacoes sobre "{clientes[f'{search}']['nome']}"')
    print()
    client_data(clientes[f'{search}'])
    i += 1
    print()

    choice = input('Deseja fazer outra busca?: ').lower()
    if choice.startswith('s'):
        os.system('cls')
        continue
    elif choice.startswith('n'):
        os.system('cls')
        print('Ate mais :)')
        print(f'Voce fez {i} busca(s) nessa sessao.')
        break



