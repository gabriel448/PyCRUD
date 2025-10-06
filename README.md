# PyCRUD - Sistema de Cadastro e Busca de Clientes

PyCRUD é um projeto simples escrito em Python que oferece opções para cadastro e busca de clientes. O sistema permite a execução de duas maneiras: diretamente pelo terminal utilizando os scripts Python ou por meio de uma interface gráfica desktop com arquivos executáveis.

## Como Usar

Existem duas formas de utilizar este projeto: com a interface gráfica (executáveis) ou via terminal (scripts Python).

### 1. Executando com a Interface Gráfica (Windows)

Os arquivos executáveis foram criados para facilitar o uso em computadores Windows, **não sendo necessária a instalação do Python**[cite: 1].

1.  Faça o download dos arquivos localizados na pasta `dist/`[cite: 4].
2.  Execute `CadastroClientes.exe` 

As informações dos clientes são gerenciadas e armazenadas automaticamente em um arquivo chamado `clientes.json`[cite: 4].

### 2. Executando via Terminal (a partir do código-fonte)

Para executar o projeto a partir dos scripts Python, é necessário ter o Python e as dependências do projeto instaladas.

1.  Clone o repositório para a sua máquina local.
2.  Instale as dependências listadas no arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
3.  Os códigos-fonte estão localizados na pasta `scripts/`[cite: 6]. Navegue até essa pasta para executar o app.py.

## Estrutura de Dados

As informações dos clientes são armazenadas no arquivo `clientes.json`. A estrutura de dados utilizada é a seguinte:

```json
{
  "001": {
    "nome": "Gabriel de Sousa",
    "idade": 19,
    "email": "gabriel@gmail.com",
    "tel": "(31) 99699-4910"
  }
}
