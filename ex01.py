"""
    1- Processamento de Logs de Treinamento  
    Crie um programa que analisa um arquivo CSV contendo dados de execução de um processo de treinamento. O programa deve:

    * Solicitar ao usuário o nome do arquivo CSV (ex: logs_treinamento.csv).  
    * Ler os dados usando a biblioteca `pandas`.  
    * Calcular a média e o desvio padrão da coluna `tempo_execucao`.  
    * Exibir os resultados com duas casas decimais.  
    * Tratar erros como arquivo inexistente ou formatação incorreta.

    Dica: Use `df['coluna'].mean()` e `df['coluna'].std()` para obter os resultados estatísticos.
"""

import pandas as pd, sys

fname = input("Nome do arquivo CSV: ").strip()
try:
    df = pd.read_csv(fname)
    tempos = df["tempo_execucao"]
    media = tempos.mean()
    desvio = tempos.std()
    print(f"Média: {media:.2f}")
    print(f"Desvio padrão: {desvio:.2f}")
except FileNotFoundError:
    print("Arquivo não encontrado")
    sys.exit(1)
except (KeyError, pd.errors.EmptyDataError, pd.errors.ParserError):
    print("Erro ao ler o arquivo ou coluna 'tempo_execucao' ausente")
    sys.exit(1)