import random

class personaje():
    global characters
    
    def __init__(self, vidaMax):
        self.vidaMax = vidaMax
        self.fe = 100
        self.vida = vidaMax
        self.alive = True
        self.win = False
##        self.hearts = getHearts(self.vida, self.vidaMax)
        
    def takeDamage(self, dmg):
        self.vida -= dmg
        if self.vida <= 0:
            self.vida = 0
            self.alive = False
##        self.hearts = getHearts(self.vida, self.vidaMax)

    def takeFaith(self, faith):
        self.fe -= faith
        if self.fe <= 0:
            self.fe = 0
        

class protagonista(personaje):
    
    name = 'Tú'

# aquí pondría el output... 
    def insultar(self, objetivo):
        dmg = 0
        if isinstance(characters[objetivo], fantasma):
            if characters[objetivo].fe >= 50:
                if random.randint(1, 100) < 5:
                    dmg = 1
            elif 20 <= characters[objetivo].fe < 50:
                if random.randint(1, 100) < 65:
                    dmg = 1
            else:
                dmg = 1
        elif isinstance(characters[objetivo], maniMujer):
            if characters[objetivo].fe == 100:
                dmg = 1
            else:
                dmg = 2
        elif isinstance(characters[objetivo], gato):
            if characters[objetivo].enrage != 0:
                characters[objetivo].enrageBonusDmg = True
            else:
                dmg = 2
            if self.fe <= 50:
                characters[objetivo].enrageProc = 3
            else:
                characters[objetivo].enrageProc += 1
            if characters[objetivo].enrageProc == 3:
                characters[objetivo].enrage = 3
                characters[objetivo].enrageProc = 0
                print('''
{0} se ha cabreado. Será mejor tener cuidado con él, no tardará mucho en calmarse,
normalmente es un gato tranquilo.'''.format(characters[objetivo].name))
                print()
        elif isinstance(characters[objetivo], vecina):
            if characters[objetivo].fe == 0:
                dmg = 1
        elif isinstance(characters[objetivo], rata):
            dmg = 0
            if countAdds() == 0:
                dmg = 1
        elif isinstance(characters[objetivo], trash):
            if random.randint(0,1) == 0:
                dmg = 1
            else:
                dmg = 2
        print('Insultas a {0}.'.format(characters[objetivo].name))
        if dmg == 0:
            print('No parece importarle.')
        else:
            print('''
Tu insulto le ha afectado.
La autoestima de {0} baja {1}.'''.format(characters[objetivo].name, dmg))
        print()
        characters[objetivo].takeDamage(dmg)
        if (not characters[objetivo].alive) and isinstance(characters[objetivo],trash):
            characters[objetivo].removefromlist()
        

    def persuadir(self, objetivo):
        faith = 0
        if isinstance(characters[objetivo], fantasma):
            faith = random.randint(20,40)
        elif isinstance(characters[objetivo], maniMujer):
            hayHombre = False
            for k in characters:
                if isinstance(k, maniHombre):
                    if k.alive:
                        hayHombre = True
            if not hayHombre:
                faith = 100
        elif isinstance(characters[objetivo], maniHombre):
            faith = 35
            print('''
Intentas ganarte la confianza de {0}.'''.format(characters[objetivo].name))
            if characters[objetivo].fe - faith <= 0:
                characters[objetivo].takeDamage(3)
                characters[objetivo].takeFaith(faith)
                print('''
Confía tanto en ti que se pone de tu parte. Piensa que deberías descansar.
Maniquí mujer le mira de una forma que te hiela la sangre.''')
                if characters[objetivo].vida >= 3:
                    print('La autoestima de {0} baja 3.'.format(characters[objetivo].name))
                else:
                    print('La autoestima de {0} baja {1}.'.format(characters[objetivo].name, self.vida))
            else:
                print('Ahora confía un {0}% más en tus palabras.'.format(faith))
                characters[objetivo].takeFaith(faith)
            print()
            return None
        elif isinstance(characters[objetivo], gato):
            if characters[objetivo].enrage != 0:
                characters[objetivo].enrageBonusDmg = True
            else:
                faith = 25
            if self.fe <= 50:
                characters[objetivo].enrageProc = 3
            else:
                characters[objetivo].enrageProc += 1
            if characters[objetivo].enrageProc == 3:
                characters[objetivo].enrage = 3
                characters[objetivo].enrageProc = 0
                print('''
{0} se ha cabreado. Será mejor tener cuidado con él, no tardará mucho en calmarse,
normalmente es un gato tranquilo.'''.format(character[objetivo].name))
                print()
        elif isinstance(characters[objetivo], vecina):
            if not characters[objetivo].inmune:
                faith = 10
        elif isinstance(characters[objetivo], rata):
            faith = 20
        print('Intentas parecer de fiar, persuadiendo con tus palabras a {0}.'.format(characters[objetivo].name))
        if faith == 0:
            print('No ha funcionado. Su confianza en tus palabras sigue siendo la misma.')
        else:
            print('''Parece que ha funcionado.
{0} confía ahora un {1}% más en ti.'''.format(characters[objetivo].name, faith))
        print()
        characters[objetivo].takeFaith(faith)
        if isinstance(characters[objetivo],rata):
            if characters[objetivo].fe == 0:
                print()
                characters[objetivo].fe = 100
        
    def autoayuda(self):
        print('Te recuerdas a ti mismo lo mucho que vales.')
        if self.vida + 2 >= self.vidaMax:
            if self.vidaMax - self.vida == 1:
                healing = 1
                print('Tu autoestima aumenta en {0}.'.format(healing))
            if self.vidaMax - self.vida == 0:
                healing=0
                print('Tu autoestima ya está completa.')
            self.vida = self.vidaMax
            
            
             
        else:
            self.vida += 2
            healing=2
            print('Tu autoestima aumenta en {0}.'.format(healing))
        print()
            
        for i in characters:
            if isinstance(i, gato):
                i.enrageProc = 0
                break
            
        
       

    def desconfiar(self):
        if self.fe + 50 >= 100:
            print('''
Te tapas los oídos con las manos para no escuchar lo que te dicen.''')
            print('Tu confianza en el enemigo baja un ' + str(100 - self.fe) + '%.')
            self.fe = 100
                  
        else:
            if self.fe + 50<100:
                print('''
Te tapas los oídos con las manos para no escuchar lo que te dicen.
Tu confianza en el enemigo baja un 50%.''')
            self.fe += 50
        print()
        for i in characters:
            if isinstance(i, gato):
                i.enrageProc = 0
                break

