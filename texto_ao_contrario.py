# Escreva um programa que recebe um texto do usuário e o imprime ao contrário

texto = input(str("Digite um texto: "))
indice = len(texto) - 1
textoinvertido = ""

while indice >= 0:
    textoinvertido += texto[indice]
    indice -= 1

print(textoinvertido)
