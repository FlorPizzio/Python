print('***Sistema de Empleados***')
nombre_empleado=input('nombre del empleado: ')
edad_del_empleado=int(input('edad del empleado: '))
salario_empleado=float(input('salario del empleado: '))
es_jefe_departamento=input('es jefe departamento (si/no)?')

#convertimos a un tipo bool, la variable es_jefe_departamento
es_jefe_departamento=es_jefe_departamento.lower() == 'si'

#Imprimir los valores del empleado

print('\nDatos del empleado')
print(f'Nombre:{nombre_empleado}')
print(f'edad:{edad_del_empleado}')
print(f'salario:{salario_empleado: .2f}')
print(f'Es jefe de departamento?:{es_jefe_departamento}')

