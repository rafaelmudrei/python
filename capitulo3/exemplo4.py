# uma funçao pode chamar outra funcao
def mostrar_nome_inteiro(nome, sobreNome):
    print(nome)
    sobrenome(sobreNome)

def sobrenome(sobrenome):
        print(sobreNome)

nome = "Jose"
sobreNome = "Valim"
mostrar_nome_inteiro(nome, sobreNome)

# cat_twice faz a concatenaçao entre um e dois (parte1 + parte2)
# print_twice imprime as coisas duas vezes
