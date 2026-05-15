# %%
def drenar_fila(comandos: list):
    """
    Recebe uma lista de mensagens que contém comandos de provisionamento de infraestrutura, processa a fila até que ela fique vazia ou detecte uma mensagem de "SHUTDOWN",
    retornando a lista vazia ou, caso tenho ocorrido alguma interrupção, com as mensagens restantes.
    """
    while comandos:
        comando = comandos.pop(0)
        if comando.upper() == "SHUTDOWN":
            print("\nAlerta: Comando de desligamento recebido. Abortando fila!\n")
            break
        print(f"Processando: [{comando}]")

    return comandos

fila_comandos = [
    "CREATE_EC2_INSTANCE",
    "ALLOCATE_ELASTIC_IP",
    "CREATE_RDS_DATABASE",
    "SHUTDOWN",
    "CONFIGURE_SECURITY_GROUP",
    "ATTACH_EBS_VOLUME"
]

print(drenar_fila(fila_comandos))