def opcionValida(options):
    opcion = input('Escoge una opción válida: ')
    while opcion not in options:
        opcion = input('Escoge una opción válida: ')
    return opcion


def getOpcionCorrecta(turno, cuadroSubido):
    if turno == 1:
        opcionCorrecta = '5'
    elif turno == 2:
        opcionCorrecta = '1'
    elif turno == 3:
        opcionCorrecta = '6'
    elif turno == 4:
        opcionCorrecta = '2'
    elif turno == 5:
        opcionCorrecta = '4'
    elif turno == 6:
        opcionCorrecta = '3'
    elif turno == 7:
        if cuadroSubido == 'blanco':
            opcionCorrecta = '7'
        else:
            opcionCorrecta = '8'
    return opcionCorrecta

def mostrarCuadroSubido(cuadroSubido):
    if cuadroSubido == '':
        print()
    else:
        if cuadroSubido == 'blanco':
            c = 'blanco'
        elif cuadroSubido == 'madera':
            c = 'de madera clara'
        elif cuadroSubido == 'azul':
            c = 'azul'
        elif cuadroSubido == 'metal':
            c = 'metal'
        print('7) Marco {0}'.format(c))

def descripcionCuadro(opcion, cuadroSubido):
    if opcion == '1':
        print('''
Un bebé de unos 2 años mordiendo un juguete con las encías. Tiene cara de
ser muy traviesa.
El cuadro está rajado de arriba a abajo.''')
    elif opcion == '2':
        print('''
El abuelo de joven, tendría unos 15 años. Aún tenía el pelo largo, rizado y
de color rubio.''')
    elif opcion == '3':
        print('''
Una señora muy vieja, de unos 70 años. Es un retrato bastante antiguo, se parece
mucho a la abuela.''')
    elif opcion == '4':
        print('''
Un señor con mono de trabajo azul, de unos 40 años. Parece el abuelo, pero
no tiene pelo.''')
    elif opcion == '5':
        print('''
Una mujer embarazada, de unos 25 años. ¡Es la abuela! Qué delgada estaba, casi
no la reconoces.''')
    elif opcion == '6':
        print('''
Una niña rubia de unos 5 años. Tiene cara de traviesa, se parece un poco
a ti...
El cuadro está rajado de arriba a abajo.''')
    elif opcion == '7':
        if cuadroSubido == 'madera':
            print('''
Un paisaje verde, amplio y precioso. Te da mucha paz.''')
        elif cuadroSubido == 'azul':
            print('''
Una mujer desnuda, subida en una concha gigante, rodeada de gente que
vuela. No lo entiendes muy bien.''')
        elif cuadroSubido == 'blanco':
            print('''
Una mujer rubia de unos 30 años, muy guapa, con un bebé en brazos.
El cuadro está rajado de arriba a abajo.''')
        elif cuadroSubido == 'metal':
            print('''
Dos señores con sombrero jugando a las cartas. Qué tontería de cuadro.''')


def game(cuadro):
    cuadroSubido = cuadro
    options = '0 1 2 3 4 5 6'.split()
    if cuadroSubido != '':
        options.append('7')
    optionsMenu = '1 2'.split()
    turno = 1
    cuadrosRectos = []
    
    while True:    
        print('''
1) Marco de madera oscura

2) Sin marco

3) Marco negro

4) Marco circular

5) Marco de madera roja

6) Marco desconchado''')
        print()
        mostrarCuadroSubido(cuadroSubido)
        print()
        print('Pulsa 0 para cancelar.')
        opcion = opcionValida(options)
        descripcionCuadro(opcion, cuadroSubido)
        if opcion != '0':
            if opcion not in cuadrosRectos:
                print('''
¿Quieres enderezar el cuadro?

1) Sí

2) No''')
                subir = opcionValida(optionsMenu)
                if subir == '1':
                    if opcion == getOpcionCorrecta(turno, cuadroSubido):
                        print('''
Ahora está recto.''')
                        cuadrosRectos.append(opcion)
                        turno += 1
                        if turno == 8:
                            print('''
Enderezas el último cuadro y al hacerlo te das cuenta de que tiene algo escrito:
"Hacia la mano del tenedor"''')
                            return True
                    else:
                        print('''
Una ráfaga de aire gélido vuelve a poner los cuadros tal y como estaban.
¿Cómo ha podido pasar? Aquí no hay ventanas...''')
                        cuadrosRectos = []
                        turno = 1
                else:
                    print('Lo dejas como está.')
            else:
                print('''
Este cuadro ya está recto.''')
        else:
            return False

