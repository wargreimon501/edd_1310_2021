from cola import Queue,BoundedPriorityQueue
q1=Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
q1.enqueue(13)
print(q1.to_string())

print("prueva2 de Queue")
c1={"id":1,"nombre":"mario","balance":28.5}
c2={"id":2,"nombre":"diana","balance":3456.5}
c3={"id":3,"nombre":"bartolo ","balance":100000.0}
atencion= Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())
siguiente =atencion.dequeue()
print(f"Bienvenido sr . {siguiente['nombre'] },en quie podemos servirle elñ dia de  hoy")
print(atencion.to_string())

print("Pruevas con prioridad acotadas ")

maestres = {"priorida":4,"descripcion":"maestre" , "persona":["juan p", "diego h"]}
niños= {"priorida":2,"descripcion":"niños" , "persona":["santi H", "angel  h"]}
mecanico={"priorida":4,"descripcion":"mecanico" , "persona":["diana p", "maria h"]}

cpa=BoundedPriorityQueue(7)
cpa.enqueue(maestres['priorida'],maestres)
cpa.enqueue(niños['priorida'],niños)
cpa.enqueue(mecanico['priorida'],mecanico)
cpa.to_string()
