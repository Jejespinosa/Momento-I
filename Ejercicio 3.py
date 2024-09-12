def pares_impares(cuente_num):
    pares = 0
    impares = 0
    resultados = []

    for _ in range(cuente_num):
        numero = int(input("Ingrese un número: "))
        if numero % 2 == 0:
            resultados.append(f"{numero} es par")
            pares += 1
        else:
            resultados.append(f"{numero} es impar")
            impares += 1

    return resultados, pares, impares

# Resultado
cuente_num = 400
resultados, pares, impares = pares_impares(cuente_num)

for resultado in resultados:
    print(resultado)

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
