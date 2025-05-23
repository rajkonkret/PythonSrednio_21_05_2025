from bdb import effective

import requests
from pydantic import BaseModel
from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Float
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"
response = requests.get(url)
print(response)  # <Response [200]> ok, 3xx - przekierowania, 404 -bład , 400 Bad Request, 500 po stroie serwera
print(response.text)
# {"table":"A","currency":"euro","code":"EUR","rates":[{"no":"099/A/NBP/2025","effectiveDate":"2025-05-23","mid":4.2541}]}
response_data = response.json()
print(type(response_data))  # <class 'dict'>


class Rates(BaseModel):
    no: str
    effectiveDate: str
    mid: float


class Currency(BaseModel):
    table: str
    currency: str
    code: str
    rates: List[Rates]


# data = Currency(**response.json())
data = Currency(**response_data)
print(data)
print(data.rates)  # [Rates(no='099/A/NBP/2025', effectiveDate='2025-05-23', mid=4.2541)]

engine = create_engine('sqlite:///currencies.db', echo=True)
Base = declarative_base()


class RatesDB(Base):
    __tablename__ = 'rates'
    id = Column(Integer, primary_key=True)
    no = Column(String)
    effectiveDate = Column(String)
    mid = Column(Float)
    currency_id = Column(ForeignKey('currency.id'))
    currencies = relationship("CurrencyDB", back_populates="rates")


class CurrencyDB(Base):
    __tablename__ = 'currency'
    id = Column(Integer, primary_key=True)
    table = Column(String)
    currency = Column(String)
    code = Column(String)
    rates = relationship("RatesDB", back_populates="currencies", cascade='all')


Base.metadata.create_all(engine)  # tworzenie struktury w bazie danych

Session = sessionmaker(bind=engine)
session = Session()

rates_list = []
for i in data.rates:
    rates_list.append(
        RatesDB(
            no=i.no,
            effectiveDate=i.effectiveDate,
            mid=i.mid
        )
    )

usd = CurrencyDB(
    table=data.table,
    currency=data.currency,
    code=data.code,
    rates=rates_list
)

usd.rates = rates_list

session.add(usd)
session.commit()
