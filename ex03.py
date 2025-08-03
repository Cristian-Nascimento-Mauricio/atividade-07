"""
    3- Leitura de Arquivo CSV  
    Desenvolva um programa que lê os dados de um arquivo CSV e imprime cada linha na tela. Para isso:

    * Solicite ao usuário o nome do arquivo CSV a ser lido.  
    * Utilize o módulo `csv` para abrir o arquivo e ler os dados.  
    * Exiba cada linha completa como uma lista.  
    * Trate erros como arquivo inexistente ou problemas na leitura.

    Dica: Use `csv.reader()` para ler e percorrer as linhas do arquivo.
"""

import csv, sys

fname = input("file.json").strip()
try:
    with open(fname, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("Arquivo não encontrado")
    sys.exit(1)
except csv.Error:
    print("Erro ao ler o arquivo CSV")
    sys.exit(1)