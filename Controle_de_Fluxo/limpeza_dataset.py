# %%
def desidentificar(dataset: list):
    """
    Recebe uma lista que representa um dataset usado para treinar modelos de inteligência artificial,
    retornando uma list comprehension apenas com linhas onde o valor da chave "status" seja "aprovado" e com a string "SENHA" substituida pela string "***REMOVIDO***", caso o valor da chave "texto" cotenha essa palavra.
    """
    return [dicionario['texto'].replace("SENHA", "***REMOVIDO***") if "SENHA" in dicionario['texto'] else dicionario for dicionario in dataset_bruto if dicionario['status'] != "rejeitado"]

dataset_bruto = [
    {"id": 101, "texto": "O usuário conectou com sucesso.", "status": "aprovado"},
    {"id": 102, "texto": "A SENHA digitada está desatualizada.", "status": "aprovado"},
    {"id": 103, "texto": "Tentativa de login falhou.", "status": "rejeitado"},
    {"id": 104, "texto": "Configuração de rede alterada.", "status": "aprovado"},
    {"id": 105, "texto": "A SENHA do banco foi vazada.", "status": "rejeitado"}
]

print(desidentificar(dataset_bruto))