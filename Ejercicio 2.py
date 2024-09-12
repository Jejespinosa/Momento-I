import random

def calcular_salario(base, comision, seguridad_social):
    return base + comision - seguridad_social

def salario_empleados(num_empleados):
    base = float(input("Ingrese el salario del empleado: "))
    comision = float(input("Ingrese la comisión del empleado: "))
    seguridad_social = float(input("Ingrese el valor de la seguridad social del empleado: "))
    empleados = []

    for i in range(num_empleados):
        salario_total = calcular_salario(base, comision, seguridad_social)
        empleados.append(f"Empleado {i + 1}: {salario_total:.2f} USD")
    
    return empleados

num_empleados = 1897
result = salario_empleados(num_empleados)
for empleado in result:
    print(empleado)
