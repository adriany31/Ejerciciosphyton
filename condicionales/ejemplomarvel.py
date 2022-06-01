puede_volar = input("¿puede volar?")
es_humano = input("¿es humano?")
tiene_mascara = input("¿tiene mascara?")

if puede_volar =="si":
    if es_humano =="si":
        if tiene_mascara =="si": 
            print("Iron Man")
        else: 
            print("Capitana Marvel")
    else:
        if tiene_mascara =="si":
            print("Ronan Acuser")
        else:
            
            print("Vision")
else:
    if es_humano =="si":
        if tiene_mascara == "si":
            print("Hombre araña")
        else:
            print("Hulk")
    else:
        if tiene_mascara =="si":
            print("Black Bolt")
        else:
            print("Thanos") 
            

