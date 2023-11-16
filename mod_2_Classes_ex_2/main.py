from shop import Order

def run_example():

    random_list = Order.Order.generate_random_list()
    new_order = Order.Order("Kamil", "RRrrr", random_list)
    new_order.add_product_to_order("Test1234", 3, 4, 4)
    print(f"{new_order}")

if __name__ == '__main__':
    run_example()