class fantasma(personaje):

    name = 'Fantasma'
    winMessage = '''
{0} ha dañado toda tu autoestima.
Te toca reconocerlo, estás cagado de miedo. El pánico te deja inmóvil.'''.format(name)

    def spook(self):
        dmg = 1
        if characters[0].fe < 50:
            dmg = 2
        characters[0].takeDamage(dmg)
        print('''
{0} te cuenta una historia de terror. Sólo los niños pequeños se asustan
con estas tonterías... Te haces el valiente pero en el fondo estás cagado
de miedo.'''.format(self.name))
        print('Tu autoestima baja {0}.'.format(dmg))
        print()
        
    def whisper(self):
        if characters[0].fe - 30 >= 0:
            f = 30
        else:
            f = characters[0].fe
        characters[0].takeFaith(30)
        print('''
{0} hace ruidos raros para crear ambiente de tensión.
Te metes de bruces en su juego de terror.
Ahora confias un {1}% más en él.'''.format(self.name, f))
        print()
        
    def disappear(self):
        intento = random.randint(1,3)
        print('{0} intenta hacerse invisible. Es un movimiento delicado.'.format(self.name))
        if intento == 2:
            self.fe = 100
            print('''
Aunque no lo consigue, se aleja lo suficiente de ti como para no escuchar bien
lo que dices.
Su confianza en ti baja completamente.''')
        elif intento == 3:
            self.fe = 0
            print('''
Sus poderes de fantasma le juegan una mala pasada. Acaba a tu lado a merced
de tus palabras.
Su confianza en ti ahora es total.''')
        else:
            print('''
Solo pierde el tiempo.''')
        print()
            
    def enemyAction(self):
        accion = random.randint(1,3)
        if accion == 1:
            self.spook()
        elif accion == 2:
            self.whisper()
        else:
            self.disappear()
            
