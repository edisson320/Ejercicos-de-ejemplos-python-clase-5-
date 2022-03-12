
'''Diccionarios en Python, Para tener en cuenta un diccionario las variables
no se escribre en plurarl en se utilizan las llaves {}'''

estudiante={
    'nombre':'Falcao',
    'edad':34,
    'Futbolista':True,
}
#Imprimir o acceder a todas las llaves o atributos de mi diccionario.

print (estudiante)

#Necesito acceder a un atributo o llave del diccionario.
print (estudiante['nombre'])
#Otro metodo para acceder a mi llave del diccionario
print (estudiante.get('edad'))
#Tal ves yo necesito recorrer un diccionario y obtener sus datos
for valor in estudiante.values():
    print (valor)
