# Projeto PIE9 V1 (Vulgo PIE 8) - Parte de Software
# Arduino + Gráficos em Python

Este projeto utiliza um Arduino Uno com o módulo nRF24L01 para enviar dados via rádio. Os dados são recebidos no computador via porta serial e exibidos graficamente.

## Estrutura do Projeto
- `arduino/`: Códigos para o transmissor e receptor Arduino.
- `python/`: Scripts Python para comunicação serial e geração de gráficos.
- `docs/`: Documentação do projeto.

## Configuração
1. **Arduino**:
   - Conecte o nRF24L01 conforme as instruções na pasta `arduino/`.
   - Carregue os códigos `transmissor.ino` e `receptor.ino` em dois Arduinos.

2. **Python**:
   - Instale as dependências: `pip install -r python/requirements.txt`.
   - Execute o script: `python python/main.py`.

## Funcionamento
- O transmissor envia dados do sensor para o receptor via nRF24L01.
- O receptor transmite os dados via porta serial para o computador.
- O Python recebe os dados e os exibe graficamente.
