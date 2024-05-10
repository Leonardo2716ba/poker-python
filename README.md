# Trabalho Prático de Redes de Computadores

## Implementação do Jogo de Poker Multiplayer

### Descrição

O Trabalho Prático consiste na implementação de um servidor que aguarda a conexão de dois clientes para iniciar uma partida do jogo de Poker. Cada jogador recebe 5 cartas e deve decidir entre apostar ou não apostar. As regras para pontuação são as seguintes:

- Não apostar: Perde 1 ponto.
- Apostar e perder: Perde 2 pontos.
- Apostar e ganhar: Ganha 3 pontos.

Após receber as jogadas, o servidor verifica o vencedor e informa aos jogadores. Em seguida, os jogadores decidem se desejam continuar na partida. Se um jogador desistir, a partida termina para ambos, e o servidor envia um relatório contendo informações como tempo de jogo, vitórias, derrotas, entre outros.

### Valor

O trabalho tem um valor total de 30 pontos e pode ser realizado em dupla.

### Data de Entrega

- **Entrega Final:** 06/02/2024 às 10h no moodle.
- **Checkpoint (10 pontos):** 19/12/2023.

### Pontos Extras

- **Interface Gráfica:** Até 5 pontos, dependendo da qualidade e quantidade de telas.
- **Múltiplos Jogadores (mais do que dois):** 5 pontos.
- **Múltiplas Salas de Jogo:** 5 pontos.
- **Implementação Realística do Jogo de Poker:** 10 pontos.

### Observações

- O trabalho pode ser implementado em qualquer linguagem.
- Utilizar a biblioteca sockets para comunicação entre servidor e clientes.

---