class maniMujer(personaje):

    name = 'Maniquí mujer'
    winMessage = '''
{0} ha dañado toda tu autoestima.
Caes rendido al suelo, aquí se ha acabado. ¿Tanto esfuerzo para esto, para terminar así?
¿Tanto tiempo perdido haciendo deberes, para acabar derrotado por unos maniquíes? Te dejas
llevar, esperas a que te llegue la muerte... y no llega.'''.format(name)

    def pegar(self):
        dmg = 1
        if characters[0].fe < 50:
            dmg = 2
        if characters[0].fe < 10:
            dmg = 3
        characters[0].takeDamage(dmg)
        outputs = ['{0} hace un comentario sobre tu penosa forma de bailar.', '{0} te grita: "¡BAILA NIÑO HUMANO!".',
                   '{0} te lanza una mirada aterradora, mientras con voz dulce te anima a bailar.']
        r = random.randint(0,2)
        print(outputs[r].format(self.name))
        print('Tu autoestima baja {0}.'.format(dmg))
        print()

    def heal(self):
        if self.fe == 100:
            healing = 3
        else:
            healing = 1
        if self.vida + healing >= self.vidaMax:
            self.vida = self.vidaMax
        else:
            self.vida += healing
        print('''
{0} hace un plié y relevé. ¡Qué estilo, qué delicadeza! Se regocija
en su belleza.'''.format(self.name))
        print('La autoestima de {0} aumenta {1}.'.format(self.name, healing))
        print()

    def enemyAction(self):
        if characters[0].vida == 1:
            self.pegar()
        elif self.vida == 1:
            self.heal()
        else:
            self.pegar()

class maniHombre(personaje):

    name = 'Maniquí hombre'

    def enemyAction(self):
        limite = 35
        if self.fe < 50:
            limite = 15 
        faith = random.randint(0,limite)
        characters[0].takeFaith(faith)
        outputs = ['{0} te invita amistosamente a que bailes.', '{0} te advierte del temperamento de Maniquí mujer.',
                   '{0} te coacciona para que hagas caso a Maniquí mujer.', '{0} te mira con ojos de comprensión mientras te ordena que bailes.']
        r = random.randint(0,3)
        print(outputs[r].format(self.name))
        print()

class gato(personaje):

    name = 'Puar'
    enrage = 4
    enrageBonusDmg = False
    cd = 0
    enrageProc = 0
    winMessage = '''
{0} ha dañado toda tu autoestima.
Caes al suelo rendido, no puedes aguantar ni una sola más de sus carcajadas.'''.format(name)
    
    def attack(self):
        calmado= False
        if characters[0].fe == 0:
            dmg = 4
        else:
            if self.enrage > 0:
                if self.enrageBonusDmg:
                    dmg = 3
                    self.enrageBonusDmg = False
                    self.enrage -= 1
                else:
                    dmg = 2
                    self.enrage -= 1
                if self.enrage == 0:
                    calmado = True
            else:
                dmg = 1
        characters[0].takeDamage(dmg)
        outputs = ['{0} se burla de lo delgado que estás.', '{0} se ríe escandalosamente de tu "insignificante fuerza".',
                   '{0} te lanza una mirada burlona mientras se relame el paté que le queda en las patas.',
                   '{0} comenta entre risas que se pensaba apartar de tu camino después de \nla última siestecita de la mañana.']
        r = random.randint(0,3)
        print(outputs[r].format(self.name))
        print('Tu autoestima baja {0}.'.format(dmg))
        print()
        if calmado:
            print('''\
Parece que {0} se ha calmado un poco, será mejor no volver a cabrearlo.'''.format(self.name))
            print()
            

    def heal(self):
        if self.fe == 100:
            healing = 7
        elif 70 <= self.fe < 100:
            healing = 6
        elif 50 <= self.fe < 70:
            healing = 5
        elif 30 <= self.fe < 50:
            healing = 4
        elif 0 < self.fe < 30:
            healing = 3
        else:
            healing = 0
        if self.vida + healing >= self.vidaMax:
            self.vida = self.vidaMax
        else:
            self.vida += healing
        print('''
{0} se relame la pata trasera con un solo movimiento. Es espectacular lo
elástico que es pesando lo que pesa.'''.format(self.name))

        if healing>=5:
            print('''
Tiene una técnica depuradísima. Es capaz de hacerlo mientras te lanza una
mirada asesina y suelta una risilla burlona.
Su autoestima aumenta {0}.'''.format(healing))
        elif healing>3:
            print('''
Tus palabras le tienen algo entretenido. Su técnica es perfecta, pero no
es capaz de mostrar todo su potencial. Aun así, nunca pierde la sonrisa.
Su autoestima aumenta {0}.'''.format(healing))
        else:
            print('''
Está demasiado pendiente de tus palabras como para concentrarse en su higiene.
No lo hace como es debido.
Su autoestima aumenta {0}.'''.format(healing))
        print()


    def taunt(self):
        print('''
{0} te recita el código moral de los gatos. Intenta ganarse tu confianza.'''.format(self.name))
        if random.randint(0,1) == 0:
            faith = 50
            print('Suena bastante convincente.')
        else:
            faith = 100
            print('Es imposible resistirse a la labia de {0}.'.format(self.name))
        if self.fe + faith >=100:
            print('Tu confianza aumenta un {0}%.'.format(100-self.fe))
        else:
            print('Tu confianza aumenta un {0}%.'.format(faith))
        characters[0].takeFaith(faith)
        self.cd = 4
        print()
    def enemyAction(self):
        if self.enrage != 0:
            self.attack()
        else:
            if self.fe != 0:
                if self.vida <= 2:
                    self.heal()
                elif self.cd == 0:
                    self.taunt()
                else:
                    self.attack()
            else:
                if self.cd == 0:
                    self.taunt()
                else:
                    self.attack()
        if self.cd != 0:
            self.cd -= 1
            

