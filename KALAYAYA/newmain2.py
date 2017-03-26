import sys
import os
from stat import S_IREAD
import random
import time
import minigame_lata
import minigame_furia
import minigame_fight
import minigame_cuadros

# probando github

def getHora():
    global hora
    H = int((180-hora)*(2/3))
    h = str(10 + H//60)
    m = str(H%60)
    if len(m) == 1:
        m = '0'+m
    return h+':'+m
####completeeeee
def createWinFile(salida):
    nFile = 'registro.txt'
    if salida == 'salidaMadre':
        fichero = open(nFile, 'w')
        fichero.write('74442037M')
    else:
        fichero = open(nFile, 'w')
        fichero.write('73024447A')
    fichero.close()
##    os.chmod(nFile, S_IREAD)

def ending(salida):
    global eventos
    global malo
    if salida == 'salidaMadre':
        if 'finAbuelos' not in eventos:
            primerEnding = True
        else:
            primerEnding = False
    elif salida == 'salidaAbuelos':
        if 'finMadre' not in eventos:
            primerEnding = True
        else:
            primerEnding = False
    if primerEnding:
        newPrint('''
Al salir a la calle los rayos del sol te dañan la vista. No tardas nada en
acostumbrarte. La piel se te sonroja y sientes el cálido abrazo del viento.
Miras hacia adelante y ves el lugar donde vives. Espléndido. Desde aquí ya
puedes escuchar a tus amigos jugando en el parque, a los vecinos hablando,
el ajetreo del tráfico y a un par de vendedores ambulantes tratando de
endosar sus productos de "alta necesidad".
Huele a libertad, son las {0}AM, los abuelos y D'Artacán no han vuelto aún
de la iglesia. Menos mal que te escaqueaste con ese "dolor de cabeza", de
haber ido te habrías perdido esta mañana tan entretenida.'''.format(getHora()))
        if malo == 'abuela':
            newPrint('''
De pronto recuerdas el pedacito de tarata. Das buena cuenta de él, a bocados
pequeños, para que no se acabe demasiado rápido. Está riquísima, 
ha valido la pena cogerla. Justo cuando te la acabas, llegas al parque y ahí
están tus amigos. Parece que te estaban esperando. ¡A divertirse!''')
        elif malo == 'abuelo':
            newPrint('''
Tocas tus bolsillos y descubres que ahí están las monedas.
Entras en el kiosco y compras el último sobre de cromos que queda.
¡Ahí está, Farfetch\'d! Vas a ser la envidia del recreo.''')
        elif malo == 'perro':
            newPrint('''
Tiras la pelota al suelo y la llevas hasta el parque dándole patadas. Cuando 
llegas tus maigos te ven, bajan corriendo de sus bicis y comienzan a preparar
unas porterías improvisadas con unas piedras. ¡A divertirse!''')
        newPrint('''
Ey, tú. Sí tú. Dejémosle solo...¿No crees? Me encanta cuando está así de feliz.
No nos han presentado como es debido: Soy amor, soy asco, soy miedo, soy odio...
Soy todo aquello que eres capaz de sentir. 
Después de lo que ha pasado, me parecía apropiado hablar unas cosas contigo. 
Verás, conozco muy bien a este niño. Es un buen chico: inocente, travieso... 
Me apasiona la vitalidad de ese pequeño. Le conozco tan bien que sé incluso
lo que va a hacer a continuación; su cabeza se va a llenar de remordimientos.
Va a dar la vuelta, va a tomar aire y va a volver a casa a esperar a su família 
para devolver lo que ha cogido.
Yo no soy capaz de cambiar el futuro. No manejo el transcurso de su porvenir,
lo haces tú. 
Ese es tu trabajo.
Lo hiciste bien antes, quizá de forma un poco torpe, pero nadie nace sabiendo.
Mira, no te pido que le hagas cambiar de opinión sobre volver a casa, eso lo 
hará con tu ayuda o sin ella. Cuando un sentimiento sincero,
salido del corazón, le guía... Es mucho más poderoso que yo, e incluso que tú.
Sólo te pido que vuelvas a sacarlo de ahí dentro. 
Este día se repetirá una y otra vez hasta que por fin comprenda. 
Hasta el día en el que decida, de propia voluntad, abandonar este mundo. 
Como ya hicieron otros muchos antes que él.
Dentro de esa casa hay muchos más secretos que podrían hacerle despertar de su
inocencia. Ayúdale, por favor.

''')
        createWinFile(salida)
        try:
            os.remove('save.txt')
            sys.exit()
        except:
            sys.exit()
    else:
        newPrint('''
Al salir a la calle los rayos del sol te dañan la vista. No tardas nada en
acostumbrarte. La piel se te sonroja y sientes el cálido abrazo del viento.
Miras hacia adelante y ves el lugar donde vives. Espléndido.
Te descubres caminando en sentido contrario al parque. Necesitas aclarar tu
cabeza, poner en orden tus ideas. Todo lo que has visto dentro de esa casa...
Tu corazón se encoje. Recuerdas su abrazo cálido, su dulce voz, el ritmo
de su respiración, el olor de su piel. La recuerdas. Todo viene a tu memoria. 
No estás triste, por fin has comprendido, has entendido cómo funcionan las cosas. 
La has entendido a ella. El odio te había hecho olvidarla. Pero ahora la 
comprendes. Te dejó sin decir adiós y así te dió la más grande de las lecciones. 
Te marcó la solución de este puzzle. 
Lo consisuió: creciste feliz.
Tus pies dejan de caminar, ¿Cuánto timpo llevas andando? Estás temblando, el 
miedo te invade, caes al suelo enmedio de un llanto desesperado.
Pero eres valiente, te secas las lágrimas dispuesto a continuar con tu camino.
Te paras en el borde del puente más alto de la ciudad. Cierras los ojos, sonries.
Huele a libertad, son las 12:00AM, los abuelos y D'Artacán ya han debido volver 
de la iglesia. Menos mal que te escaqueaste con ese "dolor de cabeza", de haber 
ido te habrías perdido esta mañana tan entretenida.
''')
        try:
            os.remove('save.txt')
            os.remove('log.txt')
            sys.exit()
        except: 
            os.remove('log.txt')
            sys.exit()
            
### completee
def gameOver():
    global hora
    global eventos
    global malo
    if hora <= 90 and 'campanadas' not in eventos:
        newPrint('''
Se escuchan once campanadas. Debe de quedar cerca de una hora
hasta que vuelvan los abuelos.
''')
        eventos.append('campanadas')
    if hora <= 0:
        newPrint('''
Suenan las 12 campanadas de la iglesia. Escuchas la cerradura de la 
puerta principal abrirse. Intentas esconderte, correr, pero es demasiado 
tarde. ''')
        if malo == 'abuela':
            newPrint('''
La abuela nada mas verte sabe lo que has hecho. Consigues esquivar 
el primer zapatillazo, el resto te alcnzan todos en la espalda. Intentas 
explicarle lo que ha pasado, pero duele tanto que no puedes hablar. 
No creo que te vuelva a apetecer tarta nunca más.
Te encierras en tu cuarto. No saldrás hasta que vuelvas a estar solo.
''')
        elif malo == 'abuelo':
            newPrint('''
El abuelo ya se ha dado cuenta de que su dinero ha desaparecido.
Consigues esconderte debajo de la mesa del salón. Tienes cubiertos todos
los ángulos, al menos eso pensabas. 
¡Uf! Qué golpe... no creo que mañana recuerdes nada de lo que ha pasado.
''')
        elif malo == 'perro':
            newPrint('''
D'Artacán es capaz de olfatear la situación en solo unos segndos. 
El primer lametazo lo sientes en la nuca. El resto te alcanzan todos en 
la cara. D'Artacán sabe el asco que te dan sus babas, sigue hasta que sueltas
la pelota. Después del baño desinfectante, estás tan cabreado que te vas a 
tu cuarto prometiéndote que no saldrás hasta que vuelvas a estar solo.
''')
            newPrint('''
                        GAME OVER''')
        try:
            os.remove('save.txt')
            sys.exit()
        except:
            sys.exit()

def previousWin():
    try:
        fichero = open('completed.txt','r')
        check = []
        for i in fichero:
            if i == '74442037M':
                check.append(1)
            if i == '73024447A':
                check.append(2)        
        fichero.close()
        return check
    except:
        return []
    
        
def opcionValida(options):
    opcion = input('''
Escoge una opción válida: ''')
    while opcion not in options:
        opcion = input('''
Escoge una opción válida: ''')
    return opcion

def newPrint(cadena, delay=0.015):
    for i in cadena:
        print(i, end='')
        time.sleep(delay)
    print()

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
    try:
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
    except:
        print('''
No existe partida guardada. Creando partida nueva.''')
        return None
        

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
        print('''
A la abuela no le gusta que comas con las manos. Cuando se entere de que falta un
trozo de su tarta se enfadará mucho. Agarrará su zapatilla. Más te vale salir de
casa antes de que llegue...''')
        malo = 'abuela'
    if opcion == '2':
        print('''
El abuelo es un viejo tacaño, no le va a hacer gracia que hayas cogido su dinero.
Siempre te regaña con esas cosas. Solo pensar en su palo de andar, hace que se te
erice el bello de la nuca. Más te vale salir de casa antes de que llegue...''')
        malo = 'abuelo'
    if opcion == '3':
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
    print('''|______________________________________|''')
    if not huida:
        print('''
Pulsa (0) para cancelar.''')

def movSala(despl):
    global sala
    global salaActual
    if not (salaActual == 14 and despl == '2'):
        if despl == '1':
            sala[0] -= 2
        if despl == '2':
            sala[1] += 4
        if despl == '3':
            sala[0] += 2
        if despl == '4':
            sala[1] -= 4
    else:
        sala[0] += 2
        
    
    
def getNSala():
    NSALAS = [[1,1], [1,5], [3,1], [3,5], [3,9], [5,1], [5,5], [5,9], [5,13], [7,1], [7,5], [7,13], [9,5], [9,9], [9,13], [11,9]]
    return NSALAS.index(sala) + 1

def getDescription():
    global salaActual
    DESCRIPCIONES = ['''
Está patas arriba, las sábanas bailan con el viento que entra por la ventana
entreabierta, los cajones están llenos de material de dibujo con el que has
decorado todas las paredes. La alfombra tupida está llena de piezas de Lego
y dibujos caídos del techo, hace tiempo que ya no caben en las paredes...''', ##cuarto
                     '''
Es muy pequeño. La bañera está llena de juguetes flotando, el WC está repleto
de pegatinas que vienen en los bollos. Al lado hay un mini WC que nunca has
sabido para qué sirve. Hay muchos cómics repartidos por el mobiliario, apilados
en columnas y almacenados en cajas.''', ##baño
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
tanta tela negra.''', ##taller
                     '''
La cocina apesta a eso verde tan sano que a la abuela le interesa tanto que coma.
Los cajones están abiertos y forrados por todas partes de unas pegatinas en las
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
viene de tomar el aire. Las batas largas de color rosa tapan todo el fondo del mobiliario.
Varios armarios roperos enmarcan la sala. El más grande es el de los abrigos. Al lado hay
un panel con números. En el centro de la sala, sobre la moqueta de pelo marrón, hay una silla
de madera plegáble con unos calzoncillos colgando del respaldo. Hay demasiado eco para una
habitación de este tamaño. ''', ##vestidor
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
    newPrint('''
Guardas {0} en tus bolsillos.'''.format(item))

def showLoot():
    global loot
    if len(loot) != 0:
        print('')
        for k in range(len(loot)):
            if len(str(k+1)) == 1:
                print('({0})      {1}'.format(k+1, loot[k]))
            else:
                print('({0})     {1}'.format(k+1, loot[k]))
    else:
        print('''
No hay nada en tus bolsillos.''')

def itemOptions():
    global loot
    opciones = ['0']
    for i in range(1, len(loot)+1):
        opciones.append(str(i))
    return opciones

def useItem():
    global loot
    if len(loot) == 0:
        print('''
No tienes nada en tus bolsillos.''')
        return 'noitem'
    else:
        options = itemOptions()
        showLoot()
        print('''
Pulsa 0 para cancelar.''')
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
        print('''
No parece que esto te pueda ayudar mucho.''')
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

def room():
    global salaActual
    global sala
    global loot
    global yaLooteado
    global eventos
    global hora
    print()
    print(getName())
    if getName() not in yaVisitado:
        print(getDescription())
        yaVisitado.append(getName())
    while True:
        gameOver()
        print('''
 ______________________________________________________________
|                                                              |
| (1) Interactuar        (2) Moverte            (3) Mapa       |
| (4) Bolsillos          (5) Guardar            (6) Salir      |
|______________________________________________________________|''')
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
        gameOver()
        newPrint('''
1) Caminar directamente hacia la puerta; no hay tiempo que perder...
   
2) Examinar las paredes, puede que encuentres algo útil...

