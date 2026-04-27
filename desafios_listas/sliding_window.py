#%%
def sliding_window_maximum(lista: list, k: int):
    """
    Recebe uma lista de números e um inteiro k, representando o tamanho da janela, e retorna uma nova lista contendo o valor máximo encontrado dentro de cada posição da janela.
    """
    valores_maximos = []

    for i in range(len(lista)+1 - k):
        maior = lista[i]
        janela = lista[i : i+k]
        valores_maximos.append(max(janela))

    return valores_maximos

def swm_list_comprehension(lista: list, k: int):
    """
    Também recebe uma lista de números e um inteiro k, porém usando list comprehension para retornar a lista contendo os valores máximos em apenas uma linha.
    """    
    return [max(lista[i : i+k]) for i in  range(len(lista)+1 - k)]

lista = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(sliding_window_maximum(lista, k))

print(swm_list_comprehension(lista, k))