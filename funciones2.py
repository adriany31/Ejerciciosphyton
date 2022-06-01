lista=[9,2,11,6,1,16,13,8,5,1]
cadena=""
coma=","
for i in lista:
    print(i)

    cadena+=str(i)+coma
print(cadena)

lista.sort(reverse=True)
print(f"{lista}")

buscar=input("digite el valor a buscar:")
