
'''Convertir la tupla=(50,45,20,30,40,87) en una lista que solo contenga números  PARES
'''

numerosTuplas=(50,45,20,30,40,87) 

listaNumeros=[]
for numerosTuplas in numerosTuplas:
    if numerosTuplas > 40:
        listaNumeros.append(numerosTuplas)
print(listaNumeros)