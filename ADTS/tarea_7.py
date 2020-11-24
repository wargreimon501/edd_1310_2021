class NodoDoble:
    def __init__(self,value=None,siguiente=None,anterior=None):
        self.data=value
        self.next= siguiente
        self.prev = anterior
class ListaDoble:
    def __init__(self):
        self.__head = NodoDoble(None,None,None)
        self.__tail = NodoDoble(None,None,None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0
    def is_empty(self):
        return self.__head == None
    def get_size(self):
        return self.__size
    def append (self,value):
        nuevo= NodoDoble (value)
        if self.is_empty():
            self.__head = self.__tail = nuevo
        else:
            axu=self.__tail
            self.__tail=axu.next=nuevo
            self.__tail.prev = axu
        self.__size +=1

    def trasversal(self):
        curr_node = self.__head
        while curr_node !=None:
            print(f"{curr_node.data }->", end="")
            curr_node=curr_node.next
            
        print("")

    def reverse_trasversal(self):
        curr_node= self.__tail
        while curr_node !=None:
            print(f"{curr_node.data} ->", end ="")
            curr_node = curr_node.prev
        print("")
    def  find_from_head ( self , value):
         curr_node  =  self.__head
         encontrado  =  None
         while curr_node.data!= value:
             curr_node  =  curr_node.next
         if  curr_node.data ==value :
             encontrado=curr_node
         return encontrado

    def  find_from_tail ( self , value ):
        curr_node =  self.__tail
        encontrado  =  None
        while curr_node.data !=value :
            curr_node  =  curr_node.prev
        if  curr_node.data==  value:
            encontrado=curr_node
        return encontrado
    def remove_head(self,value):
        
            curr_node  =  self.find_from_head ( value )
            curr_node.prev.next=curr_node.next
            curr_node.next.prev=curr_node.prev
            curr_node.next= None
            curr_node.prev= None    
        
    def remove_tail (self,value):
        
            cur_node  =  self.find_from_tail( value )
            cur_node.prev.next =  cur_node.next
            cur_node.next.prev  =  cur_node.prev
            cur_node.next  =  None
            cur_node.prev  =  None
    
    
        
      
      
      

    
