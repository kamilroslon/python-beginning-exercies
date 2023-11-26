from shop.Product import Product
from shop.Order import Order
import random

MIN_UNIT_PIECE = 1
MAX_UNIT_PIECE = 15
MIN_UNIT_PRICE = 1
MAX_UNIT_PRICE = 30

def order_generator(number_of_products=None):
    elements = []
    if number_of_products is not None:
        for element in range(number_of_products):
            random_number = random.randint(1, 79)
            products_name = f"Product_name_{element}"
            products_category = random_number
            unit_price = random.randint(1, MAX_UNIT_PRICE)
            unit_piece = random.randint(1, 15)
            elements.append(Product(products_name, products_category, unit_price, unit_piece))
    else:
        number_of_elements = random.randint(1, Order.MAX_ELEMENTS)
        elements = []
        for element in range(number_of_elements):
            random_number = random.randint(1, 79)
            products_name = f"Product_name_{element}"
            products_category = random_number
            unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
            unit_piece = random.randint(MIN_UNIT_PIECE, MAX_UNIT_PIECE)
            elements.append(Product(products_name, products_category, unit_price, unit_piece))
    return elements