nombre = input('Ingresa tu nombre: ')
nombre_sin_espacios= nombre.replace(" ","")

while True:
    largo = len(nombre_sin_espacios)
    print(f'Tu nombre tiene {largo} caracteres')
    break