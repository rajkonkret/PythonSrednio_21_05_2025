# generator - generuje wartość w momwncie kiedy jej potrzebuje


def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


# generator
def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # zwraca wartośc obliczenia, zapamiętuje na której skońćzył


kwa = kwadrat2(5)  # inicjalizacja generatora
print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))
print("Zrob cokolwiek")
print(next(kwa))
# Zrob cokolwiek
# 16
# print(next(kwa))  # StopIteration

kwa2 = kwadrat2(10)
for k in kwa2:
    print(k)

kwa3 = kwadrat2(10)
kwa4 = kwadrat2(20)

print(next(kwa3))
print(next(kwa4))
print(next(kwa3))
print(next(kwa4))

print(list(kwa4))
# [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
