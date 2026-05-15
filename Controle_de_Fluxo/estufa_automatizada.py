# %%
def alterar_temperatura_estufa(buffer: list):
  """
    Recebe uma lista contendo leituras de diferentes sensores de temperatura de uma estufa, usa um loop para esvaziar o buffer e try/except para lidar com falhas de conversão,
    imprimindo, se não houver falhas na leitura do sensor, o comportamento da estufa com base em critérios de temperatura definidos.
  """
  while buffer:
    try:
      temperatura = float(buffer.pop(0))
      print(f"[{temperatura}°C]", end=' ')
      if temperatura > 35.0:
        print(f"Ligando resfriamento! \n")
      elif temperatura < 15.0:
        print(f"Ligando aquecimento! \n")
      else:
        print(f"A temperatura já está ideal! \n")

    # ValueError: ocorre quando não é possível converter a temperatura para float, ou seja, temperatura não possui valor do tipo numérico
    except ValueError:
      print(f"[ ] Leitura ignorada: Falha no sensor. \n")

fila_sensores = [
    "22.5",
    "38.1",
    "ERR_SGNL",
    "14.2",
    "25.0",
    "0x00A"
]

alterar_temperatura_estufa(fila_sensores)