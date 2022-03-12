

#print("Ingrese el valor final (N) ")
#a = int(input())
#b=0
#for i in range(1, a+1):
 #   print(i)
  #  b=b+i
#print("La suma es:",b)


n=1
while n>=0:
    n=int(input("Por favor ingresa un numero entero: "))

    if n>0:
        break
    else:
        print("La operacion no se pudo realizar Digite un numero entero positivo")
suma=0
for i in range(1, n+1):
    suma=suma+i
print(f"{i}", end="+")
print(f"\n Suma correcta: {suma}")

    

