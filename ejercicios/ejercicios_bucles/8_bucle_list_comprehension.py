palabras = ["sol", "murciélago", "mar", "elefante", "luz"]

palabrasTresLetras = [palabra for palabra in palabras if len(palabra)>3]
print (palabrasTresLetras)

palabrasFor = []

# Ahora con un for
for palabra in palabras:
    if len(palabra)>3:
        palabrasFor.append(palabra)
        
print(palabrasFor)
