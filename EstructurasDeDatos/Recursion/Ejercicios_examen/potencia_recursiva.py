def potencia_recursiva(numero,cantidad_de_potencia):
    if cantidad_de_potencia <=1 :
        return numero
    else:
        return numero* potencia_recursiva(numero,cantidad_de_potencia-1)

resultado_potencia = potencia_recursiva(5,3)
print(f"5 potenciado 3 veces es igual a {resultado_potencia}")