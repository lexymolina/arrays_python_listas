# Ejercicio No. 75: Suma de los elementos de la matriz.
'''Análisis:
Después de creada la variable suma = 0 y la matriz M con una lista vacía, el usuario digita el
valor de filas m y columnas n de la matriz, así se genera una matriz por indexación y se
imprime. Luego, se abre un ciclo for en el que:
En cada repetición se tomará una lista (fila) y se sumarán los elementos (columnas) de dicha
fila, guardándolos en suma.
Al finalizar se imprime suma.'''

126

# Construcción:
import random
suma = 0
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
  print(M[k][j], end=" ")
print()
for i in range(m):
 for j in range(n):
  suma = suma + M[i][j]
# output
print("Suma de los elementos de la matriz:", suma)