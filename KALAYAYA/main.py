import sys
import random
import time
import minigame_lata
import minigame_furia
import minigame_fight
import minigame_cuadros

def opcionValida(options):
    opcion = input('Escoge una opción válida: ')
    while opcion not in options:
        opcion = input('Escoge una opción válida: ')
    return opcion

def newPrint(cadena, delay=0.025):
    for i in cadena:
        print(i, end='')
        time.sleep(delay)

def contenido(a, b):
    ## devuelve True si todos los items de a están en b.
    ## False otherwise.
    dev = True
    for i in a:
        if i not in b:
            dev = False
    return dev

def new_load():
    print('''
¿Quieres empezar un nuevo juego o continuar?
1) Nuevo Juego                   2) Continuar''')
    options = '1 2'.split()
    opcion = opcionValida(options)
    if opcion == '1':
        return True
    else:
        return False

def cargar():
    fichero = open('save.txt', 'r')
    tipos = ['MALO', 'COORDENADAS', 'LOOT', 'YAVISITADO', 'EVENTOS', 'YALOOTEADO', 'HORA']
    variables = []
    var = []
    final = False
    for i in fichero:
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
    fichero.close()
    return variables

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
        fichero = open('save.txt', 'w')
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
        fichero.close()
        print('Partida guardada correctamente.')
    except:
        print('Error al guardar')
    

# GLOBAL VARIABLES (SALA, SALAACTUAL, LOOT, YALOOTEADO, YAVISITADO, EVENTOS, YALOOTEADO, HORA)
#inputs sobre 70 caracteres de largo, me lo paso por los cojones
# SALA = coordenadas de la sala
# SALAACTUAL = número de sala, obtenida a partir de getNSala(sala)

def showIntroduction():
    print('''
¡Despierta! Son las 9:00 AM, hoy no hay cole, Jorge y Marta seguro que están
ya en la calle jugando con esas nuevas bicis que les han regalado sus padres.
¿Te vas a quedar en la cama tumbado todo el día? La abuela y el abuelo deben
haber llevado a D'Artacán de paseo. Estarán de vuelta a las 11:00 AM. Tienes
2 horas para hacer lo que te de la gana. ¿Qué te parece si buscas algo con lo
que divertirte?

Das vueltas por la casa sin saber qué hacer. En cierto lugar encuentras:''')
    elegirMalo()
    print('''
Vuelves a tu cuarto para ponerte los zapatos. La casa no es demasiado grande.
La puerta de salida está en la habitación más alejada de donde duermes. Para
conseguir llegar hasta ella tendrás que agudizar tus sentidos y ayudarte de
las cosas que vayas encontrando.''')
    

def elegirMalo():
    global malo
    print('''
1) Una tarta recién hecha que despide un riquísimo olor. Seguro que a la abuela
no le importará que te comas un trocito.

2) Unas monedas apiladas de más grandes a más pequeñas. Podrías comprar unos cromos
con ellas, seguro que te tocaría el que te falta para completar la colección.

3) Una pelota mordisqueada. D'Artacán ha debido jugar con ella, seguro que ahora
piensa que es suya y sólo suya.

¿Qué decides coger?''')
    options = '1 2 3'.split()
    opcion = opcionValida(options)
    if opcion == '1':
        print()
        print('''
A la abuela no le gusta que comas con las manos. Cuando se entere de que falta un
trozo de su tarta se enfadará mucho. Agarrará su zapatilla. Más te vale salir de
casa antes de que llegue...''')
        malo = 'abuela'
    if opcion == '2':
        print()
        print('''
El abuelo es un viejo tacaño, no le va a hacer gracia que hayas cogido su dinero.
Siempre te regaña con esas cosas. Solo pensar en su palo de andar, hace que se te
erice el bello de la nuca. Más te vale salir de casa antes de que llegue...''')
        malo = 'abuelo'
    if opcion == '3':
        print()
        print('''
Oh, vaya… creo que a D’Artacán le gusta mucho esa pelota. Cuando vea que alguien
la ha cogido se va a poner furioso. Más te vale salir de casa antes de que llegue...''')
        malo = 'perro'  

def getName():
    global salaActual
    NOMBRES = ['TU CUARTO', 'TU BAÑO', 'TRASTERO', 'SALÓN',
               'LAVANDERÍA', 'TALLER DEL ABUELO', 'COCINA', 'PASILLO ESTRECHO',
               'PASILLO CORTO', 'VESTIDOR ABUELOS', 'ESCALERA',
               'RECIBIDOR', 'HABITACIÓN ABUELOS', 'BAÑO ABUELOS']
    return NOMBRES[salaActual-1]

def getValidMoves():
    global sala
    NSALAS = [[1,1], [1,5], [3,1], [3,5], [3,9], [5,1], [5,5], [5,9], [5,13], [7,1], [7,5], [7,13], [9,5], [9,9]]
    return [[sala[0]-2, sala[1]] in NSALAS, [sala[0], sala[1]+4] in NSALAS,
            [sala[0]+2, sala[1]] in NSALAS, [sala[0], sala[1]-4] in NSALAS]

def excepciones():
    global eventos
    global salaActual
    mPosibles = getValidMoves()
    if salaActual == 1:
        mPosibles[2] = False
    elif salaActual == 3:
        mPosibles[0] = False
        mPosibles[1] = False
    elif salaActual == 4:
        mPosibles[3] = False
        if 'neverLav' in eventos:
            mPosibles[1] = False
    elif salaActual == 6:
        if 'clipUsed' not in eventos:
            mPosibles[0] = False
    elif salaActual == 8:
        if 'neverLav' in eventos:
            mPosibles[0] = False
        if 'winGato' not in eventos:
            mPosibles[1] = False
    elif salaActual == 11:
        if 'keyUsed' not in eventos:
            mPosibles[2] = False
    elif salaActual == 12:
        if 'exitOpen' not in eventos:
            mPosibles[2] = False
    elif salaActual == 13:
        if 'mascarillaPuesta' not in eventos:
            mPosibles[1] = False
    elif salaActual == 14:
        if 'windowOpen' not in eventos:
            mPosibles[1] = False
    return mPosibles


def opcionesMovValidas():
    options = ['0']
    movPosibles = excepciones()
    for i in range(len(movPosibles)):
        if movPosibles[i]:
            options.append(str(i+1))
    return options

def movimiento(huida=False):
    movPosibles = excepciones()
    mostrarMapa(huida)
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
    if not huida:
        print('''  Pulsa (0) para cancelar.''')
    print()

def movSala(despl):
    global sala
    if despl == '1':
        sala[0] -= 2
    if despl == '2':
        sala[1] += 4
    if despl == '3':
        sala[0] += 2
    if despl == '4':
        sala[1] -= 4
    
    
def getNSala():
    NSALAS = [[1,1], [1,5], [3,1], [3,5], [3,9], [5,1], [5,5], [5,9], [5,13], [7,1], [7,5], [7,13], [9,5], [9,9]]
    return NSALAS.index(sala) + 1

def getDescription():
    global salaActual
    DESCRIPCIONES = ['''
Está patas arriba, las sábanas bailan con el viento que entra de la ventana
entreabierta, los cajones están llenos de material de dibujo con el que has
decorado todas las paredes. La alfombra tupida está llena de piezas de Lego
y dibujos caídos del techo, hace tiempo que ya no caben en las paredes...''', ##cuarto
                     '''
Es muy pequeño. La bañera está llena de juguetes flotando, el WC está lleno
de pegatinas que vienen en los bollos. Al lado hay un mini WC que nunca has
sabido para qué sirve. ''', ##baño
                     '''
Es un lugar oscuro. Las estanterías son tan altas que ni saltando llegas a ver
el primer estante. El polvo que hay entre los miles de objetos almacenados se
te mete en la nariz y te hace estornudar. Una pequeña bombilla ilumina la sala
desde arriba, la mayor parte de la luz se la quedan las partes altas de la
estantería. La luz que llega a la altura de tus ojos es muy pobre, apenas sirve
para distinguir objetos. ''', ##trastero
                     '''
Es una habitación pequeña, toda cubierta de mantas gruesas y pelo de animal. 
En las vitrinas hay juegos de cubertería cara, impecables, parece que el polvo
no los ha rozado nunca. En una de las paredes hay una mujer de piedra blanca
brillante, muy alta, con un brazo extendido hacia el cielo.''', ##salon
                     '''
Es un cuarto pequeño, decorado con azulejos azules y blancos que forman un mosaico
de pajarillos. No hay techo, puedes ver el sol, los pájaros, la libertad.
Te sientes tan cerca de lo que quieres... Los enormes muros te devuelven a la realidad.
La sala está prácticamente vacía, lo único que la ocupa es una pequeña lavadora de color
crema, calzada con un par de ladrillos, que crea terremotos cuando se pone en marcha.''', ##lavanderia
                     '''
El taller del abuelo es un lugar misterioso, huele a sudor y trabajo. Está lleno
de utensilios raros y puntiagudos. Jamás te ha dejado entrar, dice que es peligroso.
Un día miraste a través de la cerradura de la puerta, no entendiste para qué quería
tanto látex negro.''', ##taller
                     '''
La cocina apesta a eso verde tan sano que a la abuela le interesa tanto que coma.
Los cajones están abiertos  y forrados por todas partes de unas pegatinas en las
que a veces se quedan atrapados unos bichitos alados muy feos. En el centro hay una
mesa grande donde coméis los cuatro juntos. La silla de D'Artacán tiene un cojín
para que llegue bien al plato.''', ##cocina
                     '''
El pasillo de la casa se divide en dos partes. La parte estrecha y la parte corta.
Esta parte es diáfana, no hay ni un mueble ni un cuadro, nada.''', ##pasilloestrecho
                     '''
Esta parte del pasillo es pequeña y recargada, todos los cuadros de la casa están apilados aquí.
No conoces  a ninguna de las personas que te siguen con la mirada desde las paredes.
Hay un mueble de madera alargado a cada lado del pasillo, lo que lo hace aún más estrecho
que la otra parte. ''', ##pasillocorto
                     '''
Es una habitación muy pequeña, poco iluminada y que huele a rancio, como el abuelo cuando
viene de tomar el aire. Las batas largas de color rosa tapan todo el fondo de los armarios.
Varios armarios roperos enmarcan la sala. El más grande es el de los abrigos. Al lado hay
un panel con números. En el centro de la sala, sobre la moqueta de pelo marrón, hay una silla
de madera plegáble con unos calzoncillos colgando del respaldo. Hay demasiado eco para una
habiación de este tamaño. ''', ##vestidor
                     '''
Las escaleras llevan al segundo piso. Los peldaños de madera crujen cuando los pisas.
La barandilla está astillada por debajo y demasiado pulida por encima.
Te encanta deslizarte por ella, es larguísima.
''', ##escalera
                     '''
Es la parte más bonita de la casa. Es espacioso y las paredes no tienen el
color amarillo con manchas del resto de la casa. En cambio son blancas y lisas.
La penetra por la vidriera de la puerta, convirtiendo esta sala en la más
luminosa de la casa. En la pared derecha hay un mueble de diseño moderno,
blanco y verde, con dos grandes cajones de cristal repletos de libros que
nadie ha leido. Siempre están en el mismo sitio. Sobre el mueble hay un par
de fuentes de bambú, crees que son chinas. Hacen un ruido muy divertido cuando
una de las partes se llena de agua y cae.
''', ##hall
                     '''
Nunca antes habías estado en esta habitación. La habitación de los abuelos es muy
distinta a la tuya, todo está ordenado, todos los cajones están cerrados y los
dibujos que hay por las paredes son distintos. Aparecen superhéroes, vestidos con
los trajes negros apretados que viste en la guarida secreta del abuelo. La cama es
muy grande y tiene unas mantas muy gordas por encima. Un alfombra granate decora el
centro de la habitación que enmarcan los dos armarios de madera oscura. A la izquierda
del armario, colgado en la pared hay un espejo redondo. A cada lado de la cama hay una
mesita pequeña con un vaso de agua y un par de libros.''', ##habitacion
                     '''
Es el doble de grande que el tuyo. Está más limpio y no tiene pegatinas.
Tiene una toalla redonda en el suelo de color crema. Los grifos están relucientes.
Al fondo hay una cortina que separa una parte del baño de la otra.'''] ##baño
    return DESCRIPCIONES[salaActual-1]

