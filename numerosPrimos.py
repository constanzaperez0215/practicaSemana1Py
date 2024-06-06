def numeros_primos(num):
    if num == 1 or num == 0:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

print(numeros_primos(int(input('Ingresa el numero: '))))



def numeros_primos2(num):
    if num == 1 or num == 0:
        return print(f'{num} no es un numero primo')
    for x in range(2, num):
        if num % x == 0:
            return print(f'{num} no es un numero primo')
    return print(f'{num} es un numero primo')

numeros_primos2(int(input('Ingresa el numero: ')))
