# Ejercicio No. 72: Producto punto de dos vectores.
'''Sean u = (x, y), v = (a, b) el producto entre u y v está dado por el producto del primer
elemento de u con el primer elemento de v mas el producto del segundo elemento de u con el
segundo elemento de v. En caso de haber más elementos, se continúa esta metodología
sucesivamente.
Hacer el diagrama de flujo y el programa en Python que calcule el producto punto de dos
vectores.
Análisis:
El usuario tiene que ingresar la cantidad n de elementos vacíos que tendrán vector1 y vector2.
Dos ciclos for se encargan de pedirle al usuario el valor de cada elemento de vector1 y
vector2, mientras que, en seguida, el tercer bucle for se encarga de sumar los productos de los
pares de elementos vector1[i]*vector2[i], guardándolos en producto. Por último, se imprimen
los vectores generados y el producto punto producto.'''

# Construcción:
resultado = 0
# input
n = int(input("Número de elementos de los vectores: "))

# processing
vector1 = [None] * n

124
print("Elementos del segundo vector:")
for i in range(n):
 print("Posición:", i)
 vector1[i] = int(input("Valor: "))
 vector2 = [None] * n
print("Elementos del segundo vector:")
for i in range(n):
 print("Posición:", i)
 vector2[i] = int(input("Valor: "))
for i in range(n):
  resultado += vector2[i]*vector1[i]

# output
print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("El producto punto entre los dos vectores es:", resultado)