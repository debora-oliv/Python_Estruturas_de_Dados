# %%
def analisar_semelhanca_exoplaneta(exoplanetas: dict):
  """
  Recebe um dicionário de dados sobre exoplanetas no formato {planeta, esi} (sendo ESI um número que indica o quão parecido o planeta é com a Terra),
  retornando uma lista apenas com os nomes dos planetas com ESI >= 0.80.
  """
  return [exoplaneta['planeta'] for exoplaneta in exoplanetas if exoplaneta['esi'] >= 0.80]

dados_sonda = [
    {"planeta": "Kepler-452b", "esi": 0.83},
    {"planeta": "Gliese 667 Cc", "esi": 0.84},
    {"planeta": "HD 209458 b (Osíris)", "esi": 0.15},
    {"planeta": "Proxima Centauri b", "esi": 0.87},
    {"planeta": "TRAPPIST-1b", "esi": 0.35}
]

print(analisar_semelhanca_exoplaneta(dados_sonda))