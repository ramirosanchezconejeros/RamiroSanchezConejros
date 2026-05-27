edad_ingre=input("ingrese alguan edad: ")
aux=edad_ingre.strip()
edad=0
if aux.isnumeric():
    edad=int(aux)
    if 0<=edad<=120:
        print(f"Edad registrada: {edad}")
    else:
        print("la edad ingresada supera el limite del programa")
else:
    print("la edad ingresada no es valida")