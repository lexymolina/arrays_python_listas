# Ejercicio No. 73: Generación de una matriz.
'''Para crear una matriz en Python se usan listas dentro de una lista y se comprende en que
dentro de la lista principal: la primera lista es la fila 0, la segunda es la fila 1 y así
sucesivamente. En este ejercicio se busca crear una matriz 3 x 3 y se busca imprimirla en
pantalla como las matrices que conocemos.
Análisis:
Después de creada la matriz M con tres listas en las que cada una contiene tres elementos, se
abre un ciclo for con un rango de 3 tal que:
En cada repetición se tomará una lista (fila), se imprimirán los elementos (columnas) de dicha
fila y se hará un salto de línea.'''

# Construcción:
M = [[1,2,3], [4,5,6], [7,8,9]]

# processing
for i in range(3):
 for j in range(3):
  print(M[i][j], end=" ")
print() # output