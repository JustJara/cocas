def findmaxnum(lista,max_num_actual):

    if len(lista)== 0:
        return max_num_actual
    if lista[0] > max_num_actual:
        return findmaxnum(lista[1:],lista[0])
    if max_num_actual > lista[0]:
        return findmaxnum(lista[1:],max_num_actual)
    

lista = [11,2,4,7,19,25,10000,3,54]
print(findmaxnum(lista,0))


    