#valarors aleatorios con la funcion rand int
#import random (una de las formas)

from random import randint
 #como generar un numero aleatorio entre 1 y 10:
numero=randint(1, 10)
print(f'numero aleatorio entre 1 y 10:{numero}')

#simular un dado de 6 caras
dado= randint(1,6)
print(f'resultado de lazar el dado:{dado}')
