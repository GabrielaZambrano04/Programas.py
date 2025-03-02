def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:  # Intercambio si el elemento es mayor que el siguiente
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Definir una matriz 3x3
matriz = [
    [5, 8, 2],
    [1, 9, 4],
    [6, 3, 7]
]

# Mostrar la matriz original
print("Matriz original:")
imprimir_matriz(matriz)

# Seleccionar la fila a ordenar
fila_a_ordenar = int(input("\nIngrese el número de fila que desea ordenar (0-2): "))

if 0 <= fila_a_ordenar < len(matriz):
    # Ordenar la fila seleccionada
    bubble_sort(matriz[fila_a_ordenar])

    # Mostrar la matriz después de ordenar la fila
    print("\nMatriz con la fila ordenada:")
    imprimir_matriz(matriz)
else:
    print("\nNúmero de fila fuera de rango. Intente de nuevo.")