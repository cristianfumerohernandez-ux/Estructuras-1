try:
    documento = input("Introduce un documento .txt a leer:  ")
    archivo = open(documento, "r", encoding="utf-8")
    contenido = archivo.read()
    for numero_linea,linea in enumerate(archivo,start=1):
        numero = linea.strip()
        print(numero)
    
except FileNotFoundError:
    
    print("❌ Error: El archivo 'datos.txt' no fue encontrado.")
except OSError:
    print("❌ Error: Ha habido un error en la lectura del disco ")