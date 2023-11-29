import datetime
class Product:
    def __init__(self, name, category_name, unit_price, pieces):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price
        self.pieces = pieces

    def __str__(self):
        return f"Product's name: {self.name} | Product's category: {self.category_name} | Unit price: {self.unit_price} | Pieces: {self.pieces}"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.name == other.name and self.category_name == other.category_name and self.unit_price == other.unit_price)

class Products_Expiration(Product):
    def __init__(self, name, category_name, unit_price, pieces, production_year, number_of_years_of_validity):
        super().__init__(name, category_name, unit_price, pieces)
        self.production_year = int(production_year)
        self.number_of_years_of_validity = int(number_of_years_of_validity)

    def does_expire(self):
        date_now_year = datetime.datetime.now().year
        return date_now_year > self.production_year + self.number_of_years_of_validity
