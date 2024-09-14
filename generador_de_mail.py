#   GENERADOR DE MAIL

nombre_completo='Gaston Exequiel Bustamante'
print(f'nombre de usuario:{nombre_completo}')

#PROCESAR O NORMALIZAR EL NOMBRE DEL EMAIL
#LIMPIAR LOS ESPACIOS EN BLANCO

nombre_de_usuario=nombre_completo.strip()
#reemplazar los espacios en blanco por puntos
nombre_normalizado=nombre_de_usuario.replace(' ','.')

#convertir en minusculas
nombre_normalizado=nombre_normalizado.lower()
print(f'nombre de usuario normalizado:{nombre_normalizado}')

#DATOS DE LA EMPRESA
nombre_de_empresa=' Sakura Pink '
print(F'\nNombre de la empresa:{nombre_de_empresa}')
extencion_del_dominio='.com.ar'
print(f'Extencion del dominio:{extencion_del_dominio}' )
#quitamos los espacios en blancos y convertimos a mayusculas
nombre_empresa_normalizado=nombre_de_empresa.replace(' ', '').lower()
dominio_mail_normalizado=f'@{nombre_empresa_normalizado}{extencion_del_dominio}'
print(f'dominio del mail normalizado:{dominio_mail_normalizado}')

#creamos el email final
email=f'{nombre_normalizado}{dominio_mail_normalizado}'
print(f'\nEmail final generado:{email}')





