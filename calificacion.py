notas=int(input("digite la cantidad de notas de los estudiantes: "))
vec=[]
n=0

for i in range(1,notas+1):
    nota=int(input("nota: "))
    n=n+nota
    vec.append(nota)
    