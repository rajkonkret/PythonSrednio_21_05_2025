from functools import total_ordering

print(1 + 2)


class MyNumber:
    def __init__(self, value):
        self.value = value


num1 = MyNumber(5)
num2 = MyNumber(15)
# print(num1 < num2)  # TypeError: '<' not supported between instances of 'MyNumber' and 'MyNumber'
print(num1.value < num2.value)  # True


@total_ordering  # automatycznie generuje pozostałe operatory porównania
class MyNuber2:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


num3 = MyNuber2(5)
num4 = MyNuber2(15)
num5 = MyNuber2(15)
print(id(num3))
print(id(num4))
print(id(num5))
# 2938285549008
# 2938283535824
# 2938285549072
print(num3 < num4)  # True
print(num3 > num4)  # False
print(num4 == num5)  # True
