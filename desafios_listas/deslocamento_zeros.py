# %%
def deslocamento_zero(lista: list):
    """
    Recebe uma lista de números inteiros e move todos os zeros para o final, mantendo a ordem original dos elementos não-zeros.
    """
    posicao = 0

    for i in range(len(lista)):
        if lista[i] != 0:
            lista[posicao], lista[i] = lista[i], lista[posicao]
            posicao += 1

    return lista

# %%
lista = [1, 0, 0, 3, 12]
print(deslocamento_zero(lista))