from shop import Order, Apple, Potato, Product

def run_example():

    random_list = Product.generate_random_list()
    new_order = Order.Order("Kamil", "RRrrr", random_list)
    print(f"{new_order}")

if __name__ == '__main__':
    run_example()

