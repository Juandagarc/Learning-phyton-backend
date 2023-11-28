import random
import string

# Función para añadir letras mayúsculas y minúsculas
def agregar_letras(password):
    for _ in range(5):
        # Generar una letra mayúscula o minúscula aleatoria
        letra = random.choice(string.ascii_letters)
        password += letra
    return password

# Función para añadir números
def agregar_numeros(password):
    for _ in range(5):
        # Generar un dígito aleatorio
        digito = random.randint(0, 9)
        password += str(digito)
    return password

# Función para añadir símbolos
def agregar_simbolos(password):
    for _ in range(5):
        # Generar un símbolo aleatorio
        simbolo = random.choice(string.punctuation)
        password += simbolo
    return password

# Función para revolver la contraseña
def revolver_contrasena(password):
    # Convertir la contraseña a una lista
    lista_contraseña = list(password)
    # Revolver la lista
    random.shuffle(lista_contraseña)
    # Dejar solo los primeros 8 caracteres de la lista, el resto se borra
    lista_contraseña = lista_contraseña[:10]
    # Convertir la lista en una cadena
    password = "".join(lista_contraseña)
    return password

# Función para generar la contraseña completa
def generar_contrasena():
    contraseña = ""
    # Añadir letras mayúsculas y minúsculas
    contraseña = agregar_letras(contraseña)
    # Añadir números
    contraseña = agregar_numeros(contraseña)
    # Añadir símbolos
    contraseña = agregar_simbolos(contraseña)
    # Revolver la contraseña
    contraseña = revolver_contrasena(contraseña)
    return contraseña

# Generar la contraseña
contraseña_generada = generar_contrasena()
# Imprimir la contraseña
print(contraseña_generada)
# se imprime la letra 10 de assciletters
# letra = string.ascii_letters[10]
# print(letra)
# Al parecer funciona como un arreglo