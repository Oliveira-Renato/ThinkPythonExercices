def do_twice(func, arg):
    """chama uma função duas vezes
       FUNC = nome da função
       arg = argumento
    """
    func(arg)
    func(arg)


def print_twice(arg):
    """exibe na tela o argumento duas vezes

       FUNC = nome da função
       arg = argumento
    """
    print(arg)
    print(arg)


def do_four(func, obj):
        """ chama uma função quatro vezes
            FUNC = nome da função
            arg = argumento
        """
        do_twice(func,obj)
        do_twice(func, obj)

    
do_twice(print, 'spam')
print('-------')

do_four(print, 'bolacha')