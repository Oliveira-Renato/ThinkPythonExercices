""" print(end='')
    print('+', end='')#1 esse primeiro, 3, 5, 7
    print(' - - - - ', end='')#2 esse segundo, 4, 6, 8
    print('+')
    print('|', end='')
    print(' ' * 9, end='')
    print('|', end='')
    -------------------------------------------------------
    Criando uma grande usando apenas comandos visto até agora
"""    
def do_twice(func, arg):
    print_twice(arg)
    print_twice(arg)


def print_twice(arg):
    print(arg, end='')
    print(arg, end='')

#------------------------------------------------------------

def primeira_linha(): #COMEÇA AQUI
    print('+ ', end='')
    do_twice(print, '- - - - + ')
    do_nothing()
    

def do_nothing():
    print('')
    segunda_linha()

def segunda_linha():
    espaco = ' ' * 9 + '|'
    print('|', end='')
    do_twice(print, espaco )
    nada()

def nada():
    print('')

def repete_barra(): 
    segunda_linha()
    segunda_linha()
    segunda_linha()

def repete_inicio():
    primeira_linha()
    repete_barra()
    

def mais_duas_vezes():
    repete_inicio()
    repete_inicio()
    ultima_linha()

def ultima_linha(): #CHEGA
    print('+ ', end='')
    do_twice(print, '- - - - + ')
    nada()


primeira_linha()
repete_barra()
repete_inicio()
mais_duas_vezes()
