# Presentado por Juan David García Arce

#librerias:
import random

#variables:
numero_secreto = random.randint(1, 10)
numero_usuario = 0
intentos = 0

#codigo:
print("Bienvenido al juego de adivinar el numero secreto entre 1 y 10")
while numero_usuario != numero_secreto:
    numero_usuario = int(input("Ingrese un numero: "))
    intentos = intentos + 1
    if numero_usuario > numero_secreto:
        print("El numero secreto es menor")
    elif numero_usuario < numero_secreto:
        print("El numero secreto es mayor")
    else:
        print("Felicidades, has adivinado el numero secreto")
        print("Te ha tomado", intentos, "intentos")