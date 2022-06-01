print("El siguiente prigrama le mostrara el estado del clima \n Menu")
valor=int(input("presione 1. para ver el estado del clima 2. para el residuo de una division y 3. para salir"))
while valor<3:
    if valor == 1:
        print("El estado del clima es calido")
    elif valor == 2:
        r1=int(input("Dijite un valor"))
        r2=int(input("Dijite un valor menor que el anterior numero"))
        resultado=r1%r2
        print(f'El valor de el residuo es: {resultado}')   
    elif valor == 3:
        print("salir")    
           
    break
print("Un gusto complacerte, esperamos que vuelvas")