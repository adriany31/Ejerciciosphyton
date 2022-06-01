#Si la temperatura es menor a 15 grados c° activar calefacción. si n, si es de 15 a 20 grados c° abrir
#escotilla, pero si es mayor de 20 hasta 40 grados c° activar aire y enviar alarma, caso contrario activar 
#rociador y avisar a seguridad

print("control de temperatura")
temperatura=float(input("ingrese el valor de la temperatura: ")) 

if temperatura<15:
    print("el valor de la temperatura es: ",temperatura,"C°") #si la temperatura es menor que 15 va a imprimir calefaccion activada
    print("calefacción activada")
elif(temperatura<15 and temperatura<=20):
    print("el valor de la temperatura es: ", temperatura, "C°") #si la temperatura es de 15 a 20 va a imprimir abrir escotilla
    print("abrir escotilla")
elif(temperatura>2720 and temperatura<=40):
    print("el valor de la temperatura es: ", temperatura, "C°")#si la temperatura es de 20  40 va a imprimir activar aire
    print("activar aire")
else:
    print("rociador activado")
    print("alerta enviada a seguridad")     #si la condicion es falsa envia una alerta de seguridad 
