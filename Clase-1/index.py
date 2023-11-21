# tic tac toe game

posiciones_puntaje = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

jugador = 1

turno = 1

def imprimir_tic_tac_toe(matriz):
    cont = 0
    for fila in matriz:
        print(f" {fila[0]} │ {fila[1]} │ {fila[2]}")
        cont += 1
        if cont <= 2:
            print("───┼───┼───")

def validar_posicion (fila, columna):
    if fila > 2 or fila < 0:
        return False
    if columna > 2 or columna < 0:
        return False
    if posiciones_puntaje[fila][columna] != " ":
        return False
    return True


def cambiar_turno (jugador):
    if jugador == 1:
        return 2
    else:
        return 1

def ingresar_posicion (matriz, jugador):
    columna = int(input("Ingrese la columna: "))
    fila = int(input("Ingrese la fila: "))
    if validar_posicion(fila - 1, columna - 1):
        if jugador == 1:
            matriz[fila - 1][columna - 1] = "X"
        else:
            matriz[fila - 1][columna - 1] = "O"
    else:
        print("Posición no válida")
        ingresar_posicion(matriz, jugador)

def hallar_ganador (matriz):
    for fila in matriz:
        if fila[0] == fila[1] == fila[2] != " ":
            return fila[0]
    for i in range(3):
        if matriz[0][i] == matriz[1][i] == matriz[2][i] != " ":
            return matriz[0][i]
    if matriz[0][0] == matriz[1][1] == matriz[2][2] != " ":
        return matriz[0][0]
    if matriz[0][2] == matriz[1][1] == matriz[2][0] != " ":
        return matriz[0][2]
    return 0


def jugar(turno, matriz, jugador):
    while turno <= 9:
        print(f"Turno {turno}")
        ingresar_posicion(matriz, jugador)
        imprimir_tic_tac_toe(matriz)
        turno += 1
        ganador = hallar_ganador(matriz)
        if ganador != 0:
            print(f"El ganador es el jugador {jugador}")
            break
        else:
            jugador = cambiar_turno(jugador)

jugar(turno, posiciones_puntaje, jugador)
