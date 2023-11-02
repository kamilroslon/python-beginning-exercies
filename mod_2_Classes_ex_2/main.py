import random
class Product:
    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price

class Order:
    def __init__(self, first_name, last_name, products_list=None):
        self.first_name = first_name
        self.last_name = last_name
        if products_list is None:
            products_list = []
        self.products_list = products_list
        self.summary_price = calculate_order(products_list)


class Apple:
    def __init__(self, species_name, size, price_per_kg):
        self.species_name = species_name
        self.size = size
        self.price_per_kg = price_per_kg

class Potato:
    def __init__(self, species_name, size, price_per_kg):
        self.species_name = species_name
        self.size = size
        self.price_per_kg = price_per_kg

def calculate_order(products_list):
    total_price = 0
    for product in products_list:
        total_price += product.unit_price
    return total_price

def generate_random_products():
    number_of_products = random.randint(1,15)
    products = []
    for product_number in range(number_of_products):
        products_name = f"Some_Product_Name-{product_number}"
        products_category = f"Some_Products_Category-{product_number}"
        unit_price = random.randint(1, 8)
        products.append(Product(products_name, products_category, unit_price))
    return products

def print_order_summary(order):
    print("First name: ", order.first_name)
    print("Last name: ", order.last_name)
    print("Summary: ", order.summary_price)

def print_list_of_products(products):
    for product in products:
        print("Product's name: ", product.name + " Product's category: " + product.category_name + " Unit price: " + str(product.unit_price))
def run_example():
    apple_1 = Product("Apple", "Fruit", 2)
    potato_1 = Product("Potato", "Vegetable", 3)
    product_list_1 = [apple_1, potato_1]
    new_order = Order("Kamil", "R", product_list_1)
    apple = Apple("Macintosh", 2, 2)
    potato = Potato("Random Potato", 1, 1)
    # print_order_summary(new_order)
    random_products = generate_random_products()
    print_list_of_products(random_products)
    new_order_1 = Order("Kamil", "Rosłon",random_products)
    print_order_summary(new_order_1)

if __name__ == '__main__':
    run_example()

