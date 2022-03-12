listaNumeros=[]
for k in range(0,5,1):
    numeroIngresado = int(input("Ingrese Numero: "))
    listaNumeros.append(numeroIngresado)
    
buscarNumero = int(input('¿Que numero Busca? '))
if(buscarNumero in listaNumeros):
    print ('Si esta en la Lista')
else:
    print ('No esta en la lista')
    
    


