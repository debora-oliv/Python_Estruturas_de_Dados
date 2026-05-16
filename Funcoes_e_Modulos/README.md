# Funções e Módulos
O objetivo foi exercitar documentação de código adotando, por preferência pessoal e familiaridade, o padrão **Google Style Docstrings** com ação, parâmetros e retornos bem definidos e também type hints. Além disso, exercitar a importação, instalação e uso de pacotes externos.

Para isso, foi criado um script que simula o download de um "dump" de texto da internet e usa o poder do Regex para caçar informações confidenciais que não deveriam estar ali, como endereços de IP, e-mails e datas.

# Funções

A arquitetura do script foi dividida em funções de responsabilidade única para separar a camada de rede, a regra de negócios (Regex) e a interface.

**`coletar_texto_url(url: str) -> str`**: Realiza o GET na URL fornecida, valida se a requisição foi bem-sucedida e retorna o texto em formato bruto, tratando exceções de conexão caso a URL seja inválida ou o servidor esteja fora do ar.

**`escanear_vazamentos(texto: str, tipo_dado: str) -> list[str]`**: Recebe o texto bruto, aplica expressões regulares (Regex) específicas com base no tipo de dado solicitado e retorna uma lista contendo todas as ocorrências encontradas no texto ou, caso nada tenha sido encontrado, retorna uma lista vazia.

**`renderizar_dashboard()`**: Concentra toda a lógica da interface web, criando os campos de entrada, botões de ação e exibindo tabelas e métricas com os dados processados pelas funções anteriores.

# Pacotes e Bibliotecas
**`requests`**: Pacote usado para buscar o texto bruto diretamente da URL via requisições HTTP.

**`streamlit`**: Pacote usado para construir uma tela interativa na web.

**`re (Regex)`**: Biblioteca padrão do Python usado varrer textos em busca de padrões sensíveis ou maliciosos.

# Execução
**1. Instalação dos pacotes/dependências:**
```
pip install -r requirements.txt
```

**2. Iniciar a aplicação web no terminal:**
```
streamlit run main.py
```

**3. Cole essa URL no campo de texto do dashboard no Streamlit: **`https://gist.githubusercontent.com/debora-oliv/d6d7cae4455f1018a519d5e69d01ce1d/raw/da188b87e750fd465b8e17e96c26889918aecb16/fake_data.txt`**
