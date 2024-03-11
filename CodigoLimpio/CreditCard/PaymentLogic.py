class ExcesiveInterestException(Exception):
    pass

class InvalidPurchaseException(Exception):
    pass









# Calcula la cuota de una compra con tarjeta de crédito
# purchase_amount : Monto de la compra
# num_payments : Número de cuotas para difereir la compra
# interest_rate : Tasa de interés expresada en porcentaje (Está dividida por 100)
def CalcPayment(purchase_amount : float, num_payments : int, interest_rate : float) -> float:
    interest_percent = interest_rate/100
    if interest_rate > 4:
        # Disparar una siutuacion excepcional que el invocador debe solucionar
        raise ExcesiveInterestException("ERROR: La tasa de interés supera el máximo. No puede superar 3.8%")
    if purchase_amount <= 0:
        raise InvalidPurchaseException("Error: El valor de la compra debe ser mayor a 0")
    if interest_rate == 0:
        return purchase_amount/num_payments
    if num_payments == 1:
        return purchase_amount
    else:
        return (purchase_amount * interest_percent) / (1 - (1 + interest_percent) ** (-num_payments))
    




