def consultar_cuotas (cantidad_cuotas,gasto_total):
    interes_mensual = (gasto_total*0.031) / (1-(1+0.031)**(-cantidad_cuotas))
    if cantidad_cuotas == 1:
        return(f"A {cantidad_cuotas} cuota debes de pagar {gasto_total}$ ")
    if cantidad_cuotas > 1:
        print(f"Cada cuota debe pagar {interes_mensual}")


print("Hola acá puedes calcular el valor total a la cantidad de cuotas que te toca pagar de tu tarjeta de crédito")
gasto_total = int(input("Ingrese la cantidad del gasto que realizará o realizó: "))
cantidad_cuotas = int(input("Ingrese a cuantas cuotas desea.(Recuerde que deben ser de 1 a 36)"))
print(consultar_cuotas(cantidad_cuotas,gasto_total))