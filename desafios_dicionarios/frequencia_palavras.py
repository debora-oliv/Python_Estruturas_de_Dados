# %%
def contagem_palavras(frase: str):
    """
    Recebe e pré-processa uma frase (string), retornando quantas vezes cada palavra aparece.
    """
    frase = frase.lower()
    palavras = frase.replace(".", " ").replace(",", " ").replace(";", " ").replace(":", " ").replace("!", " ").replace("?", " ").replace("  ", " ").split()

    contagem = {}

    for palavra in palavras:
        if palavra not in contagem:
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1

    return contagem

frase = "O rato roeu a roupa. A roupa do rei."

print(contagem_palavras(frase))