peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)

if imc <= 18.5:
    result = "magreza"

elif imc <= 24.9:
    result = "peso normal"

elif imc <= 29.9:
    result = "sobre peso"

elif imc <= 34.9:
    result = "obesidade de grau I"

elif imc <= 39.9:
    result = "obesidade de grau II"

else:
    result = "obesidade de grau III"

print("Teu IMC é %2.1f e indica %s" % (imc, result))
