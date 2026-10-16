suma = 0
while True:
    num = input("Introduce un nº para sumar, salir par terminar: ")
    if(num != "salir"):
        suma += int(num)
        print(f"Suma total: {suma} y nº sumando: {num}")
    else:
        print(f"Finalizando, resultado: {suma}")
        break