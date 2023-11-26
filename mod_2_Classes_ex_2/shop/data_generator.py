from shop.Product import Product
import random

MAX_UNIT_PRICE = 30
MAX_NUMBER_OF_PRODUCTS = 20

def order_generator(number_of_products=None):
    elements = []
    if number_of_products is not None:
        # number_of_elements = random.randint(1, MAX_NUMBER_OF_PRODUCTS)

        for element in range(number_of_products):
            random_number = random.randint(1, 79)
            products_name = f"Product_name_{element}"
            products_category = random_number
            unit_price = random.randint(1, MAX_UNIT_PRICE)
            unit_piece = random.randint(1, 15)
            elements.append(Product(products_name, products_category, unit_price, unit_piece))
    else:
        number_of_elements = random.randint(1, MAX_NUMBER_OF_PRODUCTS)
        elements = []
        for element in range(number_of_elements):
            random_number = random.randint(1, 79)
            products_name = f"Product_name_{element}"
            products_category = random_number
            unit_price = random.randint(1, MAX_UNIT_PRICE)
            unit_piece = random.randint(1, 15)
            elements.append(Product(products_name, products_category, unit_price, unit_piece))
    return elements