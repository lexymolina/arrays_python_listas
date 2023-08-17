# Ejercicio No. 70: Posición del mayor y menor en un vector.
'''Hacer el diagrama de flujo y el programa en Python que lea un vector a de n elementos, que
averigüe e imprima cual es el mayor y el menor, y en qué posición se encuentran.
Análisis:
Se crean las variables mayor y menor, con un número muy grande (como 100^10) y un
número muy pequeño (como -(100^10)), respectivamente. Luego se le pide al usuario el
número n de elementos y se crea una lista vector vacía con ese número. Así entonces se abre
un ciclo for con rango n en el que:
Al empezar, se le pide al usuario el elemento que será guardado en la posición i de vector. Si
ese elemento es mayor a mayor, ese número será el nuevo mayor. Si el número es menor a
menor, ese número será el nuevo menor. En ambas condiciones también se guardan en las
variables pos_mayor y pos_menor las posiciónes que ocuparon los números mayor y menor.

122

Finalmente, se imprime el valor y la posición de los valores máximo y mínimo.'''

# Construcción:
mayor = -(100**10)
menor = 100**10
# input
n = int(input("Número de elementos: "))

# processing
vector = [None]*n
for i in range(n):
 print("Posición", i)
 vector[i] = int(input("Valor: "))
if vector[i] > mayor:
 mayor = vector[i]
pos_mayor = i
if vector[i] < menor:
 menor = vector[i]
pos_menor = i

# output
print("Valor del mayor:", mayor)
print("Posición del mayor:", pos_mayor)
print("Valor del menor:", menor)
print("Posición del menor:", pos_menor)