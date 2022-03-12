''''Creando ***tuplas*** en Python, me sirbe para datos que voy alamcenar 
como datos inmutables que son una catidad determinada que no se pede cambiar'''

estudiantes=('Carlos','JuanCarlos')
print (estudiantes)

#Esto es un error no se pude hacer
''''estudiantes.append('Martha')
print (estudiantes)'''

#Recorrido tuplas
for estudiantes in estudiantes:
    print (estudiantes)
    
#Convertir una tupla en una lista 
listaEstudiantes = list(estudiantes)
print (listaEstudiantes)
listaEstudiantes.append("El nuevo")
newTuple=tuple(listaEstudiantes)
print(newTuple)