# Escreva um programa que recebe um texto do usuário e conta a quantidade de palavras do texto informado.

# -*- encoding: UTF-8 -*-
texto = str(input("Digite seu texto: "))
indice = 0
palavra = 1

while indice < len(texto):
    if texto[indice] == " ":
        palavra += 1
    indice += 1

print("Esse texto tem {} palavras.".format(palavra))


# se colocar mais de 1 espaço, ele contará errado. Conserte.