3) Buscar en los cajones. Va a ser complicado, están hasta los topes...

Pulsa 0 para cancelar.''')
        options = '0 1 2 3'.split()
        opcion = opcionValida(options)
        if opcion == '0':
            break
        if opcion == '1':
            newPrint('''
Pisas una de tus mega-construcciones Lego, duele tanto que caes al suelo
y te retuerces durante un rato aguantando el llanto. Desde el suelo
la habitación parece mucho más grande.''')
            newPrint('''
1) Alargar la mano y buscar bajo la cama.

2) Construir una fortaleza con piezas de Lego.

Pulsa 0 para cancelar.''')
            options = '0 1 2'.split()
            opcion1 = opcionValida(options)
            if opcion1 == '1':
                if calcetines not in yaLooteado:
                    newPrint('Encuentras {0} - Llevaban ahí abajo mucho tiempo.'.format(calcetines))
                    getLoot(calcetines)
                else:
                    newPrint('Solo encuentras polvo.')
            if opcion1 == '2':
                newPrint('''
La construcción es colosal, las columnas góticas y los arcos ojivales
son tu punto fuerte.''')
        if opcion == '2':
            newPrint('''
1) Observar los dibujos.

2) Revisar el muro de las tareas.

Pulsa 0 para cancelar.''')
            options = '0 1 2'.split()
            opcion2 = opcionValida(options)
            if opcion2 == '1':
                if clip not in yaLooteado:
                    newPrint('''
Ahí está la abuela, y ahí el abuelo. Ese es Puar jugando en el campo y
ahí estáis Marta y tú cogidos de la mano, el dibujo de D'Artacán dormido
se tambalea en la pared hasta que cae al suelo.

Encuentras {0} - No podía sostenerse mucho más ahí con esto.'''.format(clip))
                    getLoot(clip)
                else:
                    newPrint('''
El dibujo de D'Artacán dormido era más bonito cuando aún estaba colgado.''')
            if opcion2 == '2':
                newPrint('''
Tienes pendiente: limpiar el baño, la cocina, el salón, el pasillo y el
vestidor de los abuelos.''')
        if opcion == '3':
            if iman not in yaLooteado and 'pelusa' not in eventos:
                newPrint('''
Sacas una pelusa enorme. Pesa demasiado para ser una pelusa, es suave...''')
                newPrint('''
1) Frotarla con la mano.

2) Tirarla a la basura.

Pulsa 0 para cancelar''')
                options = '0 1 2'.split()
                opcion3 = opcionValida(options)
                if opcion3 == '1':
                    newPrint('''
Dentro parece haber algo, aunque te da bastante asco tocar la pelusa.
Encuentras {0} - Jugar a ser Magneto atrayendo hacia tus manos
las chinchetas es de las cosas que más te divierten. A la abuela
no le hace tanta gracia.'''.format(iman))
                    getLoot(iman)
                if opcion3 == '2':
                    newPrint('''
Podría ser un monstruo, no necesitas más interrupciones.''')
                    eventos.append('pelusa')
            else:
                newPrint('''
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
        gameOver()
        newPrint('''
1) Buscar en el cajón que hay debajo del lavabo.

2) Examinar las cajas.

3) Mirar en la bañera.

4) Lavarte las manos.

Pulsa 0 para cancelar.
''')
        options = '0 1 2 3 4'.split()
        opcion = opcionValida(options)
        if opcion == '1':
            if evPosibles[0] not in eventos:
                newPrint('No puedes abrir las puertas, hay algo bloqueándolas.')
            else:
                if hilo not in yaLooteado:
                    newPrint("")
                    newPrint('''
El cajón está casi vacío. Encuentras {0} - Normalmente esas
cosas están en el baño de la abuela, pero lo cogiste para jugar
y nadie lo ha echado en falta.
'''.format(hilo))
                    getLoot(hilo)
                else:
                    newPrint('Ya solo queda polvo en el cajón.')
        elif opcion == '2':
            newPrint('''
La caja más grande y pesada está frente al lavabo, es la de los cómics
de superhéroes.''')
            newPrint("")
            newPrint('''
1) Apartar la caja.

2) Mejor dejarla donde está.''')
            options = '1 2'.split()
            opcion2 = opcionValida(options)
            if opcion2 == '1':
                if evPosibles[1] not in eventos:
                    newPrint('''
No hay mucho sitio donde ponerla...''')
                else:
                    if evPosibles[0] not in eventos:
                        newPrint('''
Pones la caja dentro de la bañera vacía. Será mejor que recuerdes que
está ahí la proxima vez que vayas a darte un baño.''')
                        eventos.append(evPosibles[0])
                    else:
                        newPrint('''
Donde está ya no molesta... Será mejor que recuerdes que está ahí
la próxima vez que vayas a darte un baño...''')
        elif opcion == '3':
            if evPosibles[1] not in eventos:
                newPrint('''
