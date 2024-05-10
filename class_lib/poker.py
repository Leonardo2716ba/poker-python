import random

def criar_baralho():
    naipes = ['Copas', 'Ouros', 'Paus', 'Espadas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baralho = [{'valor': valor, 'naipe': naipe} for naipe in naipes for valor in valores]
    return baralho

def embaralhar(baralho):
    random.shuffle(baralho)

def distribuir_maos(baralho, num_jogadores):
    maos = {i: [] for i in range(num_jogadores)}
    for _ in range(2):  # Distribui duas cartas para cada jogador em uma mão de Texas Hold'em
        for jogador in range(num_jogadores):
            maos[jogador].append(baralho.pop(0))
    return maos

def exibir_maos(maos):
    for jogador, mao in maos.items():
        print(f"Jogador {jogador + 1}: {', '.join([carta['valor'] + ' de ' + carta['naipe'] for carta in mao])}")

def main():
    num_jogadores = int(input("Digite o número de jogadores: "))
    baralho = criar_baralho()
    
    # Embaralha o baralho apenas uma vez
    embaralhar(baralho)
    
    maos = distribuir_maos(baralho, num_jogadores)
    exibir_maos(maos)

if __name__ == "__main__":
    main()
