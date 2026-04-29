#%%
import math

def encontrar_servidor_proximo(cliente: tuple, servidores: list):
    """
    Recebe uma tupla representando as coordenadas de um cliente (x_cliente, y_cliente) e uma lista de tuplas representando os servidores disponíveis (id_servidor, x_servidor, y_servidor),
    calcula a Distância Euclidiana entre o cliente e todos os servidores da lista, retornando uma tupla (id_mais_proximo, menor_d) com o id do servidor mais próximo do cliente e sua a distância exata até ele.
    """
    x_cliente, y_cliente = cliente
    id_mais_proximo, x_servidor, y_servidor = servidores[0]

    menor_d = math.sqrt(((x_servidor-x_cliente) ** 2) + ((y_servidor-y_cliente) ** 2))

    for id_servidor, x_servidor, y_servidor in servidores[1:]:
        d = math.sqrt(((x_servidor-x_cliente) ** 2) + ((y_servidor-y_cliente) ** 2))
        if d < menor_d:
            id_mais_proximo = id_servidor
            menor_d = d

    return (id_mais_proximo, menor_d)

cliente = (12, 5)

servidores = [
    ('aws-sa-east-1a', 10, 5),
    ('aws-sa-east-1b', 15, 8),
    ('aws-us-east-1', 45, 80),
    ('aws-eu-west-1', 120, -30)
]

print(encontrar_servidor_proximo(cliente, servidores))