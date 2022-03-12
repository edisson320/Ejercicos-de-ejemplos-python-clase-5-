'''Construir un programa que reciba el tamaño de una lista y la llene 
   con números entregados por el usuario
'''

numeros=[]

longitud=int(input("Ingrese el tamaño de una lista: "))

for i in range(longitud):
    numero=int(input("Ingrese numero: "))
    numeros.append(numero)
print(numeros)