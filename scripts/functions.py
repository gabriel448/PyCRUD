import json
import os

def salvar(cadastros, caminho):
    with open (caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(cadastros, arquivo, ensure_ascii = False, indent = 2)
    return

def load(cadastros, caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        salvar(cadastros, caminho)
        return load(cadastros, caminho)

def tel_format(tel):
    telefone = tel.strip()
    remove = '-()'
    tabela = str.maketrans("", "", remove)
    telefone_clean = telefone.translate(tabela)
    tel_format = f"({telefone_clean[:2]}) {telefone_clean[2:6]}-{telefone_clean[6:]}"
    return tel_format

def error(mensagem):
    os.system('cls')
    print(mensagem)

def check(age, email, tel, search_code):
    try:
        #idade
        x = int(age)
        if x < 0 or x > 150:
            error('Idade invalida, digite uma idade entre 0 e 150')
            return False
    except:
        error('Idade Invalida, use caracteres validos')
        return False
    #email
    y = '@' in email.strip() and '.com' in email.strip()
    if not y:
        error('Email invalido')
        return False
    
    #telefone
    telefone = tel.strip()
    remove = '-()'
    tabela = str.maketrans("", "", remove)
    telefone_clean = telefone.translate(tabela)
    try:
        int(telefone_clean)
    except:
        error('telefone invalido')
        return False
    
    if len(telefone) != 10:
        error('telefone invalido')
        return False
    
    #search_code
    cadastros = load({},CAMINHO_ARQUIVO)
    for code in cadastros.keys():
        if code == search_code:
            error('Um cliente ja possui esse codigo')
            return False
    return True

from zcadastro import CAMINHO_ARQUIVO