class Queue:

    def __init__(self):

        self.list = []

    def __str__(self) -> str:
        #return stringinversedlist(self.list)
        return "\n".join(map(str,self.list))

    def is_empty(self):
        return len(self.list)  == 0
        
    def enqueue(self,e):
        self.list.append(e)

    def dequeue(self):

        if self.is_empty():
            return ("No existen elementos en la pila para retornar")
        else:
            return self.list.pop(0)

    def first(self):
        if self.is_empty():
            return ("No existen elementos de la pila para retornar")
        else:
            return self.list[0]

    def len(self):
        return len(self.list)

    def delete(self):
        self.list = None


q = Queue()
print(q.is_empty())
print(q)
q.enqueue(5)
q.enqueue(8)
q.enqueue(2)
print("Cola:")
print(q)
print(f"Cola despues de primer dequeue: ")
q.dequeue()
print(q)
print("Proximo a procesar de la cola: ")
next = q.first()
print(next)
print("Cola después de primer first: ")
print(q)