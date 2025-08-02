# Projeto - Cadastro e Busca de Clientes

Este projeto contém dois programas simples escritos em Python, que foram convertidos em executáveis (.exe) para facilitar a execução em qualquer computador com Windows, **sem precisar instalar Python**.

## Programas

- `cadastro.exe`: permite cadastrar novos clientes e salvar suas informações em um arquivo `.json`.
- `busca.exe`: permite buscar as informações de um cliente usando um código identificador.

## Como usar

1. Baixe os arquivos da pasta `dist/`.
2. Execute o `cadastro.exe` para adicionar um novo cliente.
3. Execute o `busca.exe` para pesquisar um cliente existente.
4. As informações são salvas automaticamente no arquivo `clientes.json`.

## Scripts originais

Os códigos-fonte em Python estão na pasta `scripts/`.

## Exemplo de estrutura de dados (`clientes.json`)

```json
{
  "1234": {
    "nome": "João da Silva",
    "idade": 30,
    "altura": "1.75"
  }
}
