def buscar_en_matriz(matriz, valor):
    for i in range(len(matriz)):  # Recorremos filas
        for j in range(len(matriz[i])):  # Recorremos columnas
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición si se encuentra
    return None  # Retorna None si no se encuentra

# Definir una matriz 3x3
matriz = [
    [5, 8, 2],
    [1, 9, 4],
    [6, 3, 7]
]

# Valor a buscar
valor_buscado = int(input("Ingrese el valor a buscar en la matriz: "))

# Llamamos a la función de búsqueda
resultado = buscar_en_matriz(matriz, valor_buscado)

# Mostrar el resultado
if resultado:
    print(f"El valor {valor_buscado} se encontró en la posición {resultado}")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")