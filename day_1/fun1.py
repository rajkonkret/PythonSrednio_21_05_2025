# funkcja - fragment kodu, który możemy wykonać w dowolnym momencie
# funkcja musi zostać najpierw zadeklarowana
# wywołanie funkcji uruchamia kod

a = 10
b = 90


# snake_case
# dekalracja funkcji
# funkcje niezwracające wyniku
def dodaj():  # funkcja bez argumentów
    print(a + b)


def dodaj2(a, b):  # musimy obowiązkowo przekazac dwa parametry
    print(a + b)


# omijamy problem braku przeciążania funkcji liczbą arguemntów
def odejmij(a, b, c=0):  # argument c z watością domyślną 0
    print(a - b - c)


# funkcje zwracające wynik
def mnozenie(a, b):
    return a * b  # zróci wynik


def mnozenie2(a: int, b: int) -> (int, int, int):
    return a, b, a * b  # zwraca wiele wartości


# wywołanie funkcji
dodaj()  # 100
print(dodaj)  # <function dodaj at 0x00000194490FDA80> adres funkcji
print(type(dodaj))  # <class 'function'>
dodaj()  # dodanie nawiasów uruchamia funkcje jaka znajduje sie w zmiennej

# przekazywanie argumntów po pozycji
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(6, 90)  # 96

odejmij(1, 2)  # -1
odejmij(1, 2, 3)  # -4 c=3

# argumenty nazwane
odejmij(b=8, a=7)  # -1
odejmij(c=9, a=89, b=98)  # -18
# ctrl alt l - formatowanie kodu wg PEP8

# mieszane
odejmij(1, 2, c=89)  # -90
# ctrl d - powielanie linii
odejmij(1, b=9)

# pozycyjne muszą być przed nazwanymi!!!
# odejmij(a=1, 2, 89) # SyntaxError: positional argument follows keyword argument
# ctrl / - komentarz
# odejmij(a=1, 2)  # SyntaxError: positional argument follows keyword argument

# None - odpowiednik nulla, nie wiem, brak informacji
# print(dodaj() + dodaj2(5, 7)) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

print(mnozenie(8, 90))  # 720
wyn = mnozenie(6, 8)
print(wyn)
print("Wynik:", wyn)  # Wynik: 48
print(f"Wynik: {wyn}")  # fstring               # Wynik: 48
print(f"{a} + {b} = {a + b}")  # 10 + 90 = 100
print("Wynik: {}".format(wyn))  # Wynik: 48
print("Wynik: %s" % wyn)  # Wynik: 48
# silne typowanie - nie zmienia typó podczas operacji
# print("Wynik: " + wyn) # TypeError: can only concatenate str (not "int") to str
print("Wynik: " + str(wyn))  # Wynik: 48
print("1" + "2")  # 12  - konkatenacja, łaczenie stringów
print(1 + 2)  # 3

# funkcja mnozenie zwraca wynik
print(mnozenie(4, 5) + mnozenie(6, 2))  # 32

print(mnozenie2(4, 6))  # (4, 6, 24) -> krotka
# 4 * 6 = 24
print("%i * %i = %i" % mnozenie2(4, 6))
# 4 * 6 = 24
# rozpakowanie krotki
a, b, wyn = mnozenie2(4, 6)  # (4, 6, 24)
print(f"{a} * {b} = {wyn}")  # 4 * 6 = 24
c = mnozenie2(6, 8)
print(f"{c[0]} * {c[1]} = {c[2]}")  # 6 * 8 = 48
tup = 1, 2, 3  # krotka
print(type(tup))  # <class 'tuple'>
a, *b = tup  # * worek na pozostałe dane
print(a, b)  # 1 [2, 3]
tupla_names = "Radek", "Tomek", "Zenek", "Danusia"
name1, *name2, name3 = tupla_names
print(f"{name1=}, {name2=}, {name3=}")
# name1='Radek', name2=['Tomek', 'Zenek'], name3='Danusia'
*name1, name2, name3 = tupla_names
print(f"{name1=}, {name2=}, {name3=}")
# name1=['Radek', 'Tomek'], name2='Zenek', name3='Danusia'
