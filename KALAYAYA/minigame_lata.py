import random
import time

def opcionValida(options):
    opcion = input('Escoge una opción válida: ')
    while opcion not in options:
        opcion = input('Escoge una opción válida: ')
    return opcion

def coordPosibles():
    coords = []
    for i in (1, 3, 5, 7):
        for j in (1, 5, 9, 13, 17):
            coords.append([i, j])
    return coords

def generador():
    global posInicial
    coords = coordPosibles()
    coords.remove(posInicial)
    lata = coords.pop(random.randint(0, len(coords)-1))
    pinchos = []
    for i in range(3):
        pinchos.append(coords.pop(random.randint(0,len(coords)-1)))
    return [lata, pinchos]

def esquema():
    global pos
    ESQUEMEREITS = ['___ ___ ___ ___ ___',
                    '|_| |_| |_| |_| |_|',
                    '___ ___ ___ ___ ___',
                    '|_| |_| |_| |_| |_|',
                    '___ ___ ___ ___ ___',
                    '|_| |_| |_| |_| |_|',
                    '___ ___ ___ ___ ___',
                    '|_| |_| |_| |_| |_|']
    ESQUEMEREITS[pos[0]] = ESQUEMEREITS[pos[0]][:pos[1]] + 'X' + ESQUEMEREITS[pos[0]][pos[1]+1:]
    for i in ESQUEMEREITS:
        print(i)

def getValidMoves():
    global pos
    coordenadas = coordPosibles()
    return [[pos[0]-2, pos[1]] in coordenadas, [pos[0], pos[1]+4] in coordenadas,
            [pos[0]+2, pos[1]] in coordenadas, [pos[0], pos[1]-4] in coordenadas]

def opcionesMovValidas():
    options = []
    movPosibles = getValidMoves()
    for i in range(len(movPosibles)):
        if movPosibles[i]:
            options.append(str(i+1))
    return options

def movimiento():
    movPosibles = getValidMoves()
    print('''
 ______________________________________
|                                      |''')
    for i in range(len(movPosibles)):
        if i == 0:
            if movPosibles[i]:
                print('| (1) Arriba             ', end='')
            else:
                print('|                        ', end='')
        if i == 1:
            if movPosibles[i]:
                print('(2) Derecha   |')
            else:
                print('              |')
        if i == 2:
            if movPosibles[i]:
                print('| (3) Abajo              ', end='')
            else:
                print('|                        ', end='')
        if i == 3:
            if movPosibles[i]:
                print('(4) Izquierda |')
            else:
                print('              |')
    print('''|______________________________________|
''')
    print()

def movMano(despl):
    global pos
    if despl == '1':
        pos[0] -= 2
    if despl == '2':
        pos[1] += 4
    if despl == '3':
        pos[0] += 2
    if despl == '4':
        pos[1] -= 4

def game():
    global posInicial, pos, generatrix, lata, pinchos, vidas, intentos
    posInicial = ''
    pos = ''
    lata = ''
    pinchos = ''
    vidas = ''
    intentos = 3
    while intentos > 0:
        posInicial = [7,1]
        pos = posInicial
        lata = [1,1]
        pinchos = [[1,9],[3,1],[3,13],[5,5],[5,17],[7,13],[7,17]]
        vidas = 1
        while pos != lata and vidas > 0:
            esquema()
            movimiento()
            options = opcionesMovValidas()
            desplazamiento = opcionValida(options)
            movMano(desplazamiento)
            if pos in pinchos:
                if intentos != 1:
                    print('''
¡Ay! Te has cortado con algo que parece ser una lata abierta.
Tus reflejos te hacen quitar la mano. Te pica más la curiosidad que el corte.
Vuelves a meter la mano.''')
                    vidas -= 1
                    intentos -= 1
                else:
                    print('''
Una herida grande se abre en la palma de tu mano. Será mejor que la cures o se infectará.''')
                    intentos -= 1
                    break
            if pos == lata:
                esquema()
                print()
                print('¡Vaya, parece que has encontrado algo útil!')
                print()
                return True
            time.sleep(0.5)
    return False

posInicial = ''
pos = ''
lata = ''
pinchos = ''
vidas = ''
intentos = 3

