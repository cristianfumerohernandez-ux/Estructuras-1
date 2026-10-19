def factorial(n):
    # Caso base
    if n <=1:
        return 1
    # Recursividad
    return n*factorial(n-1)
print(factorial(500)) 

