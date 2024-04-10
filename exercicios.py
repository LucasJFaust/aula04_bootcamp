"""# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado."""

# numeros: list = range(1,11)

# for numero in numeros:
#     print(numero**2)

"""# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby"."""

# ling: list = ["Python", "Java", "C++", "JavaScript"]

# ling.remove("C++")
# ling.append("Ruby")
# print(ling)

"""# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação."""

# from typing import Dict, Any

# livro: Dict[str, Any] = {
#     "Titulo":"Game of Thrones",
#     "Autor":"Estagiário",
#     "Ano": 2005
# }

# lista_de_elementos: list = livro.items()

# for elemento in lista_de_elementos:
#     print(elemento)

"""# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário."""

# def contar_caracteres(s): # Primeiro, definimos uma função chamada contar_caracteres que recebe uma string s como argumento. Pense nessa string s como uma frase ou palavra que você quer analisar.
#     contagem = {} # Dentro da função, criamos um dicionário vazio chamado contagem. Este dicionário vai armazenar nossos resultados, onde cada chave é uma letra e cada valor é o número de vezes que essa letra aparece na string.
#     for caractere in s: # Agora, vamos passar por cada letra na string s usando um loop. Para cada letra (caractere), fazemos o seguinte:
#         contagem[caractere] = contagem.get(caractere, 0) + 1 # Usamos contagem.get(caractere, 0) para tentar pegar o valor atual dessa letra no dicionário contagem. Se a letra não estiver no dicionário ainda, usamos 0 como valor padrão. Isso significa "se não encontramos a letra ainda, vamos começar contando do zero". Depois, adicionamos 1 a esse valor, porque encontramos essa letra mais uma vez. E atualizamos o dicionário com esse novo valor para a letra.
#     return contagem

# print(contar_caracteres("engenharia de dados"))

"""# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras."""

# lista_compras = ["maçã", "banana", "cereja"]
# precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
# total = sum(precos[item] for item in lista_compras)
# print(f"Preço total: {total}")

"""6. Eliminação de Duplicatas - Objetivo: Dada uma lista de emails, remover todos os duplicados."""

# emails: list = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# emails_unicos = list(set(emails)) # Para encontrar as "cores" (ou e-mails) únicas, primeiro convertemos a lista em um conjunto, usando a função set(). No mundo da matemática, um conjunto é uma coleção de itens onde cada item é único; não há repetições. Ao converter a lista em um conjunto, automaticamente removemos todos os e-mails duplicados, assim como você faria ao pegar apenas uma bola de cada cor única.

# print(emails_unicos)

"""7. Filtragem de Dados - Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18."""

# idades = [22, 15, 30, 17, 18]
# idades_validas = [idade for idade in idades if idade >= 18] # Primeiro criamos uma variavel para atuar na lista, antes do for. Depois com o for no inteiramos da lista e com o if criamos a verificação de cada idade.

# print(idades_validas)

"""8. Ordenação Personalizada - Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome."""

# pessoas = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Bob", "idade": 25},
#     {"nome": "Carol", "idade": 20},
#     {"nome": "Xarles", "idade": 20},
#     {"nome": "Duda", "idade": 20}
# ]
# pessoas.sort(key=lambda pessoa: pessoa["nome"]) # key: Este é um parâmetro do método .sort() que nos permite especificar com base em que critério queremos ordenar a lista. Em outras palavras, o key nos diz como comparar os itens.lambda pessoa: pessoa["nome"]: Isso é o que chamamos de função lambda, uma pequena função anônima em Python. Neste caso, para cada dicionário (cada pessoa) na lista pessoas, essa função retorna o valor associado à chave "nome". O método .sort() então usa esses valores retornados (os nomes das pessoas) para determinar a ordem.

# print(pessoas)

"""9. Agregação de Dados - Objetivo: Dado um conjunto de números, calcular a média."""

# numeros = [10, 20, 30, 40, 50]
# media = sum(numeros) / len(numeros) # Aqui usamos a função sum pora somar os numeros na lista e depois dividimos o valor com o len para somar cada item individualmente e termos um divisor com o número total de itens.

# print("Média:", media)

"""10. Divisão de Dados em Grupos - Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares."""

# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares = [valor for valor in valores if valor % 2 == 0]
# impares = [valor for valor in valores if valor % 2 != 0]

