# Ejercicio No. 69: Promedio salarial de una empresa.
'''Una empresa tiene 250 empleados, por cada uno de ellos tenemos un registro que trae
grabado dos datos, el nombre del empleado y su correspondiente salario mensual. Hacer el
diagrama de flujo y el programa en Python que averigua e imprima, cuántos empleados ganan
más del promedio salarial de la empresa.
Análisis:
Para este ejercicio se crean las variables empleados, salarios, ps y resultado. Entonces se
implementa un ciclo for en un rango de 5 tal que:
Se le pide al usuario el nombre y salario de un empleado, asignando esa entrada a empleados
y salarios, respectivamente; A la variable ps, encargada del promedio salarial, se le sumará el
valor que haya adquirido salarios en esa misma iteración.
Al acabar este ciclo, la variable ps es dividida en 5, esto para promediar los salarios.

121

Para saber cuántos empleados ganan más del promedio salarial de la empresa, comenzamos
otro ciclo for en el que se verifica si cada elemento de salarios es mayor que ps, y, de ser así,
la variable resultado aumenta en 1.
Al finalizar se imprime resultado, que es ese número de empleados con un salario mayor que
el promedio.'''


# Construcción:
salarios = [None]*5
empleados = [None]*5
ps = 0
resultado = 0

# processing
for i in range(5):
 empleados[i] = input("Nombre de empleado: ")
 salarios[i] = int(input("Salario de empleado: "))
 ps += salarios[i]
 ps = ps / 5
for i in range(5):
 if salarios[i] > ps:
  resultado += 1

# output
print("Número de empleados que ganan más del ps:", resultado)