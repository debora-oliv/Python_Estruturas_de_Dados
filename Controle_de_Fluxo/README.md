# Controle de Fluxo e Laços

O objetivo foi aprimorar o domínio de estruturas de controle de fluxo, list comprehensions e tratamento de exceções por meio da resolução de problemas do mundo real simulando rotinas encontradas em engenharia de dados, automação e segurança da informação.

# Desafios

### **1. analise_logs.py**

**Foco:** `for`, `if/elif/else`, `try/except`

* **Cenário:** Auditoria e classificação de logs de acesso a uma API.

* **Descrição:** Itera sobre um lote de registros de conexões, contabilizando sucessos, erros de servidor e alertas de segurança baseados no status_code. Implementa tratamento de erros para não interromper a execução ao encontrar registros corrompidos ou com chaves ausentes.

### **2. astronomia_computacional.py**

**Foco:** `List Comprehensions`

* **Cenário:** Processamento de dados espaciais e cálculo do Earth Similarity Index (ESI) de exoplanetas.

* **Descrição:** Utiliza sintaxe enxuta para transformar e filtrar dicionários em tempo real. Separa os planetas prioritários e gera relatórios de habitabilidade, tratando dados científicos ruidosos, faltantes ou com tipagem incorreta.

### **3. drenagem_fila.py**

**Foco:** `while` , `break`

* **Cenário:** Consumo de uma fila de provisionamento de recursos em nuvem (simulação AWS).

* **Descrição:** Esvazia continuamente um buffer de comandos de infraestrutura. Demonstra o controle de fluxo crítico ao interromper imediatamente a execução ao receber um sinal de "SHUTDOWN", preservando o estado das mensagens restantes.

### **4. estufa_automatizada.py**

**Foco:**  `while`, `try/except`, `if/elif/else`

* **Cenário:** Sistema de leitura de sensores térmicos para Internet das Coisas (IoT).

* **Descrição:** Simula um software embarcado que lê dados de um buffer de hardware. O script decide se deve acionar sistemas de resfriamento ou aquecimento, e utiliza tratamento de exceções para ignorar ruídos de transmissão (strings ilegíveis ou falhas de sensor) sem travar a máquina.

### **5. limpeza_dataset.py**

**Foco:** `List Comprehensions`, `manipulação de strings`

* **Cenário:** Sanitização de dados de treinamento para modelos de Inteligência Artificial.

* **Descrição:** Focado na privacidade e segurança do dado. Filtra registros rejeitados e atua na prevenção de vazamento de informações sensíveis (PII), substituindo automaticamente palavras-chave críticas (como senhas vazadas) por máscaras de segurança, usando uma única linha de processamento otimizado.

### **6. permissoes_arquivos.py**

**Foco:** `for`, `orquestração de múltiplos raises`, `mapeamento de índices`

* **Cenário:** Auditoria automatizada de permissões de arquivos críticos no Linux (DevSecOps).

* **Descrição:** Avalia configurações de segurança em sistemas operacionais. O script converte permissões do formato octal (ex: 755) para a representação simbólica (rwx). Aplica uma validação rigorosa com try/except para barrar strings fora de padrão, valores nulos e tamanhos incorretos, garantindo a integridade do relatório de auditoria.