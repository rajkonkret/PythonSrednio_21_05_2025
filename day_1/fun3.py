# lambda - skrócony zapis funkcji
# lambda ma return
# funkcja anonimowa - mozliwosc uzycia funkcji w miejscu deklaracji
import math
from collections import Counter
from functools import reduce, lru_cache


def mnozenie(x, y):
    return x * y


print(mnozenie(6, 90))

mnozenie_lambda = lambda x, y: x * y
print(mnozenie_lambda(6, 8))  # 48

lata = [(2000, 29.7), (2001, 33.12), (2020, 32.92)]
print(max(lata))
print(min(lata))
# (2020, 32.92)
# (2000, 29.7)

print(max(lata, key=lambda c: c[1]))  # (2001, 33.12)
lata.sort(key=lambda c: c[1])
print(lata)  # [(2000, 29.7), (2020, 32.92), (2001, 33.12)]
print(max(lata))  # (2020, 32.92)
print(max(map(lambda c: (c[1], c), lata)))  # (33.12, (2001, 33.12))
print(max(map(lambda c: c[1], lata)))  # 33.12
print(max(map(lambda c: (c[1], c[0]), lata)))  # (33.12, 2001)

lista = [1, 2, 3, 4, 5]
lista_wyn = []


def zmiana_danych(x):
    return x ** 4  # potęgowanie


for i in lista:
    lista_wyn.append(zmiana_danych(i))

print(lista_wyn)  # [1, 16, 81, 256, 625]

print([i ** 4 for i in lista])  # [1, 16, 81, 256, 625]

# map() - funkcje wyższego rzędu, jako argument przyjmuję inną funkcję
# filter()
print(lista)  # [1, 2, 3, 4, 5]
print(f"Filtrowanie: {list(filter(lambda x: x > 3, lista))}")  # Filtrowanie: [4, 5]
print(lista)
for i in lista:
    if i > 3:
        print(i)
print(lista)
# [1, 2, 3, 4, 5]
# 4
# 5
# [1, 2, 3, 4, 5]

r0 = {'miasto': "Toruń"}
r1 = {"miasto": "Toruń", "ZIP": "25-900"}

print(r0['miasto'])  # Toruń
print(r1['miasto'])  # Toruń

print(r1['ZIP'])
# print(r0['ZIP']) # KeyError: 'ZIP'

print(r0.get("ZIP"))  # None
print(r0.get("ZIP", "00-000"))  # 00-000

d_zip = lambda row: row.setdefault("ZIP", "00-000")
print(d_zip(r0))
print(d_zip(r1))
# 00-000
# 25-900
print(r0)
print(r1)
# {'miasto': 'Toruń', 'ZIP': '00-000'}
# {'miasto': 'Toruń', 'ZIP': '25-900'}


# reduce()
# ((((1+2)+3)+4)+5)
liczby = [1, 2, 3, 4, 5]
wynik = reduce(lambda a, b: a + b, liczby)
print("Wynik:", wynik)  # Wynik: 15
# 1 + 2 = 3
# 3 + 3  = 6
# 6 + 4 = 10
# 10 + 5 = 15

wynik = reduce(lambda a, b: a * b, liczby)
print(wynik)  # 120

dane = ["a", "b", "a", "c", "a", "b", "b", "b", "c", "a"]

licznik = Counter(dane)
print(licznik)
# Counter({'a': 4, 'b': 4, 'c': 2})
wyn = reduce(lambda a, b: a if licznik[a] >= licznik[b] else b, licznik)
print(wyn)  # a

listy = [[1, 2], [3, 4], [5], [6, 7]]
flatten = reduce(lambda a, b: a + b, listy)
print(flatten)  # [1, 2, 3, 4, 5, 6, 7]
lista1 = [1, 2]
lista2 = [3, 4]
print(lista1 + lista2)  # [1, 2, 3, 4]

liczby = [2, 4, 4, 4, 5, 5, 7, 9]
suma, suma_danych, n = reduce(
    lambda acc, x: (acc[0] + x, acc[1] + x ** 2, acc[2] + 1),
    liczby,
    (0, 0, 0)
)

avg = suma / n
wariancja = (suma_danych / n) - (avg ** 2)
odchylenie = math.sqrt(wariancja)  # pierwastek
print(f"Średnia: {avg:.2f}, Odchylenie std: {odchylenie:.2f}")


# Średnia: 5.00, Odchylenie std: 2.00


# lru_cache

@lru_cache(maxsize=1000)  # dekorator
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


print(fib_cached(5))  # 5
print(fib_cached.cache_info())  # CacheInfo(hits=3, misses=6, maxsize=1000, currsize=6)
print(fib_cached(10))  # 55
print(fib_cached.cache_info())  # CacheInfo(hits=9, misses=11, maxsize=1000, currsize=11)
print(fib_cached(10))
print(fib_cached.cache_info())
fib_cached.cache_clear()  # CacheInfo(hits=10, misses=11, maxsize=1000, currsize=11)
print(fib_cached.cache_info())  # CacheInfo(hits=0, misses=0, maxsize=1000, currsize=0)
