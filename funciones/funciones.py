#crear funcion suma
def suma(a,b):
    c=a+b
    print(f"el resultado de la suma es:{c}")
#programa principal
a=int(input("digite un valor: "))
b=int(input("digite otro valor: "))
#llamar a la funcion
suma(a,b)

def suma1(a,b):
    c=a+b
    return c
#programa principal
a=int(input("digite un valor: "))
b=int(input("digite otro valor: "))
c=suma1
print(f"el resultado de la suma es:{c}")
#llamar a la funcion
suma(a,b)