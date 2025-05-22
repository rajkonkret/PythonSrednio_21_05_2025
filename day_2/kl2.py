class Contact:
    all_contacts = []

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
