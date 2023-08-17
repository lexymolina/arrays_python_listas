# Ejercicio No. 76: Suma de los elementos de la diagonal principal.
'''Análisis:
Después de creada la variable suma = 0 y la matriz M con una lista vacía, el usuario digita el
valor de filas m y columnas n de la matriz, así se genera una matriz por indexación y se
imprime. Luego, si el número de filas es igual al número de columnas se abre un ciclo for en
el que:
En cada repetición se recorre la matriz y, si la fila actual es igual a la columna actual, al valor
de suma se le adiciona el elemento de M de esa posición. Entonces se imprime suma.
De lo contrario, se dice que no existe una diagonal principal.'''

# Construcción:

127

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
if m == n:
 for i in range(m):
  for j in range(n):
   if i == j:
    suma = suma + M[i][j]
 print("Resultado de la traza:", suma) # output
else:
 print("No existe una diagonal principal") # output