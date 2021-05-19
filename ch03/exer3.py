""" Objetivo: imprimir uma grade usando somente o que foi visto até agora
    func = função
    arg = argumento
"""
def more_twice(func, arg):
    sev_space = ' ' * 7 #total spaces between the |
    func(arg, sev_space, arg, sev_space, arg)
    func(arg, sev_space, arg, sev_space, arg)

def do_twice(arg):
    """ chama função print_dash 2x
        arg = argumento
    """
    print_dash(arg)
    print_dash(arg)


def print_dash(arg):
    print(arg, end=' ')
    print(arg, end=' ')

def do_four(func, arg):
        """ chama função print more_twice 2x
            func = print e arg = '|'
        """
        more_twice(func, arg)
        more_twice(func, arg)
       
#funções responsaves pela contrução da grade
def teste():
    print('+', end=' ')
    do_twice('-')
    teste2()

def teste2():
    print('+', end=' ')
    do_twice('-')
    teste3()


def teste3():
    print('+')
    teste4()

def teste4():
    do_four(print, '|')
   
teste()
#repetindo a primeira parte
teste()

#repetindo as tres primeiras funções para finalizar a grade
def plus_dash():
    print('+', end=' ')
    do_twice('-')
    more_dash()

def more_dash():
    print('+', end=' ')
    do_twice('-')
    last_plus()


def last_plus():
    print('+')


#chamando função para imprimir a ultima linha   
plus_dash()



