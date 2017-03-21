def showLoot():
    global loot
    if len(loot) != 0:
        for k in range(len(loot)):
            print('({0})      {1}'.format(k+1, loot[k]))
    else:
        print('No hay nada en tus bolsillos.')

def itemOptions():
    global loot
    opciones = ['0']
    for i in range(1, len(loot)+1):
        opciones.append(str(i))
    return opciones

def opcionValida(options):
    opcion = input('Escoge una opción valida: ')
    while opcion not in options:
        opcion = input('Escoge una opción válida: ')
    return opcion

def useItem():
    global loot
    if len(loot) == 0:
        print('No tienes nada en tus bolsillos.')
    else:
        options = itemOptions()
        showLoot()
        print('Pulsa 0 para cancelar.')
        opcion = opcionValida(options)
        if opcion == '0':
            return 'cancel'
        else:
            return loot[int(opcion)-1]

def promptItem(correctItem):
    itemUsado = useItem()
    if itemUsado == correctItem:
        return True
    elif itemUsado == 'noitem':
        print('No tienes nada en los bolsillos.')
        return False
    elif itemUsado != 'cancel':
        print('No parece que esto te pueda ayudar mucho.')
        return False
    else:
        return False


def showMarcos():
    global eventos
    marcos = ['Marco de madera clara', 'Marco azul',
              'Marco blanco', 'Marco de metal']
    cuadros = ['madera', 'azul',
               'blanco', 'metal']
    descripciones = ['Un paisaje verde, amplio y precioso. Te da mucha paz.',
                     'Una mujer desnuda, subida en una concha gigante, rodeada de gente que vuela. No lo entiendes muy bien.',
                     'Una mujer rubia de unos 30 años, muy guapa, con un bebé en brazos. El cuadro está rajado de arriba a abajo.',
                     'Dos señores con sombrero jugando a las cartas. Qué tontería de cuadro.']
    cuadrosDoble = []
    marcoInEventos = ''
    cuadroEnPared = ''
    for k in cuadros:
        if k in eventos:
            marcoInEventos = k
            cuadroEnPared = marcos[cuadros.index(k)]
            marcos.remove(marcos[cuadros.index(k)])
            descripciones.remove(descripciones[cuadros.index(k)])
        else:
            cuadrosDoble.append(k)
    for j in range(len(marcos)):
        print('{0}) {1}'.format(j+1, marcos[j]))
    options = ['0']
    for i in range(len(marcos)):
        options.append(str(i+1))
    opcion = opcionValida(options)
    if opcion != 0:
        print('{0}'.format(descripciones[int(opcion)-1]))
        print()
        print('¿Quieres colgar este cuadro?')
        opcionesM = '1 2'.split()
        print('''
1) Colgar el cuadro.

2) Dejarlo en el suelo.''')
        opcionM = opcionValida(opcionesM)
        if opcionM == '1':
            eventos.append(cuadros[int(opcion)-1])
            if len(marcos) != 4:
                eventos.remove(cuadroInEventos)
                print('''
Bajas el cuadro con el {0}'''.format(cuadroEnPared.lower()))
            print('''
Cuelgas el cuadro con el {0}'''.format(marcos[int(opcion)-1].lower()))
        
    

    
            
    
def encryptSave(enc=True):
    key = 14
    if not enc:
        key = -14
    fichero1 = open('save.txt', 'r')
    fichero2 = open('savecopia.txt', 'w')
    for i in fichero1:
        fichero2.write(i)
    fichero1.close()
    fichero2.close()
    fichero1 = open('savecopia.txt', 'r')
    fichero2 = open('save.txt', 'w')
    for linea in fichero1:
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
                fichero2.write(chr(num))
            else:
                fichero2.write(linea[car])
    fichero1.close()
    fichero2.close()
            
            

    
    
