# Escritura en el archivo de texto
with open("my_notes.txt", "w") as file:
    file.write("En mi tiempo libre disfruto de escuchar musica\n")
    file.write("Mi grupo favorito es Morat.\n")
    file.write("Mi canción favorita de ellos es: Porfa no te vallas.\n")

# Lectura del archivo línea por línea
with open("my_notes.txt", "r") as file:
    for line in file:  # Leer línea por línea
        print(line.strip())  # Imprimir cada línea sin espacios adicionales

# No es necesario cerrar los archivos explícitamente al usar 'with open()', 
# ya que el bloque 'with' lo maneja automáticamente.