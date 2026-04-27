# %%
def length_encoding(lista: list):
    """
    Algoritmo que percorre uma lista e agrupa elementos adjacentes repetidos em uma estrutura [elemento, quantidade].
    """
    lista_agrupada = []
    alvo = lista[0]
    count = 1

    # o slicing pula o primeiro elemento porque ele já foi devidamente contado e armazenado 
    for num in lista[1:]:
        if num != alvo:
            lista_agrupada.append([alvo, count])
            alvo = num
            count = 1
        else:
            count += 1
    lista_agrupada.append([alvo, count])

    return lista_agrupada

# %%
lista = ['a', 'a', 'a', 'b', 'c', 'c', 'a']
print(length_encoding(lista))