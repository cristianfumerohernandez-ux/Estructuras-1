def crear_perfil_usuario(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave.capitalize()}: {valor}")
        
crear_perfil_usuario(nombre="Luis", edad=35, ciudad="Madrid")

#Alternativa:

def crear_perfil_usuario(nombre, apellido, **kwargs):
    perfil = {"nombre": nombre, "apellido":apellido}
    perfil.update(kwargs)
    return perfil

usuario = crear_perfil_usuario("Luis", "Vega", ciudad="Madrid", pais="España")
print(usuario)