from shop import Order, Apple, Potato, Product

def run_example():

    random_list = Product.generate_random_list()
    new_order = Order.Order("Kamil", "RRrrr", random_list)
    new_order.add_product_to_order("Test1234", 3, 4, 4)
    print(f"{new_order}")
    # product1 = Product.Product("Name1", "Category1", 2, 1)
    # product2 = Product.Product("Name1", "Category1", 2, 1)
    # print(f"{product1} == {product2}")
    # print(product1 == product2)

    # random_list1 = Product.generate_random_list()
    # random_list2 = Product.generate_random_list()
    # new_order1 = Order.Order("Kamil", "Rrr", random_list1)
    # new_order2 = Order.Order("Kamil", "Rrr", random_list1)

    # print(product1.name)
    #
    # print(new_order1 == new_order2)

if __name__ == '__main__':
    run_example()

