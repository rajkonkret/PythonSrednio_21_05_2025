from abc import ABC, abstractmethod


class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by

    @abstractmethod  # metoda abstarkcyjna
    def drukuj(self):
        pass  # nic nie rób


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values):
        if values > self.MAX:
            raise ValueError(f"Wartość ni emoże przekroczyc max: {self.MAX}")
        super().__init__(values)  # obowiązkowe

    def drukuj(self):
        print("Drukuje", self.values)


# TypeError: Can't instantiate abstract class NewCounter with abstract method drukuj
# nie nadpisalismy metody drukuj
class NewCounter(Counter):
    """
    Klasa dziedziczy po Counter
    """


# TypeError: Can't instantiate abstract class Counter with abstract method drukuj
# nie można stworzyc obiektów kalsy Counter bo ta klasa jest abstrakcyjna
# wymuszamy koniecznośc dziedziczenia po tej klaasie
# kalsa dziedzicząc musi nadpisac metode abstrakcyjną
# c1 = Counter()
# c1.increment()
# print(c1.values)
# c1.drukuj()
bc = BoundedCounter(30)
bc.drukuj()  # Drukuje 3
# TypeError: Can't instantiate abstract class NewCounter with abstract method drukuj
# nc = NewCounter()
