# Diccionario se crea con valores por pares (Clave : Valor) delimitados por corchetes

inventario = {
    "manzanas": 50,
    "plátano": 30,
    "taronja": 45
}

frutas = []
for producto, precio in inventario.items():
    print(f"{producto.capitalize()}: {precio}$")
    frutas.append(producto)
print(frutas)