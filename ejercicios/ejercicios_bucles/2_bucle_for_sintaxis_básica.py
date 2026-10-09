palabra = input("Introduce una palabra: ").lower()
contador = 0

for letra in palabra:
    if letra in "aeiou":
        contador += 1

print(f"La palabra contiene {contador} vocales")