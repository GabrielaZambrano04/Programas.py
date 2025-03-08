# Definir las ciudades, días de la semana y número de semanas
ciudades = ["Quito", "Guayaquil", "Cuenca", "Ambato"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 4

# Crear la matriz 3D manualmente con temperaturas aleatorias (entre 10°C y 35°C)
import random

# Inicializamos la matriz con 0
temperaturas = [[[random.randint(10, 35) for dia in range(len(dias_semana))] for semana in range(num_semanas)] for ciudad in range(len(ciudades))]

# Calcular y mostrar el promedio de temperaturas por ciudad y por semana usando bucles anidados
for ciudad in range(len(ciudades)):
    print(f"Promedio de temperaturas para {ciudades[ciudad]}:")
    for semana in range(num_semanas):
        suma_temperaturas = 0
        for dia in range(len(dias_semana)):
            suma_temperaturas += temperaturas[ciudad][semana][dia]
        promedio = suma_temperaturas / len(dias_semana)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")