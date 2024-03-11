""""

Se tiene un refugio de animales que opera estrictamente con el enfoque First-In , First-Out.

Las personas deben adoptar el que lleve mas tiempo en el refugio (orden de llegada) ó ellos pueden seleccionar el tipo de animal de su preferencia, perro ó gato (igualmente recibiran el que lleve mas tiempo en el refugio)

No esta permitido que las personas seleccionen un animal especifico.

Cree la estructura para implementar estas operaciones necesarias
"""

class shelteranimal:

    def __init__(self) -> None:
        self.cats = []
        self.dogs = []

    def __str__(self) -> str:
        return "".join(map(str,self.cats))+"".join(map(str.self.dogs))

    def enqueue(self,animal,type):
        if type == "Cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeuedogs(self):
        if len(self.dogs)==0:
            return "no existen perros en el refugio"
        else:
            return self.dogs.pop(0)

    def dequeucats(self):
        if len(self.cats)==0:
            return "No existen gatos en el refugio"
        else:
            return self.cats.pop(0)

    def dequeueAny(self):
        if len(self.cats)==0:
            if len(self.dogs)>0:
                return self.dogs.pop(0)
            else:
                return "No existen animales en el refugio"
        else:
            return self.cats.pop(0)


customqueue = shelteranimal()

customqueue.enqueue("Cat1","Cat")
customqueue.enqueue("Cat2","Cat")
customqueue.enqueue("Dog1","Dog")

print(customqueue.dequeueAny())

customqueue.enqueue("Dog2","Dog")

print(customqueue.dequeuedogs())
