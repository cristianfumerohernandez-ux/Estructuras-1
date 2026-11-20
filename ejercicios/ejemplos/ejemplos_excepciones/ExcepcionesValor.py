


# Programa para suma de números enteros positivos
numero = int(input("Ingrese un número entero positivo: "))
numero2 = int(input("Ingrese otro número entero positivo: "))
resultado = numero + numero2
print("El resultado de la suma es:", resultado)





# TRY | EXCEPT | FINALLY
                        
                        
while True:
    try: 
        numero = int(input("Ingrese un número entero positivo: "))
        numero2 = int(input("Ingrese otro número entero positivo: "))
        resultado = numero + numero2
        print("El resultado de la suma es:", resultado)
        break
    except ValueError:
        print("Error: Por favor, ingrese solo números enteros positivos.")
    finally:
        print("Proceso completado.")