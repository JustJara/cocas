def stringinversedlist(lista):
    if not lista:
        return ''
    return str(lista[-1]) + '\n' + stringinversedlist(lista[:-1])


class Stack:

    def __init__(self,maxcap) -> None:
        self.stacks = []
        self.maxcap = maxcap

    def __str__(self) -> str:
        return stringinversedlist(self.stacks)
        #return '\n'.join(map(str,reversed(self.list)))

    def is_empty(self):
        return len(self.list)  == 0
        
    def push(self,e):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.maxcap:
            self.stacks[-1].append(e)
        else:
            self.stacks.append([e])


    def pop(self):

        while len(self.stacks[-1]) == 0 and len(self.stacks) > 0:
            self.stacks.pop()

        if len(self.stacks[-1]) == 0:
            return 'no existen elementos para retornar'
        else:
            return self.stacks[-1].pop()


    def len(self,numberstack):
        return len(self.stacks[numberstack])

    def delete(self):
        self.stacks = None

customsetofstacks = Stack(2)

customsetofstacks.push("Plato 1")
customsetofstacks.push("Plato 2")
customsetofstacks.push("Plato 3")
customsetofstacks.push("Plato 4")

print(customsetofstacks)

customsetofstacks.pop()

print(customsetofstacks)
customsetofstacks.pop()
print(customsetofstacks)
customsetofstacks.pop()
print(customsetofstacks)