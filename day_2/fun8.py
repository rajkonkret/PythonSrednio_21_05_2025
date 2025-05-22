# zrobic funkcję dekorator, która zamieni wynik działania funkcji (zwraca tekst)
# na duże litery


def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # * - dowolna ilosc argumentów pozycyjnych
        # ** - dowolna ilosc argumentów nazwanych
        return result.upper()

    return wrapper


# \033[1m: Set text style to bold
def bold_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "\033[1m" + result + "\033[0m"

    return wrapper


# kolejnośc dekoratorów ma znaczenie
@bold_decorator
@uppercase_decorator
def greeting():
    return "Hello World!!!"


@uppercase_decorator
def greeting2(string):
    return f"Podałeś {string}"


print(greeting())  # HELLO WORLD!!!

print(greeting2("Radek"))  # PODAŁEŚ RADEK


def wrap(*args):  # * dowolna ilośc argumentów pozycyjnych
    print(args)


wrap()
wrap(1)
wrap(1, 2)
wrap(1, 2, 3, 4, 5, 6, 7, 8, 9)


# HELLO WORLD!!!
# ()
# (1,)
# (1, 2)
# (1, 2, 3, 4, 5, 6, 7, 8, 9)

def wrap_all(*args, **kwargs):  # ** argumenty słownikowe
    print(f"{args=}, {kwargs=}")


wrap_all(a=1)  # args=(), kwargs={'a': 1}
wrap_all(1, 2)  # args=(1, 2), kwargs={}
wrap_all(1, 2, f=90)  # args=(1, 2), kwargs={'f': 90}
