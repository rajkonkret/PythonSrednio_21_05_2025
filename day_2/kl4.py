# __missing__ gdy nie znajdzie klucza w słowniku

class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


d_python = {}
print(type(d_python))
print(d_python)
# print(d_python['name']) # KeyError: 'name'

d1 = DefaultDict()
print(d1['name'])  # default


class AutoDict(dict):
    def __missing__(self, key):
        self[key] = 0
        return key


a1 = AutoDict()
print(a1)  # {}
print(a1['name'])  # name - zwrócił dodany klucz
print(a1)  # {'name': 0}


class CaseInsensitiveDict(dict):
    def __missing__(self, key):
        return self.get(key.lower())


c1 = CaseInsensitiveDict()
c1['name'] = "Radek"
print(c1["NamE"])  # Radek - działa pomimo małych liter w słowniku dla kluczy
