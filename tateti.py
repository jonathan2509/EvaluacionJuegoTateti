#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

TURNO = {0: 'La computadora va', 1: 'Vas'}
CELDAS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def dibujarTabla(tabla):
    """ Esta función dibuja una tabla con los valores seleccionados por el usuario 
    y por la computadora.
    Contiene una lista con los valores seleccionados, por default es una lisa de 
    diez elemenos con un espacio como valor.
    """
    opEmptyRow = ' ' * 7
    emptyRow = ' ' * 8
    print('7' + opEmptyRow + '*8' + opEmptyRow + '*9' + opEmptyRow)
    print('    ' + tabla[7] + '   *    ' + tabla[8] + '   *    ' + tabla[9] + '    ')
    print(emptyRow + '*' + emptyRow + '*' + emptyRow)
    print('********+********+********')
    print('4' + opEmptyRow + '*5' + opEmptyRow + '*6' + opEmptyRow)
    print('    ' + tabla[4] + '   *    ' + tabla[5] + '   *    ' + tabla[6] + '    ')
    print(emptyRow + '*' + emptyRow + '*' + emptyRow)
    print('********+********+********')
    print('1' + opEmptyRow + '*2' + opEmptyRow + '*3' + opEmptyRow)
    print('    ' + tabla[1] + '   *    ' + tabla[2] + '   *    ' + tabla[3] + '    ')
    print(emptyRow + '*' + emptyRow + '*' + emptyRow)

def SeleccionarLetraJugador():
    """
        Le da la opcion al jugador de elegir que desea ser.
        Esta lista contiene dos elementos, en primer lugar la letra del jugador y en segundo la de computadora.
    """
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        print('¿Deseas ser X o O?')
        letra = input().upper()
    if letra == 'X':
    	return ['X', 'O']
    else: 
    	return ['O', 'X']

def inicioAleatorio():
    return random.randint(0, 1)

def JugarDeNuevo():
    """Consulta al jugador si quiere jugar nuevamente.
   	   Devuelve True en caso del que el  jugador haya seleccionado "S" o "SI" y False
   	   en caso de selccionar cualquier otra letra.
    """
    print('¿Quieres jugar de nuevo? (sí/no)?')
    return input().lower().startswith('s')

def hacerMovimiento(tabla, letra, move):
    tabla[move] = letra

def esGanador(tabla, letra):
    """ Aqui se hace la verificación si ganó, dado los valores de la tabla
    y una letra. Devuelve verdadero si se da alguna de estas combinaciones.
    Sino False.
    """
    hTop = (tabla[7] == letra and tabla[8] == letra and tabla[9] == letra) # Horizontal superior.
    hMiddle = (tabla[4] == letra and tabla[5] == letra and tabla[6] == letra) # Horizontal medio.
    hBottom = (tabla[1] == letra and tabla[2] == letra and tabla[3] == letra) # Horizontal inferior.
    vLeft = (tabla[7] == letra and tabla[4] == letra and tabla[1] == letra) # Vertical izquierda.
    vCenter = (tabla[8] == letra and tabla[5] == letra and tabla[2] == letra) # Vertical centro.
    vRight = (tabla[9] == letra and tabla[6] == letra and tabla[3] == letra) # Vertical derecha.
    xTopDiagonal = (tabla[9] == letra and tabla[5] == letra and tabla[1] == letra) # Diagonal superior izquierda
    xBottomDiagonal = (tabla[7] == letra and tabla[5] == letra and tabla[3] == letra) # Diagonal inferior izquierda
    return (hTop or hMiddle or hBottom or vLeft or vCenter or vRight or xTopDiagonal or xBottomDiagonal)

def tablaDuplicada(tabla):
    """Duplica la tabla original y devuelve el duplicado de la lista original.
    """
    return [celda for celda in tabla]

def espacioLibre(tabla, move):
    """Evalúa si la celda esta disponible, devuelve true en caso de que haya espacio.
    Sino false.
    """
    return tabla[move] == ' '

