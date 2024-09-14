#MANEJO DE INDICES 
cadena1= 'hola mundo'
print(cadena1)
#recuperar el primer caracter
primer_caracter=cadena1[0] #recupera el caracter de 'H'
print(primer_caracter) 
ultimo_caracter= cadena1[9] #recupera 'o'
print(ultimo_caracter)

#inmutabilidad en cadenas
# se refiere a que una cadena es inmutable osea no puede modificarse pero ai sobreescribirse, por ejemplo:
cadena2=cadena1
print(cadena1)
cadena1= 'adios'
print(cadena1)
#caracteres 

#estos caracteres se introducen usando el caracter de diagonal inverida '\' por ejemplo:

#Nueva_linea='n\' osea que inserta un salto de linea

print('hola \n mundo ')

#tabulacion \t= inserta un tabulador horizontal, util para alinear el texto

_ejemplo='none'

print('python es \t genial')

#comillas simples= \' permite incluir comillas simples en una cadena delimitado por comillas simples

_ejemplo='none'

print('Juan\' "Perez') #ejemplo de ambas comillas

#comillas dobles \"= perimite incluir comillas dobles en una cadena delimitada por comillas dobles.

_ejemplo='none' 

print("Karla\" Gomez")
#barra invertida= \\ permite incluir una barra invertida en la cadena
_ejemplo='none'


print('caracter \\ diagonal invertida')

#Concatenacion de cadenas:
# es una operacion que permite combinar una o mas cadenas para formar una nueva cadena,para formar una nueva cadena
#existen diferentes formas:

#Uso de operador + es el mas directo para concatenar cadenas, simplemente debemos colocarlo entre las cadenas que deseamos unir

_ejemplo='none'

cadena1= 'Hola'
cadena2='Mundo'
concatenacion= cadena1+cadena2 #sin espacios
concatenacion= cadena1+' '+cadena2 #con espacio
print(concatenacion)


#Uso del operador join, la funcion join nos permite unir tantas cadenas como necesitemos

_ejemplo='none'

concatenacion=''.join([cadena1,' ', cadena2])

print(concatenacion)

#formateo de cadenas, exiten varias maneras de formatear cadenas ,que incluyen la capacidad de concatenar textos, variables e incluso dar otro tipo de formateo, como por ej:

#f-string(Python 3.6):esta es la opcion mas recomendada

#rto:f'hola{variable}'

#METODO format: es muy versartil y poderoso permite realizar cadenas complejas

#rto= 'hola {}'. format(variable)

nombre='Juan'
edad=30
#f-string

mensaje=f'hola me llamo {nombre} y tengo {edad} años'

print(mensaje)

#metodo Format

mensaje='hola me llamo {} y tengo {} años'.format(nombre,edad)
print(mensaje)

#   METOODOS DE CADENAS
#MAYUSCULAS= upper()
#MINUSCULAS=lower()
#BORRA ESPACIOS= sprit()

print(f'cadena original:{cadena1}')
mayusculas=cadena1.upper()

print(f'cadena en mayusculas:{mayusculas}')
print(f'cadena en minusculas:{cadena1.lower()}') #converir minuscula

cadena0=' hola Juan '

print(f'cadena con espacios:{cadena0}')
print(f'cadena sin espacios:{cadena0.strip()}')

#OBTENER LARGO DE UNA CADENA: para esto se utliza la funcion de LEN la cual se ultiliza par saber la longitud d ela isma
#la funcion len funciona con varios tipos de datos incluyendo, cadenas, listas, etc.

# se tienen en cuenta todos tipos de caracteres, espacios blancos, etc.

cadena6= 'Hola, mundo!'
largo_de_cadena=len(cadena6)
print(f'cadena original:{cadena6}')
print(f'largo de cadena: {largo_de_cadena}')

#SUBCADENAS
#Obtenemos la subcadena de hola [(inicio:fin) sin incuirlo]
subcadena_hola=cadena6[0:4]
print(f'subcadena de hola:{subcadena_hola}')

 #Obtene la subcadena de mundo
subcadena_mundo=cadena6[6:11]
print(f'subcadena de mundo:{subcadena_mundo}')

#BUSCAR SUBCADENA
indice=cadena6.find('mundo')
print(f'indice de la subcadena mundo:{indice}')

indice=cadena6.find('Hola')
print(f'indice de la subcadena hola:{indice}')

#REMPLAZA SUBCADENAS
Nueva_cadena=cadena6.replace('mundo','a todos')
print(f'cadena nueva remplazada:{Nueva_cadena}')
Nueva_cadena=cadena6.replace('Hola', 'Adios')
print(f'cadena nueva remplazada hola por adios: {Nueva_cadena}')

#SEPARAR CADENAS (SPLIT)
datos='Hola, mundo'
lista=datos.split()
print(lista)

datos='Juan,30,Mexico'
lista=datos.split(',')

print(lista)

texto='hola'
veces=4

resultado=texto*veces

print(resultado)

