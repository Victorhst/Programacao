# Escreva um programa que recebe um texto do usuário e conta a quantidade de palavras do texto informado.

# -*- encoding: UTF-8 -*-
texto = str(input("Digite seu texto: "))
contador = 1

for palavras in texto:
    texto.replace('  ', ' ')
    if palavras in " ":
        contador += 1

print('Esse texto tem {} palavras.'.format(contador))
