# Estrutura que permite a repetição de um conjunto de comandos, também conhecidos com "laço" ou "loop".

# A primeira estrutura de repetição do Python é o while. Exemplo:

N = 0

while N < 5:
    print(N)
    N += 1

# O while é mais recomendado quando não se sabe ao certo quatas vezes a repetição será feita,
# pois a condição é um teste booleano qualquer, e não necessariamente uma contagem.
# Com o while, podemos implementar qualquer algoritmo que envolva repetição.

import random
soma = 0
numero = random.randint(1,10)

while numero != 5:
    soma += numero
    numero = random.randint(1,10)

print(soma)

# Outra forma de importar o randint:

from random import randint
contador = 0
soma = 0

while contador < 10:
    numero = randint(1, 5)
    soma += numero
    contador += 1
