# Ejercicio No. 74: Generación de una matriz por indexación.
'''Análisis:
Después de creada la matriz M con una lista vacía, el usuario digita el valor de filas m y
columnas n de la matriz, entonces se abre un ciclo for con un rango de m tal que:
En cada repetición se le adicionará a M una nueva lista (fila) y se le agregarán n números
aleatorios entre el 1 y el 9 a dicha fila.
Para imprimir la lista se abre otro bucle for en el que en cada repetición se tomará una lista
(fila), se imprimirán los elementos (columnas) de dicha lista y se hará un salto de línea.'''

# Construcción:
import random
M = []
# input
m = int(input("Filas de la matriz: "))
n = int(input("Columnas de la matriz: "))
# processing
for i in range(m):
 M.append([])
for j in range(n):
 M[i].append(random.randint(1,9))
for k in range(m):
 for j in range(n):
  print(M[k][j], end=" ") # output
print()