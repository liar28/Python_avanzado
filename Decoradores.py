def decorador(func):
    def wrap():
        print('Esto se añade a la función')
        func()
    return wrap

# def saludo():
#     print('Hola')
# saludo = decorador(saludo)

@decorador
def saludo():
    print('Hola')
    

if __name__ == '__main__':
    saludo()
