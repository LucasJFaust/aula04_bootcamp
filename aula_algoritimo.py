lista_de_numeros: list = [40,50,60,70,-408593,1,50]

# Usamos as funções para diminuirmos trabalho que necessitam de repetição. Por exemplo, abaixo, teriamos que fazer varias vezes essa ordenação, por isso "empacotamos" a ação em uma função.

def ordenar_lista_de_numeros(numeros: list) -> list: # A função precisa de um input, que nesse caso é uma lista de numeros com typagem list, e estou dizendo que o output vai ser um tipo list também.
    nova_lista_de_numeros = numeros.copy() # Aqui seguimos uma boa prática que nunca mudar o que recebemos, por isso criamos uma nova variável para receber numeros, a transformação e copiarmos.

    for i in range(len(nova_lista_de_numeros)):
        for j in range(i+1, len(nova_lista_de_numeros)):
            if nova_lista_de_numeros[i] > nova_lista_de_numeros[j]:
                nova_lista_de_numeros[i], nova_lista_de_numeros[j] = nova_lista_de_numeros[j], nova_lista_de_numeros[i]

    return nova_lista_de_numeros # O retorne permite que a função seja envocada.

nova_lista = ordenar_lista_de_numeros(lista_de_numeros)
print(nova_lista)