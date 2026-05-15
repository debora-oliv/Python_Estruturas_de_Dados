# %%
def converter_permissoes(arquivos: list):
  """
  Recebe uma lista de dicionários contendo informações sobre arquivos no formato {arquivo, permissao},
  atualizando os valores das permissões dos dicionários de representação numérica para representação simbolica.
  """
  mapa_simbolos = ("---", "--x", "-w-", "-wx", "r--", "r-x", "rw-", "rwx") # cada índice guarda sua respectiva representação simbólica

  for arquivo in arquivos:
    try:
      if arquivo['permissao'] is None:
        raise ValueError(f"A permissão não pode ser nula.")

      if len(arquivo['permissao']) != 3:
        #arquivo['permissao'] = None
        raise ValueError(f"A permissão deve ser composta por exatamente três valores inteiros.")

      nova_permissao = ""

      for char in arquivo['permissao']:
        char = int(char)
        if char not in range(8):
          #arquivo['permissao'] = None
          raise ValueError("A permissão deve ser composta apenas por valores inteiros entre 0 e 7.")
        
        nova_permissao += mapa_simbolos[char]

      arquivo['permissao'] = nova_permissao

    # Captura qualquer ValueError levantado anteriormente e sua mensagen
    except ValueError as erro:
      print(f"{arquivo['arquivo']}: {erro} \n")
      arquivo['permissao'] = None

  return arquivos

arquivos_auditados = [
    {"arquivo": "/etc/passwd", "permissao": "644"},
    {"arquivo": "/var/www/html", "permissao": "777"},
    {"arquivo": "/root/.ssh/id_rsa", "permissao": "600"},
    {"arquivo": "/tmp/script_suspeito.sh", "permissao": "corrompido"},
    {"arquivo": "/etc/shadow", "permissao": None},
    {"arquivo": "/home/user/app.py", "permissao": "755"},
    {"arquivo": "/opt/teste.txt", "permissao": "844"},
    {"arquivo": "/opt/curto.txt", "permissao": "77"}
]

converter_permissoes(arquivos_auditados)