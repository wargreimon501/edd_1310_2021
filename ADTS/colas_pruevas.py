from cola import Queue,BoundedPriorityQueue
q1=Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
q1.enqueue(13)
print("++++++++++++")
q1.length()
print("++++++++++++")
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
hombre={"priorida":3,"descripcion":"hombre" , "persona":["roberto S", "Josefina N"]}
vigia={"priorida":4,"descripcion":"vigia" , "persona":["Jaime k", "Gerardo F"]}
capitan={"priorida":5,"descripcion":"capitan" , "persona":["luffy M.D"]}
timonel={"priorida":4,"descripcion":"timonel" , "persona":["Juan D", "Raquel H"]}
mujeres={"priorida":3,"descripcion":"mujeres" , "persona":["diana o", "maria i"]}
tercera_edad={"priorida":2,"descripcion":"3_edad" , "persona":["Miguel", "Yasmin h"]}
ninas={"priorida":1,"descripcion":"ninas" , "persona":["diana p", "maria h"]}
cpa=BoundedPriorityQueue(7)
cpa.enqueue(maestres['priorida'],maestres)
cpa.enqueue(niños['priorida'],niños)
cpa.enqueue(mecanico['priorida'],mecanico)
cpa.enqueue(hombre['priorida'],hombre)
cpa.enqueue(vigia['priorida'],vigia)
cpa.enqueue(capitan['priorida'],capitan)
cpa.enqueue(timonel['priorida'],timonel)
cpa.enqueue(mujeres['priorida'],mujeres)
cpa.enqueue(tercera_edad['priorida'],tercera_edad)
cpa.enqueue(ninas['priorida'],ninas)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
cpa.to_string()
while cpa.is_empty()==False:
    cpa.dequeue()
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(cpa.is_empty())
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(cpa.to_string())
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
