# %%
def filtragem_criptomoedas(criptomoedas: dict, threshold: float):
    """
    Recebe um dicionário de criptomoedas no formato {'nome': preço} e um valor limite (threshold), retornando um novo dicionário contendo apenas as moedas cujo preço é estritamente maior que o limite.
    """
    moedas_acima_limiar = {}

    for k, v in criptomoedas.items():
        if v > threshold:
            moedas_acima_limiar[k] = v

    return moedas_acima_limiar

def filtragem_criptomoedas_otimizada(criptomoedas: dict, threshold: float):
    """
    Recebe um dicionário de criptomoedas no formato {'nome': preço} e um valor limite (threshold), retornando um novo dicionário contendo apenas moedas cujo preço é maior que o limite agora usando comprehension (abordagem mais rápida).
    """
    return {k:v for k,v in criptomoedas.items() if v > threshold}

cotacoes = {'BTC': 60000, 'ETH': 3000, 'ADA': 1, 'SOL': 150}

print(filtragem_criptomoedas(cotacoes, 2000))

print(filtragem_criptomoedas_otimizada(cotacoes, 2000))