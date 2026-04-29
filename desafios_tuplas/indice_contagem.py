#%%
def indice_contagem(tupla: tuple, n: int):
    """
    Recebe uma tupla de números inteiros e um inteiro n, retornando quantas vezes o número n aparece na tupla e o índice da sua primeira ocorrência.
    """
    count = 0
    for num in tupla:
        if num == n:
            count += 1
    return count, tupla.index(n)

tupla = (1, 2, 3, 2, 4, 2, 5)
n = 5

print(indice_contagem(tupla, n))