import datetime, random
from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class Product:
    name: str
    category_name: str
    unit_price: float
    pieces: int
    identifier: int

    def __str__(self):
        return f"Product's name: {self.name} | Product's category: {self.category_name} | Unit price: {self.unit_price} | Pieces: {self.pieces} | Identifier: {self.identifier}"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (
            self.name == other.name
            and self.category_name == other.category_name
            and self.unit_price == other.unit_price
            and self.pieces == other.pieces
            and self.identifier == other.identifier
        )


@dataclass
class Products_Expiration(Product):
    production_year: int
    number_of_years_of_validity: int

    def does_expire(self):
        date_now_year = datetime.datetime.now().year
        return (
            date_now_year
            > self.production_year + self.number_of_years_of_validity
        )


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class ProductsCategory(AutoName):
    HOME = auto()
    CLEANING_PRODUCTS = auto()
    TOILETRIES = auto()
    BAKERY = auto()
    FRUIT_AND_VEGETABLES = auto()
    FRESH_MEAT = auto()
    VEGAN_BIO = auto()
