# dziedziczenie po wielu klasach
class A:
    def method(self):
        print("Metoda z klasy A")


a = A()
a.method()  # Metoda z kalsy A


class B:
    def method(self):
        print("Metoda z klasy B")


b = B()
b.method()


class C(B, A):
    """
    Klasa dziedziczy po kalsie B i A
    """


c = C()
c.method()  # Metoda z klasy B
print(C.__mro__)


# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)


class D(A, B):
    """"
    Klasa dziedziczy po kalsie A i B
    """


d = D()
d.method()  # Metoda z klasy A
print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)


class E(A, B):
    def method(self):
        print("Metoda z klasy E")


e = E()
e.method()  # Metoda z klasy E


class F(A, B):
    def method(self):
        B.method(self)  # jawnie wskazane z klasy B


f = F()
f.method()  # Metoda z klasy B


class G(A, B):
    def method(self):
        super().method()  # super() - klasa nadrzędna, tutaj: A
        print("Dopisane")


g = G()
g.method()


# Metoda z klasy A
# Dopisane

class X(A, B):
    def method(self):
        super().method()
        print("Klasa X")
        B.method(self)


x = X()
x.method()
