print('creador de contraseña')
operarion=input('ingresa la operacion: ')
num1=int(input('ingresa numero 1: '))
num2=int(input('ingresa numero 2: '))


#suma,resta,multicacion, exponenciales, raiz

#if  condicion=
if operarion =='suma':
    suma=num1+num2
    print(f'la suma es:{suma}')

elif operarion=='resta':
    resta=num1-num2
    print(f'la resta es:{resta}')
elif operarion=='division':
    division=num1//num2
    print(f'la division es:{division}')
elif operarion=='multiplicacion':
    multiplicacion=num1*num2
    print(f'la resta es:{multiplicacion}')
else:
    print('operacion incorrecta') 

