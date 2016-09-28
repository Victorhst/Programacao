nota_1 = float(input("Informe a primeira nota: "))
nota_2 = float(input("Informe a segunda nota: "))
media = (nota_1 + nota_2) / 2
print("Sua média é: ", media)

carga_horaria = int(input("Qual a carga horária das disciplinas?: "))
faltas = int(input("Informe o numero de faltas: "))
max_faltas_permitidas = (25/100) * carga_horaria


if media >= 7:
    if faltas < max_faltas_permitidas:
        result = "Aprovado por nota."
    else:
        result = "Reprovado por falta."
elif media >= 4:
    if faltas < max_faltas_permitidas:
        result = "Aguardando final."
    else:
        result = "Reprovado por falta."
else:
    result = "Reprovado por nota."

print(result)
