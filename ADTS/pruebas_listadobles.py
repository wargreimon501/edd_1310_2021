
from listas_dobles import DoubleLinkedList
ld=DoubleLinkedList()
print("esta vacia: ",ld.is_empty())
ld.append(10)
ld.append(20)
ld.append(30)
print(f"la lista tiene {ld.get_size()}")
ld.trasversal()
ld.reverse_trasversal()
ld.remove_from_head(20)
ld.trasversal()
