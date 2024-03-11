def stringinversedlist(lista):
    if not lista:
        return ''
    return str(lista[-1]) + '\n' + stringinversedlist(lista[:-1])


class Stack:

    def __init__(self) -> None:
        self.list = []
        self.aux = []
        self.order = []

    def __str__(self) -> str:
        return stringinversedlist(self.list)
        #return '\n'.join(map(str,reversed(self.list)))

    def is_empty(self):
        return len(self.list)  == 0
        
    def push(self,e):
        self.list.append(e)

    def sortstack(customstack):

        ordenstack = Stack()
        auxiliarstack = Stack()

        while not customstack.is_empty():
            currentop = customstack.pop()

            if ordenstack.is_empty():
                ordenstack.push(currentop)
            elif ordenstack.top() > currentop:
                ordenstack.push(currentop)
            else:
                while not ordenstack.is_empty() and ordenstack.top() < currentop:
                    auxiliarstack.push(ordenstack.pop())

                ordenstack.push(currentop)

                while not auxiliarstack.is_empty():
                    ordenstack.push(auxiliarstack.pop())
                
        return ordenstack


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



customstack = Stack()
customstack.push(50)
customstack.push(20)
customstack.push(10)
customstack.push(50)
customstack.push(5)
customstack.push(35)

print(customstack)

print(Stack.sortstack(customstack))

