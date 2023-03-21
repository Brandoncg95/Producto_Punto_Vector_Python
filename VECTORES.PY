import random

# Pedir al usuario la cantidad de números que quiere que tenga cada vector
n = int(input("Ingrese la longitud de los vectores: "))

# Generar dos vectores aleatorios de la misma longitud con valores entre 0 y 10
vector1 = [random.randint(0, 10) for i in range(n)]
print("El primer vector es:", vector1)
vector2 = [random.randint(0, 10) for i in range(n)]
print("El primer vector es:", vector2)

# Calcular el producto punto de los dos vectores
producto_punto = sum([vector1[i] * vector2[i] for i in range(n)])

# Imprimir el resultado
print("El producto punto de los vectores es:", producto_punto)
