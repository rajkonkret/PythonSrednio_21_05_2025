# hermetyzacja - ukrycie zmiennych wewnatrz klasy, widocznośc tylko w klasie
# enkapsulacja - hermetezycja pol i metod, wystawienie metod(gettery, setery) do odczytu i zmiany wartości tych pól
class Dom:
    def __init__(self, kolor, metraz):
        # pole prywatne
        self.__metraz = metraz
        self.__kolor = kolor

    def wypisz_metraz(self):
        print(f'Mam powierzchnię {self.__metraz} m2')

    def zmien_metraz(self):
        odp = int(input("podaj nowy metraz (m2)"))
        self.__metraz = odp

    def wypisz_kolor(self):
        print("Mam kolor:", self.__kolor)

    def zmien_kolor(self):
        odp = input("Podaj nowy kolor")
        self.__kolor = odp
        self.__farba()

    def __farba(self):
        print("Zabrakło farby")


dom = Dom("zielony", 100)
# po oznaczeniu pól jako prywatne
# print(dom.metraz)  # 100 jaka jednostka? AttributeError: 'Dom' object has no attribute 'metraz'
# print(dom.__metraz) # AttributeError: 'Dom' object has no attribute '__metraz'
dom.__metraz = 120  # w jakich jednostkach?
dom.wypisz_metraz()  # Mam powierzchnię 120 m2
dom.zmien_metraz()
dom.__metraz = 120
dom.wypisz_metraz()
# Mam powierzchnię 55 m2
# dom.__farba()  # AttributeError: 'Dom' object has no attribute '__farba'
dom.zmien_kolor()
# Mam powierzchnię 100 m2
# podaj nowy metraz (m2)123
# Mam powierzchnię 123 m2
# Podaj nowy kolorczerwony
# Zabrakło farby
