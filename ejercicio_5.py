# Ejercicio No. 71: Magnitud o norma euclidiana de un vector.
'''La norma de un vector es representada como la raíz de la suma de sus elementos elevados al
cuadrado.
Hacer el diagrama de flujo y el programa en Python que calcule la magnitud o norma
euclidiana de un vector.
Análisis:
El usuario tiene que ingresar la cantidad n de elementos vacíos que tendrá vector. El primer
ciclo for se encarga de pedirle al usuario el valor de cada elemento de vector, mientras que, en
seguida, el segundo bucle for se encarga de sumar el cuadrado los elementos de vector y
guardándolos en norma, para finalmente obtener su raíz. Por último se imprime el vector
generado y la norma euclidiana norma.'''

#Construcción:

123

norma = 0

# input
n = int(input("Número de elementos del vector: "))

# processing
vector = [None] * n
for i in range(n):
 print("Posición:", i)
 vector[i] = int(input("Valor: "))
for i in range(n):
 norma = norma + vector[i]**2
 norma = norma**0.5

# output
print("Vector generado:", vector)
print("La magnitud del vector es:", norma)