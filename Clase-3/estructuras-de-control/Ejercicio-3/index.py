#Presentado por Juan David García Arce

#variables:
frase = ""
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0
suma_vocales = 0

#codigo:
print("Bienvenido al programa para contar las vocales de una frase")
frase = input("Ingrese una frase: ")

for i in frase:
    if i == "a" or i == "A":
        contador_a = contador_a + 1
    elif i == "e" or i == "E":
        contador_e = contador_e + 1
    elif i == "i" or i == "I":
        contador_i = contador_i + 1
    elif i == "o" or i == "O":
        contador_o = contador_o + 1
    elif i == "u" or i == "U":
        contador_u = contador_u + 1

suma_vocales = contador_a + contador_e + contador_i + contador_o + contador_u

print("La frase tiene", contador_a, "letras a")
print("La frase tiene", contador_e, "letras e")
print("La frase tiene", contador_i, "letras i")
print("La frase tiene", contador_o, "letras o")
print("La frase tiene", contador_u, "letras u")

print("La frase tiene", suma_vocales, "vocales en total")