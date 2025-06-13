def calculaDiametro(raio):
    return 2 * raio

def calculaCircuferencia(raio, pi):
    return (2 * raio) * pi

def calculaAreaCircuferencia(pi, raio):
    return pi * (raio ** 2)

#main
raio = int(input("digite o valor do raio:"))
pi = 3.14159

diametro = calculaDiametro(raio)
circuferencia = calculaCircuferencia(raio, pi)
areaCircuferencia = calculaAreaCircuferencia

print("o valor do diametro é", diametro)
print("o valor da circuferencia é", circuferencia)
print("o valor da circuferencia é", areaCircuferencia)