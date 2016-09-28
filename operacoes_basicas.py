num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

adc = num1 + num2
sub = num1 - num2
div = num1 / num2
multi = num1 * num2


if num1 > num2:
    result1 = "O número {} é maior que o número {}.".format(num1, num2)
elif num1 < num2:
    result1 = "O número {} é maior que o número {}.".format(num2, num1)
else:
    result1 = "Ambos os números digitados são iguais."

if num1 and num2 % 2 == 0:
    result2 = "Ambos os números são pares."
elif num1 % 2 == 0 and num2 % 2 != 0:
    result2 = "O número {} é par e o número {} é ímpar.".format(num1, num2)
elif num2 % 2 == 0 and num1 % 2 != 0:
    result2 = "O número {} é par e o número {} é ímpar.".format(num2, num1)
else:
    result2 = "Ambos os números são ímpares."

print(result1, result2)
print("""O resultado das operações entre os números são os seguintes:\nAdição = {}\nSubtração = {}\
      \nDivisão = {}\nMultiplicação = {}""".format(round(adc, 2), round(sub, 2), round(div, 2), round(multi, 2)))
