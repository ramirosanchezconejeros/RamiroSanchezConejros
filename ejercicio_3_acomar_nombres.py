nombres = ["a mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
nombres_normalizados=[]
for i in nombres:
    nombres_normalizados.append(i.strip().casefold().capitalize())
print(nombres_normalizados)
