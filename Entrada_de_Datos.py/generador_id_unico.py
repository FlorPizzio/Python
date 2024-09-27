print('***Sistema generador de ID unico***')
from random import randint
nombre=input(f'cual es tu noooombre?: ')
apellido=input(f'cual es tu apeelido?: ')
anio_nacimimiento=input(f'cual es tu año de nacimiento? (YYYY): ')   #Y YEAR

#Normalizar valores
nombre_2=nombre.strip().upper()[0:2]
apellido_2=apellido.strip().upper()[0:2]
anio_nacimimiento_2= anio_nacimimiento.strip()[2:]  #tambien puede ser del indice 2:4

#generar el valor aleatorio
aleatorio= randint(1000,9999)

#generamos el valor de ID unico
id_unico=f'{nombre_2}{apellido_2}{anio_nacimimiento_2}{aleatorio}'

print(f'''\nHola{nombre},
Tu nuevo numero de identificacion (ID) generado po el sistema es: {id_unico}
felicidades!
''')
