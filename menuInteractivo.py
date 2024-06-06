opciones = ['Fideos', 'Arroz','Porotos','Lentejas']
contador=1
for opcion in opciones:
    print(f'{contador}.- {opcion}')
    contador += 1


select_opciones= int(input('Ingresa el número de tu opción: '))


while True:
    if select_opciones == 1:
        print(f'Haz seleccionado {opciones[0]}')
        break

    elif select_opciones == 2:
        print(f'Haz seleccionado {opciones[1]}')
        break

    elif select_opciones == 3:
        print(f'Haz seleccionado {opciones[2]}')
        break

    elif select_opciones == 4:
        print(f'Haz seleccionado {opciones[3]}')
        break

    else:
        print('Por favor ingrsa un numero')
        break