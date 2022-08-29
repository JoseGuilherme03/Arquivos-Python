def cabecalho(titulo):
    print()
    print("-=" * len(titulo))
    print(f"\033[93m            {titulo}        \033[m")
    print("-=" * len(titulo))
    print()


def embaralha_palavra(palavra_sorteada):
    from random import shuffle

    palavra_embaralhada = list(palavra_sorteada)
    shuffle(palavra_embaralhada)
    return "".join(palavra_embaralhada)


def verifica_acerto(palavra_correta):
    frases_motivacao = [
        "ERROU!!. Tente novamente, não desista!!.",
        "ERROU!!. Tente novamente, você ira acertar o quanto antes...",
        "ERROU!!. Tente novamente, você vai conseguir acertar...",
        "ERRO!!. Tente novamente, você quase acertou... ",
    ]
    cont = 0
    tentativas = 5

    while True:
        jogador = str(input("\nDigite a palavra: ")).lower()

        if jogador == palavra_correta:
            print(
                f"\n\033[32mPARABÉNS!! você acertou a palavra na {cont+1}° tentativa\033[m"
            )
            break
        elif cont <= 3:
            print(f"\033[31m{frases_motivacao[cont]}\033[m")
            cont += 1

        print(f"{tentativas-1} tentativas restantes")
        tentativas -= 1

        if tentativas == 0:
            print(f"\033[31mGAME OVER!!. A palavra correta era {palavra_correta}\033[m")
            print()
            break
        print()
