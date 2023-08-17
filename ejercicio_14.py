# Ejercicio No. 80: Elementos pares e impares de la matriz.
'''Crear e imprimir 2 vectores así: El vector b que tenga todos los números pares de la matriz, y
el vector c que tenga los números impares.
Análisis:
Después de creadas las listas vacías b, c y M; el usuario digita el valor de filas m y columnas n
de la matriz, así se genera una matriz por indexación y se imprime. Luego se abre un ciclo for
en el que:
En cada repetición se recorre la matriz y, si el módulo de M[i][j] es igual a cero, entonces a b
se le agrega ese valor par de M. De lo contrario, el valor es adicionado a c.'''

# Construcción:
import random
b = []
c = []
M = []
# input
m = int(input("Filas de la matriz: "))

131
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
  if M[i][j] % 2 == 0:
   b.append(M[i][j])
else:
 c.append(M[i][j])

# output
print("Elementos pares de la matriz:", b)
print("Elementos impares de la matriz:", c)