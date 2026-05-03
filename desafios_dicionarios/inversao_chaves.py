# %%
def inverter_chaves(funcionarios: dict):
    """
    Recebe uma estrutura onde as chaves são nomes de funcionários e os valores são seus respectivos departamentos,
    retornando um dicionário onde as chaves são os departamentos e os valores são uma lista com o(s) nome(s) do(s) funcionário(s).
    """
    inverso = {}

    for nome, departamento in funcionarios.items():
        if departamento not in inverso:
            inverso[departamento] = []
        inverso[departamento].append(nome)

    return inverso

funcionaris = {'Ana': 'TI', 'João': 'RH', 'Carlos': 'TI', 'Maria': 'Vendas'}

print(inverter_chaves(funcionaris))
# %%
