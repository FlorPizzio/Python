print('***operadores de asignacion***')

numero=5
print(f'valor de numero:{numero}')

numero =10

print(f'valor de numero:{numero}')

cadena='saludos desde python'

print(f'valor de la cadena:{cadena}')

#asignacion multiple

x, y, z= 5, 'Hola', -9.15
print(f'valor de x: {x} \nvalor de y:{y} \nvalor de z:{z}')

#asignacion encadenada

a = b = c=10
print(f'valor de a:{a}, valor de b:{b },valor de c:{c}')

#Intercambios de valores de una variable, sin utilizar variables temporales
x, y= 5, 10
print(f'valores iniciales de x:{x} y valores inciales de y:{y}')
#aplicando el concepto de asignacion multiple, intercambiamos valores

x, y=y, x
print(f'valores invertidos de:\n x:{x}, y:{y}')

#recibir multiples valores de la entrada del usuario

nombre, apellido= input('ingresa tu nombre y apellido separados por coma(,): ').split(',')
print(f'nombre:{nombre} y apellido:{apellido}')

print('***operadores de asignacion compuesta:***')

c, d=10, 15
print(f'valor inicial:de c: {c} de de: {d}')

#operador compuesto +=

c += d      #a= a + b

print(f'Operador c +=d es: {c}')

#operador compuesto de resta  -=
c=10        #reiniciamos la variable c

c -= d       #c = c + b
print(f'Operador c -=d es: {c}')

#operador compuesto de multiplicacion *=
c=10        #reiniciamos el valor

c *= d

print(f'Operador c *= d es: {c}')

#Operador de division /=

c= 10 #reiciamos valor

c /= d

print(f'Operador c /= d es: {c:.2f}')

