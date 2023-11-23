# Presentado por Juan David García Arce

def fareheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_fareheit(c):
    return (c * 9/5) + 32

print("Que desea realizar?")
print("1. Convertir de Fareheit a Celsius")
print("2. Convertir de Celsius a Fareheit")

opcion = int(input("Ingrese la opción: "))

if opcion == 1:
    f = float(input("Ingrese la temperatura en Fareheit: "))
    print(f"{f} Fareheit son {fareheit_to_celsius(f)} Celsius")
elif opcion == 2:
    c = float(input("Ingrese la temperatura en Celsius: "))
    print(f"{c} Celsius son {celsius_to_fareheit(c)} Fareheit")