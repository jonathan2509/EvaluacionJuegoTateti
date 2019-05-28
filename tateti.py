#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

CELLS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
TURN = {0: 'La computadora va', 1: 'Vas'}

def printTable(table):
    """
        Descripción: Función que dibuja una tabla con los valores seleccionados tanto
                     por el usuario como por la computadora.
        Parámetros:
            1 - table: Contiene una lista con los valores seleccionados. Por defecto es
                       una lista de 10 elementos con un espacio como valor.
    """
    opEmptyRow = ' ' * 7
    emptyRow = ' ' * 8
    print '1' + opEmptyRow + '*2' + opEmptyRow + '*3' + opEmptyRow
    print '    ' + table[1] + '   *    ' + table[2] + '   *    ' + table[3] + '    '
    print emptyRow + '*' + emptyRow + '*' + emptyRow
    print '********+********+********'
    print '4' + opEmptyRow + '*5' + opEmptyRow + '*6' + opEmptyRow
    print '    ' + table[4] + '   *    ' + table[5] + '   *    ' + table[6] + '    '
    print emptyRow + '*' + emptyRow + '*' + emptyRow
    print '********+********+********'
    print '7' + opEmptyRow + '*8' + opEmptyRow + '*9' + opEmptyRow
    print '    ' + table[7] + '   *    ' + table[8] + '   *    ' + table[9] + '    '
    print emptyRow + '*' + emptyRow + '*' + emptyRow

def SeleccionarLetraJugador():
    """
        Le da la opcion al jugador de elegir que desea ser.
        Esta lista contiene dos elementos, en primer lugar la letra del jugador y en segundo la de computadora.
    """

    """
        Descripción: Función que brinda al jugador la posibilidad de seleccionar la letra
                     que desea ser.
        Retorna:
            1 - Una lista que contiene dos elementos. El primero la letra del jugador y el
                segundo la letra de la computadora.
    """
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        print '¿Deseas ser X o O?'
        letra = raw_input().upper()
    if letra == 'X':
    	return ['X', 'O']
    else: 
    	return ['O', 'X']

def randomStart():
    return random.randint(0, 1)

def JugarDeNuevo():
    """Consulta al jugador si quiere jugar nuevamente.
   	   Devuelve True en caso del que el  jugador haya seleccionado "S" o "SI" y False
   	   en caso de selccionar cualquier otra letra.
    """
    print '¿Quieres jugar de nuevo? (sí/no)?'
    return raw_input().lower().startswith('s')

def makeMove(table, letra, move):
    table[move] = letra

def esGanador(table, letra):
    """
        Descripción: Dados los valores de la tabla y una letra, verifica si ganó o no.
        Retorna:
            1 - True si ganó con alguna de las posibles combinaciones, en caso contrario False.
    """
    hTop = (table[7] == letra and table[8] == letra and table[9] == letra) # Horizontal superior.
    hMiddle = (table[4] == letra and table[5] == letra and table[6] == letra) # Horizontal medio.
    hBottom = (table[1] == letra and table[2] == letra and table[3] == letra) # Horizontal inferior.
    vLeft = (table[7] == letra and table[4] == letra and table[1] == letra) # Vertical izquierda.
    vCenter = (table[8] == letra and table[5] == letra and table[2] == letra) # Vertical centro.
    vRight = (table[9] == letra and table[6] == letra and table[3] == letra) # Vertical derecha.
    xTopDiagonal = (table[9] == letra and table[5] == letra and table[1] == letra) # Diagonal superior izquierda
    xBottomDiagonal = (table[7] == letra and table[5] == letra and table[3] == letra) # Diagonal inferior izquierda
    return (hTop or hMiddle or hBottom or vLeft or vCenter or vRight or xTopDiagonal or xBottomDiagonal)

def duplicateTable(table):
    """
        Descripción: Duplica la tabla original.
        Retorna:
            1 - Duplicado de la lista original.
    """
    return [cell for cell in table]

def hasFreeSpace(table, move):
    """
        Descripción: Función que evalúa si la celda está disponible o no.
        Retorna:
            1 - True en el caso de que haya espacio y False en caso contrario.
    """
    return table[move] == ' '

