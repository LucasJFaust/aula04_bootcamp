# lista = ["Sapato", 39, 10.38, True]
from typing import Dict

produto_01: Dict[str,int]

import json

produto_01: dict = {
    "nome":"Sapato",
    "quantidade":39,
    "preco":10.38,
    "disponibilidade": True
}

produto_02: dict = {
    "nome":"Televisao",
    "quantidade":10,
    "preco":70.38,
    "disponibilidade": False
}

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)

carrinho_json = json.dumps(carrinho)

print(carrinho_json)