import sys
import json
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QTabWidget,
    QVBoxLayout, QLabel, QPushButton, QLineEdit, QFormLayout, QMessageBox,
    QTextEdit, QSpacerItem, QSizePolicy
)
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt


from zcadastro import cadastrar_gui
from ybusca import buscar_gui
from xupdate import update_gui
from wdelete import deletar_gui
from functions import load
from dir import CAMINHO_ARQUIVO


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Clientes")
        self.resize(600, 700)

        
        self.tabs = QTabWidget()
        self.tabs.addTab(self.tab_cadastrar(), "Cadastrar")
        self.tabs.addTab(self.tab_buscar(), "Buscar")
        self.tabs.addTab(self.tab_update(), "Atualizar")
        self.tabs.addTab(self.tab_deletar(), "Deletar")
        self.tabs.addTab(self.tab_json(), "JSON")

        self.setCentralWidget(self.tabs)

       
        self.apply_dark_theme()

    def apply_dark_theme(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(20, 20, 20))   # fundo
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(30, 30, 30))     # campos input
        palette.setColor(QPalette.AlternateBase, QColor(45, 45, 45))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(50, 0, 0))     # botões 
        palette.setColor(QPalette.ButtonText, QColor(220, 50, 50))
        palette.setColor(QPalette.Highlight, QColor(200, 0, 0)) # seleção 
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(palette)

    # -------------------------------
    # Aba Cadastro
    def tab_cadastrar(self):
        tab = QWidget()
        layout = QFormLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(40, 40, 40, 40)

        self.input_code = QLineEdit()
        self.input_code.setPlaceholderText("Ex: 001")

        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText("Ex: João Silva")

        self.input_idade = QLineEdit()
        self.input_idade.setPlaceholderText("Ex: 25")

        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("Ex: joao@email.com")

        self.input_tel = QLineEdit()
        self.input_tel.setPlaceholderText("Ex: (11) 99999-9999")

        btn_cadastrar = QPushButton("Cadastrar")
        btn_cadastrar.setMinimumHeight(30)
        btn_cadastrar.clicked.connect(self.handle_cadastrar)

        layout.addRow("Código:", self.input_code)
        layout.addRow("Nome:", self.input_nome)
        layout.addRow("Idade:", self.input_idade)
        layout.addRow("Email:", self.input_email)
        layout.addRow("Telefone:", self.input_tel)
        layout.addRow(btn_cadastrar)

        tab.setLayout(layout)
        return tab

    def handle_cadastrar(self):
        code = self.input_code.text()
        nome = self.input_nome.text()
        idade = self.input_idade.text()
        email = self.input_email.text()
        tel = self.input_tel.text()

        sucesso, msg = cadastrar_gui(code, nome, idade, email, tel)
        if sucesso:
            QMessageBox.information(self, "Sucesso", msg)
            self.input_code.clear()
            self.input_nome.clear()
            self.input_idade.clear()
            self.input_email.clear()
            self.input_tel.clear()
        else:
            QMessageBox.warning(self, "Erro", msg)

    # -------------------------------
    # Aba Buscar
    def tab_buscar(self):
        tab = QWidget()
        layout = QFormLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(40, 40, 40, 40)

        self.input_busca = QLineEdit()
        self.input_busca.setPlaceholderText("Ex: 001")

        btn_buscar = QPushButton("Buscar Cliente")
        btn_buscar.setMinimumHeight(30)
        btn_buscar.clicked.connect(self.handle_buscar)

        layout.addRow("Código do cliente:", self.input_busca)
        layout.addRow(btn_buscar)

        tab.setLayout(layout)
        return tab

    def handle_buscar(self):
        code = self.input_busca.text()
        sucesso, resultado = buscar_gui(code)
        if sucesso:
            dados = "\n".join([f"{k}: {v}" for k, v in resultado.items()])
            QMessageBox.information(self, "Cliente encontrado", dados)
        else:
            QMessageBox.warning(self, "Erro", resultado)

    # -------------------------------
    # Aba Atualizar
    def tab_update(self):
        tab = QWidget()
        layout = QFormLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(40, 40, 40, 40)

        self.input_update_code = QLineEdit()
        self.input_update_code.setPlaceholderText("Ex: 001")

        self.input_update_field = QLineEdit()
        self.input_update_field.setPlaceholderText("nome / idade / email / tel")

        self.input_update_value = QLineEdit()
        self.input_update_value.setPlaceholderText("Ex: Maria Souza")

        btn_update = QPushButton("Atualizar Cliente")
        btn_update.setMinimumHeight(30)
        btn_update.clicked.connect(self.handle_update)

        layout.addRow("Código:", self.input_update_code)
        layout.addRow("Campo:", self.input_update_field)
        layout.addRow("Novo valor:", self.input_update_value)
        layout.addRow(btn_update)

        tab.setLayout(layout)
        return tab

    def handle_update(self):
        code = self.input_update_code.text()
        field = self.input_update_field.text().strip().lower()
        value = self.input_update_value.text()

        sucesso, msg = update_gui(code, field, value)
        if sucesso:
            QMessageBox.information(self, "Sucesso", msg)
            self.input_update_code.clear()
            self.input_update_field.clear()
            self.input_update_value.clear()
        else:
            QMessageBox.warning(self, "Erro", msg)

    # -------------------------------
    # Aba Deletar
    def tab_deletar(self):
        tab = QWidget()
        layout = QFormLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(40, 40, 40, 40)

        self.input_delete_code = QLineEdit()
        self.input_delete_code.setPlaceholderText("Ex: 001")

        btn_delete = QPushButton("Deletar Cliente")
        btn_delete.setMinimumHeight(30)
        btn_delete.clicked.connect(self.handle_delete)

        layout.addRow("Código do cliente:", self.input_delete_code)
        layout.addRow(btn_delete)

        tab.setLayout(layout)
        return tab

    def handle_delete(self):
        code = self.input_delete_code.text()
        sucesso, msg = deletar_gui(code)
        if sucesso:
            QMessageBox.information(self, "Sucesso", msg)
            self.input_delete_code.clear()
        else:
            QMessageBox.warning(self, "Erro", msg)

    # -------------------------------
    # Aba JSON
    def tab_json(self):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(15)

        self.text_json = QTextEdit()
        self.text_json.setReadOnly(True)
        self.text_json.setStyleSheet("font-family: monospace;")
        self.text_json.setMinimumHeight(400)

        btn_refresh = QPushButton("Recarregar JSON")
        btn_refresh.setMinimumHeight(0)
        btn_refresh.clicked.connect(self.load_json)

        layout.addWidget(QLabel("Visualização do JSON de clientes:"))
        layout.addWidget(self.text_json, 1)  # ocupa espaço flexível
        layout.addWidget(btn_refresh)

        tab.setLayout(layout)
        return tab

    def load_json(self):
        dados = load({}, CAMINHO_ARQUIVO)
        self.text_json.setText(json.dumps(dados, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
