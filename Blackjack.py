import random

baralho = []
valores = {"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
naipes = ['♠', '♥', '♦', '♣']
for valor in valores:
    for naipe in naipes:
        carta = (valor, naipe)
        baralho.append(carta)

def calcularPontuação(mao):
    total = 0 
    for carta in mao:
        total += valores[carta[0]]
    return total

maoJogador = [random.choice(baralho), random.choice(baralho)]
maoDealer = [random.choice(baralho), random.choice(baralho)]
partida = True

print(f"Suas cartas são: {maoJogador}")
print(f"A soma das cartas dá {calcularPontuação(maoJogador)} pontos")

if calcularPontuação(maoJogador) == 21:
    print("BLACKJACK! Você ganhou!")
else:
    while calcularPontuação(maoJogador) < 21:
        print(f"Sua pontuação atual: {calcularPontuação(maoJogador)}")
        print("Deseja comprar ou parar?")
        jogada = input().lower()

        if jogada == "comprar":
            nova_carta = random.choice(baralho)
            maoJogador.append(nova_carta)
            print(f"Você comprou: {nova_carta}")

            if calcularPontuação(maoJogador) > 21:
                print(f"Sua mão: {maoJogador}, somando {calcularPontuação(maoJogador)}")
                print("Você estourou! Perdeu.")
                partida = False
                break

            elif calcularPontuação(maoJogador) == 21:
                print("Você fez 21!")
                break

        elif jogada == "parar":
            print(f"Sua mão final: {maoJogador}")
            print(f"Sua pontuação final: {calcularPontuação(maoJogador)}")
            break

if partida == True:
    while calcularPontuação(maoDealer) <= 17:
        nova_carta = random.choice(baralho)
        maoDealer.append(nova_carta)

    if calcularPontuação(maoDealer) == 21:
        print("O Dealer conseguiu um BLACKJACK!")
        print("Você perdeu! Boa sorte na próxima vez.")
    elif calcularPontuação(maoDealer) > 21:
        print("O Dealer estourou!")
        print("Parabens! Você ganhou.")
    elif calcularPontuação(maoDealer) == calcularPontuação(maoJogador):
        print("Empate!")
    else:
        print(f"Sua mão deu {calcularPontuação(maoJogador)}")
        print(f"A mão do Dealer deu {calcularPontuação(maoDealer)}")
        if calcularPontuação(maoDealer) < 21:
            if calcularPontuação(maoJogador) > calcularPontuação(maoDealer):
                print("Parabens! Você ganhou.")
            else:
             print("Você perdeu! Boa sorte na próxima vez.")