def mapa():
    global sala
    mapa = ['___ ___', '|_|-|_|', '___ _|_ ___',
            '|_| |_|-|_|', '_|_ _|_ _|_ ___', '|_|-|_|-|_|-|_|',
            '_|_ _|_     _|_', '|_|-|_|     |_|',
            '    _|_ ___ _|_', '    |_|-|_|-|C|']
    mapa[sala[0]] = mapa[sala[0]][:sala[1]]+'X'+mapa[sala[0]][sala[1]+1:]
    for i in mapa:
        print(i)

def mostrarMapa(huida=False):
    global salaActual
    mapa()
    print()
    print('Estás en: ' + getName())
    print()
    if not huida:
        print(getDescription())

def getLoot(item):
    global loot
    loot.append(item)
    yaLooteado.append(item)

def showLoot():
    global loot
    if len(loot) != 0:
        for k in range(len(loot)):
            if len(str(k+1)) == 1:
                print('({0})      {1}'.format(k+1, loot[k]))
            else:
                print('({0})     {1}'.format(k+1, loot[k]))
    else:
        print('No hay nada en tus bolsillos.')

def itemOptions():
    global loot
    opciones = ['0']
    for i in range(1, len(loot)+1):
        opciones.append(str(i))
    return opciones

def useItem():
    global loot
    if len(loot) == 0:
        print('No tienes nada en tus bolsillos.')
        return 'noitem'
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
    global hora
    itemUsado = useItem()
    if not isinstance(correctItem, list):
        if itemUsado == correctItem:
            return True
    else:
        if itemUsado in correctItem:
            return True
    if itemUsado == 'noitem':
        return False
    elif itemUsado != 'cancel':
        print('No parece que esto te pueda ayudar mucho.')
        hora -= 1
        return False
    else:
        return False



def act():
    global salaActual
    if salaActual == 1:
        cuarto()
    elif salaActual == 2:
        lavabo()
    elif salaActual == 3:
        trastero()
    elif salaActual == 4:
        salon()
    elif salaActual == 5:
        lavanderia()
    elif salaActual == 6:
        taller()
    elif salaActual == 7:
        cocina()
    elif salaActual == 8:
        pasilloEstrecho()
    elif salaActual == 9:
        pasilloCorto()
    elif salaActual == 10:
        vestidor()
    elif salaActual == 11:
        escalera()
    elif salaActual == 12:
        hall()
    elif salaActual == 13:
        habitacion()
    elif salaActual == 14:
        wc()
    elif salaActual == 15:
        calle()

def room():
    global salaActual
    global sala
    global loot
    global yaLooteado
    global eventos
    global hora
    print(getName())
    print()
    if getName() not in yaVisitado:
        print(getDescription())
        yaVisitado.append(getName())
    while True:
        print('''
 ______________________________________________________________
|                                                              |
| (1) Interactuar        (2) Moverte            (3) Mapa       |
| (4) Bolsillos          (5) Guardar            (6) Salir      |
|______________________________________________________________|
''')
        print()
        options = '1 2 3 4 5 6'.split()
        pOption = opcionValida(options)
        if pOption == '1':
            act()
        if pOption == '2':
            movimiento()
            desplazar = opcionValida(opcionesMovValidas())
            if desplazar != '0':
                movSala(desplazar)
                salaActual = getNSala()
                hora -= 1
                break
        if pOption == '3':
            mostrarMapa()
        if pOption == '4':
            showLoot()
        if pOption == '5':
            save()
        if pOption == '6':
            sys.exit()

#def excepciones():
    #excepciones va a devolverme True/False y printear que no se puede mover.
    #salas cerradas o que necesiten llave.
            
def cuarto():
    global loot
    global yaLooteado
    global hora
    global eventos
    global salaActual
    calcetines = 'PAR DE CALCETINES MALOLIENTES'
    clip = 'CLIP ROTO'
    iman = 'IMÁN'
    while True:
        print('''
1) Caminar directamente hacia la puerta; no hay tiempo que perder...
   
2) Examinar las paredes, puede que encuentres algo útil...

3) Buscar en los cajones. Va a ser complicado, están hasta los topes...

Pulsa 0 para cancelar.
''')
        options = '0 1 2 3'.split()
        opcion = opcionValida(options)
        if opcion == '0':
            break
        if opcion == '1':
            print()
            print('''
Pisas una de tus mega-construcciones Lego, duele tanto que caes al suelo
y te retuerces durante un rato aguantando el llanto. Desde el suelo
la habitación parece mucho más grande.''')
            print()
            print('''
1) Alargar la mano y buscar bajo la cama.

2) Construir una fortaleza con piezas de Lego.

Pulsa 0 para cancelar.
    ''')
            options = '0 1 2'.split()
            opcion1 = opcionValida(options)
            print()
            if opcion1 == '1':
                if calcetines not in yaLooteado:
                    print('Encuentras {0} - Llevaban ahí abajo mucho tiempo.'.format(calcetines))
                    getLoot(calcetines)
                else:
                    print('Solo encuentras polvo.')
            if opcion1 == '2':
                print('''
La construcción es colosal, las columnas góticas y los arcos ojivales
son tu punto fuerte.''')
        if opcion == '2':
            print()
            print('''
1) Observar los dibujos.

2) Revisar el muro de las tareas.

Pulsa 0 para cancelar.''')
            options = '0 1 2'.split()
            opcion2 = opcionValida(options)
            print()
            if opcion2 == '1':
                if clip not in yaLooteado:
                    print('''
Ahí está la abuela, y ahí el abuelo. Ese es Puar jugando en el campo y
ahí estáis Marta y tú cogidos de la mano, el dibujo de D'Artacán dormido
se tambalea en la pared hasta que cae al suelo.

Encuentras {0} - No podía sostenerse mucho más ahí con esto.'''.format(clip))
                    getLoot(clip)
                else:
                    print('''
El dibujo era más bonito desde lejos.
    ''')
            if opcion2 == '2':
                print('''
Tienes pendiente: limpiar el baño, la cocina, el salón, el pasillo y el
vestidor de los abuelos''')
        if opcion == '3':
            if iman not in yaLooteado and 'pelusa' not in eventos:
                print('''
Sacas una pelusa enorme. Pesa demasiado para ser una pelusa, es suave...''')
                print('''
1) Frotarla con la mano.

2) Tirarla a la basura.

Pulsa 0 para cancelar''')
                options = '0 1 2'.split()
                opcion3 = opcionValida(options)
                if opcion3 == '1':
                    print('''
Dentro parece haber algo, aunque te da bastante asco tocar la pelusa.
Encuentras {0} - Jugar a ser Magneto atrayendo hacia tus ma nos
las chinchetas es de las cosas que más te divierten. A la abuela
no le hace tanta gracia.'''.format(iman))
                    getLoot(iman)
                if opcion3 == '2':
                    print('''
Podría ser un monstruo, no necesitas más interrupciones.''')
                    eventos.append('pelusa')
            else:
                print('''
No parece haber nada útil en los cajones.''')
            

