def calcular_estadisticas(numeros):
    """Calcula suma, promedio y máximo de una lista"""
    total = sum(numeros)
    promedio = total / len(numeros)
    maximo = max(numeros)
    return total, promedio, maximo  # Devuelve una tupla

# Desempaquetado de valores
suma, prom, max_val = calcular_estadisticas([10, 20, 30, 40, 50])
print(f"Suma: {suma}, Promedio: {prom}, Máximo: {max_val}")
# Salida: Suma: 150, Promedio: 30.0, Máximo: 50

def calcular_precio_con_descuento(precio, porcentaje_descuento):
    """Calcula precio final con descuento e IVA"""
    
    def aplicar_descuento(p, descuento):
        """Función auxiliar interna"""
        return p * (1 - descuento / 100)

    def aplicar_iva(p):
        """Función auxiliar interna"""
        return p * 1.21

    # Usar las funciones internas
    precio_con_descuento = aplicar_descuento(precio, porcentaje_descuento)
    precio_final = aplicar_iva(precio_con_descuento)

    return precio_final

print(calcular_precio_con_descuento(100, 10))  # 108.9
# print(aplicar_iva(9))  # No reconoce la función fuera del ámbito de la función principal