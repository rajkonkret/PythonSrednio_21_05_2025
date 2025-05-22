from pprint import pprint


class ContactList(list['Contact']):
    def search(self, name):
        matching_contact = []
        for c in self:
            if name in c.name:
                matching_contact.append(c)
        return matching_contact


contact_list = ContactList()
print(contact_list)  # []
print(contact_list.search("Radek"))  # []


class Contact:
    all_contacts = ContactList()  # wspólna lista dla wszystkich obiektów tej klasy

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):  # __repr__ dopisuje __str__ gdy jawnie nie ma
        return f"{self.name} {self.email}"


class Suplier(Contact):  # dziedziczenie po klasie Contact
    """
    Klasa Suplier dziedziczy po kalsie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


class Friend(Suplier):
    """
    klasa dziedziczy po Suplier
    """

    def __init__(self, name, mail, phone="+48000000"):
        super().__init__(name, mail)  # obowiązkowo super() - kalsa nadrzędna
        self.phone = phone

    def __repr__(self):
        # !r - opakowuje stringi cudzysłowem '', konwersja formatowania
        return f"{self.name!r} {self.email!r} ,{self.phone!r}"


c1 = Contact("Adam", "admin@wp.pl")
print(c1)  # Adam admin@wp.pl
c2 = Contact("Radek", "radek@wp.pl")
print(c2)
print(c1.all_contacts)
print(c2.all_contacts)
# [Adam admin@wp.pl, Radek radek@wp.pl]
# [Adam admin@wp.pl, Radek radek@wp.pl]
s1 = Suplier("Marek", "marek@wp.pl")
print(s1.all_contacts)  # [Adam admin@wp.pl, Radek radek@wp.pl, MArek marek@wp.pl]
s1.order("kawa")  # kawa zamówiono od Marek
print(s1.all_contacts.search("Adam"))

f1 = Friend("Kasia", "kasia@wp.pl")
f2 = Friend("Asia", "kasia@wp.pl")
f3 = Friend("Magda", "kasia@wp.pl")
f4 = Friend("Danusia", "danusia@wp.pl", "+48123456")
print(f1.all_contacts)
# [Adam admin@wp.pl, Radek radek@wp.pl, Marek marek@wp.pl, Kasia kasia@wp.pl]
print(Friend.__mro__)  # kolejnośc rozwiązywania nazw dla obiektów
# (<class '__main__.Friend'>, <class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)
print(Contact.all_contacts)
# [Adam admin@wp.pl, Radek radek@wp.pl, Marek marek@wp.pl, Kasia kasia@wp.pl]
# [Adam admin@wp.pl, Radek radek@wp.pl, Marek marek@wp.pl, Kasia kasia@wp.pl
# +48000000, Asia kasia@wp.pl ,+48000000, Magda kasia@wp.pl ,+48000000, Danusia danusia@wp.pl ,+48123456]
pprint(Contact.all_contacts)
# [Adam admin@wp.pl,
#  Radek radek@wp.pl,
#  Marek marek@wp.pl,
#  'Kasia' 'kasia@wp.pl' ,'+48000000',
#  'Asia' 'kasia@wp.pl' ,'+48000000',
#  'Magda' 'kasia@wp.pl' ,'+48000000',
#  'Danusia' 'danusia@wp.pl' ,'+48123456']
# obiekty z klasy w której użylismy !r opakowują stringi cudzysłowani ''
