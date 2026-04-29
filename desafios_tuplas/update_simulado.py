#%%
def alterar_tema(conf_usuario: tuple, novo_tema):
    """
    Recebe uma tupla que guarda as configurações de um usuário no formato (id_usuario, tema, notificacoes_ativas) e uma string com o novo tema do usuário,
    retornando uma nova tupla reaproveitando os dados da tupla original com atualização apenas do tema.
    """
    nova_conf = conf_usuario[:1] + (novo_tema,) + conf_usuario[2:]

    return nova_conf

conf_usuario = (101, 'dark', True)

print(alterar_tema(conf_usuario, 'dark-blue'))