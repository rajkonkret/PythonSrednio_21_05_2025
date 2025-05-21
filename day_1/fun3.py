# lambda - skrócony zapis funkcji
# lambda ma return
# funkcja anonimowa - mozliwosc uzycia funkcji w miejscu deklaracji


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
