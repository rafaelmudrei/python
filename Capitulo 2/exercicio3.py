# Definindo o tempo de cada trecho
print("tempo do primeiro trecho: 8min e 15seg")
minutoPrimeiroTrecho = 8 * 60  # Convertendo para segundos
segundoPrimeiroTrecho = 15
totalTempoPrimeiroTrecho = minutoPrimeiroTrecho + segundoPrimeiroTrecho  # Total em segundos
print("tempo do primeiro trecho em segundos: ", totalTempoPrimeiroTrecho)

print("tempo do segundo trecho: 7min e 12seg")
minutoSegundoTrecho = (7 * 3) * 60  # Convertendo para segundos
segundoSegundoTrecho = 12 * 3
totalTempoSegundoTrecho = minutoSegundoTrecho + segundoSegundoTrecho  # Total em segundos
print("tempo do segundo trecho em segundos: ", totalTempoSegundoTrecho)

print("tempo do terceiro trecho: 8min e 15seg")
minutoTerceiroTrecho = 8 * 60  # Convertendo para segundos
segundoTerceiroTrecho = 15
totalTempoTerceiroTrecho = minutoTerceiroTrecho + segundoTerceiroTrecho  # Total em segundos
print("tempo do terceiro trecho em segundos: ", totalTempoTerceiroTrecho)

# Somando todos os tempos em segundos
totalTempoTodosTrechosSegundos = totalTempoPrimeiroTrecho + totalTempoSegundoTrecho + totalTempoTerceiroTrecho

# Convertendo o total de segundos de volta para minutos e segundos
restanteMinutos = totalTempoTodosTrechosSegundos // 60
restanteSegundos = totalTempoTodosTrechosSegundos % 60

# Exibindo o resultado total
print("Soma do tempo de todos os trechos: ", restanteMinutos, "minutos e", restanteSegundos, "segundos")

# Hora inicial em segundos (6h52min)
horaInicialSegundos = (6 * 60 * 60) + (52 * 60)

# Hora de chegada
horaChegadaSegundos = horaInicialSegundos + totalTempoTodosTrechosSegundos

# Convertendo hora de chegada de segundos para hora, minuto e segundo
horaChegadaHoras = horaChegadaSegundos // 3600
horaChegadaSegundosRestante = horaChegadaSegundos % 3600
horaChegadaMinutos = horaChegadaSegundosRestante // 60
horaChegadaSegundosFinal = horaChegadaSegundosRestante % 60

# Exibindo o horário de chegada
print(f"A hora de chegada será: {horaChegadaHoras}:{horaChegadaMinutos:02d}:{horaChegadaSegundosFinal:02d}")
