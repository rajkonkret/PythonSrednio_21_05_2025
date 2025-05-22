generator_x = [x for x in range(5)]
print(generator_x)
print(type(generator_x))  # [0, 1, 2, 3, 4]

generator_2 = (x for x in range(5))  # tworzy generator
print(generator_2)
print(type(generator_2))  # <class 'generator'>
print(next(generator_2))
print(next(generator_2))
print(next(generator_2))
print(next(generator_2))


def generator3():
    for x in [1, 2, 3, 4, 5]:
        yield x


g3 = generator3()
print(next(g3))
print(next(g3))
print(next(g3))


def gen4():
    i = 1
    while True:  # pętla nieskońćzona
        yield i * i
        i += i


g4 = gen4()
print(next(gen4()))
print(next(gen4()))
print(next(gen4()))
print(next(gen4()))
print(next(gen4()))


def gen5():
    i = 1
    while True:
        command = yield i * i
        print(command)
        if command == "stop":
            break


g5 = gen5()
print(next(g5))
print(next(g5))
print(next(g5))
print(next(g5))
g5.send("Ok")
try:
    g5.send('stop')  # StopIteration
except Exception as e:
    print("Koniec", e)


# stop
# Koniec


def fibo_with_index(n):
    a, b = 0, 1
    for ind in range(n):
        yield ind, a
        a, b = b, a + b


fib2 = fibo_with_index(10)
print(next(fib2))
print(next(fib2))
print(next(fib2))
print(next(fib2))
print(next(fib2))  # (4, 3)

for i, n in fibo_with_index(10):
    print(f'pozycja: {i}, element: {n}')
# pozycja: 0, element: 0
# pozycja: 1, element: 1
# pozycja: 2, element: 1
# pozycja: 3, element: 2
# pozycja: 4, element: 3
# pozycja: 5, element: 5
# pozycja: 6, element: 8
# pozycja: 7, element: 13
# pozycja: 8, element: 21
# pozycja: 9, element: 34
