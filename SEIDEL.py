import numpy as np

def gauss_seidel(matriz, vector, aproximacion_inicial, tolerancia, max_iteraciones):
    n = len(vector)  # Número de variables
    x = np.copy(aproximacion_inicial)  # Copiar la aproximación inicial al vector solución
    for iteracion in range(max_iteraciones):
        x_anterior = np.copy(x)  # Guardar los valores anteriores para verificar la convergencia
        for i in range(n):
            suma = sum(matriz[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (vector[i] - suma) / matriz[i][i]

        # Verificar la convergencia
        if np.allclose(x, x_anterior, atol=tolerancia):
            print(f"Converge en {iteracion + 1} iteraciones")
            return x
        
    print("Se alcanzó el número máximo de iteraciones sin convergencia")
    return x

# Entrada
tamanio_sistema = int(input("Ingresa el tamaño del sistema: "))
A = np.zeros((tamanio_sistema, tamanio_sistema))
b = np.zeros(tamanio_sistema)

print("Ingresa los coeficientes de la matriz A:")
for i in range(tamanio_sistema):
    A[i] = [float(x) for x in input().split()]

print("Ingresa los términos del vector b:")
for i in range(tamanio_sistema):
    b[i] = float(input())

valores_iniciales = [float(x) for x in input("Ingresa la solución inicial (separada por espacios): ").split()]
tol = float(input("Ingresa la tolerancia: "))
max_iter = int(input("Ingresa el número máximo de iteraciones: "))

# Llamar al método de Gauss-Seidel
solucion = gauss_seidel(A, b, valores_iniciales, tol, max_iter)

# Mostrar la solución
print(f"Solución aproximada: {solucion}")
