from collections import Counter
import wget
import os
import matplotlib.pyplot as plt


# Verifica se o arquivo existe, se não existir vai até o local desejado e faz o download dele
if os.path.exists('livro.txt'):
    print("Arquivo já existe, e não será baixado.")
else:
    print("Arquivo não existe, baixando...")
    wget.download('https://www.gutenberg.org/files/16429/16429-0.txt','livro.txt')


# Abre e fecha o arquivo e adiciona todo o livro a variavel texto em letra minuscula
with open('livro.txt') as arquivo:
    texto = arquivo.read().lower()


# filtra o livro, tirando os caracteres especias usando compreensão de lista
texto_filtrado = ''.join([letra for letra in texto if letra.isalpha() or letra == ' '])


# O metódo abaixo filtra do mesmo jeito
"""texto_filtrado = ''
for letra in texto:
    if letra.isalpha() or letra == ' ':
        texto_filtrado += letra
print(texto_filtrado)"""


# Cria um dicionário com a frequência que aparece cada letra no texto
letras = [l for l in texto_filtrado if l.isalpha()]
frequencia_letras = Counter(letras)


# Cria um gráfico exibindo a letra e com que frequência ela aparece no texto
rotulos, valores = zip(*frequencia_letras.most_common(5))
plt.title('Ranking das letras que mais aparece no livro')
plt.bar(rotulos,valores)
plt.xlabel('Letras')
plt.ylabel('Frequência')

# adiciona um rótulo centralizado no topo da barra
for i, v in enumerate(valores):
    plt.text(i, v, str(v), color='red', fontweight='bold',horizontalalignment='center',verticalalignment='bottom')
    
plt.show()