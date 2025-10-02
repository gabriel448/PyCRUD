import sys
import json
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout,
    QFormLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QTextEdit,
    QHBoxLayout
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

# Importando as funções e variáveis dos seus arquivos originais
from functions import salvar, load, tel_format, check as original_check
from dir import CAMINHO_ARQUIVO

def check_gui(age, email, tel, search_code):
    """
    Versão da função `check` adaptada para a GUI.
    Retorna (True, None) em caso de sucesso.
    Retorna (False, "mensagem de erro") em caso de falha.
    """
    try:
        x = int(age)
        if x < 0 or x > 150:
            return False, 'Idade inválida. Digite uma idade entre 0 e 150.'
    except ValueError:
        return False, 'Idade inválida. Use apenas números inteiros.'

    y = '@' in email.strip() and '.com' in email.strip()
    if not y:
        return False, 'Email inválido. Deve conter "@" e ".com".'

    telefone = tel.strip()
    remove = '-() '
    tabela = str.maketrans("", "", remove)
    telefone_clean = telefone.translate(tabela)
    
    try:
        int(telefone_clean)
    except ValueError:
        return False, 'Telefone inválido. Use apenas números.'

    if len(telefone_clean) < 10 or len(telefone_clean) > 11:
        return False, 'Telefone inválido. O número com DDD deve ter 10 ou 11 dígitos.'

    cadastros = load({}, CAMINHO_ARQUIVO)
    if search_code in cadastros:
        return False, f'Um cliente já possui o código "{search_code}".'
        
    if not search_code:
        return False, 'O código de busca não pode estar vazio.'

    return True, None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de clientes")
        self.setMinimumSize(500, 400)

        # Widget principal e layout
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Criar as abas
        self.create_cadastro_tab()
        self.create_busca_tab()
        self.create_json_view_tab()
        
        # Conectar o sinal de mudança de aba para atualizar o JSON
        self.tabs.currentChanged.connect(self.on_tab_change)

    def on_tab_change(self, index):
        # O índice 2 corresponde à aba "Visualizar JSON"
        if index == 2:
            self.update_json_view()

    def create_cadastro_tab(self):
        """Cria a interface da aba de cadastro."""
        tab_cadastro = QWidget()
        layout = QFormLayout(tab_cadastro)
        layout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapAllRows)

        # Campos de entrada
        self.codigo_input = QLineEdit()
        self.nome_input = QLineEdit()
        self.idade_input = QLineEdit()
        self.email_input = QLineEdit()
        self.tel_input = QLineEdit()
        
        # Botão de cadastro
        cadastrar_btn = QPushButton("Cadastrar Cliente")
        cadastrar_btn.clicked.connect(self.cadastrar_cliente)

        # Adicionar widgets ao layout
        layout.addRow(QLabel("Código de Busca:"), self.codigo_input)
        layout.addRow(QLabel("Nome:"), self.nome_input)
        layout.addRow(QLabel("Idade:"), self.idade_input)
        layout.addRow(QLabel("Email:"), self.email_input)
        layout.addRow(QLabel("Telefone (com DDD):"), self.tel_input)
        layout.addRow(cadastrar_btn)

        self.tabs.addTab(tab_cadastro, "Cadastro")

    def create_busca_tab(self):
        """Cria a interface da aba de busca."""
        tab_busca = QWidget()
        layout = QVBoxLayout(tab_busca)
        
        # Layout para a busca
        search_layout = QHBoxLayout()
        self.busca_codigo_input = QLineEdit()
        self.busca_codigo_input.setPlaceholderText("Digite o código do cliente")
        buscar_btn = QPushButton("Buscar")
        buscar_btn.clicked.connect(self.buscar_cliente)
        
        search_layout.addWidget(QLabel("Código de Busca:"))
        search_layout.addWidget(self.busca_codigo_input)
        search_layout.addWidget(buscar_btn)

        # Campo para exibir resultados
        self.resultado_busca_text = QTextEdit()
        self.resultado_busca_text.setReadOnly(True)

        layout.addLayout(search_layout)
        layout.addWidget(self.resultado_busca_text)

        self.tabs.addTab(tab_busca, "Busca")

    def create_json_view_tab(self):
        """Cria a interface da aba de visualização do JSON."""
        tab_json = QWidget()
        layout = QVBoxLayout(tab_json)
        
        self.json_view_text = QTextEdit()
        self.json_view_text.setReadOnly(True)
        self.json_view_text.setFontFamily("Courier") # Fonte monoespaçada para melhor visualização

        update_btn = QPushButton("Atualizar Visualização")
        update_btn.clicked.connect(self.update_json_view)
        
        layout.addWidget(update_btn)
        layout.addWidget(self.json_view_text)

        self.tabs.addTab(tab_json, "Visualizar JSON")
        self.update_json_view() # Carrega o conteúdo inicial

    def cadastrar_cliente(self):
        """Lida com o evento de clique do botão de cadastro."""
        codigo = self.codigo_input.text().strip()
        nome = self.nome_input.text().strip()
        idade = self.idade_input.text().strip()
        email = self.email_input.text().strip()
        tel = self.tel_input.text().strip()

        is_valid, error_message = check_gui(idade, email, tel, codigo)

        if not is_valid:
            QMessageBox.warning(self, "Erro de Validação", error_message)
            return

        # Carrega os dados existentes
        cadastros = load({}, CAMINHO_ARQUIVO)

        # Formata o telefone e cria o dicionário do cliente
        telefone_formatado = tel_format(tel)
        
        # (O uso da classe Clientes é opcional aqui, podemos criar o dict diretamente)
        cliente_data = {
            'nome': nome,
            'idade': int(idade),
            'email': email,
            'tel': telefone_formatado
        }
        
        cadastros[codigo] = cliente_data
        
        # Salva o arquivo JSON
        salvar(cadastros, CAMINHO_ARQUIVO)

        QMessageBox.information(self, "Sucesso", f'Cliente "{nome}" cadastrado com sucesso!')
        
        # Limpa os campos após o cadastro
        self.codigo_input.clear()
        self.nome_input.clear()
        self.idade_input.clear()
        self.email_input.clear()
        self.tel_input.clear()
        
        # Atualiza a aba de visualização do JSON
        self.update_json_view()

    def buscar_cliente(self):
        """Lida com o evento de clique do botão de busca."""
        codigo = self.busca_codigo_input.text().strip()
        if not codigo:
            self.resultado_busca_text.setText("Por favor, digite um código para buscar.")
            return

        cadastros = load({}, CAMINHO_ARQUIVO)
        
        cliente_info = cadastros.get(codigo)

        if cliente_info:
            # Formata os dados para exibição
            resultado_formatado = f"Dados do cliente com código: {codigo}\n"
            resultado_formatado += "-" * 30 + "\n"
            for chave, valor in cliente_info.items():
                resultado_formatado += f"{chave.capitalize()}: {valor}\n"
            self.resultado_busca_text.setText(resultado_formatado)
        else:
            self.resultado_busca_text.setText(f'Cliente com o código "{codigo}" não encontrado.')

    def update_json_view(self):
        """Carrega e exibe o conteúdo atual do arquivo JSON."""
        try:
            with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as f:
                # Usamos json.load e json.dumps para formatar o texto com indentação
                dados = json.load(f)
                texto_formatado = json.dumps(dados, indent=4, ensure_ascii=False)
                self.json_view_text.setText(texto_formatado)
        except FileNotFoundError:
            self.json_view_text.setText("Arquivo 'zclientes.json' ainda não foi criado.\nCadastre um cliente para começar.")
        except json.JSONDecodeError:
            self.json_view_text.setText("Erro: O arquivo JSON parece estar corrompido ou vazio.")


if __name__ == '__main__':
    # Verifica se o arquivo JSON existe e cria um vazio se não existir
    if not os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as f:
            json.dump({}, f)
            
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())