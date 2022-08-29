# Desafio Proposto
"""
Crie um jogo que embaralhe uma palavra e a mostre ao jogador. O objetivo é acertar a palavra em até 5 tentativas. Informe sempre quantas tentativas ele ainda tem. Se ele acertar, dê os parabéns; se errar dê uma palavra de ânimo (que mude de forma aleatória). Ao final, mostre a palavra correta e o número de tentativas que ele utilizou.
"""


from random import choice
from funcoes import *


palavra_sorteada = choice(open("palavras.txt").read().split()) # Vai abrir o arquivo.txt e sorteia uma palavra)  

cabecalho("JOGO EMBARALHA PALAVRAS")

print(
    f"\033[93mTente desvendar essa palavra ->\033[m \033[32m{embaralha_palavra(palavra_sorteada)}\033[m"
)

verifica_acerto(palavra_sorteada)
