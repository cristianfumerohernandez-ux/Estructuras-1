#Clase padre
class Coche:
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0
        
    def acelera(self):
        self.velocidad += self.aceleracion
        
#Subclase Coche Volador que hereda de Coche
class CocheVolador(Coche):
    ruedas = 6 # Redifinición de atributo anterior
    def __init__(self, color, aceleracion, esta_volando = False):
        super().__init__(color, aceleracion)
        self.esta_volando = esta_volando
        
    def volar(self):
        self.esta_volando = True
        

# Instanciación de objeto de la subclase
cv1 = CocheVolador('Rojo',60)
cv1.acelera()
print(f"_______________________ \n Velocidad coche volador: {cv1.velocidad}")

cv1.volar()
print(f"_______________________ \n Vuela? {cv1.esta_volando}")


# Verificación explícita de tipos con isinstance e issubclass

print("¿cv1 es instancia de CocheVolador?:", isinstance(cv1, CocheVolador))  # True
print("¿cv1 es instancia de Coche?:", isinstance(cv1, Coche))  # True
print("¿CocheVolador es subclase de Coche?:", issubclass(CocheVolador, Coche))# True
print("¿Coche es subclase de CocheVolador?:", issubclass(Coche, CocheVolador))# False