def getPlayerMove(table):
    """
        Descripción: Permite al jugador ingresar su jugada.
        Retorna:
            1 - El siguiente movimiento del jugador.
    """
    move = ' '
    while True:
        print '¿Cuál es tu próxima jugada? (1-9)'
        move = raw_input()
        if move not in CELLS or not hasFreeSpace(table, int(move)):
            move = ' '
            print("¡Elegí una opción válida!")
        else:
            break
    return int(move)

def selectRandom(table, plays):
    """
        Descripción: Selecciona una jugada al azar de una lista de jugadas recibida.
                     Si el espacio se encuentra libre, lo agrega a la lista de
                     posibilidades.
        Retorna:
            1 - Si hay posibilidades, una jugada al azar, en caso contrario, None.
    """
    possibilities = [i for i in plays if hasFreeSpace(table, i)]
    if len(possibilities):
        return random.choice(possibilities)
    return None

def canWin(table, letra):
    """
        Descripción: Predice el siguiente movimiento correcto.
        Retorna:
            1 - El siguiente movimiento que permitirá ganar o bloquear dependiendo de su uso.
    """
    cell = 0
    for i in range(1, 10):
        copyTable = duplicateTable(table)
        if hasFreeSpace(copyTable, i):
            makeMove(copyTable, letra, i)
            if esGanador(copyTable, letra):
                cell = i
    return cell

def getComputerMove(table, computerletra, playerletra):
    """
        Descripción: Determina la siguiente jugada de la computadora.
                     Simula una IA (Inteligencia Artificial), la cual decide que
                     movimiento realizar, siguiendo los siguintes pasos:
                     1 - Evalúa si puede ganar en el siguiente movimiento, de ser posible,
                         efectúa el movimiento.
                     2 - Evalúa si el jugador puede ganar en el siguiente movimiento, de ser
                         así, lo bloquea.
                     3 - Evalúa si alguna de las esquinas se encuentra libre para ocuparla.
                     4 - Evalúa si el centro se encuentra disponible para ocuparlo.
                     5 - Evalúa si alguno de los lados se encuentra libre para ocuparlo.
        Retorna:
            1 - El siguiente movimiento de la computadora.
    """
    move = canWin(table, computerletra)
    if move: return move
    move = canWin(table, playerletra)
    if move: return move
    move = selectRandom(table, [1, 3, 7, 9])
    if move is not None: return move
    if hasFreeSpace(table, 5): return 5
    return selectRandom(table, [2, 4, 6, 8])

def fullTable(table):
    """
        Descripción: Evalúa si la tabla fue completada o no.
        Retorna:
            1 - True en caso de que esté completa, en caso de que haya al menos una celda
                vacía retorna False.
    """
    auxTable = list()
    for i, cell in enumerate(table):
        if not i:
            continue
        auxTable.append(cell)
    return all(cell in ['X', 'O'] for cell in auxTable)

def finishPlay(table, playInProgress, message):
    printTable(table)
    print message
    playInProgress = False
    return playInProgress

print 'Inciando Juego Ta-Te-Ti'
play = True
while play:
    playerletra, computerletra = SeleccionarLetraJugador()
    turn = randomStart()
    print TURN.get(turn) + ' primero.'
    playInProgress = True
    table = [' '] * 10
    while playInProgress:
        if turn:
            # Turno del jugador
            printTable(table)
            move = getPlayerMove(table)
            makeMove(table, playerletra, move)
            if esGanador(table, playerletra):
                playInProgress = finishPlay(table, playInProgress, 'Eres el Ganador!')
            elif fullTable(table):
                playInProgress = finishPlay(table, playInProgress, 'El juego termina en empate...')
            turn = 0
        else:
            # Turno de la computadora
            move = getComputerMove(table, computerletra, playerletra)
            makeMove(table, computerletra, move)
            if esGanador(table, computerletra):
                playInProgress = finishPlay(table, playInProgress, 'La computadora te ha Ganado!!')
            elif fullTable(table):
                playInProgress = finishPlay(table, playInProgress, 'El juego termina en empate...')
            turn = 1
    if not JugarDeNuevo():
        play = False