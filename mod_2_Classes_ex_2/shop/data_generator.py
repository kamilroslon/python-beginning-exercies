from shop.Product import Product, ProductsCategory
from shop.Order import Order
import random

MIN_UNIT_PIECE = 1
MAX_UNIT_PIECE = 15
MIN_UNIT_PRICE = 1
MAX_UNIT_PRICE = 30
MIN_IDENTIFIER = 1
MAX_IDENTIFIER = 999


def order_generator(number_of_products=None):
    elements = []
    if number_of_products is not None:
        for element in range(number_of_products):
            identifier = random.randint(MIN_IDENTIFIER, MAX_IDENTIFIER)
            products_name = f"Product_name_{element}"
            products_category = random.choice(list(ProductsCategory))
            unit_price = random.randint(1, MAX_UNIT_PRICE)
            unit_piece = random.randint(1, 15)
            elements.append(Product(products_name, products_category.value, unit_price, unit_piece, identifier))
    else:
        number_of_elements = random.randint(1, Order.MAX_ELEMENTS)
        elements = []
        for element in range(number_of_elements):
            identifier = random.randint(1, 999)
            products_name = f"Product_name_{element}"
            products_category = random.choice(list(ProductsCategory))
            unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
            unit_piece = random.randint(MIN_UNIT_PIECE, MAX_UNIT_PIECE)
            elements.append(Product(products_name, products_category.value, unit_price, unit_piece, identifier))
    return elements
