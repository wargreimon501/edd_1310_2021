from listas import LinKedList
l=LinKedList()
print(f"l esta vacia? {l.is_empty()}" )
l.append(10)
l.append(5)
l.append(6)
l.append(20)
print(f"l esta vacia? {l.is_empty()}" )
l.trasversal()
l.remove(10)
l.trasversal()
l.preppend(10)
l.trasversal()
x= l.tail()
print(x.data)
print(l.get())
