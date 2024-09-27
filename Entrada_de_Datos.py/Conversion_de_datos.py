print('Conversion de tipos de datos')
#Convertir de cadena a numero
numero_cadena='10'
numero_entero=int(numero_cadena)
print(f'valor numerico en cadena:{numero_cadena}')
print(f'cadena a numero:{numero_cadena}')

#convertir de cadena flotante

numero_cadena='3.14'
numero_flotante=float(numero_cadena)
print(f'cadena a flotante:{numero_flotante}')

#Convertir de numero a cadena
numero_entero=25
numero_cadena=str(numero_entero)

print(f'numero a cadena:{numero_cadena}')

#Convertir a booleanos
#Tipo de bool es falso en los sig casos:
#Si el valor es cero, cadena vacia o none, entonces es falsa
#Verdadero cuando el valor es distinto a 0, si es distinto acdena vacia o disnto a none.

numero_entero=0
booleano=bool(numero_entero)
print(f'valor booleano de 0:{booleano}')    #valor de false es 0 o 0.0

numero_entero=5
booleano=bool(numero_entero)

print(f'valor booleano de 5:{booleano}')    #true

cadena=''     #el largo de la cadena es 0
booleano=bool(cadena)
print(f'booleanos de cadena vacia:{booleano}')  #false, incluye colecciones vacias

cadena='valor'
booleano=bool(cadena)

print(f'cadena no vacia:{booleano}') #true

variable= None
booleano=bool(variable) 

print(f'valor booleano none:{booleano}')    #false




