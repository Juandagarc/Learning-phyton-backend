# Presentado por Juan David García Arce

# variables:
arreglo = []

# codigo:
# deja ingresar nombres de productos hasta ingresar la palabra salir
while True:
    producto = input("Ingrese un producto: ")
    if producto == "salir":
        break
    arreglo.append(producto)
    arreglo = list(set(arreglo))

# imprime el arreglo
print(arreglo)