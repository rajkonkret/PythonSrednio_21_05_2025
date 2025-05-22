# klasy - elemnt programowania obiektowego
# szablon, przepis, matryca, stempel
# obiekt (instancja) - zbudowany wg przepisu
# hermetyzacja, polimorfizm, dizedziczenie, abstrakacja
# klasa nakreśla cechy(zmienne) i funkcje (metody)
# konstruktor - metoda wg której tworzony jest obiekt
name = "Radek"
print(f"""
Tekst 
    wielolinijkowy {name}""")


# "Tekst
#     wielolinijkowy Radek"

# PascalCase
class MyFirstClass:
    """
    Klasa w Python
    """

    def __init__(self, x=0, y=0):
        """
        self - obiekt, który wyołał metodę
        funkcja inicjalizująca (konstruktor)
        :param x:
        :param y:
        """
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x, self.y}"


ob = MyFirstClass()
print(ob.__doc__)  # Klasa w Python, metoda magiczna __doc__
print(ob)  # <__main__.MyFirstClass object at 0x0000020549CA4E90>
# po dopisaniu __str__
# wynik: (0, 0)
# str(ob) -> (0, 0)
