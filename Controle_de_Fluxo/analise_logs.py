# %%
def analisar_logs(logs: list):
  """
    Recebe uma lista de dicionários respresentando logs no formato {ip, status_code, endpoint} vindo de fontes diferentes,
    retornando a classificação de cada log com base no seu status_code e considerando logs que possam estar corrompidos/incompletos.
  """
  status_registros = []

  for log in logs:
    try:
      status_code = log["status_code"]
      if status_code == 200:
        status_registros.append("Sucesso")
      elif status_code in (401, 403): # ou: status_code == 401 or status_code == 403
        status_registros.append("Alerta de Segurança")
      elif status_code == 500:
        status_registros.append("Erro de Servidor")

    # KeyError: ocorre quando a chave "satus_code" não existe
    # TypeError: ocorre quando o log analisado não é um dicionário
    except (KeyError, TypeError) as error:
      status_registros.append(f"Registro Inválido: {error}")

  return status_registros

logs_acesso = [
    {"ip": "192.168.1.10", "status_code": 200, "endpoint": "/api/users"},
    {"ip": "10.0.0.5", "status_code": 403, "endpoint": "/api/admin"},
    "Registro corrompido no buffer",
    {"ip": "172.16.0.2", "status_code": 500, "endpoint": "/api/process"},
    {"ip": "192.168.1.11", "endpoint": "/api/health"},
    {"ip": "10.0.0.8", "status_code": 200, "endpoint": "/api/users"}
]

print(analisar_logs(logs_acesso))