####################################################

            
def lavabo():
    global loot
    global eventos
    global salaActual
    global sala
    global yaLooteado
    global hora
    hilo = 'HILO DENTAL'
    evPosibles = 'caja tapón'.split()
    while True:
        print('''
1) Buscar en el cajón que hay debajo del lavabo.

2) Examinar los tebeos.

3) Mirar en la bañera.

4) Lavarte las manos.

Pulsa 0 para cancelar.
''')
        options = '0 1 2 3 4'.split()
        opcion = opcionValida(options)
        if opcion == '1':
            if evPosibles[0] not in eventos:
                print('No puedes abrir las puertas, hay algo bloqueándolas.')
            else:
                if hilo not in yaLooteado:
                    print()
                    print('''
El cajón está casi vacío. Encuentras {0} - Normalmente esas
cosas están en el baño de la abuela, pero lo cogiste para jugar
y nadie lo ha echado en falta.
'''.format(hilo))
                    getLoot(hilo)
                else:
                    print('Ya solo queda polvo en el cajón.')
        elif opcion == '2':
            print('''
La caja más grande y pesada está frente al lavabo, es la de los cómics
de superhéroes.''')
            print()
            print('''
1) Apartar la caja.

2) Mejor dejarla donde está.''')
            options = '1 2'.split()
            opcion2 = opcionValida(options)
            if opcion2 == '1':
                if evPosibles[1] not in eventos:
                    print('''
No hay mucho sitio donde ponerla...''')
                else:
                    if evPosibles[0] not in eventos:
                        print('''
Pones el cajón dentro de la bañera vacía. Será mejor que recuerdes que
está ahí la proxima vez que vayas a darte un baño.''')
                        eventos.append(evPosibles[0])
                    else:
                        print('''
Donde está ya no molesta... Será mejor que recuerdes que está ahí
la próxima vez que vayas a darte un baño...''')
        elif opcion == '3':
            if evPosibles[1] not in eventos:
                print('''
La bañera está llena de agua sucia y juguetes.''')
            else:
                print('''
En la bañera solo quedan los juguetes.''')
            print()
            print('''
1) Darse un baño.

2) Quitar el tapón.

Pulsa 0 para cancelar.''')
            options = '0 1 2'.split()
            opcion3 = opcionValida(options)
            if opcion3 == '1':
                if evPosibles[1] not in eventos:
                    print('''
El agua está un poco fría y sabe algo raro, pero siempre es divertido
jugar un rato con los patitos.''')
                else:
                    print('''
Ya no hay agua en la bañera.''')
            if opcion3 == '2':
                if evPosibles[1] not in eventos:
                    print('La tubería se traga todo el agua.')
                    eventos.append(evPosibles[1])
                else:
                    print('''
Por mucho que lo pongas y lo quites, no creo que vaya a cambiar nada.
Ya no hay agua.''')
        elif opcion == '4':
            print('''
La abuela siempre dice que todo se cura con agua y jabón.''')
            if 'herido' in eventos:
                print('''
¡Ay, pica! Pero la abuela dice que todo lo que pica cura.''')
                eventos.remove('herido')
        else:
            break


def trastero():
    global loot
    global eventos
    global salaActual
    global sala
    global yaLooteado
    global hora
    lata = 'LATA DE PATÉ DE GATO'
    evPosibles = 'herido bolsa'.split()
    while True:
        print('''
1) Buscar entre las cosas del suelo.

2) Palpar los objetos del primer estante, no llegas a ver lo que son...

Pulsa 0 para cancelar.

¿Qué quieres hacer? ''')
        options = '0 1 2'.split()
        opcion = opcionValida(options)
        if opcion == '1':
            print()
            print('''
Está todo lleno de herramientas de jardinería... ¿Para qué quiere el abuelo
todo esto, si no tenemos jardín?''')
            print()
            print('''
1) Trastear las máquinas.

2) Buscar entre las bolsas de recambios.

Pulsa 0 para cancelar.

¿Qué quieres hacer? ''')
            opcion1 = opcionValida(options)
            if opcion1 == '1':
                print('''
Está oscuro, no ves qué estás tocando, rozas un cuchillo muy afilado
y te abres una herida muy grande en la mano. Debes curarla rápido o
se infectará.''')
                if 'herido' not in eventos:
                    eventos.append('herido')
            if opcion1 == '2':
                print('''
Hay una que te llama la atención, es muy grande.''')
                if 'bolsa' in eventos:
                    print('''
La has abierto con el trozo de cristal y ahora está todo tirado por el suelo.

1) Examinar el contenido de la bolsa.

Pulsa 0 para cancelar.''')
                    options = '0 1'.split()
                    opcion1_1 = opcionValida(options)
                    if opcion1_1 == '1':
                        print('''
A través del corte ves mucha ropa, diplomas y unas monedas doradas muy grandes con
correas de colores, como si la bolsa sangrase recuerdos. La ropa se parece a la
que lleva tu amiga Marta: hay prendas pequeñas, medianas y otras más grandes.
Esto no puede ser de la abuela, ni las más anchas le vendrían. En los diplomas
pone que la universidad se enorgullece de entregar la matricula de honor en biología
a Ana, el apellido está tapado por una firma enorme. Tú también sacas siempre
buenas notas, ojalá un día te den un diploma. En las monedas pone Federación
Olímpica de Tenis. Son muy bonitas, decides colgarte una al cuello.''')
                else:
                    print('''
Está cerrada con un nudo muy fuerte, no puedes deshacerlo.
Quizá puedas utilizar algo para abrirla.''')
                    if promptItem('TROZO DE CRISTAL'):
                        print('''
Rajas la bolsa por un lado con el TROZO DE CRISTAL. Del interior sale mucha
ropa, diplomas y unas monedas doradas muy grandes con correas de colores,
como si la bolsa sangrase recuerdos. La ropa se parece a la que lleva tu amiga
Marta: hay prendas pequeñas, medianas y otras más grandes. Esto no puede ser
de la abuela, ni las más anchas le vendrían. En los diplomas pone que la
universidad se enorgullece de entregar la matricula de honor en biología
a Ana, el apellido está tapado por una firma enorme. Tú también sacas siempre
buenas notas, ojalá un día te den un diploma. En las monedas pone Federación
Olímpica de Tenis. Son muy bonitas, decides colgarte una al cuello.''')
                        eventos.append('bolsa')
        if opcion == '2':
            if lata in yaLooteado:
                print('No quiero volver a pasar la mano por ahí.')
            elif 'herido' in eventos:
                print('No puedo pasar la mano por sitios extraños con esta herida. Sería peligroso.')
            else:
                if minigame_lata.game():
                    print('''
Encuentras {0} - Desde aquel día en el que Puar llegó a casa con collarín,
se ha vuelto un adicto a esto.'''.format(lata))
                    getLoot(lata)
                    hora -= 3
                else:
                    eventos.append('herido')
                    hora -= 2
        else:
            break

def salon():
    global loot
    global eventos
    global yaLooteado
    global hora
    cristal = 'TROZO DE CRISTAL'
    llaves = 'LLAVES DE LA CASA'
    evPosibles = 'calcetines upSilla brokeSilla encuentra'.split()
    while True:
        print('''
1) Subirte a una silla.

2) Observar la escultura.

3) Buscar algo interesante entre las mantas.''')
        options = '0 1 2 3'.split()
        if 'neverLav' in eventos:
            print('''
4) Puerta de la lavandería.''')
            options.append('4')
        print('''
Pulsa 0 para cancelar.''')
        opcion = opcionValida(options)
        if opcion == '1':
            if 'brokeSilla' in eventos:
                print('''
Ha sido muy peligroso, no te apetece repetir la experiencia.''')
            elif 'calcetines' in eventos:
                print('''
Subes a la silla, no es muy estable...''')
                eventos.append('upSilla')
            else:
                print('''
La abuela se enfadaría mucho si me viese poner los zapatos encima de
una de sus sillas antiguas.''')
        elif opcion == '2':
            if llaves in yaLooteado:
                print('Es una mujer preciosa...')
            elif 'upSilla' in eventos:
                print('''
Tiene una llave colgando del dedo corazón... intentas alcanzarla...
la pata de la silla se parte. Será mejor no volver a intentarlo.''')
                eventos.append('brokeSilla')
                eventos.remove('upSilla')
            else:
                print('''
Tiene algo que te llama la atención. Te hace quedarte embobado mirándola...
Algo cuelga de sus dedos. Quizá puedas alcanzarlas con algo...''')
                if promptItem('GANCHO'):
                    print('''
Con el {0} alcanzas las {1} - No son las de los abuelos.
¿De quién será este juego de llaves extra?'''.format('GANCHO', llaves))
                    getLoot(llaves)
        elif opcion == '3':
            if 'calcetines' in eventos:
                print('Ya solo quedan pelusas y huesos de oliva.')
            else:
                if 'encuentra' in eventos:
                    print('Solo encuentras los calcetines con los que has estado jugando.')
                else:
                    print('Encuentras unos calcetines gordos de la abuela.')
                    eventos.append('encuentra')
                options = '0 1 2'.split()
                print('''
1) Ponértelos.

2) Jugar a las marionetas con ellos.

Pulsa 0 para cancelar.''')
                opcion3 = opcionValida(options)
                if opcion3 == '1':
                    if 'TROZO DE CRISTAL' in yaLooteado:
                        print('''
Te quitas los zapatos y te pones los calcetines gordos. ¡Qué cómodos!''')
                        eventos.append('calcetines')
                    else:
                        print('''
Te quitas los zapatos y te pones los calcetines gordos. ¡AY, DUELE!''')
                        eventos.append('calcetines')
                elif opcion3 == '2':
                    if cristal not in yaLooteado:
                        print('''
Pasas un buen rato imitando a los abuelos con los calcetines. Espera un
momento... Aquí dentro hay algo. Encuentras {0} - Uf, si
me los hubiese puesto me habría hecho mucho daño.'''.format(cristal))
                        getLoot(cristal)
                    else:
                        print('''
Pasas un buen rato imitando a los abuelos con los calcetines.''')
        elif opcion == '4':
            print('''
Es la puerta que da a lavandería. Todavía se te eriza la piel de pensar
en el fantasma. Quizá puedas usar algo para tranquilizarte.''')
            if promptItem('CARAMELO'):
                print('''
Te hace sentir extraño, más relajado.''')
                eventos.remove('neverLav')
                loot.remove('CARAMELO')
        else:
            if 'upSilla' in eventos:
                eventos.remove('upSilla')
            break