class vecina(personaje):

    name = 'Vecina molesta'
    inmune = True
    turnos = 0
    promptObligado = True
    winMessage = '''\
{0} ha dañado toda tu autoestima.
Caes al suelo rendido, jamás habías sentido tanta frustración.'''.format(name)
    

    def interrogatorio(self):
        preguntasYN = ['¿Están tus abuelos?','¿Estas solo?','¿Está tu madre?',
                     '¿Vosotros teneis termitas?','¿No te parece que el vecino es un guarro?\nNo le he visto nunca sacar la basura.',
                       '¿No eres muy pequeño para estar solo en casa?', '¿Te va bien en la escuela?', '¿Tienes nombre?',
                       '¿Eres tu lo que huele tan mal?', '¿Sabes quien está tras la puerta?', '¿Me das algo de comer?', '¿Eres un niño bueno?',
                       'Te gusta esta época del año?','¿Quieres jugar?','¿Quieres jugar conmigo?']
        preguntasSP = ['¿Tu perro ladra mucho, no?','Hace buen tiempo...','A ver cuándo arreglais las goteras...','Huele muy mal la ventana de arriba...',
                       '¿Tu abuelo no sale mucho, no?','Tu abuela y yo somos muy amigas...',
                       'Yo soy mejor, pero ella se defiende bien jugando a las cartas',
                       'Qué puerta más fea...', 'Tu gato se comió la tarta que hice hace un par de dias...',
                       'Siempre veo policía por aquí...','Tus abuelos están viejos...']
    
        preguntas = [preguntasYN, preguntasSP]
        opciones = ['''
1) Sí

2) No
''',
                    '''
1) Seguir la corriente

2) Ignorar
''']
        respuestasYN = ['2','1','1','2','1','1','1','1','2','1','2','1','1','2','1']
        respuestasSP = ['1','1','2','1','1','2','2','1','2','1','2']
        respuestas = [respuestasYN, respuestasSP]
        r = random.randint(0, len(preguntasYN)+len(preguntasSP)-2)
        D = 0
        if r >= len(preguntasYN):
            r -= len(preguntasYN)
            D = 1
        print(preguntas[D][r])
        print(opciones[D])
        options = '1 2'.split()
        opcion = opcionValida(options)
        print()
        if opcion == respuestas[D][r]:
            self.inmune = False
            print('''
{0} no esperaba que respondieses bien a su pregunta.
Te está escuchando.'''.format(self.name))
        else:
            self.inmune = True
            print('''
{0} te regaña por contestar mal a una de sus preguntas.
Esto te llena de desesperación, aunque sabes que deberías
ser paciente con las personas mayores.'''.format(self.name))
            if characters[0].vida - 3 >0:
                print('Tu autestima baja 3.')
            else:
                print('Tu autoestima baja {0}.'.format(characters[0].vida))
            characters[0].takeDamage(3)
        self.turnos += 1
        print()   
        
    def timbre(self):
        dmg = self.turnos//20 + 1
        characters[0].takeDamage(dmg)
        print('''
{0} toca insistentemente el timbre. Te hace rabiar.
Deberías ser más paciente con las personas mayores.
Tu autoestima baja {1}.'''.format(self.name, dmg))
        print()
        self.turnos += 1
        
    def knock(self):
        print('''
{0} golpea dulcemente la puerta mientras con voz sosegada te pide que
confíes en ella: "Soy una ancianita, necesito ayuda".'''.format(self.name))
        if characters[0].fe == 0:
            print('Confias totalmente en ella.')
        else:
            print('Ahora confías un 50% más en ella.')
        print()
        characters[0].takeFaith(50)
        self.turnos += 1
        
    def abrir(self):
        print('''
"¡Niño, ábreme la puerta!"''')
        options = '1 2'.split()
        if self.vida == 1:
            correctOption = '1'
        else:
            correctOption = '2'
        print('''
1) Abrir la puerta.

2) Ignorar.''')
        
        if characters[0].fe == 0:
            options.remove(correctOption)
            opcion = options[0]
            print(opcion)
        elif characters[0].fe == 50:
            opcion = options[random.randint(0,1)]
            print(opcion)
        else:
            opcion = opcionValida(options)
        if opcion == correctOption:
            if self.vida == 1:
                self.takeDamage(1)
                print('''
Abres la puerta y aprovechas para lanzar el insulto de gracia, el que faltaba para
acabar con toda la autoestima de la vecina. Se echa a llorar y se va andando, poco
a poco a su casa, ayudándose de su muleta.''')
            else:
                print('''
Intuyes sus intenciones y decides no abrir la puerta. {0} estaba
completamente convencida de que abrirías: se queda sin palabras.
'''.format(self.name))
        else:
            characters[0].takeDamage(5)
            if self.vida != 1:
                print('''
Abres la puerta, la vecina lo estaba esperando, ves sus intenciones en su sonrisa.
Intentas cerrar, pero antes de que lo hagas, lanza miles de preguntas a la vez.
Tu paciencia es incapaz de soportarlo y rompes a llorar mientras la puerta se vuelve
a cerrar.
''')
            else:
                print('''
Ignoras la petición de {0} y no abres la puerta. En un último intento
desesperado, {0} comienza a tocar el timbre y a golpear la puerta sin parar.
Tu paciencia es incapaz de soportarlo y rompes a llorar.
'''.format(self.name.lower()))
        self.turnos += 1
        
    def enemyAction(self):
        if self.fe > 0:
            self.interrogatorio()
        else:
            if self.vida == 1:
                self.abrir()
            else:
                if self.vida <= 3:
                    if self.promptObligado:
                        self.abrir()
                        self.promptObligado = False
                    else:
                        if characters[0].vida <= self.turnos//20 + 1:
                            self.timbre()
                        else:
                            if random.randint(0, 1) == 0:
                                self.timbre()
                            else:
                                self.knock()
                else:
                    if characters[0].vida <= self.turnos//20 + 1:
                        self.timbre()
                    else:
                        if random.randint(0, 1) == 0:
                            self.timbre()
                        else:
                            self.knock()


