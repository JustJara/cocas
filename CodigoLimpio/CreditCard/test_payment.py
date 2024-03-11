import unittest
import PaymentLogic


class test_Payment(unittest.TestCase):
    # Prueba que la función que calcula la cuota de la tarjeta de crédito funcione correctamente.
    def test_Payment(self):
        #1. Enumerar variables de entrada
        purchase_amount = 200000
        num_payments = 36
        interest_rate = 3.1 #Vamos a manejar siempre las tasas en porcentaje


        #2. Defino variables de salida y sus valores esperados
        expected_payment = 9297.96

        #3. Invocar la función que quiero probrar
        result = round(PaymentLogic.CalcPayment(purchase_amount, num_payments, interest_rate),2)

        #4. Verificar que el resultado sea correcto
        self.assertEqual(expected_payment, result)

        """""
        if expected_payment == result:
            print("Prueba superada")
        else:
            print(f"Prubea fallida. Esperando {expected_payment} y obtuvimos {result}")
        """

    def test_payment2(self):
       purchase_amount = 850000
       num_payments = 24
       interest_rate = 3.4

       expected_payment= 52377.50

       result = round(PaymentLogic.CalcPayment(purchase_amount,num_payments,interest_rate),2)

       self.assertEqual(expected_payment,result)

    def test_payment3(self):

       purchase_amount = 400000
       num_payments = 1
       interest_rate = 3

       expected_payment = 400000

       result = PaymentLogic.CalcPayment(purchase_amount,num_payments,interest_rate)
       self.assertEqual(result,expected_payment)

    def test_payment4(self):

        purchase_amount = 90000
        num_payments = 1
        interest_rate = 2.40

        expected_output = 90000

        result = PaymentLogic.CalcPayment(purchase_amount,num_payments,interest_rate)

        self.assertEqual(result,expected_output)
    
    def test_payment5(self):

        purchase_amount = 480000
        num_payments = 48
        interest_rate = 0

        expected_output = 10000

        result = PaymentLogic.CalcPayment(purchase_amount,num_payments,interest_rate)

        self.assertEqual(result,expected_output)

    #Prueba para controlar tasa de interes excesiva
    def test_excesive_interest(self):

        purchase_amount = 50000
        num_payments = 60
        interest_rate = 12.4

        expected_output = "ERROR, Tasa excesiva"
        testOk = False # Indicar si la prueba funciona como se espera
        try:
            result = PaymentLogic.CalcPayment(purchase_amount,num_payments,interest_rate)
            testOk = False
            #Si no genera excepción hay un problema
        except:
            testOk = True
            # Si llega aquí, es porque hizo bien las cosas
        
        self.assertTrue(testOk,"No se generó la excepción")

    def test_purchaseZero(self):

        purchase_amount = 0
        num_payments = 60
        interest_rate = 2.1

        

        
        self.assertRaises(PaymentLogic.InvalidPurchaseException,PaymentLogic.CalcPayment(purchase_amount,num_payments,interest_rate))

#Invocar las pruebas


# Este fragmento de código permite ejecutar la prueba invididualmente
# Va fijo en todas las pruebas
        
if __name__ == '__main__':
    unittest.main()