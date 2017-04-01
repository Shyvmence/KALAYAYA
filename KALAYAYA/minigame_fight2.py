import random

class personaje():
    global characters
    
    def __init__(self, vidaMax):
        self.vidaMax = vidaMax
        self.fe = 100
        self.vida = vidaMax
        self.alive = True
        self.hearts = getHearts(self.vida, self.vidaMax)
        
    def takeDamage(self, dmg):
        self.vida -= dmg
        if self.vida <= 0:
            self.vida = 0
            self.alive = False
        self.hearts = getHearts(self.vida, self.vidaMax)

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
        elif isinstance(characters[objetivo], vecina):
            if characters[objetivo].fe == 0:
                dmg = 1
        print('Insultas a {0}.'.format(characters[objetivo].name))
        if dmg == 0:
            print('No parece importarle.')
        else:
            print('Has dañado la autoestima de {0}.'.format(characters[objetivo].name))
        characters[objetivo].takeDamage(dmg)
        

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
            print('Intentas ganarte la confianza de {0}'.format(characters[objetivo].name))
            if characters[objetivo].fe - 35 <= 0:
                print('''
{0} está de tu parte. La pareja se pone a discutir.'''.format(characters[objetivo].name))
                characters[objetivo].takeDamage(3)
                characters[objetivo].takeFaith(faith)
            else:
                print('Ahora tiene más fe en tus palabras.')
                characters[objetivo].takeFaith(faith)
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
        elif isinstance(characters[objetivo], vecina):
            if not characters[objetivo].inmune:
                faith = 10
        print('Intentas ganarte la confianza de {0}'.format(characters[objetivo].name))
        if faith == 0:
            print('No se fía de ti.')
        else:
            print('Ahora tiene más fe en tus palabras.')
        characters[objetivo].takeFaith(faith)
        
    def autoayuda(self):
        if self.vida + 2 >= self.vidaMax:
            self.vida = self.vidaMax
            self.hearts = getHearts(self.vida, self.vidaMax)
        else:
            self.vida += 2
            self.hearts = getHearts(self.vida, self.vidaMax)
        for i in characters:
            if isinstance(i, gato):
                i.enrageProc = 0
                break
        print('Te recuerdas a ti mismo lo mucho que vales. Tu autoestima aumenta.')

    def desconfiar(self):
        if self.fe + 50 >= 100:
            self.fe = 100
        else:
            self.fe += 50
        for i in characters:
            if isinstance(i, gato):
                i.enrageProc = 0
                break
        print('Te tapas los oídos para no escuchar lo que te dicen.')

class fantasma(personaje):

    name = 'Fantasma'

    def spook(self):
        dmg = 1
        if characters[0].fe < 50:
            dmg = 2
        characters[0].takeDamage(dmg)
        print('''{0} te cuenta una historia de terror. Sólo los niños pequeños se asustan
con estas tonterías. ¿¡Qué ha sido eso!?'''.format(self.name))
        
    def whisper(self):
        characters[0].takeFaith(30)
        print('''{0} hace ruidos raros para crear ambiente de tensión.'''.format(self.name))
        
    def disappear(self):
        intento = random.randint(1,3)
        print('{0} intenta hacerse invisible. Es un movimiento delicado.'.format(self.name))
        if intento == 2:
            self.fe = 100
            print('Aunque no lo consigue, se aleja lo suficiente para no escuchar bien lo que dices.')
        elif intento == 3:
            self.fe = 0
            print('No lo consigue, acaba a tu lado y está a merced de tus palabras.')
        else:
            print('Solo pierde el tiempo.')
            
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

    def pegar(self):
        dmg = 1
        if characters[0].fe < 50:
            dmg = 2
        if characters[0].fe < 10:
            dmg = 3
        characters[0].takeDamage(dmg)
        print('{0} comenta que los monos bailan mejor que tú.'.format(self.name))

    def heal(self):
        if self.fe == 100:
            healing = 3
        else:
            healing = 1
        if self.vida + healing >= self.vidaMax:
            self.vida = self.vidaMax
            self.hearts = getHearts(self.vida, self.vidaMax)
        else:
            self.vida += healing
            self.hearts = getHearts(self.vida, self.vidaMax)
        print('''
{0} hace un plié y relevé. ¡Qué estilo, qué delicadeza! Se regocija
en su belleza.'''.format(self.name))

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
        print('{0} te coacciona para que bailes.'.format(self.name))

