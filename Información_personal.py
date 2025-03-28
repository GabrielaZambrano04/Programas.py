# Diccionario de información personal
Información_Personal = {
    "nombre": "Roberto Zambrano",
    "edad" : 45,
    "cuidad" : "Cuenca",
    "profesión": "Doctor"

}
# Modificación de valores
Información_Personal["cuidad"]= "Guayaquil"

# Nueva clave-valor para la profesión/especialidad
Información_Personal["especialidad"]="Alergólogo"

# Verificar si existe clave "teléfono", si no , agregarla
if "telefono" not in Información_Personal:
    Información_Personal["telefono"]= "0928110000" # Numero ficticio

# Eliminar clave edad
del Información_Personal["edad"]
print(Información_Personal)