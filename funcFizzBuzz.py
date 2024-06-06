def fizz_buzz(num):
    if num == 24 or num == 55:
        print(num)

    elif num % 15 == 0:
        print('FizzBuzz')

    elif num % 3 == 0:
        print('fizz')

    elif num % 5 == 0:
        print('buzz')

    else:
        print(num)

fizz_buzz(int(input('Ingresa el numero: ')))