# print("Pares:", pares)
# print("Ímpares:", impares)

# Exercícios com Dicionários
"""11. Atualização de Dados - Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico."""

# produtos = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]

# # Atualizar o preço do produto com id 2 para 90
# for produto in produtos:
#     if produto["id"] == 2:
#         produto["preço"] = 90

# print(produtos)

# """12. Fusão de Dicionários - Objetivo: Dados dois dicionários, fundi-los em um único dicionário."""

# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}

# dicionario_fundido = {**dicionario1, **dicionario2} # O ** é chamado de operador de desempacotamento. Ele pega todos os itens do dicionário e os coloca no novo dicionário que estamos criando (dicionario_fundido).

# print(dicionario_fundido)

"""13. Filtragem de Dados em Dicionário - Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0."""

# estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

# estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

# print(estoque_positivo)

"""14. Extração de Chaves e Valores - Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
"""
# dicionario = {"a": 1, "b": 2, "c": 3}
# chaves = list(dicionario.keys())
# valores = list(dicionario.values())

# print("Chaves:", chaves)
# print("Valores:", valores)

"""15. Contagem de Frequência de Itens - Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário."""

# texto = "engenharia de dados"
# frequencia = {} # Primeiro, criamos um dicionário vazio chamado frequencia. Pense nesse dicionário como uma tabela onde vamos anotar cada letra (caractere) que encontrarmos e quantas vezes a vimos.

# for caractere in texto: # Agora, vamos examinar cada letra (caractere) na nossa palavra misteriosa, "engenharia de dados", uma por uma.
#     if caractere in frequencia: # Aqui estamos dizendo: "Se já vimos essa letra antes (ou seja, ela já está na nossa tabela de contagens), então apenas aumente o número de vezes que vimos ela (frequencia[caractere] += 1)."
#         frequencia[caractere] += 1
#     else:
#         frequencia[caractere] = 1 # Mas, se é a primeira vez que encontramos essa letra, precisamos adicioná-la à nossa tabela com o número 1, pois é a primeira vez que a vimos.

# print(frequencia)

# Exercícios de Funções
"""# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números."""

# Primeiro criamos a lista de numeros:

# lista_numeros: list = [1,4,6,7,3,9]

# def soma_numeros(lista_de_numeros: list) -> int: # int: Isso é outra dica de tipo, indicando que a função vai retornar um número inteiro (int), que será a soma dos números da lista.
#     soma = 0
#     for numero in lista_de_numeros:
#         soma += numero
#     return soma

# # Chamada da função passando a lista de números e impressão do resultado
# resultado = soma_numeros(lista_numeros)
# print(f"A soma dos números é: {resultado}")

"""# 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário."""

# n: int = int(input("Escreva um número: "))

# def eh_primo(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# print(eh_primo(n))


"""# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida."""

# def inversao(string_normal):
#     return string_normal[::-1]

# string_normal: str = input("Escreva uma palavra: ")
# palavra_invertida = inversao(string_normal)
# print(palavra_invertida)

"""# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado."""

# def encontrar_pares(lista_numeros, soma_desejada):
#     pares_encontrados = []
#     for i in range(len(lista_numeros)):
#         for j in range(i + 1, len(lista_numeros)):
#             if lista_numeros[i] + lista_numeros[j] == soma_desejada:
#                 pares_encontrados.append((lista_numeros[i], lista_numeros[j]))
#     return pares_encontrados

# lista_teste = [1, 2, 3, 4, 5]
# soma_alvo = 5
# print(encontrar_pares(lista_teste, soma_alvo))

"""# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas"""

def chaves_ordenadas(dicionario): # Primeiro, definimos a função chaves_ordenadas que espera receber um dicionário como argumento
    lista_chaves_ordenadas = sorted(dicionario.keys()) # Dentro da função, podemos extrair as chaves do dicionário usando o método .keys(). Esse método retorna um objeto de visualização que exibe uma lista de todas as chaves no dicionário. Para ordenar essas chaves, podemos usar a função sorted(), que retorna uma nova lista contendo todos os itens do iterável fornecido em ordem ascendente. Portanto, podemos passar o objeto de visualização das chaves diretamente para a função sorted().
    return lista_chaves_ordenadas 
dicionario_teste = {"banana": 3, "maçã": 5, "pera": 2, "laranja": 7}
print(chaves_ordenadas(dicionario_teste))