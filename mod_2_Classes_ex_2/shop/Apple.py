from dataclasses import dataclass
@dataclass
class Apple:
    species_name: str
    size: int
    price_per_kg: float
    price: float = 0

    def __repr__(self):
        return f"Name: {self.species_name}, Size: {self.size}, Price per kg: {self.price_per_kg}"
    def alculate_price(self, weight):
        self.price = self.price_per_kg * weight
