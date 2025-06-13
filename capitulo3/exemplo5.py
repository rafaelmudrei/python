 # cat_twice faz a concatenaçao entre um e dois (parte1 + parte2)
def concatena_texto(texto1, texto2):
    texto_inteiro = texto1 + texto2
    imprime_2_vezes(texto_inteiro)

# print_twice imprime as coisas duas vezes
def imprime_2_vezes(texto_inteiro):
    print(texto_inteiro)
    print(texto_inteiro)

texto1 = "agua mole pedra dura"
texto2 = "tanto bate ate que fura"

concatena_texto(texto1, texto2)
