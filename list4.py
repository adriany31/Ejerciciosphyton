lista=[]
for x in range (5):
    valor=int(input('Escriba un número: '))
    lista.append(valor)
    if lista [x]<0:
        lista [x]=int(input('Escriba un número positivo: '))
print(lista)

