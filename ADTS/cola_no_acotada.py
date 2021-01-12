class Priorityqueue:
    def __init__ (self):
        self.__data = [ ]
        self.__size=0
    def is_empty(self):
        return self.__size == 0
    def length(self):
        return self.__size
    def enqueue(self,elem,priorida):
        if self.__size == 0:
            self.__data.append(elem)
        elif not self.__size==0:
            if priorida <=priorida:
                self.__data.append(elem)## no supe como poner el if 
        self.__size +=1
    def dequeue(self):
        if not self.is_empty():
            return self.__data.pop(0)
            self.__size -=1
    def to_string (self):
        cadena=""
        for elem in self.__data:
            cadena =cadena + "/"+ str(elem)
        cadena=cadena + "/"
        return cadena
