# %%
def intersecao_ordenada(lista1: list, lista2: list):
    """
    Recebe duas listas e encontra os elementos que estão presentes em ambas. A saída não contém duplicatas e obrigatoriamente mantém a ordem de aparição da primeira lista.
    """
    intersecao = []

    for num in lista1:
        if num in lista2 and num not in intersecao:
            intersecao.append(num)

    return intersecao

# %%
lista1 = [4, 9, 5, 4]
lista2 = [9, 4, 9, 8, 4]
print(intersecao_ordenada(lista1, lista2))
