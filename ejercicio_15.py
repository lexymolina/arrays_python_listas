# Ejercicio No. 81: Suma de todos los elementos periféricos.
'''Análisis:
Después de creada la variable suma = 0 y la matriz M con una lista vacía, el usuario digita el
valor de filas m y columnas n de la matriz, así se genera una matriz por indexación y se
imprime. Luego se abre un ciclo for con rango de 1 a m-1 en el que a suma se le adiciona
M[i][0] + M[i][n-1]. Después, en otro ciclo con n por rango, se hace lo mismo con suma,
pero en este caso es M[0][j] + M[m-1][j].'''
# Construcción:
import random
suma = 0
M = []
# input
m = int(input("Filas de la matriz: "))
n = int(input("Columnas de la matriz: "))
# processing
for i in range(m):

 132

M.append([])
for j in range(n):
 M[i].append(random.randint(1,9))
for k in range(m):
  for j in range(n):
   print(M[k][j], end=" ")
print()
for i in range(1, m-1):
 suma += M[i][0] + M[i][n-1]
for j in range(n):
 suma += M[0][j] + M[m-1][j]
print("Suma de los elementos periféricos de la matriz:", suma) # output