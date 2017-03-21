def opcionValida():
    global options
    opcDuplicada = ['0']
    for i in options:
        opcDuplicada.append(i)
    for k in range(len(options)):
        print('{0}   {1}'.format(k+1, opciones[k]))
    print('Pulsa 0 para cancelar.')
    opcion = input('Escoge una opción valida: ')
    while opcion not in opcDuplicada:
        opcion = input('Escoge una opción válida: ')
    return opcion
    
options = '1 2 3 4 5 6'.split()
opciones = ['VERDE', 'IGLESIA',
            'DESNUDO', 'ESPERAR',
            'MÍO', 'ABUELA']
preguntas = ['¿Qué es lo que más te desespera?', '¿Qué es lo que más te aburre?',
             '¿Qué te parece más incómodo?', '¿Qué es lo que más odias del cole?',
             '¿Tienes algún problema en casa?', '¿Qué es lo que más odias en el mundo?']

def getOpcionCorrecta(turno):
    if turno == 1:
        opcionCorrecta = '4'
    elif turno == 2:
        opcionCorrecta = '6'
    elif turno == 3:
        opcionCorrecta = '2'
    elif turno == 4:
        opcionCorrecta = '3'
    elif turno == 5:
        opcionCorrecta = '5'
    elif turno == 6:
        opcionCorrecta = '1'
    return opcionCorrecta

def correctOption(turno):
    if turno == 1:
        print('''
Cuando TJ Detweiler está a punto de contar su plan genial en el patio
de recreo y ponen anuncios. Odias eso.''')
    elif turno == 2:
        print('''
Tener que hacer los deberes junto a la abuela. Esto te llena de ira.''')
    elif turno == 3:
        print('''
Los pantalones que la abuela te hace ponerte los domingos para ir a la
iglesia. Aprietan, pican, tiran... Cada vez te sientes más furioso.''')
    elif turno == 4:
        print('''
Que Don Manuel siempre nos haga quitarnos la ropa cuando en el cole toca
grabación. Es una situación embarazosa. Te hierve la sangre.''')
    elif turno == 5:
        print('''
D'Artacán mordisquea tus juguetes, cuando él tiene los suyos propios.
Además en la mesa siempre intenta robarte el postre. Esto te llena aún
más de ira.''')
    else:
        print('''
EL BRÓCOLI!! Ahora estás completamente FURIOSO.''')
        
def game():
    global options
    global opciones
    global preguntas
    turno = 1
    while True:
        print(preguntas[turno-1])
        print()
        opcionCorrecta = getOpcionCorrecta(turno)
        choice = opcionValida()
        if choice == opcionCorrecta:
            correctOption(turno)
            turno += 1
            if turno == 7:
                return True
        elif choice != '0':
            print('''
Seguro que hay algo que te da más rabia que eso...
Ves un pajarillo, esto te llena de paz.
Ahora tendrás que volver a empezar.''')
            turno = 1
        else:
            print('''
Mejor en otro momento.''')
            return False
