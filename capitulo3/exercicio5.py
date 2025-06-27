def right_justify(palavra, tamanhoPalavra):
    espaco = ' '
    resultado = espaco * (70 - tamanhoPalavra)
    return resultado + palavra

# usando str torna tudo um texto sendo numero ou letras
palavra = str(input("digite uma palavra"))
tamanhoPalavra = len(palavra)

justificado = right_justify(palavra, tamanhoPalavra)
print(justificado)

right_justify(palavra, tamanhoPalavra) # chamada de funcao recebe argumento
