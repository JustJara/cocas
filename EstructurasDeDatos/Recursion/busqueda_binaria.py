def busqueda_binaria(lista,inicial,final,objetivo):

    mitad = (inicial+final)//2

    if lista[mitad] == objetivo:
        return print(f"El objetivo {objetivo} fue encontrado en la posición {mitad}")
    if inicial > final:
        return print(f"El objetivo {objetivo} NO fue encontrado en la LISTA")
    if objetivo < lista[mitad]:
        busqueda_binaria(lista,inicial,mitad-1,objetivo)
    if objetivo > lista[mitad]:
        busqueda_binaria(lista,mitad+1,final,objetivo)

lista = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
busqueda_binaria(lista,0,len(lista)-1,5)


