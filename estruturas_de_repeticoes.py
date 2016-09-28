# Repetição pré testada

# ENQUANTO (Condição) FAÇA:
#       (bloco de código)
# FIM ENQUANTO

i = 1

while i <= 10:
    print(i)
    i += 1

# Exemplo com mais uma variável somando

i = 1
cont = i

while cont <= 10:
    print(cont)
    cont += 1

# Exemplo com mais uma variável somando

i = 10
cont = i

while cont >= 1:
    print(cont)
    cont -= 1

# Exemplo para printar números pares (==)

num = 0

while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1

# Exemplo para printar números ímpares (!=)

num = 0

while num <= 100:
    if num % 2 != 0:
        print(num)
    num += 1
