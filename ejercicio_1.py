# Ejercicio No. 67: Vector con números aleatorios.
# Análisis:
# En este ejercicio se importa la librería random y se asigna el valor de None a todos los espacios del vector x. Luego ingresa a un ciclo for realizando 10 iteraciones, en cada una se le asigna un valor aleatorio de entre 0 y 1 a x y se imprime cada valor.

# Construcción:
import random
x = [None]*10
# processing
for i in range(10):
 x[i] = random.random()
 print(x[i]) # output
 