class gato(personaje):

    name = 'Puar'
    enrage = 4
    enrageBonusDmg = False
    cd = 0
    enrageProc = 0
    
    def attack(self):
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
            else:
                dmg = 1
        characters[0].takeDamage(dmg)

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
            self.hearts = getHearts(self.vida, self.vidaMax)
        else:
            self.vida += healing
            self.hearts = getHearts(self.vida, self.vidaMax)

    def taunt(self):
        if random.randint(0,1) == 0:
            faith = 50
        else:
            faith = 100
        characters[0].takeFaith(faith)
        self.cd = 4

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

    def interrogatorio(self):
        preguntasYN = ['¿Están tus abuelos?','¿Estas solo?','¿Está tu madre?',
                     '¿Vosotros teneis termitas?','¿No te parece que el vecino es un guarro?\nNo le he visto nunca sacar la basura.',
                       '¿No eres muy pequeño para estar solo en casa?']
        preguntasSP = ['¿Tu perro ladra mucho, no?','Hace buen tiempo...','A ver cuándo arreglais las goteras...','Huele muy mal la ventana de arriba...',
                       '¿Tu abuelo no sale mucho, no?','Tu abuela y yo somos muy amigas...','Yo soy mejor, pero ella se defiende bien jugando a las cartas']
    
        preguntas = [preguntasYN, preguntasSP]
        opciones = ['''
1) Sí

2) No''',
                    '''
1) Seguir la corriente

2) Ignorar''']
        respuestasYN = ['2','1','2','2','2','2']
        respuestasSP = ['2','1','1','2','2','1','1']
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
        if opcion == respuestas[D][r]:
            self.inmune = False
        else:
            characters[0].takeDamage(3)
            self.inmune = True
        self.turnos += 1
            
        
    def timbre(self):
        dmg = self.turnos//20 + 1
        characters[0].takeDamage(dmg)
        self.turnos += 1
        
    def knock(self):
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
            characters[0].takeDamage(5)
            print('''
Abres la puerta, la vecina lo estaba esperando, ves sus intenciones en su sonrisa.
Intentas cerrar, pero antes de que lo hagas, lanza miles de preguntas a la vez.
Tu paciencia es incapaz de soportarlo y rompes a llorar mientras la puerta se vuelve
a cerrar.''')
            ## pierdes cuando ignoras OUTPUT!!!
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

# isinstance == erección
# True

#me guardo los pjs en una lista: characters
#los enemigos tendrán un atributo que será name
#tendrán una función llamada enemyAction()

## def cambiarme(self, lista):
## lista[lista.index(self)] = 4

def opcionValida(options):
    opcion = input('Escoge una opción valida: ')
    while opcion not in options:
        opcion = input('Escoge una opción válida: ')
    return opcion

def getHearts(vida, vidaMax):
    corazones = '♥'*vida + '♡'*(vidaMax-vida)
    return corazones

def showCurrentHealth():
    global characters
    for i in characters:
        print('{0}: {1}'.format(i.name, i.hearts))
        print('{0}: {1}'.format(i.name, i.fe))
        
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

def checkWin():
    global characters
    win = True
    for i in range(1, len(characters)):
        if characters[i].alive:
            win = False
    return win

def game(sala):
    createCharacters(sala)
    while True:
        showCurrentHealth()
        playerOption()
        if not checkWin():
            enemyTurn()
            if not characters[0].alive:
                return False
        else:
            return True

characters = []