class rata(personaje):

    name = 'Rata'

    winMessage = '''
{0} ha dañado toda tu autoestima.
Te toca reconocerlo, estás cagado de miedo. El pánico te deja inmóvil.'''.format(name)

    def bite(self):
        dmg = 1
        if characters[0].fe < 50:
            dmg = 2
        if random.randint(1, 20) == 1:
            dmg = 3
            print('''HIPER COLMILLO''')
        characters[0].takeDamage(dmg)
        print('''
{0} '''.format(self.name))
        print('Tu autoestima baja {0}.'.format(dmg))
        print()
        
    def tailwhip(self):
        if characters[0].fe - 40 >= 0:
            f = 40
        else:
            f = characters[0].fe
        characters[0].takeFaith(40)
        print('''
{0} 
{1}%'''.format(self.name, f))
        print()
        
    def beatup(self):
        dmg = countAdds()
        print('''
''')
        characters[0].takeDamage(dmg)
            
    def enemyAction(self):
        if characters[0].vida == 1:
            self.bite()
        else:
            if countAdds() >= 2:
                self.beatup()
            else:
                if random.randint(0,4) == 0:
                    self.tailwhip()
                else:
                    self.bite()
        if countAdds() < 3:
            if self.fe == 100:
                chance = 100
            elif self.fe == 20 or self.fe == 80:
                chance = 50
            else:
                chance = 0
            if random.randint(1,100) <= chance:
                characters.append(trash(2))
                characters[len(characters)-1].takeFaith(100)
            
                    
