#presentado por Juan David García Arce

#Variables:
factorial = 1
numero = 0

#Codigo:
print("Bienvenido al programa para calcular el factorial de un numero")
numero = int(input("Ingrese un numero: "))

print("El factorial de", numero, "es: ")

#con for:
for i in range(1, numero + 1):
    factorial = factorial * i
print("con for seria: ",factorial)

#con while:
factorial = 1
i = 1
while i <= numero:
    factorial = factorial * i
    i = i + 1
print("con while seria: ",factorial)