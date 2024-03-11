class Queue:

    def __init__(self) -> None:
        self.list = []
    
    def __str__(self) -> str:
        return ''.join(map(str,self.list))

    def is_empty(self):
        return len(self.list ) == 0

    def add(self,e):
        self.list.append(e)

    def remove_min(self):
        if self.is_empty():
            return 'No existen elementos en la pila para retornar'
        else:
            maxprioridad = self.list[0]
            for item in self.list[1:]:
                if item[0] < maxprioridad[0]:
                    maxprioridad = item

            self.list.remove(maxprioridad)
            return maxprioridad

    def min(self):
        if self.is_empty():
            return 'No existen elementos en la pila para retornar'
        else:
            maxprioridad = self.list[0]
            for item in self.list[1:]:
                if item[0] < maxprioridad[0]:
                    maxprioridad = item

            return maxprioridad

custompriority = Queue()
custompriority.add((2,'John'))
custompriority.add((3,'Jorge'))
custompriority.add((1,'Mario'))

print(custompriority)

print(custompriority.min())
