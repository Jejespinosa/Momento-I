import random

def clasificar_funcionamiento(puntuacion):
    if puntuacion == 2:
        return "Funcionamiento defectuoso"
    elif puntuacion == 3:
        return "Funcionamiento moderado"
    elif puntuacion == 4:
        return "Funcionamiento óptimo"

def funcionamiento_cabinas(num_cabinas):
    cabinas = []

    for i in range(num_cabinas):
        puntuacion = random.randint(2, 4)
        clasificacion = clasificar_funcionamiento(puntuacion)
        cabinas.append(f"Cabina {i + 1}: Puntuación {puntuacion} - {clasificacion}")

    return cabinas

# Resultado
num_cabinas = 407
result = funcionamiento_cabinas(num_cabinas)
for cabina in result:
    print(cabina)