La bañera está llena de agua sucia y juguetes.''')
            else:
                newPrint('''
En la bañera solo quedan los juguetes.''')
            newPrint("")
            newPrint('''
1) Darse un baño.

2) Quitar el tapón.

Pulsa 0 para cancelar.''')
            options = '0 1 2'.split()
            opcion3 = opcionValida(options)
            if opcion3 == '1':
                if evPosibles[1] not in eventos:
                    newPrint('''
El agua está un poco fría y sabe algo raro, pero siempre es divertido
jugar un rato con los patitos.''')
                else:
                    newPrint('''
Ya no hay agua en la bañera.''')
            if opcion3 == '2':
                if evPosibles[1] not in eventos:
                    newPrint('La tubería se traga todo el agua.')
                    eventos.append(evPosibles[1])
                else:
                    newPrint('''
Por mucho que lo pongas y lo quites, no creo que vaya a cambiar nada.
Ya no hay agua.''')
        elif opcion == '4':
            newPrint('''
La abuela siempre dice que todo se cura con agua y jabón.''')
            if 'herido' in eventos:
                newPrint('''
¡Ay, pica! Pero la abuela dice que todo lo que pica cura.''')
                eventos.remove('herido')
                hora -= 2
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
        gameOver()
        newPrint('''
1) Buscar entre las cosas del suelo.

2) Palpar los objetos del primer estante, no llegas a ver lo que son...

Pulsa 0 para cancelar.

¿Qué quieres hacer? ''')
        options = '0 1 2'.split()
        opcion = opcionValida(options)
        if opcion == '1':
            newPrint('''
Está todo lleno de herramientas de jardinería... ¿Para qué quiere el abuelo
todo esto, si no tenemos jardín?''')
            newPrint('''
1) Trastear las máquinas.

2) Buscar entre las bolsas de recambios.

Pulsa 0 para cancelar.

¿Qué quieres hacer? ''')
            opcion1 = opcionValida(options)
            if opcion1 == '1':
                if 'herido' not in eventos:
                    newPrint('''
Está oscuro, no ves qué estás tocando, rozas un cuchillo muy afilado
y te abres una herida muy grande en la mano. Debes curarla rápido o
se infectará.''')
                    eventos.append('herido')
                else:
                    newPrint('''
Está oscuro, no ves qué estás tocando, rozas un cuchillo muy afilado.
Te abres aun más la herida de la mano. Debes curarla rápido o se
infectará.''')
            if opcion1 == '2':
                newPrint('''
Hay una que te llama la atención, es muy grande.''')
                if 'bolsa' in eventos:
                    newPrint('''
La has abierto con el trozo de cristal y ahora está todo tirado por el suelo.

1) Examinar el contenido de la bolsa.

Pulsa 0 para cancelar.''')
                    options = '0 1'.split()
                    opcion1_1 = opcionValida(options)
                    if opcion1_1 == '1':
                        newPrint('''
A través del corte ves mucha ropa, diplomas y unas monedas doradas muy grandes con
correas de colores, como si la bolsa sangrase recuerdos. La ropa se parece a la
que lleva tu amiga Marta: hay prendas pequeñas, medianas y otras más grandes.
Esto no puede ser de la abuela, ni las más anchas le vendrían. En los diplomas
pone que la universidad se enorgullece de entregar la matricula de honor en biología
a Ana, el apellido está tapado por una firma enorme. Tú también sacas siempre
buenas notas, ojalá un día te den un diploma. En las monedas pone Federación
Olímpica de Tenis. Son muy bonitas, decides colgarte una al cuello.''')
                else:
                    newPrint('''
Está cerrada con un nudo muy fuerte, no puedes deshacerlo.
Quizá puedas utilizar algo para abrirla.''')
                    if promptItem('TROZO DE CRISTAL'):
                        newPrint('''
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
                newPrint('''
No quiero volver a pasar la mano por ahí.''')
            elif 'herido' in eventos:
                newPrint('''
No puedo pasar la mano por sitios extraños con esta herida. Sería peligroso.''')
            else:
                if minigame_lata.game():
                    newPrint('''
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
        gameOver()
        newPrint('''
1) Subirte a una silla.

2) Observar la escultura.

3) Buscar algo interesante entre las mantas.''')
        options = '0 1 2 3'.split()
        if 'neverLav' in eventos:
            newPrint('''
4) Puerta de la lavandería.''')
            options.append('4')
        newPrint('''
Pulsa 0 para cancelar.''')
        opcion = opcionValida(options)
        if opcion == '1':
            if 'brokeSilla' in eventos:
                newPrint('''
Ha sido muy peligroso, no te apetece repetir la experiencia.''')
            elif 'calcetines' in eventos:
                if 'upSilla' in eventos:
                    newPrint('''
Ya estás subido a la silla.''')
                else:
                    newPrint('''
Subes a la silla, no es muy estable...''')
                eventos.append('upSilla')
            else:
                newPrint('''
La abuela se enfadaría mucho si me viese poner los zapatos encima de
una de sus sillas antiguas.''')
        elif opcion == '2':
            if llaves in yaLooteado:
                newPrint('Es una mujer preciosa...')
            elif 'upSilla' in eventos:
                newPrint('''
Tiene una llave colgando del dedo corazón... intentas alcanzarla...
la pata de la silla se parte. Será mejor no volver a intentarlo.''')
                eventos.append('brokeSilla')
                eventos.remove('upSilla')
            else:
                newPrint('''
Tiene algo que te llama la atención. Te hace quedarte embobado mirándola...
Algo cuelga de sus dedos. Quizá puedas alcanzarlas con algo...''')
                if promptItem('GANCHO'):
                    newPrint('''
Con el {0} alcanzas las {1} - No son las de los abuelos.
¿De quién será este juego de llaves extra?'''.format('GANCHO', llaves))
                    getLoot(llaves)
        elif opcion == '3':
            if 'calcetines' in eventos:
                newPrint('Ya solo quedan pelusas y huesos de oliva.')
            else:
                if 'encuentra' in eventos:
                    newPrint('Solo encuentras los calcetines con los que has estado jugando.')
                else:
                    newPrint('Encuentras unos calcetines gordos de la abuela.')
                    eventos.append('encuentra')
                options = '0 1 2'.split()
                newPrint('''
1) Ponértelos.

2) Jugar a las marionetas con ellos.

Pulsa 0 para cancelar.''')
                opcion3 = opcionValida(options)
                if opcion3 == '1':
                    if 'TROZO DE CRISTAL' in yaLooteado:
                        newPrint('''
Te quitas los zapatos y te pones los calcetines gordos. ¡Qué cómodos!''')
                        eventos.append('calcetines')
                    else:
                        newPrint('''
Te quitas los zapatos y te pones los calcetines gordos. ¡AY, DUELE!''')
                        eventos.append('calcetines')
                elif opcion3 == '2':
                    if cristal not in yaLooteado:
                        newPrint('''
Pasas un buen rato imitando a los abuelos con los calcetines. Espera un
momento... Aquí dentro hay algo. Encuentras {0} - Uf, si
me los hubiese puesto me habría hecho mucho daño.'''.format(cristal))
                        getLoot(cristal)
                    else:
                        newPrint('''
Pasas un buen rato imitando a los abuelos con los calcetines.''')
        elif opcion == '4':
            newPrint('''
Es la puerta que da a lavandería. Todavía se te eriza la piel de pensar
en el fantasma. Quizá puedas usar algo para tranquilizarte.''')
            if promptItem('CARAMELO'):
                newPrint('''
Te hace sentir extraño, más relajado.''')
                eventos.remove('neverLav')
                loot.remove('CARAMELO')
                hora -= 2
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
        gameOver()
        if 'cuboSuelo' not in eventos:
            newPrint('''
1) Examinar la habitación.

Pulsa 0 para cancelar.''')
            options = '0 1'.split()
        else:
            newPrint('''
1) Examinar la habitación.

2) Buscar entre la ropa sucia.

Pulsa 0 para cancelar.''')
            options = '0 1 2'.split()
        opcion = opcionValida(options)
        if opcion == '1':
            if 'cuboSuelo' not in eventos:
                newPrint('''
No hay nada más aparte de la lavadora, el tendedero y un cubo enorme y pesado.''')
            else:
                newPrint('''
Ahora está todo hecho un desastre, toda la ropa está tirada por el suelo.''')
            newPrint('''
1) Buscar en la lavadora.

2) Buscar en el cubo.

3) Buscar en el tendedero.

Pulsa 0 para cancelar.''')
            options = '0 1 2 3'.split()
            opcion1 = opcionValida(options)
            if opcion1 == '1':
                newPrint('''
Está vacía, no encuentras nada.''')
            elif opcion1 == '2':
                if 'cuboSuelo' in eventos:
                    newPrint('''
Ahora ya no es tan imponente, todas sus entrañas están esparcidas por el suelo.''')
                else:
                    newPrint('''