def lavanderia():
    global loot
    global yaLooteado
    global hora
    global salaActual
    global eventos
    global hora
    ropa = 'ROPA INTERIOR SUCIA DE LA ABUELA'
    evPosibles = 'try cuboSuelo furia neverLav winRata'.split()
    while True:
        if 'cuboSuelo' not in eventos:
            print('''
1) Examinar la habitación.

Pulsa 0 para cancelar.''')
            options = '0 1'.split()
        else:
            print('''
1) Examinar la habitación.

2) Buscar entre la ropa sucia.

Pulsa 0 para cancelar.''')
            options = '0 1 2'.split()
        opcion = opcionValida(options)
        if opcion == '1':
            if 'cuboSuelo' not in eventos:
                print('''
No hay nada más aparte de la lavadora, el tendedero y un cubo enorme y pesado.''')
            else:
                print('''
Ahora está todo hecho un desastre, toda la ropa está tirada por el suelo.''')
            print('''
1) Buscar en la lavadora.

2) Buscar en el cubo.

3) Buscar en el tendedero.

Pulsa 0 para cancelar.''')
            options = '0 1 2 3'.split()
            opcion1 = opcionValida(options)
            if opcion1 == '1':
                print('''
Está vacía, no encuentras nada.''')
            elif opcion1 == '2':
                if 'cuboSuelo' in eventos:
                    print('''
Ahora ya no es tan imponente, todas sus entrañas están esparcidas por el suelo.''')
                else:
                    print('''
Es demasiado alto, no alcanzas a mirar qué hay dentro.''')
                    if 'try' in eventos:
                        print('''
1) Tumbarlo.

2) Coger fuerzas.

Pulsa 0 para cancelar.''')
                        options = '0 1 2'.split()
                    else:
                        print('''
1) Tumbarlo.

Pulsa 0 para cancelar.''')
                        options = '0 1'.split()
                    opcion1_1 = opcionValida(options)
                    if opcion1_1 == '1':
                        if 'cuboSuelo' in eventos:
                            print('''
Ya has conseguido tirar el cubo, tanto esfuerzo... Seguro que mañana
tienes agujetas.''')
                        elif 'furia' in eventos:
                            print('''
Descargas toda tu furia en un empujón colosal. El cubo no puede soportar
tanto empeño y se desploma, vertiendo todo su contenido por el suelo.
Quizá deberias aprender de esto y usar esta nueva habilidad con Miguel
"La Roca", debe pesar más o menos lo mismo. Así aprenderá a llevar su propio
bocadillo al cole.''')
                            eventos.append('cuboSuelo')
                        else:
                            print('''
Pesa demasiado, no puedes con él.''')
                            eventos.append('try')
                    elif opcion1_1 == '2':
                        if 'cuboSuelo' in eventos:
                            print('''
No crees que haga falta sentir más odio. De lo contrario, te saldrán bultos
en el cuello como a la abuela.''')
                        elif 'furia' in eventos:
                            print('''
Estás furioso, deberías aprovechar estos sentimientos para algo útil.''')
                        else:
                            print('''
Tratas de encontrar rabia en tu interior, un sentimiento que te haga estar
furioso y poder pagarlo con el cubo. Como hace el abuelo con D'Artacán.''')
                            print()
                            if minigame_furia.game():
                                eventos.append('furia')
                                hora -= 3
            elif opcion1 == '3':
                print('''
Antes Puar podía caminar por encima de las cuerdas. Ahora posiblemente se
partirían.''')
        elif opcion == '2':
            if 'winRata' in eventos:
                if ropa not in yaLooteado:
                    print('''
Buscas entre la ropa. Encuentras {0} - Jamás hubieses pensado
que fuese tan grande.'''.format(ropa))
                    getLoot(ropa)
                else:
                    print('''
No crees que el resto de ropa vaya a serte útil.''')
            else:
                if 'winRata2' not in eventos:
                    print('''
De entre las prendas de ropa emerge un calcetín que fantasmagóricamente
se mueve, de forma torpe rueda montaña abajo y se coloca en posición de
defensa. Parece que no está dispuesto a dejarte tocar a sus compañeros
sin arriesgar su vida primero.''')
                    print()
                    print('''
1) Huir.

2) Plantar cara al fantasma.

Pulsa 0 para cancelar.''')
                    options = '0 1 2'.split()
                    opcion2 = opcionValida(options)
                    if opcion2 == '1':
                        print('''
Das media vuelta y sales despavorido jurándote a ti mismo que no volverás
a pisar la lavandería nunca más.''')
                        eventos.append('neverLav')
                        movimiento(True)
                        options = opcionesMovValidas()
                        options.remove('0')
                        desplazar = opcionValida(options)
                        movSala(desplazar)
                        salaActual = getNSala()
                        print(getName())
                        print()
                        if getName() not in yaVisitado:
                            print(getDescription())
                            yaVisitado.append(getName())
                        break
                    elif opcion2 == '2':
                        print('''
Desde siempre has creído en los fantasmas; hoy es el día de enfrentarse a uno
de ellos. Cuando cuentes esta historia en el cole puedes obviar la parte de
que es minúsculo.''')
                else:
                    print('''
De algún modo te lo esperabas. Sabes perfectamente que dentro de ese calcetín
está esa rata tan valiente que conociste en el baño de los abuelos. Sabías
que volveríais a medir vuestras fuerzas. Siempre has tenido esa capacidad
de ver a lo que estás destinado. Notas en el ambiente que será una batalla dura,
que pondrá en riesgo la percepción que tienes de ti mismo.
Te remangas y te preparas para la batalla.''')
                if minigame_fight.game(salaActual, 'winRata2' in eventos):
                    if 'winRata2' not in eventos:
                        print('''
El fantasma cae rendido. Poco a poco, de dentro del calcetín emerge un pequeño
ratoncito. Te lanza una mirada de odio y huye hacia un hueco en la pared. No sabes
por qué, pero crees que volverás a ver a ese valiente ratoncito que se alzó contra
un enemigo al que no podía vencer, por defender a los suyos.
Esto te llena de determinación.''')
                    else:
                        print('''
La rata cae rendida. Te lanza una mirada de aprobación. Acepta que tienes el derecho
de rebuscar entre la ropa sucia que tan fieramente ha defendido. Por último se gira
y huye hacia un hueco en la pared.
''')
                    eventos.append('winRata')
                    hora -= 3
                else:
                    hora -= 1
        else:
            break

