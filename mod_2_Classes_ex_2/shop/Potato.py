class Potato:
    def __init__(self, species_name, size, price_per_kg):
        self.species_name = species_name
        self.size = size
        self.price_per_kg = price_per_kg
        self.price = 0

    def calculate_price(self, weight):
        self.price = self.price_per_kg * weight
