
def removePrimeiroDigito(numero):
    return numero // 10000

def removeSegundoDigito(numero):
    return (numero % 10000 ) // 1000

def removeTerceiroDigito(numero):
    return (numero % 1000) // 100

def removeQuartoDigito(numero):
    return (numero % 100) // 10

def removeQuintoDigito(numero):
    return numero % 10
#main
numero = int(input("entre com um numero de 5 digitos"))

primeiro_digito = removePrimeiroDigito(numero)
segundo_digito = removeSegundoDigito(numero)
terceiro_digito = removeTerceiroDigito(numero)
quarto_digito = removeQuartoDigito(numero)
quinto_digito = removeQuintoDigito(numero)

print(primeiro_digito)
print(segundo_digito)
print(terceiro_digito)
print(quarto_digito)
print(quinto_digito)

