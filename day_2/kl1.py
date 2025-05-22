# klasy - elemnt programowania obiektowego
# szablon, przepis, matryca, stempel
# obiekt (instancja) - zbudowany wg przepisu
# hermetyzacja, polimorfizm, dizedziczenie, abstrakacja
# klasa nakreśla cechy(zmienne) i funkcje (metody)
# konstruktor - metoda wg której tworzony jest obiekt
import math

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
        self - obiekt, który wywołał metodę
        funkcja inicjalizująca (konstruktor)
        :param x:
        :param y:
        """
        # self.x = x
        # self.y = y
        self.move(x, y)

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        """
        Obliczanie odległości pomiędzy dwoma punktami
        using the Pythagorean theorem:  sqrt(x*x + y*y)
        :param other:
        :return: float
        """
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"{self.x, self.y}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x, self.y}"


ob = MyFirstClass()
print(ob.__doc__)  # Klasa w Python, metoda magiczna __doc__
print(ob)  # <__main__.MyFirstClass object at 0x0000020549CA4E90>
# po dopisaniu __str__
# wynik: (0, 0)
# str(ob) -> (0, 0)

point1 = MyFirstClass()
print(point1)
point1.move(56, 98)
print(point1)  # (56, 98)

point2 = MyFirstClass(67, 34)
print(point2)  # (67, 34)

print(point1.calculate(point2))
# 64.93843238021688

# dopisac metode reset()
point2.reset()
print(point2)  # 64.93843238021688

lista = [point2, point1, ob]
print(lista)
# [<__main__.MyFirstClass object at 0x00000204BA1A5AD0>,
# <__main__.MyFirstClass object at 0x00000204B9F68B90>,
# <__main__.MyFirstClass object at 0x00000204BA1A5A50>]
# po nadpisaniu __repr__
# [MyFirstClass((0, 0), MyFirstClass((56, 98), MyFirstClass((0, 0)]

print(globals())  # użyte elementy w programie
print(help(ob))
# pydoc -b
# pydoc -w kl1.tml