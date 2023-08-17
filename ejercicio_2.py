# Ejercicio No. 68: Suma de los elementos de un vector.
# Análisis:
# Para este ejercicio se define la variable suma con valor 0 y el vector que contendrá 5 elementos. Se introduce un bucle for que se repetirá 5 veces tal que: Se le solicitará al usuario que introduzca un elemento. El elemento que se ha introducido se asignará al índice correspondiente del vector. Se sumará el elemento que se acaba de asignar al vector a suma. Tras ejecutar el bucle for, se imprime por pantalla la suma de todos los elementos del vector.

#Construcción:
suma = 0
vector = [None]*5

# processing
for i in range(5):
 a = int(input("Dame un elemento: "))
 vector[i] = a
 suma += vector[i]

# output
print("La suma de los elementos del vector es:", suma)