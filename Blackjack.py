import random

baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
maoJogador = [random.choice(baralho), random.choice(baralho)]
maoDealer = [random.choice(baralho), random.choice(baralho)]
partida = True

print(f"Suas cartas são: {maoJogador}")
print(f"A soma das cartas dá {sum(maoJogador)} pontos")

if sum(maoJogador) == 21:
    print("BLACKJACK! Você ganhou!")
else:
    while sum(maoJogador) < 21:
        print(f"Sua pontuação atual: {sum(maoJogador)}")
        print("Deseja comprar ou parar?")
        jogada = input().lower()

        if jogada == "comprar":
            nova_carta = random.choice(baralho)
            maoJogador.append(nova_carta)
            print(f"Você comprou: {nova_carta}")

            if sum(maoJogador) > 21:
                print(f"Sua mão: {maoJogador}")
                print("Você estourou! Perdeu.")
                partida = False
                break

            elif sum(maoJogador) == 21:
                print("Você fez 21!")
                break

        elif jogada == "parar":
            print(f"Sua mão final: {maoJogador}")
            print(f"Sua pontuação final: {sum(maoJogador)}")
            break

if partida == True:
    while sum(maoDealer) <= 17:
        nova_carta = random.choice(baralho)
        maoDealer.append(nova_carta)

    if sum(maoDealer) == 21:
        print("O Dealer conseguiu um BLACKJACK!")
        print("Você perdeu! Boa sorte na próxima vez.")
    elif sum(maoDealer) > 21:
        print("O Dealer estourou!")
        print("Parabens! Você ganhou.")
    elif sum(maoDealer) == sum(maoJogador):
        print("Empate!")
    else:
        print(f"Sua mão deu {sum(maoJogador)}")
        print(f"A mão do Dealer deu {sum(maoDealer)}")
        if sum(maoDealer) < 21:
            if sum(maoJogador) > sum(maoDealer):
                print("Parabens! Você ganhou.")
            else:
             print("Você perdeu! Boa sorte na próxima vez.")

