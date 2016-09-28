# Tupla são conjuntos de variáveis que completarão a string
# Exemplo:

nome = "abacaxi"
caracteristica = "amarelo"
quantidade = 49

# Strings são definidas com "%s" de string, "%f" para números.
print("%s é uma fruta" %(nome))
print("o %s é %s" %(nome, caracteristica))
print("existem %f %ss %ss" %(quantidade, nome, caracteristica))

# Para definir o número de casas decimais após o ponto, usa-se "%z.xf", sendo Z o número de espaço antes de vírgula
# e X o número de caracteres após a vírgula.
print("comi %.7f %ss" %(quantidade, nome))
