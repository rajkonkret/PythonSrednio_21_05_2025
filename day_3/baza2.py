# sqlalchemy - system orm do pracy z baza danych w sposób obiektowy
# pip install sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine('sqlite:///moja_baza.db', echo=True)
Base = declarative_base()


# encja - klasa odwzorowująca tabelę w bazie danych
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)

    def __repr__(self):
        return f"{self.name=}, {self.age=}"


Base.metadata.create_all(engine)  # tworzenie struktury w bazie danych

Session = sessionmaker(bind=engine)
session = Session()

# person = Person(name="Radek", age="23")
# session.add(person) #  INSERT INTO person (name, age) VALUES (?, ?)
# session.commit()

persons = session.query(Person).all()
print(persons)
# [self.name='Radek', self.age='23', self.name='Radek', self.age='23']
# SELECT person.id AS person_id, person.name AS person_name, person.age AS person_age

for p in persons:
    print(p)
    print(p.name)
# self.name='Radek', self.age='23'
# Radek
# self.name='Radek', self.age='23'
# Radek
