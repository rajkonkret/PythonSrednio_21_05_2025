class MyExceptions(Exception):
    def __init__(self, message):
        super().__init__(message)

    @staticmethod
    def sprawdz_wprowadzona_wartosc(wartosc):
        if wartosc < 0:
            raise MyExceptions("Liczba musi być większa od zera")
        if wartosc > 10000:
            raise MyExceptions("Liczba za duża")

    @staticmethod
    def sprawdz_wprowadzona_wartosc1(wartosc):
        if wartosc < 0:
            raise MyExceptions("Liczba musi być większa od zera")


try:
    x = int(input("Podaj liczbę większą od zera"))
    MyExceptions.sprawdz_wprowadzona_wartosc(x)
except MyExceptions as e:
    print("Błąd", e)
except Exception as e:
    print("Błąd", e)
else:
    print("Podana wartość", x)
finally:
    print("Koniec")
