def maiorNumero(numero1, numero2, numero3):
    if(numero1 > numero2):
        if(numero1 > numero3):
            print(f"o primeiro numero é o maior numero.")

    elif(numero2 > numero3):
        print(f"o segundo numero é o maior numero.")
    else:
        print("o terceiro numero é o maior numero")


numero1 = int(input("digite um numero"))
numero2 = int(input("digite um numero"))
numero3 = int(input("digite um numero"))

maiorNumero(numero1, numero2, numero3)