class trash(personaje):
    
    name = 'Roedor secuaz'
    winMessage = '''
'''
    
    def mordisco(self):
        dmg = 1
        characters[0].takeDamage(dmg)
        print()

    def chirrido(self):
        faith = 20
        characters[0].takeFaith(faith)
        print()

    def kiss(self):
        characters[0].vida += 1
        print()
        
    def removefromlist(self):
        characters.remove(characters[characters.index(self)])

    def enemyAction(self):
        choice = random.randint(1,100)
        if choice <= 3:
            self.kiss()
        elif 3 < choice < 80:
            self.chirrido()
        else:
            self.mordisco()



# isinstance == erección
# True
# 2 ♥ o ♥♥
#me guardo los pjs en una lista: characters
#los enemigos tendrán un atributo que será name
#tendrán una función llamada enemyAction()

## def cambiarme(self, lista):
## lista[lista.index(self)] = 4

def countAdds():
    global characters
    adds = 0
    for i in characters:
        if isinstance(i,trash):
            adds+=1
    return adds
            
def opcionValida(options):
    opcion = input('Escoge una opción válida: ')
    print()
    while opcion not in options:
        opcion = input('Escoge una opción válida: ')
        print()
    return opcion

##def getHearts(vida, vidaMax):
##    corazones = '♥'*vida + '♡'*(vidaMax-vida)
##    return corazones

def showCurrentHealth():
    global characters
    for i in characters:
##      CAJAS HP BRAH
##        l=len(str(100-i.fe))
##        if len(i.name)>8:
##            print(' '+'_'*len(i.name)+' ')
##            print('|'+i.name +'|')
##            print('|AUT: {0}/{1}'.format(i.vida, i.vidaMax)+' '*(len(i.name)-len('AUT: x/x'))+'|')
##            print('|CON: {0}'.format(100-i.fe)+' '*(len(i.name)-(len('CON: ')+l))+'|')
##        else:
##            print(' ________ ')
##            print('|'+i.name + ' '*(8-len(i.name))+'|')
##            print('|AUT: {0}/{1}'.format(i.vida, i.vidaMax)+'|')
##            print('|CON: {0}'.format(100-i.fe)+' '*(3-l)+'|')
        
        print(i.name)
        print('AUT: {0}/{1}'.format(i.vida, i.vidaMax)+ ' CON: {0}'.format(100-i.fe))
        print()
        
def playerOption():
    global characters
    while True:
        print('''
 _____________________
|                     |
| (1) Insultar        |
| (2) Persuadir       |
| (3) Autoayuda       |
| (4) Desconfiar      |
|_____________________|

''')
        print()
        options = '1 2 3 4'.split()
        opcion = opcionValida(options)
        if opcion == '1':
            target = chooseEnemy()
            if target != 0:
                characters[0].insultar(target)
                break
        if opcion == '2':
            target = chooseEnemy()
            if target != 0:
                characters[0].persuadir(target)
                break
        if opcion == '3':
            characters[0].autoayuda()
            break
        if opcion == '4':
            characters[0].desconfiar()
            break

def chooseEnemy():
    global characters
    print()
    options = ['0']
    for i in range(1, len(characters)):
        if characters[i].alive:
            print('({0})  {1}'.format(i, characters[i].name))
            options.append(str(i))
    print('Pulsa 0 para cancelar.')
    opcion = opcionValida(options)
    return int(opcion)

def enemyTurn():
    global characters
    for i in range(1, len(characters)):
        if characters[i].alive:
            characters[i].enemyAction()
        if not characters[0].alive:
            characters[i].win = True
            break

def createCharacters(salaActual):
    global characters
    characters = []
    characters.append(protagonista(5))
    if salaActual == 5:
        characters.append(fantasma(5))
    elif salaActual == 6:
        characters.append(maniMujer(3))
        characters.append(maniHombre(5))
    elif salaActual == 8:
        characters.append(gato(7))
    elif salaActual == 12:
        characters.append(vecina(5))
    elif salaActual == 14:
        characters.append(rata(5))


def checkWin():
    global characters
    win = True
    for i in range(1, len(characters)):
        if characters[i].alive:
            win = False
    return win

def showWin():
    for enemy in characters:
        if not isinstance(enemy, protagonista):
            if enemy.win:
                print(enemy.winMessage)
                print('''\
Pero eres valiente, te secas las lágrimas dispuesto a continuar con tu camino.
''')


def game(sala):
    createCharacters(sala)
    while True:
        showCurrentHealth()
        playerOption()
        if not checkWin():
            enemyTurn()
            if not characters[0].alive:
                showWin()
                return False
            elif checkWin():
                return True
        else:
            return True

characters = []
