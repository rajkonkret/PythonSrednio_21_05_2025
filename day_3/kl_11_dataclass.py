from dataclasses import dataclass
import pickle  # serializacja obiektów


# class Person:
#     def __init__(self, fn, ln, id):
#         self.fn = fn
#         self.ln = ln
#         self.id = id
#
#
# p1 = Person("Jan", "Kowalski", 1)
# print(p1)  # <__main__.Person object at 0x000002C026AA4DD0>


@dataclass
class Person:
    first_name: str
    last_name: str
    id: int

    def greets(self):
        print("My name is:", self.first_name)


p2 = Person("Jan", "Kowalski", 1)
print(p2)  # Person(first_name='Jan', last_name='Kowalski', id=1)
p2.greets()

p3 = Person("Maciej", "Nowak", 2)
print(p3)  # Person(first_name='Maciej', last_name='Nowak', id=2)

people = [p2, p3]
print(people)
# [Person(first_name='Jan', last_name='Kowalski', id=1), Person(first_name='Maciej', last_name='Nowak', id=2)]

# pickle wymaga binarne
with open('dane.pckl', "wb") as f:
    pickle.dump(people, f)

# zapis tekstowy
with open("lista.txt", "w") as fh:
    fh.write(str(people))
