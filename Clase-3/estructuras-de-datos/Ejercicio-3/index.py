# Diccionario de Sinónimos: Implementa un pequeño diccionario de sinónimos, donde el usuario puede ingresar una palabra y obtener sinónimos de esa palabra.

# Presentado por: Juan David García Arce

# variables:
diccionario = {
    "perro": ["can", "chucho", "tuso", "choco"],
    "gato": ["michi", "michino", "michifuz"],
    "pajaro": ["ave", "pajarito", "pajarillo", "pájaro"],
    "pez": ["pescado", "pescadito", "pescadillo", "pescadote"],
    "oso": ["osito", "osote", "osazo", "osazo"],
    "vaca": ["vaca", "vaca", "vaca", "vaca"],
    "caballo": ["caballo", "caballo", "caballo", "caballo"],
    "oveja": ["oveja", "oveja", "oveja", "oveja"],
    "cerdo": ["cerdo", "cerdo", "cerdo", "cerdo"],
    "conejo": ["conejo", "conejo", "conejo", "conejo"],
    "raton": ["ratón", "ratón", "ratón", "ratón"],
    "serpiente": ["serpiente", "serpiente", "serpiente", "serpiente"],
    "tortuga": ["tortuga", "tortuga", "tortuga", "tortuga"],
    "cocodrilo": ["cocodrilo", "cocodrilo", "cocodrilo", "cocodrilo"],
    "tiburon": ["tiburón", "tiburón", "tiburón", "tiburón"],
    "ballena": ["ballena", "ballena", "ballena", "ballena"],
    "delfin": ["delfín", "delfín", "delfín", "delfín"],
    "rana": ["rana", "rana", "rana", "rana"],
    "pato": ["pato", "pato", "pato", "pato"],
    "aguila": ["águila", "águila", "águila", "águila"],
    "gallina": ["gallina", "gallina", "gallina", "gallina"],
    "aguila": ["águila", "águila", "águila", "águila"]
}




# codigo:

# imprime solo el nombre de las listas
def imprimir_lista():
    print("Lista de animales: ")
    for i in diccionario:
        print(i)

# un while true para que se repita el programa y pregunta cual sinonimo quiere  ver
while True:
    imprimir_lista()
    animal = input("Ingrese el nombre de un animal: ")
    if animal in diccionario:
        print("Sinónimos de " + animal + ": ")
        for i in diccionario[animal]:
            print(i)
    else:
        print("No existe ese animal en el diccionario")
    salir = input("¿Desea salir? (si/no): ")
    if salir == "si":
        break
