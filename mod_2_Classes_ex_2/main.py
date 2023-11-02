from shop import Order, Apple, Potato, Product

def run_example():
    apple_1 = Product.Product("Apple", "Fruit", 2)
    potato_1 = Product.Product("Potato", "Vegetable", 4)
    product_list_1 = [apple_1, potato_1]
    new_order = Order.Order("Kamil", "R", product_list_1)
    apple = Apple.Apple("Macintosh", 2, 2)
    potato = Potato.Potato("Random Potato", 1, 1)
    random_products = Product.generate_random_products()
    Product.print_list_of_products(random_products)
    new_order = Order.Order("Kamil", "RRrrr", random_products)
    Order.print_order_summary(new_order)

if __name__ == '__main__':
    run_example()

