#%%
def desempacotamento_manual(lista: list):
    """
    Recebe uma lista de tuplas emparelhadas representando no formato (Produto, Preço), retornando duas tuplas "descompactadas", uma só com os nomes dos produtos e outra só com os preços correspondentes.
    """
    produtos = []
    precos = []
    for produto, preco in lista:
        produtos.append(produto)
        precos.append(preco)
    return tuple(produtos), tuple(precos)

#%%
def desempacotamento_unzip(lista: list):
    """
    Também recebe uma lista de tuplas (Produto, Preço) e "descompacta" em uma tupla só com os nomes dos produtos e outra só com os preços correspondentes,
    porém utilizando uma função nativa (zip) e passando o operador de desempacotamento *
    """
    produtos, precos = zip(*lista)
    return produtos, precos

#%%
lista = [('Maçã', 2.5), ('Banana', 1.5), ('Cereja', 5.0)]

print(desempacotamento_manual(lista))

print(desempacotamento_unzip(lista))