class Nodo:
    def __init__ (self,value,siguiente= None):
        self.data = value
        self.sigiente= siguiente
class LinkListCircular:
    def __init__(self):
        self.primero=None
        self.ultimo=None
    def is_empty(self):
        return  self.primero==None
    def insert (self,value):
        nuevo = Nodo (value)
        if self.primero==None:
            self.primero=self.ultimo=nuevo
            self.ultimo.siguiente=self.primero
        else:
            nuevo= Nodo (value)
            curr_node=self.ultimo
            self.ultimo=curr_node.siguiente=nuevo
            self.ultimo.sigiente=self.primero
            """curr_node=self.primero
            if curr_node.data > nuevo.data:
                self.ultimo=nuevo
                self.ultimo.siguinte=curr_node
                self.primero.siguiente=self.ultimo
            else:
                curr_node=self.ultimo
                curr_node=self.primero

                self.primero.sigiente=self.ultimo"""
    def trasversal (self):
        curr_node=self.primero
        while curr_node.siguiente != self.primero:
            print(f"{curr_node.data}-->",end="")
            curr_node=curr_node.siguiente
        print(curr_node.data)
        print("")
    def search (self,value):
        curr_node=self.primero
        while curr_node != self.primero:
            if curr_node.data == data:
                return True
            return False
    def remove (self,value):
        curr_node=self.primero
        if self.primero.data == value:
            self.primero=self.primero.siguiente
            self.ultimo=self.ultimo.siguiente
        else:
            anterior= None
            while curr_node.data != value and curr_node.siguiente !=self.ultimo:
                anterior=curr_node
                curr_node=curr_node.siguiente
            if curr_node.data==value:
                anterior.siguiente=curr_node.siguiente
            else:
                print("El dato no existe en la lista")
s=LinkListCircular()
print(f"la lista esta vaacia  " , s.is_empty()  )
s.insert(5)
s.insert(6)
s.insert(3)
s.insert(1)
print(f"la lista esta vaacia  " , s.is_empty()  )
#s.trasversal()
s.search(67)
print("el valor esta ", s.search(3) )
s.remove(6)
#s.trasversal()