def taller():
    global loot
    global eventos
    global yaLooteado
    global hora
    global salaActual
    evPosibles = 'dope herramientaX pelea win comboX'.split()
    palo = 'PALO DE MADERA'
    gancho = 'GANCHO'
    cuerda = 'CUERDA'
    magneto = 'MAGNETO'
    comboGancho = ['TENEDOR', 'PALO DE MADERA', 'PEGAMENTO', 'SIERRA']
    comboCuerda = ['ROPA INTERIOR SUCIA DE LA ABUELA', 'CORBATAS', 'CALCETINES SUCIOS', 'TIJERAS']
    comboMagneto = ['IMÁN', 'HILO DENTAL', 'ANILLO', 'CINTA']
    combos = [comboGancho, comboCuerda, comboMagneto]
    herramientas = 'SIERRA MARTILLO CINTA TIJERAS'.split()
    while True:
        if 'clipUsed' not in eventos:
            print('''
1) Examinar la habitación.

2) Puerta cerrada.

Pulsa 0 para cancelar.''')
            options = '0 1 2'.split()
        else:
            print('''
1) Examinar la habitación.


Pulsa 0 para cancelar.''')
            options = '0 1'.split()
        opcion = opcionValida(options)
        if opcion == '1':
            print('''
Está todo lleno de cosas interesantes. La distribución se divide en cuatro
secciones:

1) Carpintería

2) Bañera con líquidos

3) Látex negro

4) Punto

Pulsa 0 para cancelar.''')
            options = '0 1 2 3 4'.split()
            opcion1 = opcionValida(options)
            if opcion1 == '1':
                print('''
La pared está llena de muestras de madera y clavos de todas las medidas.
La mesa de trabajo es imponente, no puedes mirar lo que hay sobre ella,
es demasiado alta.

1) Panel de herramientas

2) Mesa de trabajo

Pulsa 0 para cancelar.''')
                options = '0 1 2'.split()
                opcion1_1 = opcionValida(options)
                if opcion1_1 == '1':
                    print('''
En la pared hay un tablón con clavos, estratégicamente colocados para que
sobre ellos puedan reposar las herramientas. Puedes coger una de ellas, pero
sólo una. Coger dos haría que se tumbase, están en perfecto equilibrio.''')
                    optionsH = ['0']
                    for i in herramientas:
                        if i not in loot:
                            optionsH.append(str(herramientas.index(i)+1))
                    for k in range(1, len(optionsH)):
                        print('({0}) {1}'.format(optionsH[k], herramientas[int(optionsH[k])-1]))
                        print()
                    print('Pulsa 0 para cancelar.')
                    opcionH = int(opcionValida(optionsH))
                    if opcionH != 0:
                        if len(optionsH) != 5:
                            for j in herramientas:
                                if j in loot:
                                    tool = j
                            loot.remove(tool)
                        getLoot(herramientas[opcionH-1])
                        print('Tomas prestada la herramienta.')
                elif opcion1_1 == '2':
                    print('Si tienes pensado hacer manualidades, vas a tener que hacerlas de puntillas y sin mirar.')
                    if not (contenido(comboGancho, loot) or contenido(comboCuerda, loot) or contenido(comboMagneto, loot)):
                        print('No tienes suficientes objetos para combinar.')
                    else:
                        if 'book' not in eventos:
                            print('No se te ocurre cómo combinar las cosas. Tienes una crisis de creatividad.')
                        else:
                            options = ['0', '1']
                            print('Construir usando: ')
                            comboInBag = ''
                            for i in range(len(combos)):
                                if contenido(combos[i], loot):
                                    comboInBag = i
                                    break
                            print('1) {0}, {1}, {2}, {3}'.format(combos[comboInBag][0], combos[comboInBag][1], combos[comboInBag][2], combos[comboInBag][3]))
                            opcionM = opcionValida(options)
                            if opcionM == '1':
                                if comboInBag == 0:
                                    print('Creas el {0} - Algunas especies lo consideran un Dios. No es para tanto.'.format('GANCHO'))
                                    loot.remove('TENEDOR')
                                    loot.remove('PALO DE MADERA')
                                    loot.remove('PEGAMENTO')
                                    getLoot('GANCHO')
                                elif comboInBag == 1:
                                    print('Creas la {0} - No es muy estable, pero con tu peso podrá aguantar al menos un ratito.'.format('CUERDA'))
                                    loot.remove('ROPA INTERIOR DE LA ABUELA')
                                    loot.remove('CORBATAS')
                                    loot.remove('CALCETINES SUCIOS')
                                    getLoot('CUERDA')
                                else:
                                    print('Creas el {0} - Decidido, estudiarás ingeniería.'.format('MAGNETO'))
                                    loot.remove('IMÁN')
                                    loot.remove('HILO DENTAL')
                                    loot.remove('ANILLO')
                                    getLoot('MAGNETO')
            elif opcion1 == '2':
                print('''
Hay cientos de botellas apiladas en la esquina derecha de la habitación.
Llevan una etiqueta con la cara del abuelo. La bañera está hasta los topes del
líquido amarillento que rellena las botellas. Huele rancio y asqueroso,
como a fruta podrida.

1) Probar una de las botellas.

Pulsa 0 para cancelar.''')
                options = '0 1'.split()
                opcion2 = opcionValida(options)
                if opcion2 == '1':
                    print('''
Intentas descorchar la botella, pero está muy dura. No consigues nada.
Quizá puedas utilizar algo para abrirla.''')
                    if promptItem('MARTILLO'):
                        print('''
Rompes el cuello de la botella con un golpe seco del martillo. Ten cuidado,
no te cortes. Le das un largo trago y a continuación echas todo el contenido
de tu estómago. Después de un par de minutos vomitando, empiezas a verlo todo
distinto. Los colores y las formas se mezclan entre ellos, los olores se
convierten en sonidos y puedes saborear todo lo que llega a tus oídos.''')
                        eventos.append('dope')
            elif opcion1 == '3':
                if 'pelea' not in eventos:
                    print('''
Hay pedazos de esa tela negra colgando por toda la pared de la habitación.
Colgados como murciélagos, esperando a ser cortados. En la esquina izquierda
hay dos maniquíes vestidos con esta tela, con pinchos de metal y cremalleras
tapando sus bocas. ¿Será esta la guarida secreta del abuelo?
¡Es un superhéroe!''')
                    if 'dope' in eventos:
                        print('''
Poco a poco los maniquíes cobran vida. Comienzan a moverse y a bailar, dan vueltas
a tu alrededor. Uno de ellos se para a tu lado, se acerca a tu oído. Una voz de
mujer muy dulce te susurra: "¿Quieres bailar con nosotros?"

1) Sí

2) No

Pulsa 0 para cancelar.''')
                        options = '0 1 2'.split()
                        opcion3 = opcionValida(options)
                        if opcion3 == '1':
                            print('''
La figura se aleja un segundo y vuelve con una de las máscaras. En el interior está
bordado tu nombre, por eso el abuelo te estuvo midiendo hace unas semanas. Pensó
en ti para ayudarle a combatir el crimen, qué bueno es el abuelo. El maniquí te coloca
la máscara y cierra la cremallera. Te queda perfecta. Los maniquíes siguen bailando,
no se cansan nunca. Al contrario que tú. Te están dando calambres en las piernas.

1) Seguir bailando.

2) Parar de bailar.

Pulsa 0 para cancelar.''')
                            opcion3_1 = opcionValida(options)
                            if opcion3_1 == '1':
                                print('''
Te fuerzas y sigues bailando hasta que te tuerces un tobillo y caes al suelo, te
duele mucho. Los maniquíes ven que has dejado de bailar. La voz dulce te vuelve a
susurrar: "¿No vas a seguir bailando?"
Le contestas que no puedes, te has hecho daño.''')
                                opcion3 = '2'
                            elif opcion3_1 == '2':
                                opcion3_2 = opcion3_1
                                while opcion3_2 != '1':
                                    print('''
La voz dulce te vuelve a susurrar: "¿No vas a seguir bailando?"
Le contestas que estás cansado, que tienes que irte. La voz te insiste que quiere
que bailes para siempre.

1) Seguir bailando.

2) Parar de bailar.''')
                                    opcion3_2 = opcionValida(options)
                                    if opcion3_2 == '1':
                                        print('''
Te fuerzas y sigues bailando hasta que te tuerces un tobillo y caes al suelo, te
duele mucho. Los maniquíes ven que has dejado de bailar. La voz dulce te vuelve a
susurrar: "¿No vas a seguir bailando?"
Le contestas que no puedes, te has hecho daño.''')
                                        opcion3 = '2'
                        if opcion3 == '2':
                            print('''
El ambiente se enrarece. Los maniquíes paran de bailar y poco a poco abren las
cremalleras de sus bocas. Sus dientes son cuchillas. Te miran como lo hace Puar
cuando intentas darle un baño. Te asustas y te preparas para la batalla.''')
                        ## fight maniquíes
                            if minigame_fight.game(salaActual):
                                if 'SIERRA' in loot:
                                    print('''
Aprovechas la debilidad de tus adversarios. Estás fuera de ti. Sierra en mano,
imitando las películas de espadachines, arremetes contra los maniquíes. Estocada
tras estocada consigues tumbar a los tres y comienzas a mutilarlos. Sin brazos ni
piernas no pueden hacerte daño, piensas. Cuando has terminado, en un ataque de ira,
les cortas también la cabeza. Estas criaturas no sangran.

De pronto sales del trance. ¿Qué ha pasado?''')
                                elif 'MARTILLO' in loot:
                                    print('''
Aprovechas la debilidad de tus adversarios. Estás fuera de ti. Sacas el martillo y
comienzas a aporrear sin descanso a los maniquíes. Cuando ya han dejado de moverse
aún sigues chafando sus huesos con el martillo. Quedan irreconocibles.

De pronto sales del trance. ¿Qué ha pasado?''')
                                elif 'CINTA' in loot:
                                    print('''
Aprovechas la debilidad de tus adversarios. Estás fuera de ti. Abres la cinta y
comienzas a correr en círculos alrededor de las tres figuras. Consigues atarlas
bien fuerte y las amordazas, no quieres seguir viendo esos asquerosos dientes.
Aunque les hayas tapado la boca, siguen babeando un líquido verde fosforito,
viscoso y repugnante. Arremetes a patadas contra sus cabezas hasta que tus pies
están empapados de saliva de maniquí.

De pronto sales del trance. ¿Qué ha pasado?''')
                                elif 'TIJERAS' in loot:
                                    print('''
Aprovechas la debilidad de tus adversarios. Estás fuera de ti. Cierras los ojos,
abres las tijeras y comienzas a cortar todo el látex que encuentras en tu camino.
Sigues cortando hasta que el trocito más grande es del tamaño de una uña. Miras
el espectáculo grotesco, no queda nada de lo que antes eran tres figuras horrorosas.

De pronto sales del trance. ¿Qué ha pasado?''')
                                else:
                                    print('''
Aprovechas la debilidad de tus adversarios. Estás fuera de ti. No tienes ningún arma a mano
para descargar tu ira sobre los maniquíes. Te relajas y te compadeces de ellos.

De pronto sales del trance. ¿Qué ha pasado?''')
                                print('''
Entre los restos de los maniquíes encuentras {0}'''.format(palo))
                                getLoot(palo)
                                eventos.append('pelea')
                                eventos.remove('dope')
                                hora -= 3
                            else:
                                print('''
Te levantas y los maniquíes siguen ahí, esta vez sin vida, inmóviles.
Tu corazón vuelve a latir a su ritmo normal.''')
                                eventos.remove('dope')
                                hora -= 1
                else:
                    print('''
Hay pedazos de esa tela negra colgando por toda la pared de la habitación.
Colgados como murciélagos, esperando a ser cortados. En la esquina izquierda
yacen los restos de lo que aparentemente fue una batalla encarnecida entre
figuras de madera y látex. ¿Qué habrá pasado?''')
            elif opcion1 == '4':
                print('''
Hay un rinconcito secreto con todos los utensilios necesarios para hacer punto.
La lana rosa es la que más abunda. Parece que los tapetes de punto que cubren
todos los muebles de la casa no son obra de la abuela.''')
        elif opcion == '2':
            print('''
Hay una puerta cerrada en la habitación. Quizá puedas utilizar algo para abrirla...''')
            if promptItem('CLIP ROTO'):
                print('''
Usas el clip para abrir la puerta. Termina de romperse, pero al menos la puerta se ha abierto.''')
                loot.remove('CLIP ROTO')
                eventos.append('clipUsed')
        else:
            if 'dope' in eventos:
                eventos.remove('dope')
                print('''
Tu corazón vuelve a latir a su ritmo normal.''')
            break

