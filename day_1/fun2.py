# funkcja zagnieżdzona, wewnętrzna
# dekorator - funkcja, która jako argument przyjmuje inną funkcję
# dekorator wykorzystuje zasady funkcji wew

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwracamy adres funkcji fun2, referencje


xfun = fun1()
print(xfun)  # <function fun1.<locals>.fun2 at 0x00000259859CDA80>
print(type(xfun))  # <class 'function'>
xfun()  # To jest fun2
xfun()  # To jest fun2
