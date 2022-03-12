
'''Importar librerias es como tener (resetas/codigos prefabricados) este es un ejercicio extra'''



import math

'''Variable contrladora'''
'''Declaro el bucle/ciclo/inteccion/repeticion/la vuelta'''
print ("Empanadas el machetico")
print ("******")
print ("0. Digite 0 para Salir: ")
print ("1. Digite 1 para calcular la raiz cuadrada de 1 numero: ")
print ("2. Digite 2 para calcular la potencia de 2 numero: ")
print ("******")
opcion=int(input("Digita una opcion: "))

while(opcion !=0):
    #Variable controladora
    opcion=int(input("Digita una opcion: "))
    #Pregunte por la opcion del
    if(opcion==0):
        break
    elif(opcion==1):
        numero=int(input("Digita una numero: "))
        raiz=math.sqrt(numero)
        print(f"La raiz del {numero} es {raiz}")
    elif(opcion==2):
        numero=int(input("Digita una numero: "))
        potencia=math.pow(numero, 2)
        print(f"La potencia es {potencia}")
else:
    print("No Valido")
