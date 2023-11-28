# Definir el contenido del archivo
contenido = "Hola, este es el contenido del archivo."

# Especificar la ruta de la carpeta
ruta_carpeta = "Ejercicio_1/"

# Especificar el nombre del archivo
nombre_archivo = "archivo.txt"

# Combinar la ruta de la carpeta y el nombre del archivo
ruta_archivo = ruta_carpeta + nombre_archivo

# Abrir el archivo en modo escritura
with open(ruta_archivo, 'w') as archivo:
    # Escribir el contenido en el archivo
    archivo.write(contenido)

print(f"El archivo ha sido guardado en: {ruta_archivo}")