def movimientoJugador(tabla):
    """Permite al jugador ingresar su jugada, esta devuelve el siguiente moviento 
    del jugador.
    """
    move = ' '
    while True:
        print('¿Cuál es tu próxima jugada? (1-9)')
        move = input()
        if move not in CELDAS or not espacioLibre(tabla, int(move)):
            move = ' '
            print("Tienes que elegir una opción válida!!")
        else:
            break
    return int(move)

def seleccionAleatoria(tabla, plays):
    """Selecciona una jugada aleatoria, de una lista de jugadas. Si el espacio 
    esta disponible, se agrega a la lista de posibilidades.
    Si hay alguna posibilidad la devuelve, caso contrario no.
    """
    possibilities = [i for i in plays if espacioLibre(tabla, i)]
    if len(possibilities):
        return random.choice(possibilities)
    return None

def posibilidadWinner(tabla, letra):
    """Este metodo predice el próximo movimiento correcto.
    Devuelve el siguiente movimiento, el ganador o el que bloquea.  
    """
    celda = 0
    for i in range(1, 10):
        copytabla = tablaDuplicada(tabla)
        if espacioLibre(copytabla, i):
            hacerMovimiento(copytabla, letra, i)
            if esGanador(copytabla, letra):
                celda = i
    return celda

def movimientoComputadora(tabla, letraComputadora, letraJugador):
    """Este metodo haceuna simulación de Inteligencia Artificial.
    Decide los movimiento a realizar a partir de los siguientes pasos.
    Primero, evalua si tiene la posibilidad de ganar en el siguiente paso, 
    si esto es posible, lo hace.
    Segundo, si el otro jugador puede ganar con el próximo moviento, lo bloquea.
    Tercero, si algunas de las esquinas se encuentra libre, las ocupa.
    Cuarto, evalúa si el centro se encuentra vacio para ocuparlo.
    Quinto, evalúa si alguno de los lados se encuentra libre para ocuparlo.
    Devuelve el singuiente movimiento de la computadora.
    """
    move = posibilidadWinner(tabla, letraComputadora)
    if move: return move
    move = posibilidadWinner(tabla, letraJugador)
    if move: return move
    move = seleccionAleatoria(tabla, [1, 3, 7, 9])
    if move is not None: return move
    if espacioLibre(tabla, 5): return 5
    return seleccionAleatoria(tabla, [2, 4, 6, 8])

def tablaCompleta(tabla):
    """
        Descripción: Evalúa si la tabla fue completada o no.
        Retorna:
            1 - True en caso de que esté completa, en caso de que haya al menos una celda
                vacía retorna False.
    """
    auxtabla = list()
    for i, celda in enumerate(tabla):
        if not i:
            continue
        auxtabla.append(celda)
    return all(celda in ['X', 'O'] for celda in auxtabla)

def finJuego(tabla, juegoEnCurso, message):
    dibujarTabla(tabla)
    print(message)
    juegoEnCurso = False
    return juegoEnCurso

print('Inciando Juego Ta-Te-Ti')
jugar = True
while jugar:
    letraJugador, letraComputadora = SeleccionarLetraJugador()
    turno = inicioAleatorio()
    print(TURNO.get(turno) + ' primero.')
    juegoEnCurso = True
    tabla = [' '] * 10
    while juegoEnCurso:
        if turno:
            ###Turno del jugador
            dibujarTabla(tabla)
            move = movimientoJugador(tabla)
            hacerMovimiento(tabla, letraJugador, move)
            if esGanador(tabla, letraJugador):
                juegoEnCurso = finJuego(tabla, juegoEnCurso, 'Eres el Ganador!!')
            elif tablaCompleta(tabla):
                juegoEnCurso = finJuego(tabla, juegoEnCurso, 'El juego termina en empate...')
            turno = 0
        else:
            ###Turno de la computadora
            move = movimientoComputadora(tabla, letraComputadora, letraJugador)
            hacerMovimiento(tabla, letraComputadora, move)
            if esGanador(tabla, letraComputadora):
                juegoEnCurso = finJuego(tabla, juegoEnCurso, 'La computadora te ha Ganado!!')
            elif tablaCompleta(tabla):
                juegoEnCurso = finJuego(tabla, juegoEnCurso, 'El juego termina en empate...')
            turno = 1
    if not JugarDeNuevo():
        jugar = False

