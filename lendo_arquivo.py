# Jogando o csv em memória apenas com o python:

import csv

# 1. Sempre vamos ter um path que é o caminho do arquivo, para isso criamos um variável:

caminho_do_arquivo: str = "exemplo.csv"

# 2. Como são várias linhas, vamos fazer uma lista de dicionários. Por isso vamos criar uma lista vazia:

arquivo_csv: list = []

# 3. Agora vamos usar um with. Sempre que tivermos um with, vamos ter um gerenciador de contexto, ou seja, estou saindo do python ou estou entrando no python. Sempre que trabalhamso com banco, ou por exemplo,
# o Airflow, temos que usar um gerenciador de contexto. O with abre e fecha o arquivo evitando problemas de deixar conexões em aberto.

with open(file=caminho_do_arquivo, mode="r", encoding="utf-8") as arquivo: # Aqui definimos alguns parâmetros de abertura e estamos salvando tudo em uma variável. Agora vamos usar uma função da classe csv para ler o arquivo e tranformá-lo em um dicionário.
    leitor_csv = csv.DictReader(arquivo) # Aqui nos usamos a função de leitura e  carregamos o arquivo. Contudo, essa fução só lê e não converte o DictReader.

    for linha in leitor_csv: # Para cada linha do leitor_csv vou adicionar ela no meu arquivo_csv que é uma lista vazia.
        arquivo_csv.append(linha)

print(arquivo_csv)

# O exemplo acima é uma API com funções padrões do python porque temos os parâmetros e o retorno. Um exemplo e se em uma entrevista a questão for crirar uma API só com funções nativas do python.
