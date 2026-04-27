"""
Recebe uma lista de tuplas contendo informações de alunos no formato (Nome, Idade, Nota) e ordena a lista usando as seguintes regras de prioridade:
1º - Maior Nota (ordem decrescente)
2º - Menor Idade (ordem crescente)
3º - Ordem Alfabética do Nome
"""
#%%
def ordenacao_alunos(lista: list):
    for tupla in lista:
        for i in tupla:
        sorted(key = tupla[2])
        if :


            sorted(key = tupla[1], reverse=True)
            sorted(key = tupla[0])

lista = [('Ana', 20, 9.0), ('Carlos', 22, 9.0), ('Daniel', 21, 8.5), ('Bruno', 20, 9.0)]

print(ordenacao_alunos(lista))