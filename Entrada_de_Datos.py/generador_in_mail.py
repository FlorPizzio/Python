print('***Generador de email***')
nombre=input('cual es tu nombre?: ')
apellido=input('cual es tu apellido?: ')
nombre_empresa=input('cual es el nombre de tu empresa: ')
extencion_del_dominio=input('extencion del dominio de tu empresa: ')

#normalizamos los valores recibidos
nombre=nombre.strip().lower().replace(' ','.')
apellido=apellido.strip().lower().replace(' ','.')
nombre_empresa=nombre_empresa.strip().lower().replace(' ','.')
extencion_del_dominio=extencion_del_dominio.strip().replace(' ','')

#generar email
email=f'{nombre}.{apellido}@{nombre_empresa}{extencion_del_dominio}'

print(f'''
hola {nombre} tu nuevo email generado por el sistema es:
                        {email}
felicidades!
''')
