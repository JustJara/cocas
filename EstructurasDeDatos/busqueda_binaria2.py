def busqueda_binaria(lista,inicio,fin,objetivo):

    mitad = (inicio + fin)//2

    if lista[mitad] == objetivo:
        print(f"El {objetivo} se encontró en la posición {mitad}")
    if inicio > fin:
        print(f"El {objetivo} no se encuentra dentro de la lista")
    if objetivo > lista[mitad]:
        return busqueda_binaria(lista,mitad+1,fin,objetivo)
    if objetivo < lista[mitad]:
        return busqueda_binaria(lista,inicio,mitad-1,objetivo)

lista = [1,2,3,4,5,6,7,8,10,11,15,17,19,25,66]
busqueda_binaria(lista,0,len(lista)-1,15)