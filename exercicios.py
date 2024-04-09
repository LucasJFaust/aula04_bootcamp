# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

from typing import Dict, Any

livro: Dict[str, Any] = {
    "Titulo":"Game of Thrones",
    "Autor":"Estagiário",
    "Ano": 2005
}

lista_de_elementos: list = livro.items()

for elemento in lista_de_elementos:
    print(elemento)

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.