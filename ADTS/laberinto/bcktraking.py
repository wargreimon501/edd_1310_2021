from Array2D import Array2D
from Stack import Stack
class laberintoADT:
    """
    1=pasillo, 0 pared ,s salida, e entrada
    pasillos es una tupla((2,1),(2,2)(2,3),(2,4),(3,2),(4,2))
    entradaen una tupla((5,2)
    salida(2,5)
     """
    def __init__(self ,rens,cols,pasillos,entrada,salida ):
        self.__laberinto = Array2D(rens,cols,'1')
        for pasillo in pasillos:
            self.__laberinto.set_item(pasillo[0],pasillo[1],'0')
        self.set_entrada(entrada[0],entrada[1])
        self.set_salida(salida[0],salida[1])
        self.__camino=Stack()
        self.__previa=None
    def to_string(self):
        self.__laberinto.to_string()
    """
    establese la entrada poniendo una e en la matriz ,verificar limites
    """
    def set_entrada(self,rens,cols):
        #terminar la validacion de las cordenadas
        self.__laberinto.set_item(rens,cols,'E')
        """
        estableser salida dentro de los limites perifericos de la matrix
        """
    def set_salida(self,rens,cols):
        #Terminar las validaciones
        self.__laberinto.set_item(rens,cols,'S')
    def es_salida(self,rens,cols):
        return self.__laberinto.get_item(rens,cols)=='S'
    def buscar_entrada(self):
        encontrado=False
        for renglon in range(self.__laberinto.get_num_rows()):
            for columna in range (self.__laberinto.get_num_cols()):
                tope=self.__camino.peek()#tupla
                if self.__laberinto.get_item(renglon,columna)=='E':
                    self.__camino.push(tule(renglon,columna))
                    encontrado=True
        return encontrado
    def set__previa(self,pos_previa):
        self.__previa = pos_previa
    def get__previa(self):
        return self.__previa
    def resolver_labarinto(self):
        #aplicar reglas
