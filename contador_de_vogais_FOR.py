# Dado um texto inserido pelo usuário, informe a quantidade de vogais (a, e, i, o, u)
# print(O texto tem x letras A, x letras B, [...].)
# print(O texto tem x vogais ao total.)

# -*- encoding: UTF-8 -*-
frase = str(input("Digite sua frase ou texto: "))

vogal_a = 0
vogal_e = 0
vogal_i = 0
vogal_o = 0
vogal_u = 0

for vogal in frase:
    if vogal in 'a':
        vogal_a += 1
    if vogal in 'e':
        vogal_e += 1
    if vogal in 'i':
        vogal_i += 1
    if vogal in 'o':
        vogal_o += 1
    if vogal in 'u':
        vogal_u += 1

print("A frase têm {} letras A, {} letras E, {} letras I, {} letras O e {} letras U."
      .format(vogal_a, vogal_e, vogal_i, vogal_o, vogal_u))
print("Sua frase contém {} vogais e, ao total, {} letras."
      .format(vogal_a + vogal_e + vogal_i + vogal_o + vogal_u, len(frase)))
