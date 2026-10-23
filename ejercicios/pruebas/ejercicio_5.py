code = int(input("Introduce el código de estado HTTP: "))
match code:
    case 200 | 201:
        print("EXITO")
    case code if 400 <= code <= 404:
        print("ERROR CLIENTE")
    case 500 | 503:
        print("ERROR DE SERVIDOR")
    case _ :
        print("Codigo de estado no reconocido")