def cocina():
    global loot
    global eventos
    global yaLooteado
    global salaActual
    global sala
    global hora
    while True:
        print('''
1) Mirar en la encimera.

2) Explorar el interior del armario.

3) Observar la mesa central.

4) Mirar la TV.

Pulsa 0 para cancelar.''')
        options = '0 1 2 3 4'.split()
        opcion = opcionValida(options)
        if opcion == '1':
            print('Está toda llena de brócoli. Ni a los insectos les gusta.')
            print('''
1) Abrir los cajones.

2) Usar el microondas.

3) Examinar la nevera.

Pulsa 0 para cancelar.''')
            options = '0 1 2 3'.split()
            opcion1 = opcionValida(options)
            if opcion1 == '3':
                if 'IMÁN' not in yaLooteado and 'pelusa' in eventos:
                    print('''
Estas cosas pegadas a la puerta podrían serte útiles. Encuentras {0}
- No es muy potente.'''.format('IMÁN'))
                    getLoot('IMÁN')
                else:
                    print('''
Abres la nevera y... ¡PUAJ! Huele fatal. Todo está podrido, hay gusanos
y cucarachas por todos lados.''')
                    if 'MANTEQUILLA' not in yaLooteado:
                        print('''
Encuentras {0} - Está caducada, pero no tiene gusanos.'''.format('MANTEQUILLA'))
                        getLoot('MANTEQUILLA')
            elif opcion1 == '2':
                if 'plomos' in eventos:
                    print('''
Se ha ido la luz, el microondas no funciona.
''')
                else:
                    print('¿Quieres calentar algo en el microondas?')
                    if promptItem('MANTEQUILLA'):
                        if 'tvon' in eventos:
                            print('''
¡PUM! Han saltado los plomos. No debería haber encendido la TV y el microondas a la vez,
el abuelo suele advertirlo.''')
                            eventos.remove('tvon')
                            eventos.append('plomos')
                        else:
                            print('''
La mantequilla se ha derretido. Cómo resbala...''')
                            loot.remove('MANTEQUILLA')
                            getLoot('MANTEQUILLA LÍQUIDA')
            elif opcion1 == '1':
                if 'cajonOpen' not in eventos:
                    print('''
Están atascados. El mecanismo debe estar oxidado. Quizá puedas utilizar algo para abrirlos.''')
                    if promptItem('MANTEQUILLA LÍQUIDA'):
                        eventos.append('cajonOpen')
                        loot.remove('MANTEQUILLA LÍQUIDA')
                        print('''
Ahora funcionan a la perfección.''')
                else:
                    if 'LLAVE DE LA CUBERTERÍA' not in yaLooteado:
                        print('''
Abres los cajones. Sólo ves cubiertos de plástico. Quizá puedas utilizar algo...''')
                        if promptItem(['MAGNETO', 'IMÁN']):
                            print('''
Encuentras {0}. Ahora sólo quedan cubiertos de plástico.'''.format('LLAVE DE LA CUBERTERÍA'))
                            getLoot('LLAVE DE LA CUBERTERÍA')
                    else:
                        print('''
Sólo quedan cubiertos de plástico.''')
        elif opcion == '2':
            if not 'openArmario' in eventos:
                print('''
Es un armario muy grande y pesado. Las puertas están cerradas con llave.
Quizá puedas abrirla con algo...''')
                if promptItem('LLAVE DE LA CUBERTERÍA'):
                    print('''
El armario se ha abierto de par en par.''')
                    eventos.append('openArmario')
            else:
                if 'TENEDOR' not in yaLooteado:
                    print('''
Dentro está la cubertería buena de la abuela. Sólo la saca cuando tiene visita.
Encuentras {0} - Está impecable, como si nadie lo hubiese utilizado nunca.'''.format('TENEDOR'))
                    getLoot('TENEDOR')
                else:
                    print('''
No crees que te vayan a hacer falta más cubiertos.''')
        elif opcion == '3':
            if 'CARAMELO' not in loot:
                print('''
En el centro de la mesa hay una fuente de cristal. Encuentras {0}
- A la abuela le encantan estos caramelos. Una vez probaste uno, no sabía nada
bien, te hizo sentir extraño.'''.format('CARAMELO'))
                getLoot('CARAMELO')
            else:
                print('''
La fuente de cristal está repleta de caramelos, pero mejor coger solo uno.''')
        elif opcion == '4':
            if 'plomos' in eventos:
                print('''
Se ha ido la luz, la TV no funciona.''')
            else:
                options = '0 1'.split()
                if 'tvon' not in eventos:
                    print('''
La TV está apagada.

1) Encender.

Pulsa 0 para cancelar.''')
                    opcion4 = opcionValida(options)
                    if opcion4 == '1':
                        print('Enciendes la TV.')
                        eventos.append('tvon')
                else:
                    print('''
La TV está encendida.

1) Apagar.

Pulsa 0 para cancelar.''')
                    opcion4 = opcionValida(options)
                    if opcion4 == '1':
                        print('Apagas la TV.')
                        eventos.remove('tvon')
        else:
            break

def pasilloEstrecho():
    global loot
    global yaLooteado
    global sala
    global eventos
    global salaActual
    global hora
    while True:
        options = '0 1'.split()
        print('''
1) Examinar al gato.
''')
        if 'neverLav' in eventos:
            print('''
2) Puerta de la lavandería.
''')
            options.append('2')
        print('''
Pulsa 0 para cancelar.''')
        opcion = opcionValida(options)
        if opcion == '1':
            if 'pateDado' not in eventos:
                print('''
Puar está durmiendo en medio del arco que separa las dos parrtes del pasillo.
Está muy gordo, no podrás moverlo.
Quizá puedas utilizar algo...
''')
                if promptItem('LATA DE PATÉ DE GATO'):
                    eventos.append('pateDado')
                    loot.remove('LATA DE PATÉ DE GATO')
                    print('''
Puar huele el paté y abre un ojo. Le explicas que necesitas pasar. Después de
negociar llegáis a la conclusión de que cambiaréis el servicio que requieres
por la lata de paté, pero Puar la quiere por adelantado. No sabes si hacerlo o no.
Te pide que confies en su palabra de gato, que confies en que se apartara tras
comerse la lata de paté.

1) Confiar

2) Desconfiar''')
                    options = '1 2'
                    opcion1 = opcionValida(options)
                    if opcion1 == '1':
                        print('''
Puar da buena cuenta del paté. Después, con la barriga llena, se recuesta y
comienza a ronronear. Le gritas que se aparte, que su palabra no vale nada.
No parece estar por la labor de levantarse.''')
                        if minigame_fight.game(salaActual):
                            eventos.append('winGato')
                            print('''
Puar admite la derrota. Se levanta de forma torpe y se aparta de tu camino.
Una lágrima asoma desde su ojo izquierdo.''')
                            hora -= 3
                            break
                        else:
                            print('''
Puar ha dañado toda tu autoestima. Pero eres valiente, te secas las lágrimas
y continúas tu camino.''')
                            hora -= 1
                            break
                    elif opcion1 == '2':
                        print('''
No confías en su palabra. Sabes que es un gato avaricioso y mentiroso.
No aceptas el trato.''')
                        break
                else:
                    break
            else:
                if 'winGato' not in eventos:
                    print('''
Puar está durmiendo en medio del arco que separa las dos partes del pasillo.
Esta vez no te andas con tonterías. Le gritas y te preparas para el ataque.''')
                    if minigame_fight.game(salaActual):
                        eventos.append('winGato')
                        print('''
Puar admite la derrota. Se levanta de forma torpe y se aparta de tu camino.
Una lágrima asoma desde su ojo izquierdo.''')
                        hora -= 3
                        break
                    else:
                        hora -= 1
                        break
                else:
                    print('''
Puar sigue durmiendo, pero a varios metros del arco que separa las dos partes
del pasillo.''')
                    break
        elif opcion == '2':
            print('''
Es la puerta que da a lavandería. Todavía se te eriza la piel de pensar
en el fantasma. Quizá puedas usar algo para tranquilizarte.''')
            if promptItem('CARAMELO'):
                print('''
Te hace sentir extraño, más relajado.''')
                eventos.remove('neverLav')
                loot.remove('CARAMELO')
        else:
            break

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
            eventos.append(cuadrosDoble[int(opcion)-1])
            if len(marcos) != 4:
                eventos.remove(marcoInEventos)
                print('''
Bajas el cuadro con el {0}'''.format(cuadroEnPared.lower()))
            print('''
Cuelgas el cuadro con el {0}'''.format(marcos[int(opcion)-1].lower()))

def pasilloCorto():
    global loot
    global yaLooteado
    global eventos
    global salaActual
    while True:
        print('''
1) Buscar en el interior del mueble.

2) Observar los cuadros.

3) Examinar el suelo.

Pulsa 0 para cancelar.
''')
        options = '0 1 2 3'.split()
        opcion = opcionValida(options)
        if opcion == '1':
            if 'pista' not in eventos:
                print('''
La puerta no se abre. Quizá puedas utilizar algo...''')
                promptItem('ESAESLABROMA')
            else:
                if 'PEGAMENTO' not in yaLooteado:
                    print('''
Se te había olvidado. Tú pusiste ese mensaje ahí, esta puerta se abre tirando del pomo
hacia la izquierda. Abres el armario y dentro encuentras las herramientos necesarias para
colgar cuadros y que no se caigan. Encuentras {0} - Está un poco seco,
pero puede que aún funcione.'''.format('PEGAMENTO'))
                    getLoot('PEGAMENTO')
                else:
                    print('''
No queda nada interesante aquí.''')
        elif opcion == '2':
            if 'pista' not in eventos:
                print('''
En la pared no están todos los cuadros originales. Algunos se han debido caer.
Todos están un poco inclinados.''')
                cuadros = ['madera', 'azul',
                'blanco', 'metal']
                cuadroSubido = ''
                for k in cuadros:
                    if k in eventos:
                        cuadroSubido = k
                if minigame_cuadros.game(cuadroSubido):
                    eventos.append('pista')
            else:
                print('''
Todos los cuadros están rectos.''')
        elif opcion == '3':
            if 'pista' not in eventos:
                print('''
Hay varios cuadros en el suelo, se han debido caer. Sin embargo, en la
pared solo cabe uno más. Podrías volver a colgar alguno.''')
                print()
                showMarcos()
            else:
                print('''
No hay sitio para colgar los cuadros del suelo.''')
        else:
            break