Es demasiado alto, no alcanzas a mirar qué hay dentro.''')
                    if 'try' in eventos:
                        newPrint('''
1) Tumbarlo.

2) Coger fuerzas.

Pulsa 0 para cancelar.''')
                        options = '0 1 2'.split()
                    else:
                        newPrint('''
1) Tumbarlo.

Pulsa 0 para cancelar.''')
                        options = '0 1'.split()
                    opcion1_1 = opcionValida(options)
                    if opcion1_1 == '1':
                        if 'cuboSuelo' in eventos:
                            newPrint('''
Ya has conseguido tirar el cubo, tanto esfuerzo... Seguro que mañana
tienes agujetas.''')
                        elif 'furia' in eventos:
                            newPrint('''
Descargas toda tu furia en un empujón colosal. El cubo no puede soportar
tanto empeño y se desploma, vertiendo todo su contenido por el suelo.
Quizá deberias aprender de esto y usar esta nueva habilidad con Miguel
"La Roca", debe pesar más o menos lo mismo. Así aprenderá a llevar su propio
bocadillo al cole.''')
                            eventos.append('cuboSuelo')
                        else:
                            newPrint('''
Pesa demasiado, no puedes con él.''')
                            eventos.append('try')
                    elif opcion1_1 == '2':
                        if 'cuboSuelo' in eventos:
                            newPrint('''
No crees que haga falta sentir más odio. De lo contrario, te saldrán bultos
en el cuello como a la abuela.''')
                        elif 'furia' in eventos:
                            newPrint('''
Estás furioso, deberías aprovechar estos sentimientos para algo útil.''')
                        else:
                            newPrint('''
Tratas de encontrar rabia en tu interior, un sentimiento que te haga estar
furioso y poder pagarlo con el cubo. Como hace el abuelo con D'Artacán.''')
                            newPrint("")
                            if minigame_furia.game():
                                eventos.append('furia')
                                hora -= 3
            elif opcion1 == '3':
                newPrint('''
Antes Puar podía caminar por encima de las cuerdas. Ahora posiblemente se
partirían.''')
        elif opcion == '2':
            if 'winRata' in eventos:
                if ropa not in yaLooteado:
                    newPrint('''
Buscas entre la ropa. Encuentras {0} - Jamás hubieses pensado
que fuese tan grande.'''.format(ropa))
                    getLoot(ropa)
                else:
                    newPrint('''
No crees que el resto de ropa vaya a serte útil.''')
            else:
                if 'winRata2' not in eventos:
                    newPrint('''
De entre las prendas de ropa emerge un calcetín que fantasmagóricamente
se mueve, de forma torpe rueda montaña abajo y se coloca en posición de
defensa. Parece que no está dispuesto a dejarte tocar a sus compañeros
sin arriesgar su vida primero.''')
                    newPrint("")
                    newPrint('''
1) Huir.

2) Plantar cara al fantasma.

Pulsa 0 para cancelar.''')
                    options = '0 1 2'.split()
                    opcion2 = opcionValida(options)
                    if opcion2 == '1':
                        newPrint('''
Das media vuelta y sales despavorido jurándote a ti mismo que no volverás
a pisar la lavandería nunca más.''')
                        eventos.append('neverLav')
                        movimiento(True)
                        options = opcionesMovValidas()
                        options.remove('0')
                        desplazar = opcionValida(options)
                        movSala(desplazar)
                        salaActual = getNSala()
                        newPrint(getName())
                        newPrint("")
                        if getName() not in yaVisitado:
                            newPrint(getDescription())
                            yaVisitado.append(getName())
                        break
                    elif opcion2 == '2':
                        newPrint('''
Desde siempre has creído en los fantasmas; hoy es el día de enfrentarse a uno
de ellos. Cuando cuentes esta historia en el cole puedes obviar la parte de
que es minúsculo.''')
                    else:
                        break
                else:
                    newPrint('''
De algún modo te lo esperabas. Sabes perfectamente que dentro de ese calcetín
está esa rata tan valiente que conociste en el baño de los abuelos. Sabías
que volveríais a medir vuestras fuerzas. Siempre has tenido esa capacidad
de ver a lo que estás destinado. Notas en el ambiente que será una batalla dura,
que pondrá en riesgo la percepción que tienes de ti mismo.
Te remangas y te preparas para la batalla.''')
                if minigame_fight.game(salaActual, 'winRata2' in eventos):
                    if 'winRata2' not in eventos:
                        newPrint('''
El fantasma cae rendido. Poco a poco, de dentro del calcetín emerge un pequeño
ratoncito. Te lanza una mirada de odio y huye hacia un hueco en la pared. No sabes
por qué, pero crees que volverás a ver a ese valiente ratoncito que se alzó contra
un enemigo al que no podía vencer, por defender a los suyos.
Esto te llena de determinación.''')
                    else:
                        newPrint('''
La rata cae rendida. Te lanza una mirada de aprobación. Acepta que tienes el derecho
de rebuscar entre la ropa sucia que tan fieramente ha defendido. Por último se gira
y huye hacia un hueco en la pared.
''')
                    eventos.append('winRata')
                    hora -= 3
                    break
                else:
                    hora -= 1
                    break
        else:
            break

def taller():
    global loot
    global eventos
    global yaLooteado
    global hora
    global salaActual
    evPosibles = 'dope herramientaX pelea win comboX botella'.split()
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
        gameOver()
        if 'clipUsed' not in eventos:
            newPrint('''
Está todo lleno de cosas interesantes. La distribución se divide en cuatro
secciones:

1) Carpintería

2) Bañera con líquidos

3) Látex negro

4) Punto

5) Puerta cerrada

Pulsa 0 para cancelar.''')
            options = '0 1 2 3 4 5'.split()
            opcion1 = opcionValida(options)
        else:
            newPrint('''
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
            newPrint('''
La pared está llena de muestras de madera y clavos de todas las medidas.
La mesa de trabajo es imponente, no puedes mirar lo que hay sobre ella,
es demasiado alta.

1) Panel de herramientas

2) Mesa de trabajo

Pulsa 0 para cancelar.''')
            options = '0 1 2'.split()
            opcion1_1 = opcionValida(options)
            if opcion1_1 == '1':
                newPrint('''
En la pared hay un tablón con clavos, estratégicamente colocados para que
sobre ellos puedan reposar las herramientas. Puedes coger una de ellas, pero
sólo una. Coger dos haría que se tumbase, están en perfecto equilibrio.''')
                optionsH = ['0']
                for i in herramientas:
                    if i not in loot:
                        optionsH.append(str(herramientas.index(i)+1))
                for k in range(1, len(optionsH)):
                    newPrint('''
({0}) {1}'''.format(optionsH[k], herramientas[int(optionsH[k])-1]))
                newPrint('''
Pulsa 0 para cancelar.''')
                opcionH = int(opcionValida(optionsH))
                if opcionH != 0:
                    if len(optionsH) != 5:
                        for j in herramientas:
                            if j in loot:
                                tool = j
                        loot.remove(tool)
                    newPrint('''
Tomas prestada la herramienta.''')
                    getLoot(herramientas[opcionH-1])
                    
            elif opcion1_1 == '2':
                newPrint('''
Si tienes pensado hacer manualidades, vas a tener que hacerlas de puntillas y sin mirar.''')
                if not (contenido(comboGancho, loot) or contenido(comboCuerda, loot) or contenido(comboMagneto, loot)):
                    newPrint('''
No tienes suficientes objetos para combinar.''')
                else:
                    if 'book' not in eventos:
                        newPrint('''
No se te ocurre cómo combinar las cosas. Tienes una crisis de creatividad.''')
                    else:
                        options = ['0', '1']
                        newPrint('''
Construir usando: ''')
                        comboInBag = ''
                        for i in range(len(combos)):
                            if contenido(combos[i], loot):
                                comboInBag = i
                                break
                        newPrint('''
1) {0}, {1}, {2}, {3}'''.format(combos[comboInBag][0], combos[comboInBag][1], combos[comboInBag][2], combos[comboInBag][3]))
                        opcionM = opcionValida(options)
                        if opcionM == '1':
                            if comboInBag == 0:
                                newPrint('''
Creas el {0} - Algunas especies lo consideran un Dios. No es para tanto.'''.format('GANCHO'))
                                loot.remove('TENEDOR')
                                loot.remove('PALO DE MADERA')
                                loot.remove('PEGAMENTO')
                                getLoot('GANCHO')
                            elif comboInBag == 1:
                                newPrint('''
Creas la {0} - No es muy estable, pero con tu peso podrá aguantar al menos un ratito.'''.format('CUERDA'))
                                loot.remove('ROPA INTERIOR DE LA ABUELA')
                                loot.remove('CORBATAS')
                                loot.remove('CALCETINES SUCIOS')
                                getLoot('CUERDA')
                            else:
                                newPrint('''
