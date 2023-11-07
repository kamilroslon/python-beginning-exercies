import random


class Product:
    def __init__(self, name, category_name, unit_price, pieces):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price
        self.pieces = pieces

    def __str__(self):
        return f"Product's name: {self.name} | Product's category: {self.category_name} | Unit price: {self.unit_price} | Pieces: {self.pieces}"

    # def print_product(self):
    #     print(
    #         f"Product's name: {self.name} | Product's category: {self.category_name} | Unit price: {self.unit_price} | Pieces: {self.pieces}")


def generate_random_products():
    number_of_products = random.randint(1, 25)
    products = []
    for product_number in range(number_of_products):
        some_number = random.randint(1, 3)
        products_name = f"Some_Product_Name-{product_number}"
        products_category = f"Some_Products_Category-{product_number}"
        unit_price = random.randint(1, 8)
        unit_piece = random.randint(1, 5)
        products.append(Product(products_name, products_category, unit_price, unit_piece))
    return products


def generate_random_list():
    number_of_elements = random.randint(1, 25)
    elements = []
    for element in range(number_of_elements):
        random_number = random.randint(1, 7)
        products_name = f"Product_name_{element}"
        products_category = f"Product_category_{element}"
        unit_price = random.randint(1, 15)
        unit_piece = random.randint(1, 10)
        elements.append(Product(products_name, products_category, unit_price, unit_piece))
    return elements
