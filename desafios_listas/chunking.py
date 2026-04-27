# %%
def chunking(lista: list, n: int):
    """
    Recebe uma lista e um número inteiro n e divide a lista original em várias sublistas, cada uma contendo no máximo n elementos, usando laços for.
    """
    chunks = []

    for i in range(0, len(lista), n):
        chunk = []
        limite = min(i + n, len(lista)) # em casos de listas com tamanho sem divisisão exata por n
        for j in range(i, limite):
            chunk.append(lista[j])
            chunks.append(chunk)

    return chunks

# %%
def slicing_chunking(lista: list, n: int):
    """
    Também recebe uma lista e um número inteiro n e divide em sublistas de n elementos, porém usando slicing.
    """
    chunks = []

    for i in range(0, len(lista), n):
        chunk = lista[i : i+n]
        chunks.append(chunk)

    return chunks

# %%
lista = [1, 2, 3, 4, 5, 6, 7]

print(chunking(lista, 3))

print(slicing_chunking(lista, 3))
