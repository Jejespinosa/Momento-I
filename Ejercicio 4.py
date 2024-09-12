import random

def clasificar_leucemia(puntaje):
    if puntaje < 10:
        return "No tiene Leucemia"
    elif 10 < puntaje <= 40:
        return "Nivel bajo de Leucemia"
    elif 40 < puntaje <= 69:
        return "Nivel moderado de Leucemia"
    elif 70 <= puntaje <= 100:
        return "Nivel grave de Leucemia"

def clasificacion_pacientes(num_pacientes):
    pacientes = []

    for i in range(num_pacientes):
        puntaje = random.randint(0, 100) 
        clasificacion = clasificar_leucemia(puntaje)
        pacientes.append(f"Paciente {i + 1}: Puntaje {puntaje} - {clasificacion}")

    return pacientes

# Resultado
num_pacientes = 803
result = clasificacion_pacientes(num_pacientes)
for paciente in result:
    print(paciente)