Creas el {0} - Decidido, estudiarás ingeniería.'''.format('MAGNETO'))
                                loot.remove('IMÁN')
                                loot.remove('HILO DENTAL')
                                loot.remove('ANILLO')
                                getLoot('MAGNETO')
        elif opcion1 == '2':
            newPrint('''
Hay cientos de botellas apiladas en la esquina derecha de la habitación.
Llevan una etiqueta donde pone KALAYAYA bajo un dibujo de la cara del abuelo.
La bañera está hasta los topes del líquido amarillento que rellena las botellas.
Huele rancio y asqueroso, como a fruta podrida.

1) Probar una de las botellas.

Pulsa 0 para cancelar.''')
            options = '0 1'.split()
            opcion2 = opcionValida(options)
            if opcion2 == '1':
                newPrint('''
Intentas descorchar la botella, pero está muy dura. No consigues nada.
Quizá puedas utilizar algo para abrirla.''')
                if promptItem('MARTILLO'):
                    newPrint('''
Rompes el cuello de la botella con un golpe seco del martillo. Ten cuidado,
no te cortes. Le das un largo trago y a continuación echas todo el contenido
de tu estómago. Después de un par de minutos vomitando, empiezas a verlo todo
distinto. Los colores y las formas se mezclan entre ellos, los olores se
convierten en sonidos y puedes saborear todo lo que llega a tus oídos.''')
                    eventos.append('dope')
        elif opcion1 == '3':
            if 'pelea' not in eventos:
                newPrint('''
Hay pedazos de esa tela negra colgando por toda la pared de la habitación.
Colgados como murciélagos, esperando a ser cortados. En la esquina izquierda
hay dos maniquíes vestidos con esta tela, con pinchos de metal y cremalleras
tapando sus bocas. ¿Será esta la guarida secreta del abuelo?
¡Es un superhéroe!''')
                if 'dope' in eventos:
                    newPrint('''
Poco a poco los maniquíes cobran vida. Comienzan a moverse y a bailar, dan vueltas
a tu alrededor. Uno de ellos se para a tu lado, se acerca a tu oído. Una voz de
mujer muy dulce te susurra: "¿Quieres bailar con nosotros?"

1) Sí

2) No

Pulsa 0 para cancelar.''')
                    options = '0 1 2'.split()
                    opcion3 = opcionValida(options)
                    if opcion3 == '1':
                        newPrint('''
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
                            newPrint('''
Te fuerzas y sigues bailando hasta que te tuerces un tobillo y caes al suelo, te
duele mucho. Los maniquíes ven que has dejado de bailar. La voz dulce te vuelve a
susurrar: "¿No vas a seguir bailando?"
Le contestas que no puedes, te has hecho daño.''')
                            opcion3 = '2'
                        elif opcion3_1 == '2':
                            newPrint('''
La voz dulce te vuelve a susurrar: "¿No vas a seguir bailando?"
Le contestas que estás cansado, que tienes que irte. La voz te insiste que quiere
que bailes para siempre.

1) Seguir bailando.

2) Parar de bailar.''')
                            opcion3_2 = opcionValida(options)
                            if opcion3_2 == '1':
                                newPrint('''
Te fuerzas y sigues bailando hasta que te tuerces un tobillo y caes al suelo, te
duele mucho. Los maniquíes ven que has dejado de bailar. La voz dulce te vuelve a
susurrar: "¿No vas a seguir bailando?"
Le contestas que no puedes, te has hecho daño.''')
                                opcion3 = '2'
                            elif opcion3_2 == '2':
                                opcion3 = '2'
                    if opcion3 == '2':
                        newPrint('''
El ambiente se enrarece. Los maniquíes paran de bailar y poco a poco abren las
cremalleras de sus bocas. Sus dientes son cuchillas. Te miran como lo hace Puar
cuando intentas darle un baño. Te asustas y te preparas para la batalla.''')
                    ## fight maniquíes
                        if minigame_fight.game(salaActual):
                            if 'SIERRA' in loot:
                                newPrint('''
Aprovechas la debilidad de tus adversarios. Estás fuera de ti. Sierra en mano,
imitando las películas de espadachines, arremetes contra los maniquíes. Estocada
tras estocada consigues tumbar a los dos y comienzas a mutilarlos. Sin brazos ni
piernas no pueden hacerte daño, piensas. Cuando has terminado, en un ataque de ira,
les cortas también la cabeza. Estas criaturas no sangran.

De pronto sales del trance. ¿Qué ha pasado?''')
                            elif 'MARTILLO' in loot:
                                newPrint('''
Aprovechas la debilidad de tus adversarios. Estás fuera de ti. Sacas el martillo y
comienzas a aporrear sin descanso a los maniquíes. Cuando ya han dejado de moverse
aún sigues chafando sus huesos con el martillo. Quedan irreconocibles.

De pronto sales del trance. ¿Qué ha pasado?''')
                            elif 'CINTA' in loot:
                                newPrint('''
Aprovechas la debilidad de tus adversarios. Estás fuera de ti. Abres la cinta y
comienzas a correr en círculos alrededor de las dos figuras. Consigues atarlas
bien fuerte y las amordazas, no quieres seguir viendo esos asquerosos dientes.
Aunque les hayas tapado la boca, siguen babeando un líquido verde fosforito,
viscoso y repugnante. Arremetes a patadas contra sus cabezas hasta que tus pies
están empapados de saliva de maniquí.

De pronto sales del trance. ¿Qué ha pasado?''')
                            elif 'TIJERAS' in loot:
                                newPrint('''
Aprovechas la debilidad de tus adversarios. Estás fuera de ti. Cierras los ojos,
abres las tijeras y comienzas a cortar todo el látex que encuentras en tu camino.
Sigues cortando hasta que el trocito más grande es del tamaño de una uña. Miras
el espectáculo grotesco, no queda nada de lo que antes eran tres figuras horrorosas.

De pronto sales del trance. ¿Qué ha pasado?''')
                            newPrint('''
Entre los restos de los maniquíes encuentras {0} - Debió ser algún día la columna
vertebral de esos maniquíes masacrados. Qué clase de animal habrá hecho esto...'''.format(palo))
                            getLoot(palo)
                            eventos.append('pelea')
                            eventos.remove('dope')
                            hora -= 3
                            break
                        else:
                            newPrint('''
Te levantas y los maniquíes siguen ahí, esta vez sin vida, inmóviles.
Tu corazón vuelve a latir a su ritmo normal.''')
                            eventos.remove('dope')
                            hora -= 1
                            break
            else:
                newPrint('''
Hay pedazos de esa tela negra colgando por toda la pared de la habitación.
Cuelgan como murciélagos, esperando a ser cortados y remachados. En la esquina
izquierda yacen los restos de lo que aparentemente fue una batalla encarnecida entre
figuras de madera y látex. ¿Qué habrá pasado?''')
        elif opcion1 == '4':
            newPrint('''
Hay un rinconcito secreto con todos los utensilios necesarios para hacer punto.
La lana rosa es la que más abunda. Parece que los tapetes de punto que cubren
todos los muebles de la casa no son obra de la abuela.''')
        elif opcion1 == '5':
            newPrint('''
Hay una puerta cerrada en la habitación. Quizá puedas utilizar algo para abrirla...''')
            if promptItem('CLIP ROTO'):
                newPrint('''
Usas el clip para abrir la puerta. Termina de romperse, pero al menos la puerta se ha abierto.''')
                loot.remove('CLIP ROTO')
                eventos.append('clipUsed')
        else:
            if 'dope' in eventos:
                eventos.remove('dope')
                newPrint('''
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
        gameOver()
        newPrint('''
1) Mirar en la encimera.

2) Explorar el interior del armario.

3) Observar la mesa central.

4) Mirar la TV.

Pulsa 0 para cancelar.''')
        options = '0 1 2 3 4'.split()
        opcion = opcionValida(options)
        if opcion == '1':
            newPrint('''
Está toda llena de brócoli. Ni a los insectos les gusta.''')
            newPrint('''

1) Abrir los cajones.

2) Usar el microondas.

3) Examinar la nevera.

Pulsa 0 para cancelar.''')
            options = '0 1 2 3'.split()
            opcion1 = opcionValida(options)
            if opcion1 == '3':
                if 'IMÁN' not in yaLooteado and 'pelusa' in eventos:
                    newPrint('''
Estas cosas pegadas a la puerta podrían serte útiles. Encuentras {0}
- No es muy potente.'''.format('IMÁN'))
                    getLoot('IMÁN')
                else:
                    newPrint('''
Abres la nevera y... ¡PUAJ! Huele fatal. Todo está podrido, hay gusanos
y cucarachas por todos lados.''')
                    if 'MANTEQUILLA' not in yaLooteado:
                        newPrint('''
Encuentras {0} - Está caducada, pero no tiene gusanos.'''.format('MANTEQUILLA'))
                        getLoot('MANTEQUILLA')
            elif opcion1 == '2':
                if 'plomos' in eventos:
                    newPrint('''
