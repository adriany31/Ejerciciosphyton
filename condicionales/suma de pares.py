print("digite el numero inicial")
i = int(input("digite el numero inicial"))
print("digite el numero final")
f = int(input("digite el numero final"))
suma = 0
print("**los numeros pares del rango**")
while i <= f:
    if i % 2 == 0:
        print(i)
    i+=1
    suma=suma+1
print("la suma de estos numeros es:", suma)