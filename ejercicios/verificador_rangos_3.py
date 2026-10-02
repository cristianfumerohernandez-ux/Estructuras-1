usuario = input("Introduce tu nombre de usuario: ").strip().lower()
cp = input("Introduce tu código postal: ").strip()

if not usuario:
    print("El nombre del usuario está vacío")
if not cp.isdigit():
    print("El código postal está erroneo, no es un dígito")
if usuario and cp.isdigit():
    print(f"Registro Válido. Usuario:'{usuario}' | CP: {cp} ")