Se ha ido la luz, el microondas no funciona.''')
                else:
                    newPrint('''
¿Quieres calentar algo en el microondas?''')
                    if promptItem('MANTEQUILLA'):
                        if 'tvon' in eventos:
                            newPrint('''
¡PUM! Han saltado los plomos. No debería haber encendido la TV y el microondas a la vez,
el abuelo suele advertirlo.''')
                            eventos.remove('tvon')
                            eventos.append('plomos')
                            hora -= 2
                        else:
                            newPrint('''
La mantequilla se ha derretido. Cómo resbala...''')
                            loot.remove('MANTEQUILLA')
                            getLoot('MANTEQUILLA LÍQUIDA')
            elif opcion1 == '1':
                if 'cajonOpen' not in eventos:
                    newPrint('''
Están atascados. El mecanismo debe estar oxidado. Quizá puedas utilizar algo para abrirlos.''')
                    if promptItem('MANTEQUILLA LÍQUIDA'):
                        eventos.append('cajonOpen')
                        loot.remove('MANTEQUILLA LÍQUIDA')
                        newPrint('''
Ahora funcionan a la perfección.''')
                else:
                    if 'LLAVE DE LA CUBERTERÍA' not in yaLooteado:
                        newPrint('''
Abres los cajones. Sólo ves cubiertos de plástico. Quizá puedas utilizar algo...''')
                        if promptItem(['MAGNETO', 'IMÁN']):
                            newPrint('''
Encuentras {0}. Ahora sólo quedan cubiertos de plástico.'''.format('LLAVE DE LA CUBERTERÍA'))
                            getLoot('LLAVE DE LA CUBERTERÍA')
                    else:
                        newPrint('''
Sólo quedan cubiertos de plástico.''')
        elif opcion == '2':
            if not 'openArmario' in eventos:
                newPrint('''
Es un armario muy grande y pesado. Las puertas están cerradas con llave.
Quizá puedas abrirla con algo...''')
                if promptItem('LLAVE DE LA CUBERTERÍA'):
                    newPrint('''
El armario se ha abierto de par en par.''')
                    eventos.append('openArmario')
            else:
                if 'TENEDOR' not in yaLooteado:
                    newPrint('''
Dentro está la cubertería buena de la abuela. Sólo la saca cuando tiene visita.
Encuentras {0} - Está impecable, como si nadie lo hubiese utilizado nunca.'''.format('TENEDOR'))
                    getLoot('TENEDOR')
                else:
                    newPrint('''
No crees que te vayan a hacer falta más cubiertos.''')
        elif opcion == '3':
            if 'CARAMELO' not in loot:
                newPrint('''
En el centro de la mesa hay una fuente de cristal. Encuentras {0}
- A la abuela le encantan estos caramelos. Una vez probaste uno, no sabía nada
bien, te hizo sentir extraño.'''.format('CARAMELO'))
                getLoot('CARAMELO')
            else:
                newPrint('''
La fuente de cristal está repleta de caramelos, pero mejor coger solo uno.''')
        elif opcion == '4':
            if 'plomos' in eventos:
                newPrint('''
Se ha ido la luz, la TV no funciona.''')
            else:
                options = '0 1'.split()
                if 'tvon' not in eventos:
                    newPrint('''
La TV está apagada.

1) Encender.

Pulsa 0 para cancelar.''')
                    opcion4 = opcionValida(options)
                    if opcion4 == '1':
                        newPrint('''
Enciendes la TV. ¡Están poniendo la serie de Tabla!''')
                        eventos.append('tvon')
                else:
                    newPrint('''
La TV está encendida.

1) Apagar.

Pulsa 0 para cancelar.''')
                    opcion4 = opcionValida(options)
                    if opcion4 == '1':
                        newPrint('''
Apagas la TV.''')
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
        gameOver()
        options = '0 1'.split()
        newPrint('''
1) Recorrer el pasillo.''')
        if 'neverLav' in eventos:
            newPrint('''
2) Puerta espeluznante.''')
            options.append('2')
        newPrint('''
Pulsa 0 para cancelar.''')
        opcion = opcionValida(options)
        if opcion == '1':
            if 'pateDado' not in eventos:
                newPrint('''
Puar está durmiendo en medio del arco que separa las dos partes del pasillo.
Está muy gordo, no podrás moverlo.
Quizá puedas utilizar algo...''')
                if promptItem('LATA DE PATÉ DE GATO'):
                    eventos.append('pateDado')
                    loot.remove('LATA DE PATÉ DE GATO')
                    newPrint('''
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
                        newPrint('''
Puar da buena cuenta del paté. Después, con la barriga llena, se recuesta y
comienza a ronronear. Le gritas que se aparte, que su palabra no vale nada.
No parece estar por la labor de levantarse.''')
                        if minigame_fight.game(salaActual):
                            eventos.append('winGato')
                            newPrint('''
Puar admite la derrota. Se levanta de forma torpe y se aparta de tu camino.
Una lágrima asoma desde su ojo izquierdo.''')
                            hora -= 3
                            break
                        else:
                            newPrint('''
Puar ha dañado toda tu autoestima. Pero eres valiente, te secas las lágrimas
y continúas tu camino.''')
                            hora -= 1
                            break
                    elif opcion1 == '2':
                        newPrint('''
No confías en su palabra. Sabes que es un gato avaricioso y mentiroso.
No aceptas el trato.''')
                        break
                else:
                    break
            else:
                if 'winGato' not in eventos:
                    newPrint('''
Puar está durmiendo en medio del arco que separa las dos partes del pasillo.
Esta vez no te andas con tonterías. Le gritas y te preparas para el ataque.''')
                    if minigame_fight.game(salaActual):
                        eventos.append('winGato')
                        newPrint('''
Puar admite la derrota. Se levanta de forma torpe y se aparta de tu camino.
Una lágrima asoma desde su ojo izquierdo.''')
                        hora -= 3
                        break
                    else:
                        hora -= 1
                        break
                else:
                    newPrint('''
Puar sigue durmiendo, pero a varios metros del arco que separa las dos partes
del pasillo.''')
                    break
        elif opcion == '2':
            newPrint('''
Es la puerta que da la lavandería. Todavía se te eriza la piel de pensar
en el fantasma. Quizá puedas usar algo para tranquilizarte.''')
            if promptItem('CARAMELO'):
                newPrint('''
Te hace sentir extraño, más relajado.''')
                eventos.remove('neverLav')
                loot.remove('CARAMELO')
                hora -= 2
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
        newPrint('{0}) {1}'.format(j+1, marcos[j]))
    options = ['0']
    for i in range(len(marcos)):
        options.append(str(i+1))
    opcion = opcionValida(options)
    if opcion != 0:
        newPrint('{0}'.format(descripciones[int(opcion)-1]))
        newPrint("")
        newPrint('¿Quieres colgar este cuadro?')
        opcionesM = '1 2'.split()
        newPrint('''
1) Colgar el cuadro.

2) Dejarlo en el suelo.''')
        opcionM = opcionValida(opcionesM)
        if opcionM == '1':
            eventos.append(cuadrosDoble[int(opcion)-1])
            if len(marcos) != 4:
                eventos.remove(marcoInEventos)
                newPrint('''
Bajas el cuadro con el {0}'''.format(cuadroEnPared.lower()))
            newPrint('''
Cuelgas el cuadro con el {0}'''.format(marcos[int(opcion)-1].lower()))

def pasilloCorto():
    global loot
    global yaLooteado
    global eventos
    global salaActual
    global hora
    while True:
        gameOver()
        newPrint('''
1) Buscar en el interior del mueble.

2) Observar los cuadros.

3) Examinar el suelo.

Pulsa 0 para cancelar.''')
        options = '0 1 2 3'.split()
        opcion = opcionValida(options)
        if opcion == '1':
            if 'pista' not in eventos:
                newPrint('''
La puerta no se abre. Quizá puedas utilizar algo...''')
                promptItem('ESAESLABROMA')
            else:
                if 'PEGAMENTO' not in yaLooteado:
                    newPrint('''
Se te había olvidado. Tú pusiste ese mensaje ahí, esta puerta se abre tirando del pomo
hacia la izquierda. Abres el armario y dentro encuentras las herramientos necesarias para
colgar cuadros y que no se caigan. Encuentras {0} - Está un poco seco,
pero puede que aún funcione.'''.format('PEGAMENTO'))
                    getLoot('PEGAMENTO')
                else:
                    newPrint('''
No queda nada interesante aquí.''')
        elif opcion == '2':
            if 'pista' not in eventos:
                newPrint('''
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
                    hora -= 5
            else:
                newPrint('''
Todos los cuadros están rectos.''')
        elif opcion == '3':
            if 'pista' not in eventos:
                newPrint('''
Hay varios cuadros en el suelo, se han debido caer. Sin embargo, en la
pared solo cabe uno más. Podrías volver a colgar alguno.''')
                newPrint("")
                showMarcos()
            else:
                newPrint('''
No hay sitio para colgar los cuadros del suelo.''')
        else:
            break

def escalera():
    global sala
    global loot
    global salaActual
    global eventos
    global yaLooteado
    global hora
    while True:
        gameOver()
        options = '0 1 2'.split()
        newPrint('''
1) Cuadro eléctrico

