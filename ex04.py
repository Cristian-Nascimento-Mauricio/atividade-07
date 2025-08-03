"""
    4- Leitura e Escrita de Arquivo JSON  
    Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

    * Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).  
    * Solicite ao usuário o nome do arquivo JSON.  
    * Salve os dados no arquivo usando o módulo `json`.  
    * Após salvar, leia o mesmo arquivo e imprima os dados carregados.  
    * Trate possíveis erros como ausência do arquivo ou problemas na escrita.

    Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.
"""

import json, sys

# Dados iniciais
pessoa = {
    "nome": "João Silva",
    "idade": 35,
    "cidade": "Curitiba"
}

fname = input("Nome do arquivo JSON: ").strip()

try:
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(pessoa, f, ensure_ascii=False, indent=4)

    with open(fname, "r", encoding="utf-8") as f:
        dados_carregados = json.load(f)

    print("Dados lidos do arquivo:")
    print(dados_carregados)

except IOError:
    print("Erro ao abrir ou escrever o arquivo")
    sys.exit(1)
except json.JSONDecodeError:
    print("Arquivo JSON em formato inválido")
    sys.exit(1)