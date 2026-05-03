# %%
def mesclar_estoques(estoque1: dict, estoque2: dict):
    """
    Recebe dois dicionários representando o estoque no formato {'produto': quantidade} de duas filiais de uma loja,
    retornando um dicionário com todos os produtos e, caso um produto exista em ambas as filiais, com as quantidades somadas.
    """
    estoques = {}

    for produto, qtd  in estoque1.items():
        if produto in estoque2:
            qtd += estoque2.get(produto)
        estoques[produto] = qtd

    for produto, qtd  in estoque2.items():
        if produto not in estoque1:
            estoques[produto] = qtd

    return estoques

def mesclar_estoques_otimizado(estoque1: dict, estoque2: dict):
    estoques = estoque1.copy()

    for produto, qtd in estoque2.items():
        # Se encontrar o produto atual em 'estoques', assume quantidade do produto encontrado e soma com qtd. Se não, assume 0 e soma com qtd.
        estoques[produto] = estoques.get(produto, 0) + qtd

    return estoques


estoque_filial1 = {'maçã': 50, 'banana': 20, 'goiaba': 15}
estoque_filial2 = {'banana': 30, 'laranja': 10}

print(mesclar_estoques(estoque_filial1, estoque_filial2))

print(mesclar_estoques_otimizado(estoque_filial1, estoque_filial2))