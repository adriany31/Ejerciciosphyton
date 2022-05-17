from ast import Lambda


produccion=dict(
    enero=980,
    febrero=568,
    marzo=876,
    abril=34567,
    mayo=123,
    junio=987,
    julio=459,
    agosto=3456,
    septiembre=345,
    octubre=2345,
    noviembre=4567,
    diciembre=3459,
)

minimo=min(produccion.keys(), key=Lambda k=produccion[k])
print('El mes de menor producción fue:', minimo,produccion[minimo])

maximo=max(produccion.keys(), key=Lambda k=produccion[k])
print('El mes de mayor producción fue:', maximo,produccion[maximo])

prom=tuple(produccion.values())
b=len(prom)
suma=0
for val in prom:
    suma+=val
print('El promedio es:', suma/b)

for key in produccion.keys():
    if (produccion[key]>=prom):
        print('el mes', key, 'es mayor que el promedio')
    