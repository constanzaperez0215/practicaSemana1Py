import random

def num_random():
    numero = random.randint(1, 10)
    # random.randint(1, 10) es la funcion para buscar un numero random entero dentro de sus parametros

    for _ in range(1,11):
        ingresa_numero = int(input('Introduce un numero del 1 al 10: '))
        if numero == ingresa_numero:
            print('Adivinaste el numero!')
        else:
            print('sigue intentando')


num_random()