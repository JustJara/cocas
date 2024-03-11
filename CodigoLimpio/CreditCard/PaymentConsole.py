#Interfaz de usuario tipo consola, para la funcionalidad de calcular cuota -> Responde para qué

import PaymentLogic

try:
    # 1. Leer los datos de entrada
    purchase_amount = float(input("Ingrese el valor de la compra: "))
    num_payments = int(input("Ingrese a cuántas cuótas hizo la compra: "))
    interest_rate = float(input("Ingrese a qué tasa de interés se le está haciendo la compra: "))

    # 2. Realizar el proceso

    payment = round(PaymentLogic.CalcPayment(purchase_amount,num_payments,interest_rate))

    # 3. Entregar los datos de salidak

    print(f"La cantidad a pagar en cada cuota es de: {payment}$")
except ValueError as e:
    print(f"El valor ingresado no es un número válido. Verifique que sea un número correcto. Error: {e}")
except Exception as e:
    #Maneja la excepción y la almacena en la variable "e"
    print(f"La cuota no puede ser calculada: {e}")