# dekorator - przyjmuje inną funkcję jako argument
# dodaje, modyfikuje jej działanie
# wykorzystuje zasade funkcji wewnętrznej

def dekor(func):
    def wew():
        print("Dekorator. Dodatkowy napis")
        return func()  # wynik działania funkcji

    return wew  # adres funkcji wewnętrznej


@dekor  # dekorator
def nasza_funkcja():
    print("funkcja, którą chcemy udekorować")


nasza_funkcja()
# bez dekoratora
# funkcja, którą chcemy udekorować
# po dodaniu dekoratora:
# Dekorator. Dodatkowy napis
# funkcja, którą chcemy udekorować