def escalera():
    global sala
    global loot
    global salaActual
    global eventos
    global yaLooteado
    while True:
        options = '0 1'.split()
        print('''
1) Cuadro eléctrico''')
        if 'keyUsed' not in eventos:
            print('''
2) Puerta cerrada''')
            options.append('2')
        print('''
Pulsa 0 para cancelar.''')
        opcion = opcionValida(options)
        if opcion == '1':
            print('''
La puertecita que lo cierra está rota, puedes acceder a las palancas sin
necesidad de la llave.''')
            if 'ANILLO' not in yaLooteado:
                print('''
Encuentras {0} - Estaba colgando de una de las palancas.'''.format('ANILLO'))
                getLoot('ANILLO')
            options = '0 1'.split()
            if 'plomos' in eventos:
                print('''
Los plomos están bajados.

1) Subirlos.

Pulsa 0 para cancelar.''')
                opcion1 = opcionValida(options)
                if opcion1 == '1':
                    eventos.remove('plomos')
            elif 'plomos' not in eventos:
                print('''
Los plomos están subidos.

1) Bajarlos.

Pulsa 0 para cancelar.''')
                opcion1 = opcionValida(options)
                if opcion1 == '1':
                    eventos.append('plomos')
                
        elif opcion == '2':
            print('''
Hay una puerta cerrada al final de las escaleras. Quizá puedas
utilizar algo para abrirla.''')
            if promptItem('LLAVE DE LA HABITACIÓN'):
                print('La puerta se ha abierto.')
                eventos.append('keyUsed')
        else:
            break

def passCode(code):
    if code != 'word':
        print('''
¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦
¦¦                 ¦¦
¦¦ - - - - - - - - ¦¦
¦¦                 ¦¦
¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦
¦¦¦¦¦¦¦ 1 2 3 ¦¦¦¦¦¦¦
¦¦¦¦¦¦¦ 4 5 6 ¦¦¦¦¦¦¦
¦¦¦¦¦¦¦ 7 8 9 ¦¦¦¦¦¦¦
¦¦¦¦¦¦¦¦¦ 0 ¦¦¦¦¦¦¦¦¦
¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦
''')
        respuesta = input('Introduce la contraseña: ')
        if respuesta == '51624370':
            print('''
¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦
¦¦                 ¦¦
¦¦ K A L A Y A Y A ¦¦
¦¦                 ¦¦
¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦
¦¦¦¦¦¦¦ 1 2 3 ¦¦¦¦¦¦¦
¦¦¦¦¦¦¦ 4 5 6 ¦¦¦¦¦¦¦
¦¦¦¦¦¦¦ 7 8 9 ¦¦¦¦¦¦¦
¦¦¦¦¦¦¦¦¦ 0 ¦¦¦¦¦¦¦¦¦
¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦
''')
            return True
        else:
            return False
    else:
        print('''
¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦
¦¦                 ¦¦
¦¦ - - - - - - - - ¦¦
¦¦                 ¦¦
¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦
¦¦ A B C D E F G H ¦¦
¦¦ I J K L M N O P ¦¦
¦¦ Q R S T U V W X ¦¦
¦¦¦¦¦¦¦¦ Y Z ¦¦¦¦¦¦¦¦
¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦
''')
        respuesta = input('Introduce la contraseña: ')
        if respuesta.upper() == 'KALAYAYA':
            print('''
¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦
¦¦                 ¦¦
¦¦ K A L A Y A Y A ¦¦
¦¦                 ¦¦
¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦
¦¦ A B C D E F G H ¦¦
¦¦ I J K L M N O P ¦¦
¦¦ Q R S T U V W X ¦¦
¦¦¦¦¦¦¦¦ Y Z ¦¦¦¦¦¦¦¦
¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦
''')
            return True
        else:
            return False

def vestidor():
    global loot
    global yaLooteado
    global eventos
    global sala
    global salaActual
    while True:
        options = '0 1 2 3'.split()
        print('''
1) Buscar en el armario.

2) Examinar el panel electrónico.

3) Sentarse en la silla plegable.''')
        if 'pass' in eventos:
            print('''
4) Buscar entre los cojines del sofá.''')
            options.append('4')
        print('''
Pulsa 0 para cancelar.''')
        opcion = opcionValida(options)
        if opcion == '1':
            print('''
El armario de tres cuerpos es el que más te llama la atención. Es casi más
grande que la habitación, podrías jugar ahí dentro a lo que quisieses.

1) Caminar hacia el fondo.

2) Buscar en los cajones.

Pulsa 0 para cancelar.''')
            options = '0 1 2'.split()
            opcion1 = opcionValida(options)
            if opcion1 == '1':
                print('''
Entras y caminas hacia el fondo apartando abrigos de piel que pesan el triple
que tú. Al fondo tocas algo frío con los dedos. La imagen de un campo lleno de
nieve viene a tu mente. Cuando te acercas para ver lo que realmente es, descubres
un par de cajas apiladas llenas de botellas. Las botellas tienen una etiqueta
con la cara del abuelo: "Licor KALAYAYA".
Habías tocado una de las que estaba fuera de las cajas.''')
                if 'gafas' not in eventos:
                    print('''
Sobre las cajas, al lado de las botellas ves las gafas del abuelo. Se las ha
debido de dejar aquí olvidadas.

1) Ponerte las gafas.

Pulsa 0 para cancelar.''')
                    options = '0 1'.split()
                    opcion1_1 = opcionValida(options)
                    if opcion1_1 == '1':
                        print('''
Te colocas las gafas sobre la nariz. Ves las cosas muy distintas ahora.''')
                        eventos.append('gafas')
            elif opcion1 == '2':
                print('''
Dentro de los cajones hay: calzoncillos, calcetines, camisetas interiores de algodón...''')
                if 'CORBATA' not in yaLooteado:
                    print('''
Entre toda la ropa interior encuentras {0} - Se han enredado con
unas cadenas y unas esposas de policía.'''.format('CORBATA'))
                    getLoot('CORBATA')
        elif opcion == '2':
            if 'pass' not in eventos:
                if 'gafas' not in eventos:
                    print('''
El panel es de metal, tiene botones con números y una pantalla que marca 8 espacios.
Debe ser para introducir una contraseña secreta.''')
                    juego = 'num'
                else:
                    print('''
El panel es de metal, tiene botones para todas las letras del abecedario y una pantalla
que marca 8 espacios. Debe ser para introducir una contraseña secreta.''')
                    juego = 'word'
                if passCode(juego):
                    print('''
La pantalla se ilumina de color verde. A continuación, la pared comienza a temblar. El
suelo se traga poco a poco el muro, como si se estuviese fundiendo. Al terminar el
movimiento descubres una parte de la habitación que estaba oculta tras una pared.
Ahora la habitación es el doble de grande. En esta nueva zona hay un sofá enorme, de
color rojo vivo. Las luces son de color rojizo e iluminan de forma tenue.
Hay tres cámaras en trípodes, enfocadas hacia el sofá, además de un par de plantas
tropicales en tiestos de color negro.''')
                    eventos.append('pass')
                else:
                    print('''
La pantalla se ilumina de color rojo. Los caracteres que habías introducido se borran.''')
            else:
                print('''
Ahora la habitación es el doble de grande. En esta nueva zona hay un sofá enorme, de
color rojo vivo. Las luces son de color rojizo e iluminan de forma tenue.
Hay tres cámaras en trípodes, enfocadas hacia el sofá, además de un par de plantas
tropicales en tiestos de color negro.''')
        elif opcion == '3':
            print('''
No parece muy buena idea perder tiempo en esta silla. Sobre la silla hay un libro
encuadernado en piel.''')
            if 'gafas' not in eventos:
                print('''
Lo abres, intentas leerlo pero no entiendes nada, sólo hay números.''')
            else:
                options = '1 2'.split()
                print('''
Lo abres, ahora puedes leer perfectamente todo lo que pone. Es un libro de carpintería.
Explica paso a paso como construir algunas cosas.
GANCHO, necesitas cortar, metal, madera y algo para pegar. Es un poco lioso pero te ha
quedado claro. ¿Seguir leyendo?

1) Sí

2) No
''')
                opcion3 = opcionValida(options)
                if opcion3 == '1':
                    print('''
MAGNETO, necesitas un imán, un hilo que aguante el peso un objeto donde atarlo y unirlo
todo. Hay que seguir muchos pasos pero te los has aprendido. ¿Seguir leyendo?

1) Sí

2) No
''')
                    opcion3 = opcionValida(options)
                    if opcion3 == '1':
                        print('''
CUERDA, necesitas trozos de tela, no importa que esten sucios y tijeras para darle forma.
Es el más sencillo, pero te ha costado memorizarlo.''')
                        eventos.append('book')
        elif opcion == '4':
            if 'LLAVE DE LA HABITACIÓN' not in yaLooteado:
                print('''
El sofá es enorme y tus brazos son cortos, no llegas a alcanzar nada.
Quizá puedas utilizar algo...''')
                if promptItem('MAGNETO'):
                    print('''
Metes el {0} en uno de los pliegues del sofá. Escuchas un "CLICK", tiras del hilo
atado al anillo. Pegado al {0} hay una pelusa de color rojo.
Dentro de la pelusa encuentras {1}.'''.format('MAGNETO', 'LLAVE DE LA HABITACIÓN'))
                    getLoot('LLAVE DE LA HABITACIÓN')
            else:
                print('''
Metes el {0} en uno de los pliegues del sofá. No pasa nada.'''.format('MAGNETO'))
        else:
            break

def hall():
    global eventos
    global sala
    global salaActual
    global yaLooteado
    global loot
    while True:
        print('''
1) Mirar los libros.

2) Abrir la puerta.

Pulsa 0 para cancelar.''')
        options = '0 1 2'.split()
        opcion = opcionValida(options)
        if opcion == '1':
            print('''
Hay demasiados, comienzas a sacarlos poco a poco de los cajones, en busca de 
uno que tenga más dibujos que letras. De dentro de uno de los libros cae una nota
doblada. Tiene fecha de hace 6 años. Dice: "Papá, lo siento con todo mi corazón. 
No puedo seguir con esto, no puedo vivir con ello, dijiste que se haría poco a poco 
más sencillo, pero no es así. Que él no sepa nada, nunca, tiene tus ojos.
Te quiero y siempre te querré, Ana."
''')
        elif opcion == '2':
            if 'exitOpen' not in eventos:
                print('''
Es una puerta enorme y pesada, está cerrada con llave. Quizá puedas utilizar algo.''')
                if promptItem('LLAVES DE LA CASA'):
                    print('''
Justo en el momento en el que metes la llave en la cerradura, suena el timbre.

1) Responder

2) Ignorar
''')
                    options = '1 2'.split()
                    opcion2 = opcionValida(options)
                    if opcion2 == '1':
                        print('''
Preguntas quién está al otro lado de la puerta y te responde una voz que te es familiar.
Tu vecina lleva mucho tiempo viviendo sola, aprovecha cada oportunidad para hartar a
quien sea a preguntas. Sabes lo que viene, y no te queda mucho tiempo.
Te preparas para el enfrentamiento.
''')
                        if minigame_fight.game(salaActual):
                            eventos.append('exitOpen')
                        else:
                            print('''
La vecina ha destrozado toda tu autoestima, pero tú eres fuerte, te secas las lágrimas
y te pones en pie dispuesto a seguir tu camino.''')
                    elif opcion2 == '2':
                        print('''
Vuelves a coger la llave, te alejas silenciosamente de la puerta.
''')
            else:
                print('''
Es una puerta enorme y pesada, está abierta de par en par. La vecina se ha ido llorando.''')
        else:
            break

