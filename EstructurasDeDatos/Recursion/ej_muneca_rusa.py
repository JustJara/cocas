def abrirmunecarusa(numeromuneca):

    if numeromuneca == 1:
        return print("Proceso finalizado Muneca: " + str(numeromuneca))
    abrirmunecarusa(numeromuneca-1)
    print("Proceso en muneca: " + str(numeromuneca))

abrirmunecarusa(4)