'''Cuando tengo que utilizar muchos datos los organizamos como 
si tubieramos varias cajas, es decir se crean una serie de listas'''

'''LISTAS DE DATOS --> es lo mismo que un arreglo en Java, 
se debe ingresar datos del mismo tipo'''
''''Para recorrer las listas o arreglos utilizamos un 
***for*** para escudriñar/ buscar lo que hay adentro 
de esa lista(Los auxiliares son variables locales)'''

#LISTAS DE DATOS
ciudades = ['Medellin', 'Cali','Bogota','Santa Marta','Cartagena']
print(ciudades)
for ciudad in ciudades:
    ciudad = 'Medellin'
print(ciudad)
    
    
#Lista o arreglo lista 2

numeros = [1,2,3,4,5]
suma=0
for numero in numeros:
    suma+=numero
print('La suma es: ',suma)
