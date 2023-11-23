# Presentador por Juan David García Arce

#hallar indice de masa corporal

def hallar_imc(peso, altura):
    return peso / (altura ** 2)

def hallar_clasificacion(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obeso"
    
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en m: "))
imc = hallar_imc(peso, altura)

print(f"Su IMC es {imc} y su clasificación es {hallar_clasificacion(imc)}")