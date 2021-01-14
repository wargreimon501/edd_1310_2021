
from pilas import Stack
def suma_lista_rec(lista):
    if len(lista)==1:
        return lista[0]
    else:
        return lista.pop()+suma_lista_rec(lista)
def cuenta_regresiva(n):
    if n ==0:
        return n
    else :
        print(n)
        print("----")
        return cuenta_regresiva(n-1)
def eliminar_medio(pilas):
    o=Stack()
    a=pilas.length()/2
    d=round(a)
    for x in range(1,(d)):
        u=pilas.pop()
        o.push(u)
    t=o.length()
    f=pilas.pop()
    for x in range(1,(t+1)):
        l=o.pop()
        pilas.push(l)
    return pilas.to_string()
def main():
    datos=[4,2,3,5]
    res=print(suma_lista_rec(datos))
    print(res)
def main2():
    nu=6
    print(cuenta_regresiva(nu),"BOOM!! no te ama ")#cuanta regresiva
def main3():
    k=Stack()
    k.push(47)
    k.push(42)
    k.push(49)
    k.push(44)
    k.push(33)
    k.push(21)
    k.push(90)
    k.push(69)
    k.push(59)
    k.push(74)
    k.push(26)
    k.push(35)
    print("*******************")
    print(k.to_string())
    print("*******************")
    eliminar_medio(k)#saca el valor de la mitad de la pila pero enpesando a contar del tope
main3()
