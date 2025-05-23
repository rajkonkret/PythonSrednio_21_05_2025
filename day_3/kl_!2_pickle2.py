import pickle
from dataclasses import dataclass
from kl_11_dataclass import Person

#
# @dataclass
# class Person:
#     first_name: str
#     last_name: str
#     id: int
#
#     def greets(self):
#         print("My name is:", self.first_name)

if __name__ == '__main__':
    with open('lista.txt', "r") as file:
        data = file.read()

    print(10 * "-")
    print(data)
    # [Person(first_name='Jan', last_name='Kowalski', id=1), Person(first_name='Maciej', last_name='Nowak', id=2)]
    print(type(data))  # <class 'str'>

    with open('dane.pckl', "rb") as file:
        p = pickle.load(file)

    print("-------")
    print(p)
    print(type(p))
    # [Person(first_name='Jan', last_name='Kowalski', id=1), Person(first_name='Maciej', last_name='Nowak', id=2)]
    # <class 'list'>
