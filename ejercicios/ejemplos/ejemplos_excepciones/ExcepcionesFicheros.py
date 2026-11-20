# Definimos la variable fuera para asegurar su visibilidad en el bloque finally
archivo = None

try:
    # 1. Intentamos abrir y leer el fichero
    archivo = open("datos.txt", "r", encoding="utf-8")
    contenido = archivo.read()
    print("📖 Contenido del fichero leído con éxito:")
    print(contenido)

except FileNotFoundError:
    # Captura específica si el archivo no existe en el disco
    print("❌ Error: El archivo 'datos.txt' no fue encontrado.")

except OSError as error:
    # Captura otros errores de lectura/escritura o permisos del sistema operativo
    print(f"❌ Error de entrada/salida: {error}")

except Exception as error:
    # Captura cualquier otra excepción no prevista
    print(f"❌ Ocurrió un error inesperado: {error}")

finally:
    # 2. Se ejecuta SIEMPRE para cerrar el fichero y liberar recursos
    if archivo is not None and not archivo.closed:
        archivo.close()
        print("🔒 Acción de limpieza: El fichero se ha cerrado correctamente.")
    else:
        print("🔒 Acción de limpieza: El flujo finalizó sin necesidad de cerrar ficheros abiertos.")