# A estrutura for serve para executar comandos em que se saibam a quantidade de repetições.
# for 'x' in 'range'

# Exemplo: um programa que determina a soma de todos os números pares desde 100 até 200:

soma1 = 0

for par in range(100, 202, 2):  # se colocar 200, ele somará até 198. Por isso, 202.
    soma1 += par

print(soma1)  # Printa a soma de todos os números pares entre 100 e 200.

# Faça uma função e calcule o valor de 'n', onde 'n' é a soma de divisões sucessivas de 1 até 10.
# n = (1/2) + (1/3) + (1/4) + ... + (1/10)

soma2 = 1

for x in range(1, 10):
    soma2 += (soma2/x)

print(soma2)
