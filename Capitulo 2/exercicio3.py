print("tempo do primeiro trecho: 8min e 15seg")
minutoPrimeiroTrecho = 8 * 60
segundoPrimeiroTrecho = 15
print("tempo do primeiro trecho em segundos: ", totalTempoPrimeiroTrecho)

print("tempo do segundo trecho: 7min e 12seg")
minutoSegundoTrecho = (7 * 3) * 60
segundoSegundoTrecho = 12 * 3
print("tempo do segundo trecho em segundos: ", totalTempoSegundoTrecho)

print("tempo do terceiro trecho: 8min e 15seg")
minutoTerceiroTrecho = 8 * 60
segundoTerceiroTrecho = 15
print("tempo do terceiro trecho em segundos: ", totalTempoTerceiroTrecho)

# soma o total de minutos e converte os minutos em segundos
totalTempoTodosTrechos = (minutoPrimeiroTrecho + minutoSegundoTrecho + minutoTerceiroTrecho) / 60

# soma valor total dos segundos
totalTempoTodosTrechos = (segundoPrimeiroTrecho + segundoSegundoTrecho + segundoTerceiroTrecho)

restanteMinutos = int(totalTempoTodosTrechosSegundos/ 60)
restanteSegundos = totalTempoTodosTrechosSegundos % 60

totalMinutos = totalTempoTodosTrechosMinutos + restanteMinutos
totalSegundos = totalTempoTodosTrechosSegundos + restanteSegundos

print("soma de tempo de todos os trechos: ", totalMinutos)
print("soma de tempo de todos os trechos: ", totalSegundos)

print("soma de tempo de todos os trechos: ", totalTempoTodosTrechosMinutos, "minutos")
print("soma de tempo de todos os trechos:", totalTempoTodosTrechosSegundos, "segundos")

horaInicialSegundos = (6 * 60) * 60
minutoInicialSegundos = 52 * 60
horarioInicialSegundos = horaInicialSegundos * minutoInicialSegundos

tempoTrechoMinutosSegundos = totalMinutos * 60

horaChegada = (horaInicialSegundos + tempoTrechoMinutosSegundos) / 60