2) Mirar el reloj''')
        if 'keyUsed' not in eventos:
            newPrint('''
3) Puerta cerrada''')
            options.append('3')
        newPrint('''
Pulsa 0 para cancelar.''')
        opcion = opcionValida(options)
        if opcion == '1':
            newPrint('''
La puertecita que lo cierra está rota, puedes acceder a las palancas sin
necesidad de la llave.''')
            if 'ANILLO' not in yaLooteado:
                newPrint('''
Encuentras {0} - Estaba colgando de una de las palancas.'''.format('ANILLO'))
                getLoot('ANILLO')
            options = '0 1'.split()
            if 'plomos' in eventos:
                newPrint('''
Los plomos están bajados.

1) Subirlos.

Pulsa 0 para cancelar.''')
                opcion1 = opcionValida(options)
                if opcion1 == '1':
                    eventos.remove('plomos')
            elif 'plomos' not in eventos:
                newPrint('''
Los plomos están subidos.

1) Bajarlos.

Pulsa 0 para cancelar.''')
                opcion1 = opcionValida(options)
                if opcion1 == '1':
                    eventos.append('plomos')
        elif opcion == '2':
            newPrint('''
El reloj marca las {0}.
'''.format(getHora()))
        elif opcion == '3':
            newPrint('''
Hay una puerta cerrada al final de las escaleras. Quizá puedas
utilizar algo para abrirla.''')
            if promptItem('LLAVE DE LA HABITACIÓN'):
                newPrint('La puerta se ha abierto.')
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
    global hora
    while True:
        gameOver()
        options = '0 1 2 3'.split()
        newPrint('''
1) Buscar en el armario.

2) Examinar el panel electrónico.

3) Sentarse en la silla plegable.''')
        if 'pass' in eventos:
            newPrint('''
4) Buscar entre los cojines del sofá.''')
            options.append('4')
        newPrint('''
Pulsa 0 para cancelar.''')
        opcion = opcionValida(options)
        if opcion == '1':
            newPrint('''
El armario de tres cuerpos es el que más te llama la atención. Es casi más
grande que la habitación, podrías jugar ahí dentro a lo que quisieses.

1) Caminar hacia el fondo.

2) Buscar en los cajones.

Pulsa 0 para cancelar.''')
            options = '0 1 2'.split()
            opcion1 = opcionValida(options)
            if opcion1 == '1':
                newPrint('''
Entras y caminas hacia el fondo apartando abrigos de piel que pesan el triple
que tú. Al fondo tocas algo frío con los dedos. La imagen de un campo lleno de
nieve viene a tu mente. Cuando te acercas para ver lo que es, descubres un par
de cajas apiladas llenas de las botellas que viste en el taller del abuelo.
Habías tocado una de las que estaba fuera de las cajas.''')
                if 'gafas' not in eventos:
                    newPrint('''
Sobre las cajas, al lado de las botellas ves las gafas del abuelo. Se las ha
debido de dejar aquí olvidadas.

1) Ponerte las gafas.

Pulsa 0 para cancelar.''')
                    options = '0 1'.split()
                    opcion1_1 = opcionValida(options)
                    if opcion1_1 == '1':
                        newPrint('''
Te colocas las gafas sobre la nariz. Ves las cosas muy distintas ahora.''')
                        eventos.append('gafas')
            elif opcion1 == '2':
                newPrint('''
Dentro de los cajones hay: calzoncillos, calcetines, camisetas interiores de algodón...''')
                if 'CORBATA' not in yaLooteado:
                    newPrint('''
Entre toda la ropa interior encuentras {0} - Se han enredado con
unas cadenas y unas esposas de policía aterciopeladas.'''.format('CORBATA'))
                    getLoot('CORBATA')
        elif opcion == '2':
            if 'pass' not in eventos:
                if 'gafas' not in eventos:
                    newPrint('''
El panel es de metal, tiene botones con números y una pantalla que marca 8 espacios.
Debe ser para introducir una contraseña secreta.''')
                    juego = 'num'
                else:
                    newPrint('''
El panel es de metal, tiene botones para todas las letras del abecedario y una pantalla
que marca 8 espacios. Debe ser para introducir una contraseña secreta.''')
                    juego = 'word'
                if passCode(juego):
                    newPrint('''
La pantalla se ilumina de color verde. A continuación, la pared comienza a temblar. El
suelo se traga poco a poco el muro, como si se estuviese fundiendo. Al terminar el
movimiento descubres una parte de la habitación que estaba oculta tras una pared.
Ahora la habitación es el doble de grande. En esta nueva zona hay un sofá enorme, de
color rojo vivo. Las luces son de color rojizo e iluminan de forma tenue.
Hay tres cámaras en trípodes, enfocadas hacia el sofá, además de un par de plantas
tropicales en tiestos de color negro.''')
                    eventos.append('pass')
                    hora -= 2
                else:
                    newPrint('''
La pantalla se ilumina de color rojo. Los caracteres que habías introducido se borran.''')
                    hora -= 1
            else:
                newPrint('''
Ahora la habitación es el doble de grande. En esta nueva zona hay un sofá enorme, de
color rojo vivo. Las luces son de color rojizo e iluminan de forma tenue.
Hay tres cámaras en trípodes, enfocadas hacia el sofá, además de un par de plantas
tropicales en tiestos de color negro.''')
        elif opcion == '3':
            newPrint('''
No parece muy buena idea perder tiempo en esta silla. Sobre la silla hay un libro
encuadernado en piel.''')
            if 'gafas' not in eventos:
                newPrint('''
Lo abres, intentas leerlo pero no entiendes nada, sólo hay números.''')
            else:
                options = '1 2'.split()
                newPrint('''
Lo abres, ahora puedes leer perfectamente todo lo que pone. Es un libro de carpintería.
Explica paso a paso como construir algunas cosas.

GANCHO: Necesitas serrar, algo puntiagudo y de metal, algo de madera y algo para pegar.
Es un poco lioso pero te ha quedado claro. ¿Seguir leyendo?

1) Sí

2) No
''')
                opcion3 = opcionValida(options)
                if opcion3 == '1':
                    newPrint('''
MAGNETO: Necesitas un imán, un hilo que aguante el peso, un objeto donde atarlo
y algo para unirlo todo.
Hay que seguir muchos pasos pero te los has aprendido. ¿Seguir leyendo?

1) Sí

2) No
''')
                    opcion3 = opcionValida(options)
                    if opcion3 == '1':
                        newPrint('''
CUERDA: Necesitas trozos de tela, no importa que esten sucios y tijeras para darle forma.
Es el más sencillo, pero te ha costado memorizarlo.''')
                        if 'book' not in eventos:
                            hora -= 2
                        eventos.append('book')
        elif opcion == '4':
            if 'LLAVE DE LA HABITACIÓN' not in yaLooteado:
                newPrint('''
El sofá es enorme y tus brazos son cortos, no llegas a alcanzar nada.
Quizá puedas utilizar algo...''')
                if promptItem('MAGNETO'):
                    newPrint('''
Metes el {0} en uno de los pliegues del sofá. Escuchas un "CLICK", tiras del hilo
atado al anillo. Pegado al {0} hay una pelusa de color rojo.
Dentro de la pelusa encuentras {1}.'''.format('MAGNETO', 'LLAVE DE LA HABITACIÓN'))
                    getLoot('LLAVE DE LA HABITACIÓN')
            else:
                newPrint('''
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
        gameOver()
        newPrint('''
1) Mirar los libros.

2) Abrir la puerta.

Pulsa 0 para cancelar.''')
        options = '0 1 2'.split()
        opcion = opcionValida(options)
        if opcion == '1':
            newPrint('''
Hay demasiados, comienzas a sacarlos poco a poco de los cajones, en busca de 
uno que tenga más dibujos que letras. De dentro de uno de los libros cae una nota
doblada. Tiene fecha de hace 6 años. Dice: "Papá, lo siento con todo mi corazón. 
No puedo seguir con esto, no puedo vivir con ello, dijiste que se haría poco a poco 
más sencillo, pero no es así. Que él no sepa nada, nunca, tiene tus ojos.
Te quiero y siempre te querré, Ana."
''')
        elif opcion == '2':
            if 'exitOpen' not in eventos:
                newPrint('''
Es una puerta enorme y pesada, está cerrada con llave. Quizá puedas utilizar algo.''')
                if promptItem('LLAVES DE LA CASA'):
                    newPrint('''
Justo en el momento en el que metes la llave en la cerradura, suena el timbre.

1) Responder

2) Ignorar
''')
                    options = '1 2'.split()
                    opcion2 = opcionValida(options)
                    if opcion2 == '1':
                        newPrint('''
Preguntas quién está al otro lado de la puerta y te responde una voz que te es familiar.
Tu vecina lleva mucho tiempo viviendo sola, aprovecha cada oportunidad para hartar a
quien sea a preguntas. Sabes lo que viene, y no te queda mucho tiempo.
Te preparas para el enfrentamiento.
''')
                        if minigame_fight.game(salaActual):
                            eventos.append('exitOpen')
                            hora -= 3
                            break
                        else:
                            hora -= 1
                            break
                    elif opcion2 == '2':
                        newPrint('''
Vuelves a coger la llave, te alejas silenciosamente de la puerta.
''')
            else:
                newPrint('''
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
        gameOver()
        options = '0 1 2'.split()
        newPrint('''
1) Mirarte en el espejo.

