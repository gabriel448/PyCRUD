import os
from functions import delete, load
from dir import CAMINHO_ARQUIVO

def deletar():
    cadastros = load({}, CAMINHO_ARQUIVO)

    while True:
        print('Deletar cadastro\n')
        code = input('Digite o numero do cadastro a ser deletado: ').strip()
        if code in cadastros.keys():
            os.system('cls')
            cliente = cadastros[code]['nome']
            confirm = input(f'Tem certaza que deseja deletar o cadastro do cliente "{cliente}"? [S/N]: ').strip().lower()
            if confirm.startswith('s'):
                os.system('cls')
                delete(CAMINHO_ARQUIVO,code)
                print(f'Cadastro de {cliente} excluido com sucesso')
            elif confirm.startswith('n'):
                os.system('cls')
                continue
            else:
                os.system('cls')
                print("comando invalido")
                continue
          
            choice = input('Deseja deletar outro cadastro?: ').lower()
            if choice.startswith('s'):
                os.system('cls')
                continue
            elif choice.startswith('n'):
                break
        else:
            os.system('cls')
            print('Codigo de cadastro inexistente')
    return

# --- Versão GUI ---
def deletar_gui(code):
    cadastros = load({}, CAMINHO_ARQUIVO)
    if code not in cadastros:
        return False, "Código inexistente."
    cliente = cadastros[code]['nome']
    delete(CAMINHO_ARQUIVO, code)
    return True, f'Cadastro de "{cliente}" excluído com sucesso.'
