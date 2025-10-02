import os
from functions import check, load, salvar_update
from dir import CAMINHO_ARQUIVO
import copy

def data_update(cadastro, info, update):
    copia = copy.deepcopy(cadastro)
    copia[info] = update
    return copia

def update_check( code):
    
    while True:
                cadastros = load({}, CAMINHO_ARQUIVO)
                user = cadastros[code]
                print(f'Atualizacao de cadastro de "{user['nome']}" \n')
                print('1. Nome')
                print('2. Idade')
                print('3. Email')
                print('4. Telefone\n')
                dado = input('Qual dado deseja alterar?: ').strip()
                if dado == '1':
                    update = input('\nDigite o novo nome: ').strip()
                    update = data_update(user, 'nome', update)
                    if not check(update['idade'],update['email'], update['tel'], None):
                        continue
                    else:
                        update['idade'] = int(update['idade'])
                        salvar_update(CAMINHO_ARQUIVO,code, update)
                        break
                elif dado == '2':
                    update = input('\nDigite a nova idade: ').strip()
                    update = data_update(user, 'idade', update)
                    if not check(update['idade'], update['email'], update['tel'], None):
                        continue
                    else:
                        update['idade'] = int(update['idade'])
                        salvar_update(CAMINHO_ARQUIVO,code, update)
                        break
                elif dado == '3':
                    update = input('\nDigite o novo email: ').strip()
                    update = data_update(user, 'email', update)
                    if not check(update['idade'],update['email'], update['tel'], None):
                        continue
                    else:
                        update['idade'] = int(update['idade'])
                        salvar_update(CAMINHO_ARQUIVO,code, update)
                        break
                elif dado == '4':
                    update = input('\nDigite o novo telefone: ').strip()
                    update = data_update(user, 'tel', update)
                    if not check(update['idade'],update['email'], update['tel'], None):
                        continue
                    else:
                        update['idade'] = int(update['idade'])
                        salvar_update(CAMINHO_ARQUIVO,code, update)
                        break
                else:
                    os.system('cls')
                    print('Codigo invalido, digite o numero do dado a ser alterado[1, 2, 3, 4]')
                    continue
    return
def update():
    cadastros = load({}, CAMINHO_ARQUIVO)

    while True:
        print('Atualizacao de cadastro\n')
        code = input('Digite o numero do cadastro do cliente: ').strip()
        if code in cadastros.keys():
            os.system('cls')
            update_check(code)

            cadastros = load({}, CAMINHO_ARQUIVO)
            user = cadastros[code]
            print(f'Update de {user['nome']} concluido com sucesso\n')           
            choice = input('Deseja fazer outra atualizacao?: ').lower()
            if choice.startswith('s'):
                os.system('cls')
                continue
            elif choice.startswith('n'):
                break
        else:
            os.system('cls')
            print('Codigo de cadastro inexistente')
    return