def habitacion():
    global eventos
    global sala
    global salaActual
    global yaLooteado
    global loot
    while True:
        options = '0 1 2'.split()
        print('''
1) Mirarte en el espejo.

2) Buscar en la mesita de noche.''')
        if 'mascarillaPuesta' not in eventos:
            print('''
3) ¿Olor raro?''')
            options.append('3')
        if 'openCaja' in eventos:
            print('''
4) Mirar dentro de la caja fuerte.''')
            options.append('4')
        print('''
Pulsa 0 para cancelar.''')
        opcion = opcionValida(options)
        if opcion == '1':
            if 'gafas' not in eventos:
                print('''
Tienes cara de cansado. Es normal, siendo un maestro con los números como lo eres.
Ese último 0 se llama CANCELBRAH. No esperábamos que resolvieses el puzzle con
dígitos, pero tanto calcular hace que tu vista sufra. Ve a por unas gafas, ¿quieres?''')
            else:
                print('''
Qué raro te ves con las gafas del abuelo. Un momento, ves algo a través del espejo.

1) Apartar el espejo.

Pulsa 0 para cancelar.''')
                options = '0 1'.split()
                opcion1 = opcionValida(options)
                if opcion1 == '1':
                    if 'openCaja' not in eventos:
                        print('''
Es una caja fuerte. Está cerrada, quizá puedas utilizar algo para abrirla...''')
                        if promptItem('LLAVE CAJA FUERTE'):
                            print()
                            print('La caja se ha abierto.')
                            eventos.append('openCaja')
                    else:
                        print('''
La caja se ha abierto.''')
        elif opcion == '2':
            if 'LLAVE CAJA FUERTE' not in yaLooteado:
                print('''
Entre la ropa interior encuentras {0}.'''.format('LLAVE CAJA FUERTE'))
                getLoot('LLAVE CAJA FUERTE')
            else:
                print('''
Sólo encuentras ropa interior.''')
        elif opcion == '3':
            print('''
Viene del baño de los abuelos. Abres un poco la puerta y una ráfaga de aire
pestilente te cierra la garganta.
Es horroroso, no podrás pasar a menos que utilices algo...''')
            if promptItem('MASCARILLA'):
                print('''
Te pones la mascarilla. Sigue oliendo mal, pero al menos es soportable.''')
                eventos.append('mascarillaPuesta')
        elif opcion == '4':
            if 'MASCARILLA' not in yaLooteado:
                print('''
Dentro de la caja hay un montón de papeles, guantes de plástico y...
¡Qué guay! Encuentras {0} - Siempre te ha hecho ilusión ponerte una.'''.format('MASCARILLA'))
                getLoot('MASCARILLA')
            else:
                print('''
Dentro de la caja hay un montón de papeles y guantes de plástico.

1) Revisar los papeles.

Pulsa 0 para cancelar.''')
                options = '0 1'.split()
                opcion4 = opcionValida(options)
                if opcion4 == '1':
                    print('''
Puf... qué aburrido leer papeles de mayores. Hay unos que pone "Orden de registro
de la propiedad", pero sobre todo hay papeles rotos donde salen fotos de mujeres
bajo un título en mayúsculas: "DESAPARECIDA". 
Al parecer se han perdido. Son muchas. Cuando tú te pierdes en el supermercado
pasas mucho miedo. No sabías que los mayores también se podían perder.''')
        else:
            break


def wc():
    global eventos
    global sala
    global salaActual
    global yaLooteado
    global loot
    while True:
        options = '0 1 2'.split()
        print('''
1) Lavarte las manos.

2) Apartar la cortina.
''')
        if 'winRata2' in eventos:
            print('''
3) Examinar la bañera.

4) Salir por la ventana.''')
            options.append('3')
            options.append('4')
        print('''
Pulsa 0 para cancelar.''')
        opcion = opcionValida(options)
        if opcion == '1':
            print('''
La abuela siempre dice que todo se cura con agua y jabón.
''')
            if 'herido' in eventos:
                print('''
Pica un poco, pero todo lo que pica cura.
''')
                eventos.remove('herido')
        elif opcion == '2':
            if 'winRata2' not in eventos:
                if 'fightRata2' not in eventos:
                    if 'winRata' in eventos:
                        print('''
Avanzas hacia la cortina, pero de pronto aparece aquella rata valiente
que conociste en la lavandería. En su rostro no hay malicia, no hay venganza,
solo honor. De algún modo te lo esperabas, sabías que volveríais a medir vuestras
fuerzas. Siempre has tenido esa capacidad de ver a lo que estás destinado.
Notas en el ambiente que será una batalla dura, que pondrá en riesgo la percepción
que tienes de ti mismo.
Te remangas y te preparas para la batalla.
''')
                    else:
                        print('''
Avanzas hacia la cortina, pero de pronto aparece una rata. En su mirada puedes
leer que no te piensa dejar pasar tan fácilmente.
Te remangas y te preparas para la batalla.
''')
                    eventos.append('fightRata2')         
                else:
                    if 'winRata' in eventos:
                        print('''
Ahí está la rata mirandote. En su rostro no hay malicia, no hay venganza, solo honor.
Notas en el ambiente que será una batalla dura, que pondrá en riesgo la percepción
que tienes de ti mismo. 
Te remangas y te preparas para la batalla.
''')
                if minigame_fight.game(salaActual):
                    if 'winRata' in eventos:
                        print('''
La rata cae rendida te lanza una mirada de aprobación. Acepta que tienes el derecho
a pasar hacia la cortina que tan fieramente ha defendido. 
Por último se gira y huye hacia un hueco en la pared.
''')
                    else:
                        print('''
Te lanza una mirada de odio y huye hacia un hueco en la pared. No sabes por qué, 
pero crees que volverás a ver a esa valiente ratita que se alzó contra un enemigo
al que no podía vencer, por defender lo que era suyo.  

Esto te llena de determinación. 
''')
                    print('''
Apartas la cortina y descubres que el baño sigue un buen trecho tras ella.
Hay una bañera llena de un líquido oscuro, entre rojo y verde.
Tras ella hay una bañera entreabierta. Tapada con papel de periódico.''')
            else:
                print('''
Apartas la cortina y descubres que el baño sigue un buen trecho tras ella.
Hay una bañera llena de un líquido oscuro, entre rojo y verde.
Tras ella hay una bañera entreabierta. Tapada con papel de periódico.''')                    
        elif opcion == '3':
            print('''
De aquí viene ese horrible olor. Está hasta arriba del líquido oscuro. Mientras
la observas, del fondo emerge un hueso. Es uno de los que le gustan a D'Artacán,
siempre los lleva a todos lados.

1) Tocar el líquido.

Pulsa 0 para cancelar.''')
            options = '0 1'.split()
            opcion3 = opcionValida(options)
            if opcion3 == '1':
                print('''
Metes un dedo en el líquido.... ¡ay, quema!''')
                eventos.append('herido')
        elif opcion == '4':
            print('''
Está muy alto. Quizás puedas utilizar algo para ayudarte a bajar...''')
            if promptItem('CUERDA'):
                if 'herido' in eventos:
                    print('''
Con las manos así no puedes bajar por la cuerda.''')
                else:
                    print('''
Atas la cuerda al grifo de la bañera. Ahora puedes bajar por ella hasta la calle.''')
                    eventos.append('windowOpen')
        else:
            break
################################          

####_______________________________________

print('''
 ___                   ___                                                   
(   )                 (   )                                                  
 | |   ___     .---.   | |    .---.   ___  ___    .---.   ___  ___    .---.  
 | |  (   )   / .-, \  | |   / .-, \ (   )(   )  / .-, \ (   )(   )  / .-, \ 
 | |  ' /    (__) ; |  | |  (__) ; |  | |  | |  (__) ; |  | |  | |  (__) ; | 
 | |,' /       .'`  |  | |    .'`  |  | |  | |    .'`  |  | |  | |    .'`  | 
 | .  '.      / .'| |  | |   / .'| |  | '  | |   / .'| |  | '  | |   / .'| | 
 | | `. \    | /  | |  | |  | /  | |  '  `-' |  | /  | |  '  `-' |  | /  | | 
 | |   \ \   ; |  ; |  | |  ; |  ; |   `.__. |  ; |  ; |   `.__. |  ; |  ; | 
 | |    \ .  ' `-'  |  | |  ' `-'  |   ___ | |  ' `-'  |   ___ | |  ' `-'  | 
(___ ) (___) `.__.'_. (___) `.__.'_.  (   )' |  `.__.'_.  (   )' |  `.__.'_. 
                                       ; `-' '             ; `-' '           
                                        .__.'               .__.'               
''')

##introduction()
##newload()
##if new:

if new_load():
    malo = ''
    showIntroduction()
    sala = [1,1]
    salaActual = getNSala()
    loot = []
    yaVisitado = []
    eventos = []
    yaLooteado = []
    hora = 120
    
else:
    variables = cargar()
    malo = variables[0]
    sala = variables[1]
    salaActual = getNSala()
    loot = variables[2]
    yaVisitado = variables[3]
    eventos = variables[4]
    yaLooteado = variables[5]
    hora = int(variables[6][0])
    
while True:
    room()

