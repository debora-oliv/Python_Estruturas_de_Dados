# %%
def extrair_chave(dados: dict, caminho: str):
    """
    Recebe um dicionário profundamente aninhado e uma string representando um "caminho" de chaves separadas por pontos, retornando o valor final ou None caso o caminho não exista.
    """
    chaves = caminho.split('.')

    for chave in chaves:
        if chave not in dados:
            return None
        dados = dados[chave]

    return dados

dados = {
    'empresa': {
        'departamentos': {
            'rh': {'coordenador': 'Maria'},
            'ti': {'desenvolvedor pleno': ['Luiza', 'André'], 'desenvolvedor junior': ['Felipe'], 'gerente': 'Carlos'}
        }
    }
}

print(extrair_chave(dados, 'empresa.departamentos.ti.gerente'))