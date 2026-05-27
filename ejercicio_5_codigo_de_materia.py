codigo_ingre=input("ingrese algun codigo: ")
cantidad=codigo_ingre.count("-")
if cantidad!=1:
    print("el codigo es invalido")
else:
    lista_codigo=codigo_ingre.strip().split("-")
    aux1=lista_codigo[0]
    aux2=lista_codigo[1]
    if aux1.isalpha() and aux2.isnumeric():
        print(f"Codigo valido: {aux1.upper()}-{aux2}")
    else:
        print("el codigo posee numeros en lado izquierdo o letras del lado derecho")