def factorial(n):
    resultado=0
    if n==0:
        return 1
    else:
        return factorial(n-1)*n
def printRev(n):
    if n>0:
        printRev(n-1)
        print(n)
def fibonacci(n):
    if n==0 or n==1:
        return n
    if n >1:
        return (fibonacci(n-1)+fibonacci(n-2))
def main() :
    for num in range(1,6,1):
        r=factorial(num)
        print(f"El factorial de {num} es {r}")
def main2():
    printRev(3)
def mein3():
    for num in range(11):
        print(str(fibonacci(num)))
    
mein3()
