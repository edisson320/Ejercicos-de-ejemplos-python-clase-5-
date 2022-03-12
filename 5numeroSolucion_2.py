
numeros=[]
tamano=int(input("Ingrese el tamaño: "))
for i in range(tamano):
    numero=int(input("ingrese un Numero: "))
    numeros.append(numero)
    

buscar=int(input("Ingresar el numero que busca: "))
if(buscar in numeros):
    print(f'El numero:  {buscar} Si esta')
    
else:
    print(f'El numero:  {buscar} No esta')