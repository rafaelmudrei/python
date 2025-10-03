num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2


print(f"Soma: {num1} + {num2} = {soma}")
print(f"Subtração: {num1} - {num2} = {subtracao}")
print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")
print(f"divisao: {num1} / {num2} = {divisao}")

if divisao:
    print(f"Divisão: {num1} / {num2} = {divisao}")
else:
    print("Divisão: Não é possível dividir por zero.")