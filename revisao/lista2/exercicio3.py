#def para definir o resultado da soma dos quatro numeros,  que foi pedido no argumento abaixo
def calculaSoma(num1, num2, num3, num4):
    soma = (num1 + num2 + num3 + num4) - 10
    print(f"a soma dos quatro numero é:", soma)

#para chamar os numeros
num1 = int(input("digite o primeiro numero"))
num2 = int(input("digite o segundo numero"))
num3 = int(input("digite o terceiro numero"))
num4 = int(input("digite o quarto  numero"))



# usado como um argumento
calculaSoma(num1, num2, num3, num4)