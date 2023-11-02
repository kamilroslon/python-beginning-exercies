import random
class Product:
    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price

def generate_random_products():
    number_of_products = random.randint(1,15)
    products = []
    for product_number in range(number_of_products):
        products_name = f"Some_Product_Name-{product_number}"
        products_category = f"Some_Products_Category-{product_number}"
        unit_price = random.randint(1, 8)
        products.append(Product(products_name, products_category, unit_price))
    return products

def print_list_of_products(products):
    for product in products:
        print("Product's name: ", product.name + " Product's category: " + product.category_name + " Unit price: " + str(product.unit_price))