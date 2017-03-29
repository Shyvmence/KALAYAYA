import os

def cargar():
    global MALOS
    global NSALAS
    global LOOT
    global VISITA
    global EVENTOS
    try:
        encSave(-1, 'save.txt', 'savecopia.txt')
        tipos = ['MALO', 'COORDENADAS', 'LOOT', 'YAVISITADO', 'EVENTOS', 'YALOOTEADO', 'HORA']
        VARS = [MALOS, NSALAS, LOOT, VISITA, EVENTOS]
        variables = []
        var = []
        final = False
        with open('savecopia.txt', 'r') as f:
            for i in f:
                if i != '\n':
                    if i[:len(i)-1] in tipos:
                        if tipos.index(i[:len(i)-1]) != 0:
                            variables.append(var)
                            var = []
                            if tipos.index(i[:len(i)-1]) == len(tipos)-1:
                                final = True
                    else:
                        if i[:len(i)-1].isdigit():
                            var.append(int(i[:len(i)-1]))
                        else:
                            var.append(i[:len(i)-1])
                else:
                    if final:
                        variables.append(var)
                n = len(variables)
        os.remove('savecopia.txt')
        corruptSave = False
        for i in range(len(VARS)+2):
            if i <= len(VARS)-1:
                if i == 1:
                    if variables[i] not in VARS[i]:
                        corruptSave = True
                        break
                else:
                    if not contenido(variables[i],VARS[i]):
                        corruptSave = True
                        break
            elif i == len(VARS):
                if not contenido(variables[i], LOOT):
                    corruptSave = True
                    break
            else:
                if variables[i][0] < 0 or variables[i][0] > 180:
                    corruptSave = True
                    break
        if corruptSave:
            print('''
El archivo de guardado se ha corrompido. Creando partida nueva.''')
            del variables
            return None
        else:
            return variables
    except:
        print('''
No existe partida guardada o el archivo de guardado se ha corrompido. Creando partida nueva.''')
        return None

def contenido(a, b):
    ## devuelve True si todos los items de a están en b.
    ## False otherwise.
    dev = True
    for i in a:
        if i not in b:
            dev = False
    return dev

def encSave(enc=1, fEntrada='save.txt', fSalida = 'save.txt'):
    key = 16*enc
    with open(fEntrada, 'r') as f:
        a = f.readlines()
    with open(fSalida, 'w') as f:
        for linea in a:
            for car in range(len(linea)):
                if linea[car].isalpha() and car != len(linea)-1:
                    num = ord(linea[car])
                    if ord('a')<=num<=ord('z') or ord('A')<=num<=ord('Z'):
                        num += key

                        if linea[car].isupper():
                            if num > ord('Z'):
                                num -= 26
                            elif num < ord('A'):
                                num += 26
                        elif linea[car].islower():
                            if num > ord('z'):
                                num -= 26
                            elif num < ord('a'):
                                num += 26
                    f.write(chr(num))
                else:
                    f.write(linea[car])


MALOS = ['abuelo', 'abuela', 'perro']
NSALAS = [[1,1], [1,5], [3,1], [3,5], [3,9], [5,1], [5,5], [5,9], [5,13], [7,1], [7,5], [7,13], [9,5], [9,9], [9,13], [11,9]]
LOOT = ['PAR DE CALCETINES MALOLIENTES', 'CLIP ROTO', 'IMÁN', 'HILO DENTAL', 'LATA DE PATÉ DE GATO', 'LLAVES DE LA CASA', 'TROZO DE CRISTAL', 'ROPA INTERIOR SUCIA DE LA ABUELA', 'PALO DE MADERA', 'GANCHO', 'CUERDA', 'MAGNETO', 'SIERRA', 'MARTILLO', 'CINTA', 'TIJERAS', 'MANTEQUILLA', 'MANTEQUILLA LÍQUIDA', 'LLAVE DE LA CUBERTERÍA', 'TENEDOR', 'CARAMELO', 'PEGAMENTO', 'ANILLO', 'CORBATA', 'LLAVE DE LA HABITACIÓN', 'LLAVE CAJA FUERTE', 'MASCARILLA']
VISITA = ['TU CUARTO', 'TU BAÑO', 'TRASTERO', 'SALÓN',
          'LAVANDERÍA', 'TALLER DEL ABUELO', 'COCINA', 'PASILLO ESTRECHO',
          'PASILLO CORTO', 'VESTIDOR ABUELOS', 'ESCALERA',
          'RECIBIDOR', 'HABITACIÓN ABUELOS', 'BAÑO ABUELOS']
EVENTOS = ['pelusa', 'caja', 'tapón', 'herido', 'bolsa', 'upSilla', 'brokeSilla', 'encuentra', 'calcetines', 'cuboSuelo', 'try', 'furia', 'neverLav', 'winRata', 'dope', 'pelea', 'clipUsed', 'plomos', 'cajonOpen', 'openArmario', 'tvon', 'pateDado', 'winGato', 'madera', 'azul', 'blanco', 'metal', 'pista', 'keyUsed', 'gafas', 'pass', 'book', 'exitOpen', 'openCaja', 'mascarillaPuesta', 'fightRata2', 'windowOpen', 'finMadre', 'finAbuelos', 'campanadas']


