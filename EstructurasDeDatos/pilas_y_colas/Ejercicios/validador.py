def stringinversedlist(lista):
    if not lista:
        return ''
    return str(lista[-1]) + '\n' + stringinversedlist(lista[:-1])


class stack:

    def __init__(self):

        self.list = []

    def __str__(self) -> str:
        return stringinversedlist(self.list)
        #return '\n'.join(map(str,reversed(self.list)))

    def is_empty(self):
        return len(self.list)  == 0
        
    def push(self,e):
        self.list.append(e)

    def pop(self):

        if self.is_empty():
            return ("No existen elementos en la pila para retornar")
        else:
            return self.list.pop()

    def top(self):
        if self.is_empty():
            return ("No existen elementos de la pila para retornar")
        else:
            return self.list[-1]

    def len(self):
        return len(self.list)

    def delete(self):
        self.list = None

    def  ismatch(expre):

        customstack = stack()
        openoperator = "({["
        closeoperator = ")}]"


