# funkcja zagnieżdzona, wewnętrzna
# dekorator - funkcja, która jako argument przyjmuje inną funkcję
# dekorator wykorzystuje zasady funkcji wew

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwracamy adres funkcji fun2, referencje, bez nawiasów ()


xfun = fun1()
print(xfun)  # <function fun1.<locals>.fun2 at 0x00000259859CDA80>
print(type(xfun))  # <class 'function'>
xfun()  # To jest fun2
xfun()  # To jest fun2


# zrobic funkcje plik
# funkcja przyjmuje parametr: zapis, odczyt
# w zależności od parametru zwróci funkcję odczytu lub zapisu
def plik(arg):
    print("Sprawdzam czy plik istnieje")

    def zapis():
        print("Zapisałem do pliku")

    def odczyt():
        print("Odczytałem plik")

    if arg == "zapis":
        return zapis
    else:
        return odczyt


zapis_plik = plik("zapis")
zapis_plik()
zapis_plik()
zapis_plik()
zapis_plik()
zapis_plik()

odczyt_pliku = plik("odczyt")
odczyt_pliku()
odczyt_pliku()
odczyt_pliku()
odczyt_pliku()
# Sprawdzam czy plik istnieje
# Odczytałem plik
# Odczytałem plik
# Odczytałem plik
# Odczytałem plik

fh = open('text.txt', "r")
dane = fh.read()
print(dane)  # cokolwiek
fh.close()
