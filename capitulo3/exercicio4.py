def calculaIMC(peso, altura):
    return (peso / altura) ** 2

#main
peso = float(input("digite seu peso:"))
altura = float(input("digite sua altura:"))

imc = calculaIMC(peso, altura)
print("e o seu imc é de:", imc)


