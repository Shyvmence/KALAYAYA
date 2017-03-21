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
        
