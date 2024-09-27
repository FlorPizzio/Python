print('operadores')

operarion=input('ingresa la operacion: ')
num1=int(input('ingresa numero 1: '))
num2=int(input('ingresa numero 2: '))

flag=0
while flag == 0:
    if operarion =='suma':
        suma=num1+num2
        print(f'la suma es:{suma}')

        flag=1

    elif operarion=='resta':
        resta=num1-num2

        print(f'la resta es:{resta}')

        flag=1

    elif operarion=='division':
        division=num1//num2
        print(f'la division es:{division}')
        flag=1
    elif operarion=='multiplicacion':
        multiplicacion=num1*num2
        print(f'la resta es:{multiplicacion}')

        flag=1
    else:
        print('no ingreso la operacion correcta')
        operarion=input('ingresa la operacion: ')
