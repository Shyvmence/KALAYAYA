

def save():
    global malo
    global sala
    global loot
    global yaLooteado
    global eventos
    global yaVisitado
    global hora
    tipos = ['MALO', 'COORDENADAS', 'LOOT', 'YAVISITADO', 'EVENTOS', 'YALOOTEADO', 'HORA']
    variables = [malo, sala, loot, yaVisitado, eventos, yaLooteado, hora]
    try:
        with open('save.txt', 'w') as f:
            j = 0
            for i in variables:
                fichero.write(tipos[j] + '\n')
                if isinstance(i, list):
                    for k in i:
                        fichero.write(str(k) + '\n')
                elif isinstance(i, int):
                    fichero.write(str(i) + '\n')
                else:
                    fichero.write(i + '\n')
                fichero.write('\n')
                j += 1
        encSave()
        print('''
Partida guardada correctamente.''')
    except:
        print('''
Error al guardar.''')

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
                            var.append(int(i))
                        else:
                            var.append(i[:len(i)-1])
                else:
                    if final:
                        variables.append(var)
        corruptSave = False
        for i in range(len(tipos)+2):
            if i <= len(tipos)-1:
                if not contenido(variables[i],VARS[i]):
                    corruptSave = True
                    break
            elif i == len(tipos):
                if not contenido(variables[i], LOOT):
                    corruptSave = True
                    break
            else:
                if 0 <= variables[i] <= 180:
                    corruptSave = True
                    break
        if corruptSave:
            print('''
El archivo de guardado se ha corrompido. Creando partida nueva.''')
            return None
        else:
            return variables
    except:
        print('''
No existe partida guardada o el archivo de guardado se ha corrompido. Creando partida nueva.''')
        return None
