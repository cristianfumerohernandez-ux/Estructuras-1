
"""
a = 3
print (type(a))

a = "Pepe"
print (type(a))

lista1 = [1, 2, 3]
lista2= [1, 2, 3]
lista3 = lista1

print (lista1 == lista2)

print (lista1 is lista2)

print (lista1 is lista3)

lista1[1] = 4
lista2[2] = 6
print ("Lista 1:", lista1) 
print ("Lista 2:", lista2)   
print ("Lista 3:", lista3)

saludo = "Hola que tal"

print("La" in saludo)
print("Adiós" not in saludo)
"""
"""
nombre = int (input ("Introduce tu nombre: "))
print (type(nombre))
print ("Hola, ", nombre)
"""
"""
print("Introduce dos números")
n1 = int (input("Primer número: "))
n2 = int (input("Segundo número: "))
if n1 > 0 and n2 > 0:
    print("Son mayores que cero")
    """
# print(2**-5)

nota = int(input("Introduce tu nota: "))
match nota:
    case nota if nota < 5 and nota >= 0:
        print("Suspendido")
    case nota if nota >= 5 and nota < 7 :
        print ("Aprobado")
    case nota if nota >= 7 and nota < 9:
        print ("Notable")
    case nota if nota >= 9 and nota <10:
        print ("Sobresaliente")
    case _ :
        print("Eso no furula")