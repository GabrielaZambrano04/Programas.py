def calcular_temperatura_promedio(datos_temperatura):
    """
    Calcula la temperatura promedio de cada ciudad a partir de un diccionario de temperaturas semanales.

    :param datos_temperatura: Diccionario con el formato:
                              {
                                  "Ciudad1": [[semana1], [semana2], [semana3], [semana4]],
                                  "Ciudad2": [[semana1], [semana2], [semana3], [semana4]],
                                  ...
                              }
    :return: Diccionario con la temperatura promedio de cada ciudad.
    """
    promedios = {}
    
    for ciudad, semanas in datos_temperatura.items():
        # Lista para almacenar todas las temperaturas de la ciudad
        temperaturas_ciudad = [temp for semana in semanas for temp in semana]
        
        # Calcular el promedio de la ciudad
        promedio = sum(temperaturas_ciudad) / len(temperaturas_ciudad)
        promedios[ciudad] = round(promedio, 2)  # Redondear a dos decimales
    
    return promedios


# Datos de prueba: 3 ciudades, 4 semanas de temperaturas diarias
datos_temperatura = {
    "Quito": [
        [15, 16, 14, 15, 17, 16, 15],  # Semana 1
        [16, 17, 15, 16, 18, 17, 16],  # Semana 2
        [14, 15, 13, 14, 16, 15, 14],  # Semana 3
        [15, 16, 14, 15, 17, 16, 15],  # Semana 4
    ],
    "Guayaquil": [
        [28, 29, 30, 28, 29, 30, 31],  # Semana 1
        [30, 31, 29, 30, 32, 31, 30],  # Semana 2
        [28, 29, 27, 28, 30, 29, 28],  # Semana 3
        [29, 30, 28, 29, 31, 30, 29],  # Semana 4
    ],
    "Cuenca": [
        [12, 13, 14, 12, 13, 14, 15],  # Semana 1
        [13, 14, 12, 13, 15, 14, 13],  # Semana 2
        [11, 12, 10, 11, 13, 12, 11],  # Semana 3
        [12, 13, 11, 12, 14, 13, 12],  # Semana 4
    ]
}

# Prueba de la función
resultados = calcular_temperatura_promedio(datos_temperatura)
print("Temperatura promedio por ciudad:", resultados)