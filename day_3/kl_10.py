class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    @classmethod
    def z_nazwy_pelnej(cls, nazwa_pelna):
        imie, nazwisko = nazwa_pelna.split()
        return cls(imie, nazwisko)


osoba1 = Osoba("Jan", "Kowalski")
print(osoba1.imie, osoba1.nazwisko)  # Jan Kowalski
# Jan Kowalski
name = "Jan Kowalski"
print(name.split())  # ['Jan', 'Kowalski']
imie, nazwisko = name.split()
print(f"{imie=}, {nazwisko=}")  # imie='Jan', nazwisko='Kowalski'
osoba2 = Osoba(imie, nazwisko)

# wykorzystanie metody statycznej do budowy obiektu innym konstruktorem
osoba3 = Osoba.z_nazwy_pelnej("Magda Tkacz")
print(osoba3.imie)
print(osoba3.nazwisko)
# Jan Kowalski
# ['Jan', 'Kowalski']
# imie='Jan', nazwisko='Kowalski'
# Magda
# Tkacz
