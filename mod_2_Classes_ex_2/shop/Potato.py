from dataclasses import dataclass
# class Potato:
#     def __init__(self, species_name, size, price_per_kg):
#         self.species_name = species_name
#         self.size = size
#         self.price_per_kg = price_per_kg
#         self.price = 0
#
#     def __repr__(self):
#         return f"Name: {self.species_name}, Size: {self.size}, Price per kg: {self.price_per_kg}"
#
#     def calculate_price(self, weight):
#         self.price = self.price_per_kg * weight


@dataclass
class Potato:
    species_name: str
    size: int
    price_per_kg: float
    price: float = 0

    def __repr__(self):
        return f"Name: {self.species_name}, Size: {self.size}, Price per kg: {self.price_per_kg}"
    def calculate_price(self, weight):
        self.price = self.price_per_kg * weight