2) Buscar en la mesita de noche.''')
        if 'mascarillaPuesta' not in eventos:
            newPrint('''
3) ¿Olor raro?''')
            options.append('3')
        if 'openCaja' in eventos:
            newPrint('''
4) Mirar dentro de la caja fuerte.''')
            options.append('4')
        newPrint('''
Pulsa 0 para cancelar.''')
        opcion = opcionValida(options)
        if opcion == '1':
            if 'gafas' not in eventos:
                newPrint('''
Tienes cara de cansado. Es normal, siendo un maestro con los números como lo eres.
Ese último 0 se llama CANCELBRAH. No esperábamos que resolvieses el puzzle con
dígitos, pero tanto calcular hace que tu vista sufra. Ve a por unas gafas, ¿quieres?''')
            else:
                newPrint('''
Qué raro te ves con las gafas del abuelo. Un momento, ves algo a través del espejo.

1) Apartar el espejo.

Pulsa 0 para cancelar.''')
                options = '0 1'.split()
                opcion1 = opcionValida(options)
                if opcion1 == '1':
                    if 'openCaja' not in eventos:
                        newPrint('''
Es una caja fuerte. Está cerrada, quizá puedas utilizar algo para abrirla...''')
                        if promptItem('LLAVE CAJA FUERTE'):
                            newPrint("")
                            newPrint('La caja se ha abierto.')
                            eventos.append('openCaja')
                    else:
                        newPrint('''
La caja se ha abierto.''')
        elif opcion == '2':
            if 'LLAVE CAJA FUERTE' not in yaLooteado:
                newPrint('''
Entre la ropa interior encuentras {0}.'''.format('LLAVE CAJA FUERTE'))
                getLoot('LLAVE CAJA FUERTE')
            else:
                newPrint('''
Sólo encuentras ropa interior.''')
        elif opcion == '3':
            newPrint('''
Viene del baño de los abuelos. Abres un poco la puerta y una ráfaga de aire
pestilente te cierra la garganta.
Es horroroso, no podrás pasar a menos que utilices algo...''')
            if promptItem('MASCARILLA'):
                newPrint('''
Te pones la mascarilla. Sigue oliendo mal, pero al menos es soportable.''')
                eventos.append('mascarillaPuesta')
        elif opcion == '4':
            if 'MASCARILLA' not in yaLooteado:
                newPrint('''
Dentro de la caja hay un montón de papeles, guantes de plástico y...
¡Qué guay! Encuentras {0} - Siempre te ha hecho ilusión ponerte una.'''.format('MASCARILLA'))
                getLoot('MASCARILLA')
            else:
                newPrint('''
Dentro de la caja hay un montón de papeles y guantes de plástico.

1) Revisar los papeles.

Pulsa 0 para cancelar.''')
                options = '0 1'.split()
                opcion4 = opcionValida(options)
                if opcion4 == '1':
                    newPrint('''
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
        gameOver()
        options = '0 1 2'.split()
        newPrint('''
1) Lavarte las manos.

2) Apartar la cortina.
''')
        if 'winRata2' in eventos:
            newPrint('''
3) Examinar la bañera.

4) Salir por la ventana.''')
            options.append('3')
            options.append('4')
        newPrint('''
Pulsa 0 para cancelar.''')
        opcion = opcionValida(options)
        if opcion == '1':
            newPrint('''
La abuela siempre dice que todo se cura con agua y jabón.
''')
            if 'herido' in eventos:
                newPrint('''
Pica un poco, pero todo lo que pica cura.
''')
                eventos.remove('herido')
                hora -= 2
        elif opcion == '2':
            if 'winRata2' not in eventos:
                if 'fightRata2' not in eventos:
                    if 'winRata' in eventos:
                        newPrint('''
Avanzas hacia la cortina, pero de pronto aparece aquella rata valiente
que conociste en la lavandería. En su rostro no hay malicia, no hay venganza,
solo honor. De algún modo te lo esperabas, sabías que volveríais a medir vuestras
fuerzas. Siempre has tenido esa capacidad de ver a lo que estás destinado.
Notas en el ambiente que será una batalla dura, que pondrá en riesgo la percepción
que tienes de ti mismo.
Te remangas y te preparas para la batalla.
''')
                    else:
                        newPrint('''
Avanzas hacia la cortina, pero de pronto aparece una rata. En su mirada puedes
leer que no te piensa dejar pasar tan fácilmente.
Te remangas y te preparas para la batalla.
''')
                    eventos.append('fightRata2')         
                else:
                    if 'winRata' in eventos:
                        newPrint('''
Ahí está la rata mirandote. En su rostro no hay malicia, no hay venganza, solo honor.
Notas en el ambiente que será una batalla dura, que pondrá en riesgo la percepción
que tienes de ti mismo. 
Te remangas y te preparas para la batalla.
''')
                if minigame_fight.game(salaActual):
                    if 'winRata' in eventos:
                        newPrint('''
La rata cae rendida te lanza una mirada de aprobación. Acepta que tienes el derecho
a pasar hacia la cortina que tan fieramente ha defendido. 
Por último se gira y huye hacia un hueco en la pared.
''')
                    else:
                        newPrint('''
Te lanza una mirada de odio y huye hacia un hueco en la pared. No sabes por qué, 
pero crees que volverás a ver a esa valiente ratita que se alzó contra un enemigo
al que no podía vencer, por defender lo que era suyo.  

Esto te llena de determinación. 
''')
                    newPrint('''
Apartas la cortina y descubres que el baño sigue un buen trecho tras ella.
Hay una bañera llena de un líquido oscuro, entre rojo y verde.
Tras ella hay una ventana entreabierta. Tapada con papel de periódico.''')
                    hora -= 3
                    break
                else:
                    hora -= 1
                    break
            else:
                newPrint('''
Apartas la cortina y descubres que el baño sigue un buen trecho tras ella.
Hay una bañera llena de un líquido oscuro, entre rojo y verde.
Tras ella hay una ventana entreabierta. Tapada con papel de periódico.''')                    
        elif opcion == '3':
            newPrint('''
De aquí viene ese horrible olor. Está hasta arriba del líquido oscuro. Mientras
la observas, del fondo emerge un hueso. Es uno de los que le gustan a D'Artacán,
siempre los lleva a todos lados.

1) Tocar el líquido.

Pulsa 0 para cancelar.''')
            options = '0 1'.split()
            opcion3 = opcionValida(options)
            if opcion3 == '1':
                newPrint('''
Metes un dedo en el líquido.... ¡ay, quema!''')
                eventos.append('herido')
        elif opcion == '4':
            newPrint('''
Está muy alto. Quizás puedas utilizar algo para ayudarte a bajar...''')
            if promptItem('CUERDA'):
                if 'herido' in eventos:
                    newPrint('''
Con las manos así no puedes bajar por la cuerda.''')
                else:
                    newPrint('''
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
    hora = 180
    
else:
    variables = cargar()
    if variables != None:
        malo = variables[0]
        sala = variables[1]
        salaActual = getNSala()
        loot = variables[2]
        yaVisitado = variables[3]
        eventos = variables[4]
        yaLooteado = variables[5]
        hora = int(variables[6][0])
    else:
        malo = ''
        showIntroduction()
        sala = [1,1]
        salaActual = getNSala()
        loot = []
        yaVisitado = []
        eventos = []
        yaLooteado = []
        hora = 180

previously = previousWin()
if 1 in previously:
    eventos.append('finMadre')
elif 2 in previously:
    eventos.append('finAbuelos')

MALOS = ['abuelo', 'abuela', 'perro']
NSALAS = [[1,1], [1,5], [3,1], [3,5], [3,9], [5,1], [5,5], [5,9], [5,13], [7,1], [7,5], [7,13], [9,5], [9,9], [9,13], [11,9]]
LOOT = []
EVENTOS = []

    
while True:
    gameOver()
    if salaActual <= 14:
        room()
    elif salaActual == 15:
        ending('salidaMadre')
    elif salaActual == 16:
        ending('salidaAbuelos')
